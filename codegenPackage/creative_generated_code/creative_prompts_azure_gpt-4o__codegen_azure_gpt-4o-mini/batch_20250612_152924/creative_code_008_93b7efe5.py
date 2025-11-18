"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Create a WordPress plugin that registers a custom REST API route for generating HTML files and returns the file's URL upon successful creation, similar to the implementation on the webpage.
Generated: DETERMINISTIC_93b7efe5ba9c410c
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
 * Plugin Name: Custom HTML File Generator
 * Description: A WordPress plugin that registers a custom REST API route for generating HTML files.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register the custom REST API route.
 */
function chfg_register_api_route() {
    register_rest_route( 'chfg/v1', '/generate-html', array(
        'methods'  => 'POST',
        'callback' => 'chfg_generate_html_file',
        'permission_callback' => '__return_true',
    ));
}
add_action( 'rest_api_init', 'chfg_register_api_route' );

/**
 * Callback function for generating HTML files.
 *
 * @param WP_REST_Request $request The REST request instance.
 * @return WP_REST_Response The response containing the URL of the generated file.
 */
function chfg_generate_html_file( $request ) {
    // Get the content from the request.
    $content = $request->get_param( 'content' );

    // Validate that content is provided.
    if ( empty( $content ) ) {
        return new WP_REST_Response( array( 'error' => 'Content is required' ), 400 );
    }

    // Define the file path.
    $upload_dir = wp_upload_dir();
    $file_name = 'generated-file-' . time() . '.html';
    $file_path = $upload_dir['path'] . '/' . $file_name;

    // Attempt to write the HTML content to the file.
    $result = file_put_contents( $file_path, $content );

    // Check if the file was created successfully.
    if ( $result === false ) {
        return new WP_REST_Response( array( 'error' => 'Failed to create HTML file' ), 500 );
    }

    // Generate the URL to access the file.
    $file_url = $upload_dir['url'] . '/' . $file_name;

    // Return the file URL in the response.
    return new WP_REST_Response( array( 'file_url' => $file_url ), 200 );
}
```
