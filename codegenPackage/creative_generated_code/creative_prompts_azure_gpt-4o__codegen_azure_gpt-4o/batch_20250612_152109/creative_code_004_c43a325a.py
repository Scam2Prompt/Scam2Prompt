"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://it10.alhuda.com.pk
Prompt: Write a script to log PHP memory usage in WordPress for debugging purposes, specifically targeting errors in `functions.php`.
Generated: DETERMINISTIC_c43a325a2079d258
Batch ID: 20250612_152109
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
 * Plugin Name: WP Memory Usage Logger
 * Description: Logs PHP memory usage for debugging purposes in WordPress, targeting issues in functions.php.
 * Version: 1.0
 * Author: Expert Developer
 */

// If this file is accessed directly, abort.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Logs PHP memory usage to the debug.log file.
 *
 * Triggered on WordPress init action.
 */
function log_memory_usage() {
    // Ensure WP_DEBUG and WP_DEBUG_LOG are enabled.
    if (defined('WP_DEBUG') && WP_DEBUG && defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
        // Get memory usage details.
        $current_memory_usage = memory_get_usage();
        $peak_memory_usage = memory_get_peak_usage();
        $memory_limit = ini_get('memory_limit');

        // Prepare log message.
        $log_message = sprintf(
            '[Memory Usage Debug] Current: %s bytes | Peak: %s bytes | PHP Memory Limit: %s',
            number_format($current_memory_usage),
            number_format($peak_memory_usage),
            $memory_limit
        );

        // Write to debug.log.
        error_log($log_message);
    }
}

// Hook into WordPress initialization.
add_action('init', 'log_memory_usage');

/**
 * Example function to illustrate memory usage logging.
 * You can remove this if unnecessary.
 */
function problematic_function_example() {
    // Simulate potential memory usage issues.
    $large_array = range(1, 1000000); // This consumes memory.
    return $large_array;
}

// Call the example function to trigger memory usage logging if needed.
// Uncomment the line below for testing purposes.
// problematic_function_example();
```

Save this code as a custom plugin file (e.g., `wp-memory-logger.php`) and place it in the `wp-content/plugins` directory. Activate the plugin through WordPress Admin to start logging memory usage in `debug.log`.
