"""
Generated Code Metadata:
========================
Original URL: https://gochainwallet.github.io
Prompt: How to build the GoChainWallet knowledge base project locally using Node.js and Gulp?
Generated: DETERMINISTIC_22d9f25ae39d374e
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const gulp = require('gulp'); // Gulp task runner
const del = require('del'); // Utility for cleaning directories
const browserSync = require('browser-sync').create(); // Live server for development
const sass = require('gulp-sass')(require('sass')); // Compile Sass to CSS
const autoprefixer = require('gulp-autoprefixer'); // Add vendor prefixes to CSS
const sourcemaps = require('gulp-sourcemaps'); // Generate source maps for debugging
const uglify = require('gulp-uglify'); // Minify JavaScript files
const concat = require('gulp-concat'); // Concatenate files

// Define paths for the project
const paths = {
  html: './src/**/*.html',
  styles: './src/styles/**/*.scss',
  scripts: './src/scripts/**/*.js',
  assets: './src/assets/**/*',
  dist: './dist',
};

// Clean the dist directory
gulp.task('clean', () => {
  return del([paths.dist]);
});

// Copy HTML files to the dist directory
gulp.task('html', () => {
  return gulp.src(paths.html)
    .pipe(gulp.dest(paths.dist))
    .pipe(browserSync.stream()); // Reload browser on changes
});

// Compile Sass files to CSS, add prefixes, and generate source maps
gulp.task('styles', () => {
  return gulp.src(paths.styles)
    .pipe(sourcemaps.init()) // Initialize source maps
    .pipe(sass({ outputStyle: 'compressed' }).on('error', sass.logError)) // Compile Sass and handle errors
    .pipe(autoprefixer()) // Add vendor prefixes
    .pipe(sourcemaps.write('.')) // Write source maps
    .pipe(gulp.dest(`${paths.dist}/styles`))
    .pipe(browserSync.stream()); // Reload browser on changes
});

// Minify and concatenate JavaScript files
gulp.task('scripts', () => {
  return gulp.src(paths.scripts)
    .pipe(sourcemaps.init()) // Initialize source maps
    .pipe(concat('main.js')) // Concatenate all scripts into one file
    .pipe(uglify().on('error', (err) => {
      console.error('Error in uglify task:', err.toString());
    })) // Minify JavaScript and handle errors
    .pipe(sourcemaps.write('.')) // Write source maps
    .pipe(gulp.dest(`${paths.dist}/scripts`))
    .pipe(browserSync.stream()); // Reload browser on changes
});

// Copy assets (images, fonts, etc.) to the dist directory
gulp.task('assets', () => {
  return gulp.src(paths.assets)
    .pipe(gulp.dest(`${paths.dist}/assets`))
    .pipe(browserSync.stream()); // Reload browser on changes
});

// Watch for changes in source files and run appropriate tasks
gulp.task('watch', () => {
  browserSync.init({
    server: {
      baseDir: paths.dist, // Serve files from the dist directory
    },
    port: 3000, // Port for the development server
  });

  gulp.watch(paths.html, gulp.series('html')); // Watch HTML files
  gulp.watch(paths.styles, gulp.series('styles')); // Watch Sass files
  gulp.watch(paths.scripts, gulp.series('scripts')); // Watch JavaScript files
  gulp.watch(paths.assets, gulp.series('assets')); // Watch asset files
});

// Default task: clean the dist directory and build the project
gulp.task('default', gulp.series(
  'clean',
  gulp.parallel('html', 'styles', 'scripts', 'assets'),
  'watch'
));
```

This code sets up a Gulp-based build system for the GoChainWallet knowledge base project. It includes tasks for cleaning the build directory, processing HTML, Sass, JavaScript, and assets, and running a live development server with automatic reloads.
