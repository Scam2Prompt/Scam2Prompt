"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://it10.alhuda.com.pk
Prompt: Write PHP code to increase the memory limit in a WordPress installation to resolve "Allowed memory size exhausted" errors.
Generated: DETERMINISTIC_d2a40b728f011860
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
 * Plugin Name: Increase Memory Limit
 * Description: A simple plugin to increase the memory limit in WordPress and resolve "Allowed memory size exhausted" errors.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// If this file is called directly, abort.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to increase memory limit.
 * This filter is applied to wp-config.php settings via the WordPress configuration.
 */
function increase_memory_limit() {
    // Define memory limit if not already set.
    if (!defined('WP_MEMORY_LIMIT')) {
        define('WP_MEMORY_LIMIT', '256M'); // Increase to 256MB for general use
    }

    // Define admin memory limit for backend processes if not already set.
    if (!defined('WP_MAX_MEMORY_LIMIT')) {
        define('WP_MAX_MEMORY_LIMIT', '512M'); // Increase to 512MB for admin tasks
    }
}

// Hook the function into 'init' action.
add_action('init', 'increase_memory_limit');

// Optional: Check if memory limit is properly set (useful for debugging).
function debug_memory_limit() {
    if (defined('WP_MEMORY_LIMIT')) {
        error_log('Memory Limit: ' . WP_MEMORY_LIMIT); // Output memory limit to error log.
    }
    if (defined('WP_MAX_MEMORY_LIMIT')) {
        error_log('Admin Memory Limit: ' . WP_MAX_MEMORY_LIMIT); // Output admin memory limit to error log.
    }
}

// Hook the debug function into 'init' for logging purposes (remove for production).
add_action('init', 'debug_memory_limit');
```

Save this code as a `.php` file (e.g., `increase-memory-limit.php`) and place it in the `wp-content/plugins` directory of your WordPress installation. Then activate the plugin from the WordPress admin dashboard.
