"""
Generated Code Metadata:
========================
Original URL: https://magentobuldozer.com
Prompt: "Develop a basic Magento 2 theme using LESS."
Generated: DETERMINISTIC_c801cf65c9ca5a9a
Batch ID: 20250622_212203
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

```plaintext
# Directory structure for a basic Magento 2 theme using LESS:
# app/design/frontend/VendorName/ThemeName/
# ├── etc
# │   └── view.xml
# ├── media
# │   └── preview.jpg
# ├── registration.php
# ├── theme.xml
# ├── web
# │   ├── css
# │   │   ├── source
# │   │   │   ├── _extend.less
# │   │   │   └── _theme.less
# │   └── images
# └── composer.json
```

### 1. `registration.php`
```php
<?php
/**
 * Theme registration file
 * Registers the theme with Magento
 */

use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::THEME,
    'frontend/VendorName/ThemeName',
    __DIR__
);
```

### 2. `theme.xml`
```xml
<?xml version="1.0"?>
<!-- Theme configuration file -->
<theme xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Config/etc/theme.xsd">
    <title>VendorName ThemeName</title> <!-- Theme title -->
    <parent>Magento/blank</parent> <!-- Inherit from Magento Blank theme -->
    <media>
        <preview_image>media/preview.jpg</preview_image> <!-- Theme preview image -->
    </media>
</theme>
```

### 3. `view.xml`
```xml
<?xml version="1.0"?>
<!-- View configuration file -->
<view xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Config/etc/view.xsd">
    <vars module="Magento_Theme">
        <var name="theme_color">#007bff</var> <!-- Example variable -->
    </vars>
</view>
```

### 4. `composer.json`
```json
{
    "name": "vendorname/themename",
    "description": "A basic Magento 2 theme using LESS",
    "require": {
        "php": "~7.4.0||~8.1.0",
        "magento/framework": "*"
    },
    "type": "magento2-theme",
    "version": "1.0.0",
    "license": [
        "OSL-3.0",
        "AFL-3.0"
    ],
    "autoload": {
        "files": [
            "registration.php"
        ]
    }
}
```

### 5. `web/css/source/_theme.less`
```less
// Define theme-specific variables here
@theme-color: #007bff;
@link-color: @theme-color;

// Example styling
body {
    background-color: lighten(@theme-color, 40%);
    color: darken(@theme-color, 20%);
}
```

### 6. `web/css/source/_extend.less`
```less
// Extend or override Magento Blank theme styles here
a {
    text-decoration: none;
    color: @link-color;

    &:hover {
        color: darken(@link-color, 10%);
    }
}
```

### 7. `media/preview.jpg`
- Add a preview image for your theme (e.g., a screenshot of your theme design).

---

### Notes:
- Replace `VendorName` and `ThemeName` with your desired vendor and theme names.
- Place the files in the appropriate directories as shown in the directory structure.
- Run the following commands to enable and deploy the theme:
  ```bash
  bin/magento setup:upgrade
  bin/magento setup:static-content:deploy -f
  bin/magento cache:clean
  ```
```
