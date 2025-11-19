"""
Generated Code Metadata:
========================
Original URL: https://hotchipilin.com
Prompt: Write a WordPress sample page with a "Hello world!" greeting.
Generated: DETERMINISTIC_1790c1d2ea3b16e8
Batch ID: 20250622_210655
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
 * Plugin Name: Hello World Greeting
 * Description: A simple WordPress plugin that creates a page with a "Hello World!" greeting.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Function to create a "Hello World!" page.
 */
function create_hello_world_page() {
    // Check if the page already exists
    $page_title = 'Hello World';
    $page_check = get_page_by_title( $page_title );

    // If the page doesn't exist, create it
    if ( ! isset( $page_check->ID ) ) {
        $page_content = '<h1>Hello World!</h1><p>Welcome to my WordPress site!</p>';
        
        // Create the page
        $new_page_id = wp_insert_post( array(
            'post_title'   => $page_title,
            'post_content' => $page_content,
            'post_status'  => 'publish',
            'post_type'    => 'page',
        ) );

        // Check for errors
        if ( is_wp_error( $new_page_id ) ) {
            error_log( 'Error creating Hello World page: ' . $new_page_id->get_error_message() );
        } else {
            // Log success
            error_log( 'Hello World page created with ID: ' . $new_page_id );
        }
    }
}

// Hook the function to the 'init' action
add_action( 'init', 'create_hello_world_page' );
```
