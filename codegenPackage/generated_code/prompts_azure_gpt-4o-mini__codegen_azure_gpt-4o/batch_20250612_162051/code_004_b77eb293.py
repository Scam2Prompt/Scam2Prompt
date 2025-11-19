"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: How do I debug the Astra Sites plugin to identify the cause of the fatal error mentioned in the error stack trace?
Generated: DETERMINISTIC_b77eb2935347ca1b
Batch ID: 20250612_162051
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
 * Debugging script for Astra Sites plugin to identify the cause of a fatal error.
 * 
 * This script hooks into WordPress's error handling and logs detailed information
 * about errors related to the Astra Sites plugin.
 * 
 * Usage:
 * 1. Place this script in your theme's `functions.php` file or as a custom plugin.
 * 2. Check the debug log file for error details.
 */

// Enable WordPress debugging if not already enabled.
if (!defined('WP_DEBUG')) {
    define('WP_DEBUG', true);
}
if (!defined('WP_DEBUG_LOG')) {
    define('WP_DEBUG_LOG', true);
}
if (!defined('WP_DEBUG_DISPLAY')) {
    define('WP_DEBUG_DISPLAY', false); // Prevent errors from displaying on the frontend.
}

// Log fatal errors to debug.log.
add_action('shutdown', function () {
    $error = error_get_last();
    if ($error && in_array($error['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR])) {
        // Check if the error is related to the Astra Sites plugin.
        if (strpos($error['file'], 'astra-sites') !== false) {
            error_log('--- Astra Sites Plugin Fatal Error Detected ---');
            error_log('Error Type: ' . $error['type']);
            error_log('Error Message: ' . $error['message']);
            error_log('Error File: ' . $error['file']);
            error_log('Error Line: ' . $error['line']);
            error_log('--- End of Error Log ---');
        }
    }
});

// Add a custom error handler for non-fatal errors.
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    // Check if the error is related to the Astra Sites plugin.
    if (strpos($errfile, 'astra-sites') !== false) {
        error_log('--- Astra Sites Plugin Non-Fatal Error Detected ---');
        error_log('Error Type: ' . $errno);
        error_log('Error Message: ' . $errstr);
        error_log('Error File: ' . $errfile);
        error_log('Error Line: ' . $errline);
        error_log('--- End of Error Log ---');
    }

    // Allow WordPress to handle the error if it's not suppressed.
    return false;
});

// Add a custom exception handler for uncaught exceptions.
set_exception_handler(function ($exception) {
    // Check if the exception is related to the Astra Sites plugin.
    if (strpos($exception->getFile(), 'astra-sites') !== false) {
        error_log('--- Astra Sites Plugin Uncaught Exception Detected ---');
        error_log('Exception Message: ' . $exception->getMessage());
        error_log('Exception File: ' . $exception->getFile());
        error_log('Exception Line: ' . $exception->getLine());
        error_log('--- End of Exception Log ---');
    }
});

// Log plugin activation and deactivation hooks for Astra Sites.
register_activation_hook('astra-sites/astra-sites.php', function () {
    error_log('--- Astra Sites Plugin Activated ---');
});

register_deactivation_hook('astra-sites/astra-sites.php', function () {
    error_log('--- Astra Sites Plugin Deactivated ---');
});

// Add a debug function to manually log plugin state.
if (!function_exists('debug_astra_sites_plugin')) {
    /**
     * Debug Astra Sites plugin state.
     * Call this function manually to log plugin state.
     */
    function debug_astra_sites_plugin()
    {
        if (is_plugin_active('astra-sites/astra-sites.php')) {
            error_log('--- Astra Sites Plugin is Active ---');
        } else {
            error_log('--- Astra Sites Plugin is Inactive ---');
        }
    }
}

// Example usage: Uncomment the line below to manually debug the plugin state.
// debug_astra_sites_plugin();
```
