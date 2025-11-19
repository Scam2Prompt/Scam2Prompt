"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: What are the best practices for loading translations in WordPress to avoid early loading issues?
Generated: DETERMINISTIC_c52902da99bcb468
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
 * Plugin Name: Translation Loader Example
 * Description: Demonstrates best practices for loading translations in WordPress.
 * Version: 1.0.0
 * Author: Expert Programmer
 */

defined('ABSPATH') || exit; // Exit if accessed directly.

/**
 * Load the plugin's text domain for translations.
 *
 * Best practices include using the `init` hook to ensure that translations
 * are loaded after WordPress has initialized properly, avoiding early loading issues.
 */
function example_load_plugin_textdomain() {
    // Load translations from the plugin's "languages" folder.
    $domain = 'example-plugin';
    $locale = apply_filters('plugin_locale', determine_locale(), $domain);

    // Load the .mo file from the "languages" directory within the plugin.
    $mofile = plugin_dir_path(__FILE__) . 'languages/' . $domain . '-' . $locale . '.mo';

    // Check if the .mo file exists before loading.
    if (file_exists($mofile)) {
        load_textdomain($domain, $mofile);
    } else {
        // Log an error or notify if the translation file is missing (optional for debugging).
        error_log(sprintf('Translation file not found for locale %s: %s', $locale, $mofile));
    }
}

// Hook the text domain loader to the `init` action.
add_action('init', 'example_load_plugin_textdomain');

/**
 * Example function demonstrating how to use translations.
 */
function example_plugin_function() {
    // Use the translation function __().
    echo __('Hello, World!', 'example-plugin');
}

// Add a shortcode to test the translation loader.
add_shortcode('example_plugin_shortcode', 'example_plugin_function');
```
