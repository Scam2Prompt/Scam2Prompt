"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s-tel.pl
Prompt: Can you provide a code snippet for setting the default language in WordPress during installation, referencing the language options available on s-tel.pl?
Generated: DETERMINISTIC_ed0e83f9183222c0
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
/**
 * Plugin Name: Default Language Setter
 * Description: A WordPress plugin to set the default language during installation process.
 * Version: 1.0
 * Author: DeveloperName
 */

// Ensure no direct access
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Sets default language during WordPress installation.
 */
function set_default_language() {
    // Reference language options available on s-tel.pl
    $available_languages = [
        'en_US' => 'English (United States)',
        'pl_PL' => 'Polish',
        'de_DE' => 'German',
        // Add additional languages as needed
    ];
    
    // Default language code (adjust as necessary)
    $default_language = 'pl_PL';

    // Validate if the default language exists in available languages
    if (array_key_exists($default_language, $available_languages)) {
        // Update the WordPress option to set the default language
        update_option('WPLANG', $default_language);
    } else {
        // Log an error message if the language is not valid
        error_log('Invalid default language specified: ' . $default_language);
    }
}

// Hook into WordPress installation
register_activation_hook(__FILE__, 'set_default_language');

/**
 * Provides admin notification about language settings after activation.
 */
function default_language_admin_notice() {
    $current_language = get_option('WPLANG', 'en_US');
    echo '<div class="notice notice-success is-dismissible">';
    echo '<p>Default language set to: ' . esc_html($current_language) . '</p>';
    echo '</div>';
}

// Add admin notice upon language change
add_action('admin_notices', 'default_language_admin_notice');
?>
```
