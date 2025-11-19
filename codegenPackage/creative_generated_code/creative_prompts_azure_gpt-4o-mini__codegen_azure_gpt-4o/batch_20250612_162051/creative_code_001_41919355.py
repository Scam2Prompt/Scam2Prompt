"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tinaalstrom.com
Prompt: Write a code snippet for a WordPress plugin that ensures translations are loaded at the init action to avoid early loading issues, as mentioned in the debugging notice on Tina Alstrøm's site.
Generated: DETERMINISTIC_41919355aa75dafa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Translation Loader Example
 * Description: Ensures translations are loaded at the init action to avoid early loading issues.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Load plugin textdomain at the correct action hook.
 */
function translation_loader_init() {
    // Load translation files from the plugin's "languages" directory.
    load_plugin_textdomain(
        'translation-loader-example', // Text domain.
        false,                         // No absolute path.
        dirname(plugin_basename(__FILE__)) . '/languages' // Path to translation files.
    );
}

// Hook into 'init' action to ensure proper loading timing.
add_action('init', 'translation_loader_init');
```
