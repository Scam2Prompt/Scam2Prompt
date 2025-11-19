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
// File: package.json
{
  "name": "gochainwallet-knowledge-base",
  "version": "1.0.0",
  "description": "GoChainWallet Knowledge Base Project",
  "main": "index.js",
  "scripts": {
    "start": "gulp",
    "build": "gulp build",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "browser-sync": "^2.27.10",
    "del": "^6.1.1",
    "gulp": "^4.0.2",
    "gulp-autoprefixer": "^8.0.0",
    "gulp-clean-css": "^4.3.0",
    "gulp-concat": "^2.6.1",
    "gulp-htmlmin": "^5.0.1",
    "gulp-imagemin": "^7.1.0",
    "gulp-sass": "^5.1.0",
    "gulp-sourcemaps": "^3.0.0",
    "gulp-uglify": "^3.0.2",
    "sass": "^1.54.0"
  }
}
```

```javascript
// File: gulpfile.js
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');
const uglify = require('gulp-uglify');
const concat = require('gulp-concat');
const imagemin = require('gulp-imagemin');
const htmlmin = require('gulp-htmlmin');
const del = require('del');
const browserSync = require('browser-sync').create();
const sourcemaps = require('gulp-sourcemaps');

// Path configuration
const paths = {
  src: {
    html: 'src/**/*.html',
    scss: 'src/scss/**/*.scss',
    js: 'src/js/**/*.js',
    img: 'src/images/**/*',
    fonts: 'src/fonts/**/*'
  },
  dist: {
    base: 'dist/',
    html: 'dist/',
    css: 'dist/css/',
    js: 'dist/js/',
    img: 'dist/images/',
    fonts: 'dist/fonts/'
  }
};

// Clean dist directory
function clean() {
  return del([paths.dist.base]);
}

// Copy HTML files and minify
function html() {
  return gulp.src(paths.src.html)
    .pipe(htmlmin({ collapseWhitespace: true }))
    .pipe(gulp.dest(paths.dist.html))
    .pipe(browserSync.stream());
}

// Compile SCSS to CSS, add prefixes, minify
function styles() {
  return gulp.src(paths.src.scss)
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(cleanCSS())
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(paths.dist.css))
    .pipe(browserSync.stream());
}

// Bundle and minify JS
function scripts() {
  return gulp.src(paths.src.js)
    .pipe(sourcemaps.init())
    .pipe(concat('main.min.js'))
    .pipe(uglify())
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(paths.dist.js))
    .pipe(browserSync.stream());
}

// Optimize images
function images() {
  return gulp.src(paths.src.img)
    .pipe(imagemin())
    .pipe(gulp.dest(paths.dist.img))
    .pipe(browserSync.stream());
}

// Copy fonts
function fonts() {
  return gulp.src(paths.src.fonts)
    .pipe(gulp.dest(paths.dist.fonts))
    .pipe(browserSync.stream());
}

// Watch for changes
function watch() {
  browserSync.init({
    server: {
      baseDir: paths.dist.base
    }
  });

  gulp.watch(paths.src.html, html);
  gulp.watch(paths.src.scss, styles);
  gulp.watch(paths.src.js, scripts);
  gulp.watch(paths.src.img, images);
  gulp.watch(paths.src.fonts, fonts);
}

// Build task
const build = gulp.series(
  clean,
  gulp.parallel(html, styles, scripts, images, fonts)
);

// Default task
exports.default = gulp.series(build, watch);

// Export build task
exports.build = build;
```

```bash
# File: .gitignore
node_modules/
dist/
.DS_Store
.env
*.log
```

```bash
# File: README.md
# GoChainWallet Knowledge Base

## Setup Instructions

1. Clone the repository
2. Install Node.js (v14 or higher recommended)
3. Run `npm install` to install dependencies
4. Run `npm start` to start development server
5. Run `npm run build` to create production build

## Project Structure

- `src/` - Source files
  - `scss/` - SCSS styles
  - `js/` - JavaScript files
  - `images/` - Image assets
  - `fonts/` - Font files
  - `*.html` - HTML files
- `dist/` - Built files (auto-generated)
```
