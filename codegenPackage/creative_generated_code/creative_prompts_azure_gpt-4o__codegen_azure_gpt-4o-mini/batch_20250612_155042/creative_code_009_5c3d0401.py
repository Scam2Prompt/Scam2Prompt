"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.167079.com
Prompt: Generate a WordPress function to safely deactivate all plugins when a critical error is encountered.
Generated: DETERMINISTIC_5c3d0401c26a7e2d
Batch ID: 20250612_155042
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
 * Safely deactivates all plugins when a critical error is encountered.
 *
 * This function should be hooked into an appropriate WordPress action.
 * It checks for critical errors using a custom flag and deactivates all plugins if needed.
 *
 * @return void
 */
function deactivate_all_plugins_on_critical_error() {
    // Check if the critical error flag is set.
    // This flag can be set by other parts of the code or plugins.
    if (defined('CRITICAL_ERROR_OCCURRED') && CRITICAL_ERROR_OCCURRED) {
        // Get all active plugins.
        $active_plugins = get_option('active_plugins');

        // Check if there are any active plugins to deactivate.
        if (!empty($active_plugins)) {
            // Deactivate all active plugins.
            deactivate_plugins($active_plugins);
        }
    }
}

// Hook the function to 'init', which runs early in the WordPress lifecycle.
add_action('init', 'deactivate_all_plugins_on_critical_error');

/**
 * Example of setting the critical error flag.
 * This should be called from within your error handling logic.
 */
function set_critical_error() {
    // Set the flag to indicate a critical error has occurred.
    define('CRITICAL_ERROR_OCCURRED', true);
}

// You may want to call this function when a critical error is detected.
```
