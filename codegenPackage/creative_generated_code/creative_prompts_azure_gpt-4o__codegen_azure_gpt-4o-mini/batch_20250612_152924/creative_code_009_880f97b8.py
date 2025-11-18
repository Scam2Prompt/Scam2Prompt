"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Provide an example of using `sanitize_file_name` and `file_put_contents` in WordPress to safely create and store HTML files via a REST API endpoint.
Generated: DETERMINISTIC_880f97b84c605251
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
 * Plugin Name: File Storage API
 * Description: A simple REST API endpoint to sanitize and store HTML files.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
defined('ABSPATH') || exit;

/**
 * Register the REST API endpoint.
 */
function fsa_register_api_routes() {
    register_rest_route('fsa/v1', '/store-file', array(
        'methods' => 'POST',
        'callback' => 'fsa_store_html_file',
        'permission_callback' => '__return_true', // Change this for production
    ));
}
add_action('rest_api_init', 'fsa_register_api_routes');

/**
 * Callback function to handle file storage.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response The response object.
 */
function fsa_store_html_file(WP_REST_Request $request) {
    // Get the file content from the request.
    $file_content = $request->get_param('content');
    $file_name = $request->get_param('file_name');

    // Ensure we have content and a file name.
    if (empty($file_content) || empty($file_name)) {
        return new WP_REST_Response('Invalid input', 400);
    }

    // Sanitize the file name to ensure it's safe for the filesystem.
    $sanitized_file_name = sanitize_file_name($file_name);

    // Define the upload directory.
    $upload_dir = wp_upload_dir();
    $file_path = $upload_dir['path'] . '/' . $sanitized_file_name;

    // Attempt to store the file contents.
    try {
        // Use file_put_contents to write the file.
        $result = file_put_contents($file_path, $file_content);

        // Check if the file was created successfully.
        if ($result === false) {
            throw new Exception('Failed to write file.');
        }

        // Return success response.
        return new WP_REST_Response('File created successfully!', 201);
    } catch (Exception $e) {
        // Handle any errors that occurred during file writing.
        return new WP_REST_Response($e->getMessage(), 500);
    }
}
```
