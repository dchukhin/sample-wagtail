const gulp = require("gulp");
const rename = require("gulp-rename");
const webpack = require("webpack-stream");

gulp.task('javascript', function() {
  return gulp
    .src("./sample_wagtail/assets/js/webpack_entry.js")
    .pipe(webpack(require("./webpack.config.js")))
    .pipe(rename("main.js"))
    .pipe(gulp.dest("./sample_wagtail/static/js/"));
});

gulp.task('watch-js', function(done) {
  gulp.watch(["./apps/sample_wagtail/assets/js/**/*.js"], gulp.series("javascript"));
  done();
})


gulp.task('styles', function() {
  const sass = require('gulp-sass')(require('sass'));
  return gulp
    .src("./sample_wagtail/assets/styles/sass_entry.scss")
    .pipe(sass().on('error', sass.logError))
    .pipe(rename("main.css"))
    .pipe(gulp.dest("./sample_wagtail/static/css/"));
});

gulp.task('watch-css', function(done) {
  gulp.watch(
    [
    './sample_wagtail/assets/styles/sass_entry.scss',
    './apps/sample_wagtail/assets/styles/sass/**/*.scss'
    ], gulp.series('styles')
  );
  done();
});



exports.default = gulp.series('styles', 'javascript', 'watch-css', 'watch-js');