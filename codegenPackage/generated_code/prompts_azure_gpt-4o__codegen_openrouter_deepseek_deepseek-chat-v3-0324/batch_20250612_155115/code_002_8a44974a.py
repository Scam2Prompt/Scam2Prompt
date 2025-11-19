"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Generate PHP code to retrieve and list all available themes, including Twenty Twenty-Five, from a WordPress installation.
Generated: DETERMINISTIC_8a44974a6ae12746
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Retrieves and lists all available themes in a WordPress installation.
 *
 * @package WordPress
 */

// Ensure WordPress environment is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * List all available WordPress themes including Twenty Twenty-Five.
 */
function list_all_wordpress_themes() {
    // Check if get_themes function exists (for WP < 3.4)
    if (!function_exists('wp_get_themes')) {
        $themes = get_themes();
    } else {
        $themes = wp_get_themes();
    }

    // Check if themes were retrieved successfully
    if (empty($themes)) {
        echo '<p>No themes found.</p>';
        return;
    }

    // Output the list of themes
    echo '<h2>Available WordPress Themes</h2>';
    echo '<ul>';

    foreach ($themes as $theme) {
        $theme_name = $theme->get('Name');
        $theme_version = $theme->get('Version');
        $theme_author = $theme->get('Author');

        echo '<li>';
        echo '<strong>' . esc_html($theme_name) . '</strong>';
        echo ' (Version: ' . esc_html($theme_version) . ')';
        echo ' by ' . esc_html($theme_author);
        echo '</li>';
    }

    echo '</ul>';
}

// Call the function to display themes
list_all_wordpress_themes();
```
