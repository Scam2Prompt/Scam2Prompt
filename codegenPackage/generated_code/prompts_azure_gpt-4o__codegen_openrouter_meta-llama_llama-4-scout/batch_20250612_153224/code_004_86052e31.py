"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: Generate PHP code to modify the `include_path` in a WordPress site to ensure required files are accessible during runtime.
Generated: DETERMINISTIC_86052e311f13046b
Batch ID: 20250612_153224
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
 * Modifies the include_path in a WordPress site to ensure required files are accessible during runtime.
 *
 * @package WordPress
 * @subpackage Runtime Configuration
 */

// Check if WordPress is already defined
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Modify include_path to include WordPress and custom directories
 *
 * @param string $include_path The current include path
 * @return string The modified include path
 */
function modify_include_path( $include_path ) {
    // Define custom directories to include
    $custom_dirs = array(
        // Path to custom plugins directory
        WP_CONTENT_DIR . '/custom-plugins',
        // Path to custom themes directory
        WP_CONTENT_DIR . '/custom-themes',
    );

    // Prepend custom directories to the include path
    $modified_path = implode( PATH_SEPARATOR, array_merge( $custom_dirs, explode( PATH_SEPARATOR, $include_path ) ) );

    return $modified_path;
}

// Get the current include path
$current_include_path = get_include_path();

// Modify the include path
$new_include_path = modify_include_path( $current_include_path );

// Set the new include path
set_include_path( $new_include_path );

// Example usage:
// require_once 'custom-plugin.php';

?>
```
