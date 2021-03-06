# Generated by Django 3.2.12 on 2022-02-15 02:30

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.typed_table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('show_back_button', models.BooleanField(blank=True, default=False, help_text='Should this page show a back button at the top of the page?')),
                ('body', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('nav_heading', wagtail.core.blocks.CharBlock(help_text='The heading that should appear for this section in the scrolling navigation on the side of the page.', max_length=80, required=False)), ('body', wagtail.core.blocks.StreamBlock([('rich_text', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.core.blocks.CharBlock()), ('numeric', wagtail.core.blocks.FloatBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
