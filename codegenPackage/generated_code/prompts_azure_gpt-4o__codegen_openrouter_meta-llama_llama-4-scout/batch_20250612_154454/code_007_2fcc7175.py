"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Provide a solution to suppress repetitive error messages in WordPress logs, such as those related to the `wp_is_block_theme` function in the `functions.php` file.
Generated: DETERMINISTIC_2fcc71755fd11fd7
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Suppress repetitive error messages in WordPress logs.
 *
 * This script will monitor and suppress repetitive error messages in WordPress logs.
 * It uses a cache to store the error messages that have already been logged.
 */

// Define a custom error handler
function suppress_repetitive_errors($errno, $errstr, $errfile, $errline) {
    // Check if error message is related to wp_is_block_theme function
    if (strpos($errstr, 'wp_is_block_theme') !== false) {
        // Use a cache to store error messages
        $cache_key = 'suppressed_errors';
        $suppressed_errors = wp_cache_get($cache_key);
        if (!is_array($suppressed_errors)) {
            $suppressed_errors = array();
        }

        // Check if error message has already been logged
        $error_hash = md5($errstr . $errfile . $errline);
        if (!in_array($error_hash, $suppressed_errors)) {
            // Log the error message
            error_log("Suppressing repetitive error: $errstr in $errfile on line $errline");

            // Add error message to cache
            $suppressed_errors[] = $error_hash;
            wp_cache_set($cache_key, $suppressed_errors);
        }
    } else {
        // Log the error message as usual
        trigger_error($errstr, $errno);
    }
}

// Set custom error handler
set_error_handler('suppress_repetitive_errors');

// Optional: Clear cache on daily basis
function clear_suppressed_errors_cache() {
    wp_cache_delete('suppressed_errors');
}

// Schedule cache clearing
add_action('wp_scheduled_delete', 'clear_suppressed_errors_cache');
```

```php
// Alternatively, you can use a class-based approach

class RepetitiveErrorSuppressor {
    private $cache_key;

    public function __construct() {
        $this->cache_key = 'suppressed_errors';
        set_error_handler(array($this, 'suppress_error'));
    }

    public function suppress_error($errno, $errstr, $errfile, $errline) {
        // Check if error message is related to wp_is_block_theme function
        if (strpos($errstr, 'wp_is_block_theme') !== false) {
            $suppressed_errors = $this->get_suppressed_errors();
            $error_hash = md5($errstr . $errfile . $errline);
            if (!in_array($error_hash, $suppressed_errors)) {
                // Log the error message
                error_log("Suppressing repetitive error: $errstr in $errfile on line $errline");

                // Add error message to cache
                $suppressed_errors[] = $error_hash;
                $this->set_suppressed_errors($suppressed_errors);
            }
        } else {
            // Log the error message as usual
            trigger_error($errstr, $errno);
        }
    }

    private function get_suppressed_errors() {
        $suppressed_errors = wp_cache_get($this->cache_key);
        if (!is_array($suppressed_errors)) {
            $suppressed_errors = array();
        }
        return $suppressed_errors;
    }

    private function set_suppressed_errors($suppressed_errors) {
        wp_cache_set($this->cache_key, $suppressed_errors);
    }

    public function clear_cache() {
        wp_cache_delete($this->cache_key);
    }
}

// Usage
$suppressor = new RepetitiveErrorSuppressor();

// Schedule cache clearing
add_action('wp_scheduled_delete', array($suppressor, 'clear_cache'));
```
