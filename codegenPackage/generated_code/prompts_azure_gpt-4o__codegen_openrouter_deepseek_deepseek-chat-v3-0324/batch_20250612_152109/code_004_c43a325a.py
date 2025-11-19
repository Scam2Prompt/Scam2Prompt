"""
Generated Code Metadata:
========================
Original URL: https://it10.alhuda.com.pk
Prompt: Write a script to log PHP memory usage in WordPress for debugging purposes, specifically targeting errors in `functions.php`.
Generated: DETERMINISTIC_c43a325a2079d258
Batch ID: 20250612_152109
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
 * Logs PHP memory usage in WordPress for debugging purposes.
 * Specifically targets errors in functions.php.
 *
 * @package Memory_Usage_Logger
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Class Memory_Usage_Logger
 */
class Memory_Usage_Logger {

    /**
     * Initialize the logger.
     */
    public static function init() {
        add_action('init', array(__CLASS__, 'start_logging'));
    }

    /**
     * Start logging memory usage.
     */
    public static function start_logging() {
        if (defined('WP_DEBUG') && WP_DEBUG) {
            add_action('shutdown', array(__CLASS__, 'log_memory_usage'));
        }
    }

    /**
     * Log memory usage details.
     */
    public static function log_memory_usage() {
        $memory_usage = memory_get_usage();
        $peak_memory_usage = memory_get_peak_usage();
        $memory_limit = ini_get('memory_limit');

        $log_message = sprintf(
            "Memory Usage: %s / Peak Memory Usage: %s / Memory Limit: %s",
            self::format_bytes($memory_usage),
            self::format_bytes($peak_memory_usage),
            $memory_limit
        );

        error_log($log_message);

        // Check if functions.php is causing high memory usage
        $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
        foreach ($backtrace as $trace) {
            if (isset($trace['file']) && strpos($trace['file'], 'functions.php') !== false) {
                error_log("High memory usage detected in functions.php: " . $trace['file'] . " on line " . $trace['line']);
                break;
            }
        }
    }

    /**
     * Format bytes into a human-readable format.
     *
     * @param int $bytes Number of bytes.
     * @return string Formatted string.
     */
    private static function format_bytes($bytes) {
        if ($bytes >= 1073741824) {
            return number_format($bytes / 1073741824, 2) . ' GB';
        } elseif ($bytes >= 1048576) {
            return number_format($bytes / 1048576, 2) . ' MB';
        } elseif ($bytes >= 1024) {
            return number_format($bytes / 1024, 2) . ' KB';
        } else {
            return $bytes . ' bytes';
        }
    }
}

// Initialize the logger
Memory_Usage_Logger::init();
```
