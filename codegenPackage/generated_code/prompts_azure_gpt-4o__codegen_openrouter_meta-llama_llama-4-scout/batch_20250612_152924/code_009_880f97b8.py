"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Provide an example of using `sanitize_file_name` and `file_put_contents` in WordPress to safely create and store HTML files via a REST API endpoint.
Generated: DETERMINISTIC_880f97b84c605251
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
 * REST API endpoint to create and store HTML files.
 */

// Define the REST API endpoint
add_action( 'rest_api_init', 'register_html_file_endpoint' );

function register_html_file_endpoint() {
    register_rest_route( 'html-file/v1', '/create', array(
        'methods' => 'POST',
        'callback' => 'create_html_file',
        'permission_callback' => '__return_true', // Update this to your permission logic
    ) );
}

/**
 * Create and store an HTML file via the REST API endpoint.
 *
 * @param WP_REST_Request $request The REST API request object.
 *
 * @return WP_REST_Response The REST API response object.
 */
function create_html_file( $request ) {
    try {
        // Get the file name and content from the request
        $file_name = $request->get_param( 'file_name' );
        $content = $request->get_param( 'content' );

        // Validate the file name and content
        if ( empty( $file_name ) || empty( $content ) ) {
            return rest_ensure_response( array( 'error' => 'File name and content are required.' ), 400 );
        }

        // Sanitize the file name
        $sanitized_file_name = sanitize_file_name( $file_name );

        // Get the file path
        $file_path = wp_upload_dir()['path'] . '/' . $sanitized_file_name . '.html';

        // Check if the file already exists
        if ( file_exists( $file_path ) ) {
            return rest_ensure_response( array( 'error' => 'File already exists.' ), 409 );
        }

        // Create and store the HTML file
        $result = file_put_contents( $file_path, $content );

        if ( $result === false ) {
            return rest_ensure_response( array( 'error' => 'Failed to create the file.' ), 500 );
        }

        // Return a success response
        return rest_ensure_response( array( 'message' => 'File created successfully.' ), 201 );
    } catch ( Exception $e ) {
        // Return an error response
        return rest_ensure_response( array( 'error' => $e->getMessage() ), 500 );
    }
}
```
