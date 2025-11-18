"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gochainwallet.github.io
Prompt: Explain how to use Gulp to watch for changes and build the GoChainWallet Knowledge Base project locally. Include the specific commands provided in the GoChainWallet documentation.
Generated: DETERMINISTIC_5609abd30c2f7297
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gulpfile.js
// This file is used to automate tasks like watching for changes and rebuilding the project.
// Make sure to install the necessary dependencies before running the commands.

const gulp = require('gulp'); // Import Gulp
const sass = require('gulp-sass')(require('sass')); // Import Sass compiler
const cleanCSS = require('gulp-clean-css'); // Import CSS minifier
const concat = require('gulp-concat'); // Import concatenation plugin
const uglify = require('gulp-uglify'); // Import JavaScript minifier
const sourcemaps = require('gulp-sourcemaps'); // Import sourcemaps generator
const del = require('del'); // Import plugin to clean the build directory
const browserSync = require('browser-sync').create(); // Import BrowserSync for live reloading

// File paths
const paths = {
  styles: {
    src: 'src/scss/**/*.scss', // Source directory for SCSS files
    dest: 'dist/css' // Destination directory for compiled CSS files
  },
  scripts: {
    src: 'src/js/**/*.js', // Source directory for JavaScript files
    dest: 'dist/js' // Destination directory for compiled JS files
  },
  html: {
    src: 'src/**/*.html', // Source directory for HTML files
    dest: 'dist' // Destination directory for HTML files
  }
};

// Task: Clean the build directory
function clean() {
  return del(['dist']);
}

// Task: Compile SCSS to CSS, generate sourcemaps, and minify the output
function styles() {
  return gulp
    .src(paths.styles.src)
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError)) // Compile SCSS to CSS and handle errors
    .pipe(cleanCSS()) // Minify the CSS
    .pipe(sourcemaps.write('.')) // Write sourcemaps
    .pipe(gulp.dest(paths.styles.dest))
    .pipe(browserSync.stream()); // Stream changes to BrowserSync
}

// Task: Concatenate and minify JavaScript files
function scripts() {
  return gulp
    .src(paths.scripts.src)
    .pipe(sourcemaps.init())
    .pipe(concat('main.js')) // Concatenate all JS files into main.js
    .pipe(uglify().on('error', function (err) {
      console.error(err.toString()); // Log errors to the console
    }))
    .pipe(sourcemaps.write('.')) // Write sourcemaps
    .pipe(gulp.dest(paths.scripts.dest))
    .pipe(browserSync.stream()); // Stream changes to BrowserSync
}

// Task: Copy HTML files to the build directory
function html() {
  return gulp.src(paths.html.src).pipe(gulp.dest(paths.html.dest)).pipe(browserSync.stream());
}

// Task: Watch for changes and automatically rebuild the project
function watchFiles() {
  browserSync.init({
    server: {
      baseDir: 'dist' // Serve files from the build directory
    }
  });

  gulp.watch(paths.styles.src, styles); // Watch SCSS files for changes
  gulp.watch(paths.scripts.src, scripts); // Watch JS files for changes
  gulp.watch(paths.html.src, html); // Watch HTML files for changes
}

// Define complex tasks
const build = gulp.series(clean, gulp.parallel(styles, scripts, html));
const watch = gulp.series(build, watchFiles);

// Export tasks for use in CLI
exports.clean = clean; // Export clean task
exports.styles = styles; // Export styles task
exports.scripts = scripts; // Export scripts task
exports.html = html; // Export HTML task
exports.build = build; // Export build task
exports.watch = watch; // Export watch task

// Default task (run when you execute 'gulp' in the CLI)
exports.default = watch;

// Specific commands (from documentation):
// To build the project locally, run: gulp build
// To watch for changes and develop locally, run: gulp watch
```
