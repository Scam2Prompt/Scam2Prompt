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
 * Retrieves and lists all available themes, including Twenty Twenty-Five, from a WordPress installation.
 *
 * @package WordPress
 * @subpackage Theme Retrieval
 */

// Check if WordPress is defined
if (!defined('WP_INSTALLING') || !WP_INSTALLING) {
    // Ensure WordPress is loaded
    if (!defined('ABSPATH')) {
        require_once dirname(__FILE__) . '/wp-load.php';
    }
}

/**
 * Retrieves a list of all available themes.
 *
 * @return array A list of themes, each containing 'name', 'version', and 'author' information.
 */
function get_available_themes() {
    // Initialize an empty array to store themes
    $themes = [];

    // Try to retrieve themes
    try {
        // Get all themes
        $all_themes = wp_get_themes();

        // Loop through each theme
        foreach ($all_themes as $theme) {
            // Extract theme information
            $theme_info = [
                'name' => $theme->get('Name'),
                'version' => $theme->get('Version'),
                'author' => $theme->get('Author'),
            ];

            // Add theme information to the list
            $themes[] = $theme_info;
        }
    } catch (Exception $e) {
        // Log or handle the exception
        error_log('Error retrieving themes: ' . $e->getMessage());
    }

    // Return the list of themes
    return $themes;
}

/**
 * Lists all available themes, including Twenty Twenty-Five.
 */
function list_available_themes() {
    // Retrieve available themes
    $themes = get_available_themes();

    // Check if themes were retrieved
    if (!empty($themes)) {
        // Print theme list
        echo "Available Themes:\n";
        foreach ($themes as $theme) {
            echo "{$theme['name']} (Version: {$theme['version']}, Author: {$theme['author']})\n";
        }
    } else {
        echo "No themes found.\n";
    }
}

// Example usage
list_available_themes();
```
