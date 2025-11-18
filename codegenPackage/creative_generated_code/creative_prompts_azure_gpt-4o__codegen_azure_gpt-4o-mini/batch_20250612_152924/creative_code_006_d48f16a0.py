"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Write a WordPress function that sanitizes user input for a REST API endpoint, ensuring the filename ends with `.html` and safely writes the file to the server's root directory.
Generated: DETERMINISTIC_d48f16a0654e4caf
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
 * Sanitizes user input for a REST API endpoint and writes the file to the server's root directory.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response The response object containing the result of the operation.
 */
function my_custom_api_save_file( WP_REST_Request $request ) {
    // Retrieve the 'filename' parameter from the request
    $filename = $request->get_param( 'filename' );

    // Sanitize the filename
    $sanitized_filename = sanitize_file_name( $filename );

    // Check if the sanitized filename ends with '.html'
    if ( ! preg_match( '/\.html$/i', $sanitized_filename ) ) {
        return new WP_REST_Response( 'Invalid file type. Filename must end with .html', 400 );
    }

    // Define the full file path
    $file_path = ABSPATH . $sanitized_filename;

    // Attempt to write an empty HTML file to the server
    $content = '<!DOCTYPE html><html><head><title>Document</title></head><body></body></html>';

    // Use error handling to ensure we catch any issues during file writing
    try {
        if ( file_put_contents( $file_path, $content ) === false ) {
            throw new Exception('Could not write the file.');
        }
    } catch ( Exception $e ) {
        return new WP_REST_Response( 'File write failed: ' . $e->getMessage(), 500 );
    }

    // Return a success response
    return new WP_REST_Response( 'File created successfully: ' . $sanitized_filename, 201 );
}

// Register the REST API endpoint
add_action( 'rest_api_init', function () {
    register_rest_route( 'myplugin/v1', '/save-file', array(
        'methods'  => 'POST',
        'callback' => 'my_custom_api_save_file',
        'permission_callback' => '__return_true', // Adjust permission checks as needed
    ) );
} );
?>
```
