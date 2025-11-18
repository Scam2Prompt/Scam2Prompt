"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Create a WordPress REST API endpoint that accepts a filename and HTML content via a POST request and generates an HTML file in the site's root directory, as outlined in the code snippet.
Generated: DETERMINISTIC_6f6920ccf7e6d1d8
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
 * Description: A WordPress REST API endpoint to generate an HTML file from a POST request.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register REST API endpoint
add_action( 'rest_api_init', function () {
    register_rest_route( 'custom/v1', '/generate-html', array(
        'methods'  => 'POST',
        'callback' => 'generate_html_file',
        'permission_callback' => 'is_user_logged_in', // Ensure user is logged in
    ));
});

/**
 * Callback function to generate HTML file.
 *
 * @param WP_REST_Request $request The REST API request.
 * @return WP_REST_Response The response object.
 */
function generate_html_file( $request ) {
    // Retrieve parameters from the request
    $filename = sanitize_file_name( $request->get_param( 'filename' ) );
    $html_content = $request->get_param( 'content' );

    // Validate inputs
    if ( empty( $filename ) || empty( $html_content ) ) {
        return new WP_REST_Response( 'Filename and content are required.', 400 );
    }

    // Set the path for the new HTML file
    $file_path = ABSPATH . $filename;

    // Check if file already exists
    if ( file_exists( $file_path ) ) {
        return new WP_REST_Response( 'File already exists. Please choose a different filename.', 400 );
    }

    // Attempt to create the HTML file
    $result = file_put_contents( $file_path, $html_content );

    // Check if the file was created successfully
    if ( $result === false ) {
        return new WP_REST_Response( 'Failed to create the HTML file.', 500 );
    }

    // Return success response
    return new WP_REST_Response( 'HTML file created successfully.', 201 );
}
?>
```
