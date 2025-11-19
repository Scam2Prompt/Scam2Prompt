"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s-tel.pl
Prompt: What are the steps to configure WordPress for multilingual support, specifically using the language selections mentioned on s-tel.pl?
Generated: DETERMINISTIC_20df9f4158f27ab3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// WordPress Configuration for Multilingual Support with Polylang Plugin

/**
 * This script automates the setup for multilingual support in WordPress 
 * using the Polylang plugin. It assumes Polylang is installed and activated.
 * Ensure you back up your database before running this script.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Hook into WordPress admin initialization
add_action('admin_init', function () {
    // Check if Polylang is active
    if (!is_plugin_active('polylang/polylang.php')) {
        error_log('Polylang plugin is not activated. Please install and activate it.');
        return;
    }

    // Define languages to configure (based on s-tel.pl's selection)
    $languages = [
        ['slug' => 'en', 'name' => 'English', 'locale' => 'en_US', 'rtl' => false],
        ['slug' => 'pl', 'name' => 'Polish', 'locale' => 'pl_PL', 'rtl' => false],
        ['slug' => 'de', 'name' => 'German', 'locale' => 'de_DE', 'rtl' => false],
    ];

    // Add languages to Polylang
    foreach ($languages as $language) {
        if (!pll_get_language($language['slug'])) {
            $result = pll_register_string(
                $language['name'], // Display name
                $language['slug'], // Slug
                $language['locale'], // Locale
                $language['rtl']    // Right-to-left flag
            );

            // Log errors if any
            if (is_wp_error($result)) {
                error_log('Failed to add language: ' . $language['slug'] . '. Error: ' . $result->get_error_message());
            }
        }
    }

    // Set the default language (e.g., English)
    $default_language = 'en'; // Change to the desired default language slug
    if (!pll_set_default_language($default_language)) {
        error_log('Failed to set the default language: ' . $default_language);
    }

    // Optional: Assign existing content to a language
    // Ensure you have a backup before running this on production!
    $default_post_language = $default_language; // Default content language
    $all_posts = get_posts(['numberposts' => -1, 'post_type' => 'post']);
    foreach ($all_posts as $post) {
        if (!pll_get_post_language($post->ID)) {
            pll_set_post_language($post->ID, $default_post_language);
        }
    }

    // Confirmation message
    error_log('Polylang multilingual configuration completed.');
});
```
