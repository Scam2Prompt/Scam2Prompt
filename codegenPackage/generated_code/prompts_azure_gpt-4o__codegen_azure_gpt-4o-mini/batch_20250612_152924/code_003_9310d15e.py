"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Implement a WordPress REST API route using `register_rest_route` that allows creating HTML files with validation for filename and content, as described in the webpage's code.
Generated: DETERMINISTIC_9310d15e1fc80dd0
Batch ID: 20250612_152924
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
 * Plugin Name: Custom HTML File Creator
 * Description: A WordPress plugin that provides a REST API route to create HTML files with validation.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register the REST API route for creating HTML files.
 */
add_action( 'rest_api_init', function () {
    register_rest_route( 'custom/v1', '/create-html', array(
        'methods'  => 'POST',
        'callback' => 'create_html_file',
        'permission_callback' => '__return_true', // Adjust permissions as needed
    ));
});

/**
 * Callback function to handle the creation of HTML files.
 *
 * @param WP_REST_Request $request The request object.
 * @return WP_REST_Response The response object.
 */
function create_html_file( WP_REST_Request $request ) {
    // Get parameters from the request
    $filename = sanitize_file_name( $request->get_param( 'filename' ) );
    $content  = $request->get_param( 'content' );

    // Validate filename
    if ( empty( $filename ) || ! preg_match( '/^[a-zA-Z0-9-_]+\.html$/', $filename ) ) {
        return new WP_REST_Response( array( 'error' => 'Invalid filename. Only alphanumeric characters, dashes, and underscores are allowed, and it must end with .html.' ), 400 );
    }

    // Validate content
    if ( empty( $content ) ) {
        return new WP_REST_Response( array( 'error' => 'Content cannot be empty.' ), 400 );
    }

    // Define the path to save the HTML file
    $upload_dir = wp_upload_dir();
    $file_path  = $upload_dir['path'] . '/' . $filename;

    // Attempt to create the HTML file
    if ( file_put_contents( $file_path, $content ) === false ) {
        return new WP_REST_Response( array( 'error' => 'Failed to create the HTML file.' ), 500 );
    }

    // Return success response
    return new WP_REST_Response( array( 'message' => 'HTML file created successfully.', 'file_path' => $file_path ), 201 );
}
```
