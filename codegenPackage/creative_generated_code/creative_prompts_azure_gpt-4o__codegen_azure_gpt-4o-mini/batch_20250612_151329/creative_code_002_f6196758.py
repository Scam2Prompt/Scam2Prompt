"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: Generate PHP code for loading translations in WordPress plugins during the `init` action, specifically addressing the error "_load_textdomain_just_in_time was called incorrectly."
Generated: DETERMINISTIC_f6196758644e1cd1
Batch ID: 20250612_151329
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
 * Plugin Name: My Custom Plugin
 * Description: A simple WordPress plugin to demonstrate loading translations correctly.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
defined('ABSPATH') || exit;

/**
 * Load the plugin's text domain for translations.
 *
 * This function hooks into the 'init' action to ensure that the text domain
 * is loaded correctly, addressing the _load_textdomain_just_in_time issue.
 */
function my_custom_plugin_load_textdomain() {
    // Specify the path to the language files
    $plugin_dir = plugin_dir_path(__FILE__) . 'languages/';
    $plugin_slug = 'my-custom-plugin';

    // Load the text domain
    // The second parameter is the domain, and the third is a path to the directory where .mo files are located
    $loaded = load_plugin_textdomain($plugin_slug, false, $plugin_dir);

    // Check if the text domain loaded successfully
    if (!$loaded) {
        error_log('Translation files not found for: ' . $plugin_slug);
    }
}

// Hook the function to the 'init' action
add_action('init', 'my_custom_plugin_load_textdomain');
```
