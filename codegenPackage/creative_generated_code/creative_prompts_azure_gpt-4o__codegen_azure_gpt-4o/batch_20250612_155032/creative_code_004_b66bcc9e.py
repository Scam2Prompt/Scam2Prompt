"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnbase.ltd
Prompt: Write PHP code to log errors from a WordPress plugin into a custom error log file for debugging purposes.
Generated: DETERMINISTIC_b66bcc9ed3e0e5df
Batch ID: 20250612_155032
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
 * Plugin Name: Custom Error Logger
 * Description: Logs errors into a custom log file for debugging purposes.
 * Version: 1.0
 * Author: Your Name
 */

// Define the custom log file location.
define('CUSTOM_ERROR_LOG_FILE', plugin_dir_path(__FILE__) . 'custom-error.log');

/**
 * Logs error messages to the custom error log file.
 *
 * @param string $message The error message to log.
 */
function log_plugin_error($message) {
    // Check if the log file is writable.
    if (!is_writable(CUSTOM_ERROR_LOG_FILE) && !file_exists(CUSTOM_ERROR_LOG_FILE)) {
        error_log("Custom Error Logger: Unable to write to log file. Check file permissions.", 0);
        return;
    }

    // Prepare timestamp and format error message.
    $timestamp = date('Y-m-d H:i:s');
    $formatted_message = "[{$timestamp}] ERROR: {$message}" . PHP_EOL;

    // Write the error message to the log file.
    file_put_contents(CUSTOM_ERROR_LOG_FILE, $formatted_message, FILE_APPEND | LOCK_EX);
}

/**
 * Example usage: Hook into WordPress plugin error handling.
 */
function handle_plugin_error_example() {
    try {
        // Simulate some plugin logic that may throw an exception.
        if (rand(0, 1)) {
            throw new Exception('Simulated plugin error occurred.');
        }

        // Perform normal plugin operations.
        // ...

    } catch (Exception $e) {
        // Log the error to the custom log file.
        log_plugin_error($e->getMessage());
    }
}

// Add an initialization action to demonstrate error logging.
add_action('init', 'handle_plugin_error_example');
```
