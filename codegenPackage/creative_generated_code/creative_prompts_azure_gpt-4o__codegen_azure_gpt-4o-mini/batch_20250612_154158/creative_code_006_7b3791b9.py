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
/**
 * Deactivate all plugins and themes in a WordPress installation to identify the source of a critical error.
 * 
 * This script can be utilized in a WordPress environment to safely deactivate all plugins 
 * and switch to a default theme, helping diagnose issues caused by plugins or themes.
 */

// Load WordPress environment
require_once('wp-load.php');

// Function to deactivate all plugins
function deactivate_all_plugins() {
    // Check user capabilities for safety
    if (!current_user_can('activate_plugins')) {
        return new WP_Error('permission_denied', 'You do not have permission to deactivate plugins.');
    }

    // Get all active plugins
    $active_plugins = get_option('active_plugins');

    // Deactivate each plugin
    foreach ($active_plugins as $plugin) {
        deactivate_plugins($plugin);
    }

    // Clear the cache
    wp_cache_flush();
    
    return true; // Return true on successful deactivation
}

// Function to switch to a default theme
function switch_to_default_theme() {
    // Check user capabilities for safety
    if (!current_user_can('switch_themes')) {
        return new WP_Error('permission_denied', 'You do not have permission to switch themes.');
    }

    // Define the default theme (e.g., 'twentytwentyone')
    $default_theme = 'twentytwentyone';

    // Switch theme
    switch_theme($default_theme);
    
    return true; // Return true on successful theme switch
}

// Main execution block
try {
    // Deactivate all plugins
    $deactivate_plugins_result = deactivate_all_plugins();
    if (is_wp_error($deactivate_plugins_result)) {
        throw new Exception($deactivate_plugins_result->get_error_message());
    }

    // Switch to the default theme
    $switch_theme_result = switch_to_default_theme();
    if (is_wp_error($switch_theme_result)) {
        throw new Exception($switch_theme_result->get_error_message());
    }

    // Success message
    echo 'All plugins have been deactivated and the theme has been switched to the default theme.';

} catch (Exception $e) {
    // Handle errors gracefully
    error_log('Error: ' . $e->getMessage());
    echo 'An error occurred: ' . $e->getMessage();
}
?>
```
