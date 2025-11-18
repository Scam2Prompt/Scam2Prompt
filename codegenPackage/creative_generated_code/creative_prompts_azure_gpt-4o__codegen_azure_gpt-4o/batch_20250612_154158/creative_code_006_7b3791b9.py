"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.699539.com
Prompt: Provide steps and code snippets to safely deactivate plugins and themes in WordPress to identify the source of a critical error.
Generated: DETERMINISTIC_7b3791b995bc9fa3
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Safe Deactivation of Plugins and Themes in WordPress for Debugging Purposes

/**
 * Step 1: Define a function to deactivate all plugins.
 * This function iterates through all active plugins and deactivates them one by one.
 */
function deactivate_all_plugins() {
    // Get all active plugins
    $active_plugins = get_option('active_plugins');

    if (!empty($active_plugins)) {
        foreach ($active_plugins as $plugin) {
            // Deactivate each plugin safely
            deactivate_plugins($plugin, true); // Second argument ensures no redirection
        }
    }
}

/**
 * Step 2: Deactivate the active theme and switch to a default theme.
 * Recommended default themes include 'twentytwentyone', 'twentytwentytwo'.
 */
function switch_to_default_theme() {
    $default_themes = ['twentytwentyone', 'twentytwentytwo', 'twentytwentythree'];

    foreach ($default_themes as $theme) {
        if (wp_get_theme($theme)->exists()) {
            // Switch to the default theme
            switch_theme($theme);
            return;
        }
    }

    // If no default theme exists, log an error
    error_log('No default themes available to switch to.');
}

/**
 * Step 3: Hook the debugging functions to run on admin_init for safety.
 */
function debug_deactivate_plugins_and_theme() {
    // Ensure only administrators can trigger this
    if (!current_user_can('administrator')) {
        wp_die('Access denied. You must be an administrator to perform this action.');
    }

    // Debugging steps
    deactivate_all_plugins();
    switch_to_default_theme();

    // Notify the admin that plugins and themes have been deactivated
    add_action('admin_notices', function() {
        echo '<div class="notice notice-warning is-dismissible">';
        echo '<p>All plugins have been deactivated, and the theme has been switched to a default theme for debugging purposes.</p>';
        echo '</div>';
    });
}

// Hook the debugging process to the admin area
add_action('admin_init', 'debug_deactivate_plugins_and_theme');
?>
```
