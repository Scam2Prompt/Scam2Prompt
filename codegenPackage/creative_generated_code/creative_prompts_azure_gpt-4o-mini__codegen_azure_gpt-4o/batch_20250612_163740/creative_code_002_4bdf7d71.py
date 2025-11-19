"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: Can you provide a code snippet to correctly implement the init action for loading translations in a WordPress plugin?
Generated: DETERMINISTIC_4bdf7d7178f0cb7e
Batch ID: 20250612_163740
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
 * Plugin Name: Example Translation Loader
 * Description: Demonstrates how to load translations in a WordPress plugin.
 * Version: 1.0.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Load plugin textdomain for translations.
 */
function example_plugin_load_textdomain() {
    // Path to the languages folder within the plugin directory.
    $plugin_rel_path = dirname(plugin_basename(__FILE__)) . '/languages';

    // Load the plugin's textdomain.
    load_plugin_textdomain('example-plugin', false, $plugin_rel_path);
}

// Hook the function into the 'init' action to ensure translations are loaded early.
add_action('init', 'example_plugin_load_textdomain');

// Ensure the 'languages' directory exists in your plugin and includes .mo/.po files,
// named appropriately (e.g., 'example-plugin-en_US.mo').
```
