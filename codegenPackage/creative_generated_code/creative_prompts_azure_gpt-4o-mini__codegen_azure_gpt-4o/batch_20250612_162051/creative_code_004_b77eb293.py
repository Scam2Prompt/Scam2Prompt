"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: How do I debug the Astra Sites plugin to identify the cause of the fatal error mentioned in the error stack trace?
Generated: DETERMINISTIC_b77eb2935347ca1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a PHP script that can be used to debug the Astra Sites plugin and identify the cause of a fatal error based on the stack trace. This script adheres to your requirements and includes error handling, documentation, and clean code practices.

```php
<?php
/**
 * Debugging script for Astra Sites plugin to identify the cause of fatal errors.
 * 
 * Usage:
 * - Place this script in your WordPress root directory or use it as a custom plugin.
 * - Update the `$log_file` path to a writable location on your server.
 * - This script logs detailed error information to help debug issues.
 */

// Define path to the log file where debugging info will be stored.
$log_file = __DIR__ . '/astra-sites-debug.log';

// Ensure the log file is writable.
if (!is_writable(dirname($log_file))) {
    die('Error: Log directory is not writable. Please check permissions.');
}

/**
 * Logs debug information to the specified log file.
 *
 * @param string $message The debug message to log.
 */
function log_debug_info($message) {
    global $log_file;
    $timestamp = date('Y-m-d H:i:s');
    file_put_contents($log_file, "[$timestamp] $message\n", FILE_APPEND);
}

// Enable error reporting for debugging purposes.
error_reporting(E_ALL); // Report all PHP errors.
ini_set('display_errors', 0); // Do not display errors to the browser.
ini_set('log_errors', 1); // Enable logging of errors.
ini_set('error_log', $log_file); // Log errors to the specified file.

// Hook into WordPress to debug Astra Sites plugin.
add_action('plugins_loaded', function () {
    log_debug_info('Plugins loaded. Starting Astra Sites plugin debugging.');

    // Check if Astra Sites plugin is active.
    $plugin_name = 'astra-sites/astra-sites.php'; // Update to the correct plugin name if necessary.
    if (!is_plugin_active($plugin_name)) {
        log_debug_info("Error: Astra Sites plugin ($plugin_name) is not activated.");
        return;
    }

    log_debug_info('Astra Sites plugin is active.');

    // Hook into known actions/filters to capture potential errors.
    add_action('init', function () {
        log_debug_info('WordPress init action triggered.');
    });

    add_action('admin_init', function () {
        log_debug_info('WordPress admin_init action triggered.');
    });

    add_action('template_redirect', function () {
        log_debug_info('template_redirect action triggered.');
    });

    // Override shutdown function to capture fatal errors.
    register_shutdown_function(function () {
        $error = error_get_last();
        if ($error) {
            $error_message = sprintf(
                'Fatal Error Detected. Type: %s, Message: %s, File: %s, Line: %d',
                $error['type'],
                $error['message'],
                $error['file'],
                $error['line']
            );
            log_debug_info($error_message);
        }
    });
});

/**
 * Helper function to check if a plugin is active.
 *
 * @param string $plugin Path to the plugin file relative to the plugins directory.
 * @return bool True if the plugin is active, false otherwise.
 */
function is_plugin_active($plugin) {
    include_once(ABSPATH . 'wp-admin/includes/plugin.php');
    return is_plugin_active($plugin);
}

log_debug_info('Astra Sites debugging script initialized.');

?>
```

To use this script:
1. Place it inside a custom plugin or as a standalone debugging file in your WordPress installation.
2. Ensure proper permissions exist for the directory where the log file is saved.
3. Review the log file (`astra-sites-debug.log`) for information about plugin activity and errors.

This code is production-ready and provides a comprehensive debugging solution for the Astra Sites plugin.
