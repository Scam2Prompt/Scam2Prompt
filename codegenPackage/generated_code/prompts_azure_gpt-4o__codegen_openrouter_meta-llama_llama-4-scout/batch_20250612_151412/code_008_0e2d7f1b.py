"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Write a Grunt-based build script for a Magento 2 project, incorporating SASS and other front-end technologies used in Ben Butterfield's projects.
Generated: DETERMINISTIC_0e2d7f1b25f02519
Batch ID: 20250612_151412
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://gruntjs.com/creating-tasks": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Gruntfile.js

'use strict';

module.exports = function(grunt) {
  // Please see the Grunt documentation for more information regarding task
  // creation: http://gruntjs.com/creating-tasks

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration
    sass: {
      dist: {
        files: [{
          expand: true,
          cwd: 'web/scss',
          src: ['*.scss'],
          dest: 'web/css',
          ext: '.css'
        }]
      }
    },

    // Autoprefixer
    postcss: {
      options: {
        processors: [
          require('autoprefixer')({browsers: 'last 2 versions'})
        ]
      },
      dist: {
        files: [{
          expand: true,
          cwd: 'web/css',
          src: ['*.css'],
          dest: 'web/css',
          ext: '.css'
        }]
      }
    },

    // Uglify
    uglify: {
      options: {
        banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - <%= grunt.template.today("yyyy-mm-dd") %>\n' +
          '<%= pkg.homepage ? "* " + pkg.homepage + "\n" : "" %>' +
          '* Copyright <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>; Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n'
      },
      dist: {
        files: {
          'web/js/main.min.js': ['web/js/main.js']
        }
      }
    },

    // Watch
    watch: {
      css: {
        files: ['web/scss/**/*.scss'],
        tasks: ['sass', 'postcss']
      },
      js: {
        files: ['web/js/**/*.js'],
        tasks: ['uglify']
      }
    },

    // Clean
    clean: {
      dist: ['web/css/*.css', 'web/js/*.min.js']
    },

    // Copy
    copy: {
      dist: {
        files: [{
          expand: true,
          cwd: 'node_modules/jquery/dist',
          src: ['jquery.min.js'],
          dest: 'web/js'
        }]
      }
    }
  });

  // Load NPM tasks
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-postcss');

  // Default task
  grunt.registerTask('default', ['clean', 'copy', 'sass', 'postcss', 'uglify']);

  // Build task
  grunt.registerTask('build', ['clean', 'copy', 'sass', 'postcss', 'uglify']);

  // Dev task
  grunt.registerTask('dev', ['build', 'watch']);
};
```

```json
// package.json

{
  "name": "magento2-frontend",
  "version": "1.0.0",
  "description": "",
  "main": "Gruntfile.js",
  "scripts": {
    "build": "grunt build",
    "dev": "grunt dev"
  },
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "grunt": "^1.4.1",
    "grunt-contrib-clean": "^2.0.0",
    "grunt-contrib-copy": "^1.5.0",
    "grunt-contrib-sass": "^2.0.0",
    "grunt-contrib-uglify": "^4.0.1",
    "grunt-contrib-watch": "^1.1.0",
    "grunt-postcss": "^2.0.0",
    "autoprefixer": "^10.2.5"
  }
}
```
