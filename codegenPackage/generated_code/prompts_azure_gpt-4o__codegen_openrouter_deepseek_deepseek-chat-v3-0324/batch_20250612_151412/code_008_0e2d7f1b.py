"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Write a Grunt-based build script for a Magento 2 project, incorporating SASS and other front-end technologies used in Ben Butterfield's projects.
Generated: DETERMINISTIC_0e2d7f1b25f02519
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
module.exports = function(grunt) {
    'use strict';

    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        // Clean task configuration
        clean: {
            var: {
                src: ['var/*']
            },
            pub: {
                src: ['pub/static/*']
            }
        },

        // SASS compilation configuration
        sass: {
            options: {
                sourceMap: true,
                outputStyle: 'compressed',
                includePaths: [
                    'node_modules/',
                    'app/design/frontend/'
                ]
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: 'app/design/frontend/<Vendor>/<theme>/web/css/source',
                    src: ['**/*.scss'],
                    dest: 'pub/static/frontend/<Vendor>/<theme>/<locale>/css',
                    ext: '.css'
                }]
            }
        },

        // PostCSS configuration for autoprefixer
        postcss: {
            options: {
                map: true,
                processors: [
                    require('autoprefixer')({
                        browsers: ['last 2 versions', 'ie >= 9']
                    })
                ]
            },
            dist: {
                src: 'pub/static/frontend/<Vendor>/<theme>/<locale>/css/*.css'
            }
        },

        // Watch task configuration
        watch: {
            sass: {
                files: ['app/design/frontend/<Vendor>/<theme>/web/css/source/**/*.scss'],
                tasks: ['sass', 'postcss']
            },
            js: {
                files: ['app/design/frontend/<Vendor>/<theme>/web/js/**/*.js'],
                tasks: ['uglify']
            }
        },

        // Uglify JS configuration
        uglify: {
            options: {
                sourceMap: true,
                preserveComments: 'some'
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: 'app/design/frontend/<Vendor>/<theme>/web/js',
                    src: ['**/*.js'],
                    dest: 'pub/static/frontend/<Vendor>/<theme>/<locale>/js',
                    ext: '.min.js'
                }]
            }
        },

        // Babel configuration for ES6+ transpilation
        babel: {
            options: {
                sourceMap: true,
                presets: ['@babel/preset-env']
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: 'app/design/frontend/<Vendor>/<theme>/web/js',
                    src: ['**/*.js'],
                    dest: 'pub/static/frontend/<Vendor>/<theme>/<locale>/js',
                    ext: '.js'
                }]
            }
        },

        // Image optimization configuration
        imagemin: {
            dynamic: {
                options: {
                    optimizationLevel: 3,
                    progressive: true
                },
                files: [{
                    expand: true,
                    cwd: 'app/design/frontend/<Vendor>/<theme>/web/images',
                    src: ['**/*.{png,jpg,gif,svg}'],
                    dest: 'pub/static/frontend/<Vendor>/<theme>/<locale>/images'
                }]
            }
        },

        // Copy static files configuration
        copy: {
            static: {
                files: [{
                    expand: true,
                    cwd: 'app/design/frontend/<Vendor>/<theme>/web',
                    src: ['**/*', '!**/*.scss', '!**/*.js'],
                    dest: 'pub/static/frontend/<Vendor>/<theme>/<locale>'
                }]
            }
        },

        // Concurrent task configuration
        concurrent: {
            dev: {
                tasks: ['watch:sass', 'watch:js'],
                options: {
                    logConcurrentOutput: true
                }
            }
        }
    });

    // Load Grunt plugins
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-postcss');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-babel');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-concurrent');

    // Register tasks
    grunt.registerTask('default', [
        'clean',
        'sass',
        'postcss',
        'babel',
        'uglify',
        'imagemin',
        'copy'
    ]);

    grunt.registerTask('dev', [
        'clean',
        'sass',
        'postcss',
        'babel',
        'uglify',
        'imagemin',
        'copy',
        'concurrent:dev'
    ]);
};
```
