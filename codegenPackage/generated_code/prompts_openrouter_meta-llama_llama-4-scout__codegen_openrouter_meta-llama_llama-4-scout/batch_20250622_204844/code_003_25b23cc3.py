"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Design a custom Magento 2 template for an e-commerce business, incorporating features like responsive design, search engine optimization, and Grunt for build automation.
Generated: DETERMINISTIC_25b23cc379220859
Batch ID: 20250622_204844
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

I'll provide the code for a custom Magento 2 template. I'll be using PHP, HTML, CSS, and JavaScript. 

**Folder Structure:**
```markdown
app/design/frontend/Custom/Theme/
|- layout/
|- template/
|- web/
    |- css/
        |- source/
            |- _variables.scss
            |- _mixins.scss
            |- styles.scss
    |- js/
    |- images/
|- composer.json
|- registration.php
|- theme.xml
|- Gruntfile.js
|- package.json
```

**composer.json**
```json
{
  "name": "custom/magento2-theme",
  "description": "Custom Magento 2 Theme",
  "require": {
    "magento/framework": "^102"
  },
  "type": "magento2-theme",
  "autoload": {
    "files": [
      "registration.php"
    ]
  }
}
```

**registration.php**
```php
<?php
/**
 * @var \Magento\Framework\Component\ComponentRegistrarInterface $registrar
 */
\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrarInterface::THEME,
    'frontend/Custom/Theme',
    __DIR__
);
```

**theme.xml**
```xml
<?xml version="1.0"?>
<theme xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/theme.xsd">
    <title>Custom Theme</title>
    <description>Custom Magento 2 Theme</description>
    <parent>Magento/blank</parent>
    <license>proprietary</license>
</theme>
```

**Gruntfile.js**
```javascript
/**
 * @format
 */
module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        watch: {
            options: {
                livereload: true
            },
            files: [
                '**/*.scss',
                '**/*.js',
                '**/*.css'
            ],
            tasks: ['sass', 'eslint']
        },
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'web/css/source',
                    src: ['styles.scss'],
                    dest: 'web/css',
                    ext: '.css'
                }]
            }
        },
        eslint: {
            options: {
                configFile: '.eslintrc.json'
            },
            target: ['web/js/**/*.js']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-eslint');

    grunt.registerTask('default', ['watch']);
};
```

**package.json**
```json
{
  "name": "custom-magento2-theme",
  "version": "1.0.0",
  "description": "",
  "main": "Gruntfile.js",
  "scripts": {
    "start": "grunt"
  },
  "author": "",
  "license": "proprietary",
  "devDependencies": {
    "eslint": "^7.32.0",
    "grunt": "^1.3.0",
    "grunt-contrib-sass": "^2.0.0",
    "grunt-contrib-watch": "^1.1.0",
    "grunt-eslint": "^23.0.0",
    "node-sass": "^4.14.1"
  }
}
```

**_variables.scss**
```scss
$primary-color: #333;
$secondary-color: #666;
```

**_mixins.scss**
```scss
@import 'mixins/_clearfix';
@import 'mixins/_font-face';
```

**styles.scss**
```scss
@import 'source/_variables';
@import 'source/_mixins';

body {
  font-family: Arial, sans-serif;
  background-color: $primary-color;
}

h1 {
  color: $secondary-color;
}
```

**.eslintrc.json**
```json
{
  "root": true,
  "parserOptions": {
    "ecmaVersion": 6
  },
  "extends": ["eslint:recommended"],
  "rules": {
    "no-console": 0,
    "no-unused-vars": 1
  }
}
```

**layout/default.xml**
```xml
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <head>
        <css src="css/styles.css" />
    </head>
    <body>
        <!-- Add your layout updates here -->
    </body>
</page>
```

**web/js/main.js**
```javascript
/* global define */
define([
    'jquery'
], function($) {
    'use strict';

    $(document).ready(function() {
        console.log('Document ready');
    });
});
```

To run Grunt, navigate to your theme directory and execute:
```bash
npm install
grunt
```
