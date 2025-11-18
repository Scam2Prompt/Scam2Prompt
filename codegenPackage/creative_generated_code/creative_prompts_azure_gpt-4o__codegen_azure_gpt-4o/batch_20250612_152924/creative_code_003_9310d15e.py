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
 * Plugin Name: Custom HTML File Creator API
 * Description: Adds a REST API route for creating HTML files with validation.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// If this file is called directly, abort.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register the REST API route.
 */
function register_html_file_creator_route() {
    register_rest_route(
        'custom-api/v1', // Namespace and endpoint.
        '/create-html-file', // Route.
        array(
            'methods'  => 'POST',
            'callback' => 'handle_create_html_file_request',
            'permission_callback' => 'html_file_creator_permission_check',
            'args'     => array(
                'filename' => array(
                    'required'          => true,
                    'validate_callback' => 'validate_filename',
                    'description'       => 'The name of the HTML file (without extension).',
                    'type'              => 'string',
                ),
                'content' => array(
                    'required'          => true,
                    'description'       => 'The HTML content to be saved in the file.',
                    'type'              => 'string',
                ),
            ),
        )
    );
}

/**
 * Permission callback to restrict access to authenticated users.
 */
function html_file_creator_permission_check( $request ) {
    // Only allow users with 'edit_posts' capability to use this API.
    return current_user_can( 'edit_posts' );
}

/**
 * Validate the filename to prevent invalid or unsafe values.
 */
function validate_filename( $param, $request, $key ) {
    // Check if the filename contains only alphanumeric characters, dashes, and underscores.
    return preg_match( '/^[a-zA-Z0-9_-]+$/', $param ) === 1;
}

/**
 * Handle the API request to create an HTML file.
 */
function handle_create_html_file_request( $request ) {
    // Sanitize and retrieve parameters from the request.
    $filename = sanitize_file_name( $request->get_param( 'filename' ) );
    $content  = wp_kses_post( $request->get_param( 'content' ) );

    // Define the directory for saving the file (in wp-content/uploads).
    $upload_dir = wp_upload_dir();
    $save_path  = trailingslashit( $upload_dir['basedir'] ) . $filename . '.html';

    // Attempt to write the file.
    if ( file_put_contents( $save_path, $content ) === false ) {
        return new WP_Error(
            'file_creation_failed',
            'Failed to create the HTML file. Please check server permissions.',
            array( 'status' => 500 )
        );
    }

    // Return success response with the file URL.
    return rest_ensure_response(
        array(
            'success'  => true,
            'message'  => 'HTML file created successfully.',
            'file_url' => trailingslashit( $upload_dir['baseurl']'] ) . $filename . '.html',
        )
    );
}

// Hook to register the REST route.
add_action( 'rest_api_init', 'register_html_file_creator_route' );
?>
```
