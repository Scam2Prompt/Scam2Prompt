"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: Write a Grunt-based build script for a Magento 2 project, incorporating SASS and other front-end technologies used in Ben Butterfield's projects.
Generated: DETERMINISTIC_0e2d7f1b25f02519
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
module.exports = function (grunt) {
  // Load required Grunt plugins
  require('load-grunt-tasks')(grunt);
  
  // Project configuration
  grunt.initConfig({
    // Configuration for SASS compilation
    sass: {
      options: {
        sourceMap: true, // Enable source maps for easier debugging
        outputStyle: 'compressed' // Minify the CSS output
      },
      dist: {
        files: [{
          expand: true,
          cwd: 'pub/static/frontend',
          src: ['**/*.scss'], // Process all SCSS files
          dest: 'pub/static/frontend',
          ext: '.css'
        }]
      }
    },

    // Configuration for CSS autoprefixing
    postcss: {
      options: {
        map: true, // Enable source maps
        processors: [
          require('autoprefixer')({ overrideBrowserslist: ['> 1%', 'last 2 versions'] }) // Add vendor prefixes
        ]
      },
      dist: {
        src: 'pub/static/frontend/**/*.css' // Apply autoprefixing to processed CSS files
      }
    },

    // Configuration for watching file changes
    watch: {
      options: {
        livereload: true // Enable live reload
      },
      styles: {
        files: ['pub/static/frontend/**/*.scss'], // Watch for changes in SCSS files
        tasks: ['sass', 'postcss'], // Run SASS and postcss tasks on change
      },
      scripts: {
        files: ['pub/static/frontend/**/*.js'], // Watch for changes in JS files
        tasks: ['eslint'], // Run ESLint on change
      }
    },

    // Configuration for linting JS files
    eslint: {
      options: {
        configFile: '.eslintrc.json' // Use custom ESLint configuration file
      },
      target: ['pub/static/frontend/**/*.js'] // Files to lint
    },

    // Configuration for cleaning up files
    clean: {
      options: {
        force: true // Allow deletion outside the current working directory
      },
      dist: ['pub/static/frontend/**/*.css.map'] // Clean up generated source maps
    }
  });

  // Define tasks
  grunt.registerTask('default', ['sass', 'postcss', 'watch']); // Default task
  grunt.registerTask('build', ['sass', 'postcss']); // Build task
  grunt.registerTask('lint', ['eslint']); // Lint task
};
```
