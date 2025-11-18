"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://criterio.cl
Prompt: Write a script to programmatically switch between WordPress themes, such as "Twenty Twenty-Five," based on user roles or preferences.
Generated: DETERMINISTIC_c4f9678a5b3a7701
Batch ID: 20250612_154307
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
 * Plugin Name: Dynamic Theme Switcher
 * Description: A plugin to programmatically switch WordPress themes based on user roles or preferences.
 * Version: 1.0.0
 * Author: Your Name
 */

// Prevent direct access to the file for security purposes.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Switches the WordPress theme based on user roles or preferences.
 */
function switch_theme_based_on_user_role() {
    // Check if the user is logged in.
    if (is_user_logged_in()) {
        // Get the current logged-in user.
        $current_user = wp_get_current_user();

        // Check user roles and switch themes accordingly.
        if (in_array('administrator', $current_user->roles)) {
            // Switch to the theme "Twenty Twenty-Five" for administrators.
            $theme_to_switch = 'twentytwentyfive';
        } elseif (in_array('editor', $current_user->roles)) {
            // Switch to the theme "Twenty Twenty-Two" for editors.
            $theme_to_switch = 'twentytwentytwo';
        } else {
            // Switch to the default theme for all other roles.
            $theme_to_switch = 'twentytwentyone';
        }

        // Get the current theme.
        $current_theme = wp_get_theme()->get('TextDomain');

        // Switch theme only if it's different from the current one.
        if ($current_theme !== $theme_to_switch) {
            switch_theme($theme_to_switch);
        }
    } else {
        // For non-logged-in users, switch to a default theme.
        $default_theme = 'twentytwentythree';
        $current_theme = wp_get_theme()->get('TextDomain');

        if ($current_theme !== $default_theme) {
            switch_theme($default_theme);
        }
    }
}

// Hook into the 'init' action to check and switch themes.
add_action('init', 'switch_theme_based_on_user_role');

/**
 * Error handling: Ensure themes exist.
 */
function validate_theme_existence($theme_slug) {
    if (!wp_get_theme($theme_slug)->exists()) {
        error_log("The theme '{$theme_slug}' does not exist. Please ensure it is installed.");
        return false;
    }
    return true;
}

// Validate all themes used in the function.
add_action('admin_init', function () {
    $themes_to_validate = ['twentytwentyfive', 'twentytwentytwo', 'twentytwentyone', 'twentytwentythree'];

    foreach ($themes_to_validate as $theme) {
        validate_theme_existence($theme);
    }
});
```
