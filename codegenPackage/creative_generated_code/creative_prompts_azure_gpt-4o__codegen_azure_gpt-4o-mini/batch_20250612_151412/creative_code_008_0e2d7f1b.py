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
// Gruntfile.js for Magento 2 Project
module.exports = function(grunt) {

    // Load required Grunt tasks
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-copy');

    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        // Compile SASS to CSS
        sass: {
            options: {
                sourceMap: true,
                outputStyle: 'expanded' // can also be 'compressed'
            },
            dist: {
                files: [{
                    expand: true, // Enable dynamic expansion
                    cwd: 'src/scss/', // Source folder
                    src: ['**/*.scss'], // Source files
                    dest: 'pub/static/frontend/Magento/your_theme/css/', // Destination folder
                    ext: '.css' // Destination file extension
                }]
            }
        },

        // Minify CSS files
        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'pub/static/frontend/Magento/your_theme/css/',
                    src: ['*.css', '!*.min.css'], // Exclude minified files
                    dest: 'pub/static/frontend/Magento/your_theme/css/',
                    ext: '.min.css'
                }]
            }
        },

        // Minify JavaScript files
        uglify: {
            my_target: {
                files: [{
                    expand: true,
                    cwd: 'src/js/', // Source folder
                    src: '**/*.js', // Source files
                    dest: 'pub/static/frontend/Magento/your_theme/js/', // Destination folder
                    ext: '.min.js' // Destination file extension
                }]
            }
        },

        // Optimize images
        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'src/images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'pub/static/frontend/Magento/your_theme/images/'
                }]
            }
        },

        // Watch for changes in files
        watch: {
            sass: {
                files: ['src/scss/**/*.scss'], // Watch SASS files
                tasks: ['sass', 'cssmin'], // Tasks to run
                options: {
                    spawn: false, // Do not spawn a new process
                }
            },
            js: {
                files: ['src/js/**/*.js'], // Watch JS files
                tasks: ['uglify'],
                options: {
                    spawn: false,
                }
            },
            images: {
                files: ['src/images/**/*.{png,jpg,gif}'], // Watch images
                tasks: ['imagemin'],
                options: {
                    spawn: false,
                }
            }
        }
    });

    // Register default task
    grunt.registerTask('default', ['sass', 'cssmin', 'uglify', 'imagemin']);

    // Handle errors gracefully
    grunt.event.on('grunt.log.error', function(err) {
        grunt.log.error('Error during task execution: ' + err);
    });

};
```
