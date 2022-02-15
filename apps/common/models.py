from django.db import models
from django.utils.translation import gettext_lazy
from wagtail.admin.edit_handlers import FieldPanel, HelpPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class IndexedTimeStampedModel(models.Model):
    created = AutoCreatedField("created", db_index=True)
    modified = AutoLastModifiedField("modified", db_index=True)

    class Meta:
        abstract = True


class TextOrTableStreamBlock(blocks.StreamBlock):
    rich_text = blocks.RichTextBlock()
    table = TypedTableBlock([
        ("text", blocks.CharBlock()),
        ("numeric", blocks.FloatBlock()),
        ("rich_text", blocks.RichTextBlock()),
        ("image", ImageChooserBlock())
    ])


class StreamAndNavHeadingBlock(blocks.StructBlock):
    """A Block with a navigation heading and a StreamBlock."""

    nav_heading = blocks.CharBlock(
        max_length=80,
        required=False,
        help_text=(
            "The heading that should appear for this section in the scrolling "
            "navigation on the side of the page."
        ),
    )
    body = TextOrTableStreamBlock()


class GenericPage(Page):
    """A generic page."""
    subpage_types = ["common.GenericPage"]

    show_back_button = models.BooleanField(
        default=False,
        blank=True,
        help_text="Should this page show a back button at the top of the page?",
    )
    body = StreamField(
        [
            ("section", StreamAndNavHeadingBlock()),
        ]
    )

    search_fields = Page.search_fields + [
        index.SearchField("search_description"),
        index.SearchField("body"),
    ]
    content_panels = Page.content_panels + [
        # show a HelpPanel explaining how to fill out search_description
        MultiFieldPanel(
            [
                HelpPanel(
                    content="The <strong>Search description</strong> field will be shown in search result listings and will also be included in the page's metadata for external search engines. It should be a short summary of the page's contents"
                ),
                FieldPanel("search_description"),
            ],
            heading="Search Description",
        ),
        FieldPanel("show_back_button"),
        StreamFieldPanel("body"),
    ]

    promote_panels = [
        # This MultiFieldPanel is copy-pasted from wagtail.admin.edit_handlers so we can override
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title"),
                # override Page's promote_panels to remove search_description (since we
                # include it in content_panels). Also, don't show "show_in_menus",
                # since we don't use that field in this project.
                # FieldPanel("show_in_menus"),
                # FieldPanel('search_description'),
            ],
            gettext_lazy("Common page configuration"),
        ),
    ]
