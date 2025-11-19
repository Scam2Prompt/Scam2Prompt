"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Design a custom Magento 2 template for an e-commerce business, incorporating features like responsive design, search engine optimization, and Grunt for build automation.
Generated: DETERMINISTIC_25b23cc379220859
Batch ID: 20250622_204844
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://opensource.org/licenses/MIT": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

```php
<?php
/**
 * Custom Magento 2 Theme
 * 
 * @category    Design
 * @package     Magento_CustomTheme
 * @author      Developer Name
 * @license     https://opensource.org/licenses/MIT MIT License
 */

namespace Magento\CustomTheme\view\frontend\layout;

/**
 * Default layout handles
 */
class default_head_blocks
{
    /**
     * Add CSS and JS files
     *
     * @return void
     */
    public function beforeGenerateHtml(\Magento\Framework\View\Layout $layout)
    {
        $layout->getUpdate()->addHandle('custom_theme_head');
    }
}
```

```xml
<!-- app/design/frontend/Vendor/CustomTheme/Magento_Theme/layout/default_head_blocks.xml -->
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="robots" content="INDEX,FOLLOW"/>
        <css src="css/styles-m.css" media="all"/>
        <css src="css/styles-l.css" media="screen and (min-width: 768px)"/>
        <script src="js/custom.js"/>
    </head>
</page>
```

```xml
<!-- app/design/frontend/Vendor/CustomTheme/theme.xml -->
<theme xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Config/etc/theme.xsd">
    <title>Custom Theme</title>
    <parent>Magento/blank</parent>
    <media>
        <preview_image>media/preview.jpg</preview_image>
    </media>
</theme>
```

```scss
// app/design/frontend/Vendor/CustomTheme/web/css/source/_variables.less
@import 'source/lib/_lib.less'; // Magento UI library

// Theme variables
@theme__color__primary: #ff5501;
@theme__color__secondary: #006bb4;
@theme__font-family__base: 'Open Sans', sans-serif;
```

```scss
// app/design/frontend/Vendor/CustomTheme/web/css/source/_extend.less
.navigation {
    .level0 {
        > .level-top {
            text-transform: uppercase;
            font-weight: 600;
        }
    }
}

.page-main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}
```

```json
// app/design/frontend/Vendor/CustomTheme/package.json
{
  "name": "custom-theme",
  "version": "1.0.0",
  "description": "Custom Magento 2 Theme",
  "devDependencies": {
    "grunt": "^1.0.4",
    "grunt-contrib-less": "^2.0.0",
    "grunt-contrib-watch": "^1.1.0",
    "grunt-contrib-cssmin": "^3.0.0",
    "grunt-contrib-uglify": "^4.0.1"
  }
}
```

```js
// app/design/frontend/Vendor/CustomTheme/Gruntfile.js
module.exports = function(grunt) {
    grunt.initConfig({
        less: {
            development: {
                files: {
                    "web/css/styles.css": "web/css/source/styles.less"
                }
            }
        },
        watch: {
            styles: {
                files: ['web/css/source/**/*.less'],
                tasks: ['less'],
                options: {
                    spawn: false
                }
            }
        },
        cssmin: {
            target: {
                files: {
                    'web/css/styles.min.css': ['web/css/styles.css']
                }
            }
        },
        uglify: {
            options: {
                mangle: true
            },
            my_target: {
                files: {
                    'web/js/custom.min.js': ['web/js/custom.js']
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('default', ['less', 'cssmin', 'uglify']);
    grunt.registerTask('dev', ['watch']);
};
```

```xml
<!-- app/design/frontend/Vendor/CustomTheme/etc/view.xml -->
<view xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Config/etc/view.xsd">
    <media>
        <images module="Magento_Catalog">
            <image id="category_page_grid" type="small_image">
                <width>240</width>
                <height>300</height>
            </image>
            <image id="category_page_list" type="small_image">
                <width>240</width>
                <height>300</height>
            </image>
            <image id="product_base_image" type="image">
                <width>700</width>
                <height>700</height>
            </image>
        </images>
    </media>
</view>
```

```xml
<!-- app/design/frontend/Vendor/CustomTheme/Magento_Catalog/layout/catalog_product_view.xml -->
<page layout="1column" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceBlock name="page.main.title">
            <arguments>
                <argument name="css_class" xsi:type="string">product-title</argument>
            </arguments>
        </referenceBlock>
        <referenceContainer name="content">
            <container name="product.info.media" htmlTag="div" htmlClass="product media" before="product.info.main"/>
        </referenceContainer>
    </body>
</page>
```
