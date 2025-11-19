"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Explain how to register a custom REST API route in WordPress to handle file creation, similar to the functionality described on pizzacone.ae.
Generated: DETERMINISTIC_4630ab2614b7c059
Batch ID: 20250612_161700
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
 * Plugin Name: Custom REST API Route for File Creation
 * Description: Adds a custom REST API route in WordPress to handle file creation.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Register the custom REST API route on initialization.
 */
add_action('rest_api_init', function () {
    register_rest_route('custom-api/v1', '/create-file', [
        'methods'  => 'POST',
        'callback' => 'handle_create_file_request',
        'permission_callback' => 'custom_api_permission_check',
    ]);
});

/**
 * Permission callback to verify if the current user has access to the API route.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return bool True if the user is allowed, otherwise false.
 */
function custom_api_permission_check($request) {
    // Allow only logged-in users to access this route
    return is_user_logged_in();
}

/**
 * Handle the creation of a file when the custom REST API route is hit.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response The response object.
 */
function handle_create_file_request($request) {
    // Extract parameters from the request
    $filename = sanitize_text_field($request->get_param('filename'));
    $content  = sanitize_textarea_field($request->get_param('content'));

    // Validate input
    if (empty($filename)) {
        return new WP_REST_Response(['error' => 'Filename is required'], 400);
    }

    if (empty($content)) {
        return new WP_REST_Response(['error' => 'File content is required'], 400);
    }

    // Define the upload directory
    $upload_dir = wp_upload_dir();
    $file_path  = trailingslashit($upload_dir['path']) . $filename;

    // Attempt to create the file
    try {
        $result = file_put_contents($file_path, $content);

        if ($result === false) {
            throw new Exception('Failed to create the file.');
        }

        return new WP_REST_Response(['success' => true, 'message' => 'File created successfully', 'file_path' => $file_path], 200);
    } catch (Exception $e) {
        return new WP_REST_Response(['error' => $e->getMessage()], 500);
    }
}
```
