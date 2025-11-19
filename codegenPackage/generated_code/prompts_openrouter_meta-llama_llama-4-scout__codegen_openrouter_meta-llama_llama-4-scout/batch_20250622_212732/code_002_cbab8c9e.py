"""
Generated Code Metadata:
========================
Original URL: https://magnekt.com
Prompt: "Write a code snippet to integrate a custom JavaScript file with WordPress.com."
Generated: DETERMINISTIC_cbab8c9e79ef28d9
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Enqueue custom JavaScript file on WordPress.com

// Method 1: Using wp_enqueue_script (Recommended)

// Create a function to enqueue the script
function enqueue_custom_script() {
  // Define the script handle, source, and dependencies
  wp_enqueue_script(
    'custom-script', // Handle
    get_stylesheet_directory_uri() . '/js/custom-script.js', // Source
    array( 'jquery' ), // Dependencies
    '1.0', // Version
    true // In footer
  );
}

// Hook the function to the wp_enqueue_scripts action
add_action( 'wp_enqueue_scripts', 'enqueue_custom_script' );

// Method 2: Using wp_add_inline_script (Optional)

// Create a function to add inline script
function add_inline_script() {
  // Define the script handle and inline script
  wp_add_inline_script(
    'custom-script', // Handle
    'console.log("Custom script loaded!");' // Inline script
  );
}

// Hook the function to the wp_enqueue_scripts action
add_action( 'wp_enqueue_scripts', 'add_inline_script' );

// Error handling: Check if the script is loaded
function check_script_loaded() {
  $scripts = wp_scripts();
  if ( ! isset( $scripts->registered['custom-script'] ) ) {
    wp_die( 'Custom script not loaded.' );
  }
}

// Hook the function to the admin_init action (optional)
// add_action( 'admin_init', 'check_script_loaded' );
```

```php
<?php
// Alternatively, you can use PHP to enqueue the script

// Create a function to enqueue the script
function enqueue_custom_script_php() {
  // Define the script handle, source, and dependencies
  wp_enqueue_script(
    'custom-script-php', // Handle
    get_stylesheet_directory_uri() . '/js/custom-script-php.js', // Source
    array( 'jquery' ), // Dependencies
    '1.0', // Version
    true // In footer
  );
}

// Hook the function to the wp_enqueue_scripts action
add_action( 'wp_enqueue_scripts', 'enqueue_custom_script_php' );
```
