"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Explain how to register a custom REST API route in WordPress to handle file creation, similar to the functionality described on pizzacone.ae.
Generated: DETERMINISTIC_4630ab2614b7c059
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Register a custom REST API route in WordPress to handle file creation

// Hook into the 'rest_api_init' action to register the custom route
add_action('rest_api_init', function () {
    // Register the route
    register_rest_route('custom/v1', '/create-file', array(
        'methods'  => 'POST', // HTTP method
        'callback' => 'handle_create_file', // Callback function to handle the request
        'permission_callback' => 'custom_permission_check', // Permission callback
    ));
});

/**
 * Permission callback to check if the user has the required permissions.
 *
 * @return bool True if the user is allowed, false otherwise.
 */
function custom_permission_check() {
    // Check if the user is logged in and has the 'edit_posts' capability
    if (current_user_can('edit_posts')) {
        return true;
    }
    return new WP_Error('rest_forbidden', __('You do not have permission to access this route.'), array('status' => 403));
}

/**
 * Callback function to handle the file creation request.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response|WP_Error The response or an error object.
 */
function handle_create_file(WP_REST_Request $request) {
    // Get the 'filename' and 'content' parameters from the request
    $filename = sanitize_text_field($request->get_param('filename'));
    $content = $request->get_param('content');

    // Validate the filename
    if (empty($filename)) {
        return new WP_Error('invalid_filename', __('Filename is required.'), array('status' => 400));
    }

    // Sanitize and ensure the filename is safe
    $filename = preg_replace('/[^a-zA-Z0-9_\-\.]/', '', $filename);

    // Define the file path (in the uploads directory)
    $upload_dir = wp_upload_dir();
    $file_path = trailingslashit($upload_dir['basedir']) . $filename;

    // Check if the file already exists
    if (file_exists($file_path)) {
        return new WP_Error('file_exists', __('A file with this name already exists.'), array('status' => 400));
    }

    // Attempt to create the file
    if (file_put_contents($file_path, $content) === false) {
        return new WP_Error('file_creation_failed', __('Failed to create the file.'), array('status' => 500));
    }

    // Return a success response
    return new WP_REST_Response(array(
        'success' => true,
        'message' => __('File created successfully.'),
        'file_path' => $file_path,
    ), 200);
}
?>
```
