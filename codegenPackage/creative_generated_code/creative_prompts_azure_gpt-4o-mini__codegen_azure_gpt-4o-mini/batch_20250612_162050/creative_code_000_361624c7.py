"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://broodroomstudios.com
Prompt: How can I use the `WP_USE_THEMES` constant in WordPress to manage theme loading?
Generated: DETERMINISTIC_361624c7b52bd59a
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
 * WordPress Theme Loader
 *
 * This script demonstrates how to manage theme loading using the WP_USE_THEMES constant.
 * It checks if themes should be loaded and then includes the appropriate theme's functions.
 */

// Define the WP_USE_THEMES constant to indicate whether to use themes
define('WP_USE_THEMES', true);

// Load WordPress core
require_once('wp-load.php');

// Check if the constant is set to true
if (WP_USE_THEMES) {
    // Get the current theme's directory
    $current_theme = wp_get_theme();

    // Check if the theme is valid
    if ($current_theme->exists()) {
        // Load the theme's functions.php file
        $functions_file = get_template_directory() . '/functions.php';

        // Check if the functions file exists
        if (file_exists($functions_file)) {
            require_once($functions_file);
        } else {
            // Handle error: functions.php file not found
            error_log('Error: functions.php file not found in theme directory: ' . $functions_file);
            echo 'Error loading theme functionality. Please check the theme files.';
        }
    } else {
        // Handle error: theme does not exist
        error_log('Error: Current theme does not exist: ' . $current_theme->get('Name'));
        echo 'Error: Active theme is invalid. Please activate a valid theme.';
    }
} else {
    // Handle case where themes are not being used
    echo 'Themes are not being used. Set WP_USE_THEMES to true to load theme functionalities.';
}
?>
```
