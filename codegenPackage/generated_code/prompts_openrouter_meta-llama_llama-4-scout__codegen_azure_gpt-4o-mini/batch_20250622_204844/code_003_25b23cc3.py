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

```xml
<!-- app/design/frontend/Vendor/theme/Magento_Theme/layout/default.xml -->
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <head>
        <title>Your Store Title</title>
        <meta name="description" content="Your Store Description" />
        <link rel="stylesheet" href="css/styles.css" />
    </head>
    <body>
        <referenceContainer name="header.container">
            <block class="Magento\Framework\View\Element\Template" name="custom.header" template="Magento_Theme::html/header.phtml"/>
        </referenceContainer>
        <referenceContainer name="content">
            <block class="Magento\Framework\View\Element\Template" name="custom.content" template="Magento_Theme::html/content.phtml"/>
        </referenceContainer>
        <referenceContainer name="footer.container">
            <block class="Magento\Framework\View\Element\Template" name="custom.footer" template="Magento_Theme::html/footer.phtml"/>
        </referenceContainer>
    </body>
</page>
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/templates/html/header.phtml

/** 
 * Custom Header Template
 * 
 * This template renders the header of the website, including the logo and navigation.
 */
?>
<header>
    <div class="logo">
        <a href="<?= $block->getUrl() ?>">
            <img src="<?= $block->getViewFileUrl('images/logo.png') ?>" alt="Store Logo" />
        </a>
    </div>
    <nav>
        <!-- Add navigation links here -->
    </nav>
</header>
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/templates/html/content.phtml

/** 
 * Custom Content Template
 * 
 * This template is used for rendering the main content area of the page.
 */
?>
<main>
    <h1>Welcome to Our Store</h1>
    <p>Your content goes here.</p>
</main>
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/templates/html/footer.phtml

/** 
 * Custom Footer Template
 * 
 * This template renders the footer of the website, including copyright information.
 */
?>
<footer>
    <p>&copy; <?= date('Y') ?> Your Store Name. All rights reserved.</p>
</footer>
```

```json
// Gruntfile.js
module.exports = function(grunt) {
    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        less: {
            development: {
                options: {
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    "css/styles.css": "less/styles.less" // destination file and source file
                }
            }
        },
        watch: {
            files: ['less/**/*.less'],
            tasks: ['less']
        }
    });

    // Load the plugin that provides the "less" task
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s)
    grunt.registerTask('default', ['less', 'watch']);
};
```

```less
// less/styles.less
@import "variables.less"; // Import variables for colors, fonts, etc.

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background: @header-bg-color;
    padding: 20px;
}

footer {
    background: @footer-bg-color;
    padding: 10px;
    text-align: center;
}
```

```json
// package.json
{
    "name": "magento2-custom-theme",
    "version": "1.0.0",
    "devDependencies": {
        "grunt": "^1.4.1",
        "grunt-contrib-less": "^2.0.0",
        "grunt-contrib-watch": "^1.1.0"
    }
}
```

```bash
# Installation commands
npm install
```

```bash
# To run the Grunt tasks
grunt
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/registration.php

use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::THEME,
    'frontend/Vendor/theme',
    __DIR__
);
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/etc/view.xml

/** 
 * View configuration for the custom theme
 */
<view xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/etc/view.xsd">
    <media>
        <images>
            <image id="logo" src="images/logo.png" />
        </images>
    </media>
</view>
```

```php
<?php
// app/design/frontend/Vendor/theme/Magento_Theme/etc/frontend/di.xml

/** 
 * Dependency Injection configuration for the custom theme
 */
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Magento\Framework\View\Element\Template">
        <arguments>
            <argument name="template" xsi:type="string">Magento_Theme::html/content.phtml</argument>
        </arguments>
    </type>
</config>
```

This code provides a basic structure for a custom Magento 2 theme with responsive design, SEO-friendly elements, and Grunt for build automation. Ensure to replace `Vendor` and `theme` with your actual vendor and theme names.
