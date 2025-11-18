"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Implement a WordPress REST API route using `register_rest_route` that allows creating HTML files with validation for filename and content, as described in the webpage's code.
Generated: DETERMINISTIC_9310d15e1fc80dd0
Batch ID: 20250612_152924
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
 * Plugin Name: Custom HTML File Creator
 * Description: Adds a REST API route to create HTML files with validation for filename and content.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Hook to register the REST API route
add_action( 'rest_api_init', function () {
    register_rest_route( 'custom/v1', '/create-html', array(
        'methods' => 'POST',
        'callback' => 'create_html_file',
        'permission_callback' => 'is_user_logged_in', // Ensure the user is logged in
    ));
});

/**
 * Callback function to create an HTML file
 *
 * @param WP_REST_Request $request Current request.
 * @return WP_REST_Response Response object.
 */
function create_html_file( WP_REST_Request $request ) {
    // Get filename and content from the request
    $filename = sanitize_file_name( $request->get_param( 'filename' ) );
    $content = sanitize_textarea_field( $request->get_param( 'content' ) );

    // Validate filename
    if ( empty( $filename ) || ! preg_match( '/^[a-zA-Z0-9_-]+\.html$/', $filename ) ) {
        return new WP_REST_Response( array( 'message' => 'Invalid filename. Use only alphanumeric characters, dashes, or underscores, ending with .html' ), 400 );
    }

    // Validate content
    if ( empty( $content ) ) {
        return new WP_REST_Response( array( 'message' => 'Content cannot be empty.' ), 400 );
    }

    // Define the upload directory and file path
    $upload_dir = wp_upload_dir();
    $file_path = $upload_dir['path'] . '/' . $filename;

    // Attempt to create the HTML file
    if ( file_put_contents( $file_path, $content ) === false ) {
        return new WP_REST_Response( array( 'message' => 'Unable to create file. Please check permissions.' ), 500 );
    }

    // Return success response
    return new WP_REST_Response( array( 'message' => 'File created successfully.', 'file_url' => $upload_dir['url'] . '/' . $filename ), 201 );
}
```
