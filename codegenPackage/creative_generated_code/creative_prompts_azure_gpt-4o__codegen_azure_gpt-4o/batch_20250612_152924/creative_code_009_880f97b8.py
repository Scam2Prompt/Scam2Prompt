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
 * Plugin Name: Safe File Creator
 * Description: A WordPress plugin to safely create and store HTML files via a REST API endpoint.
 */

// Register the REST API endpoint
add_action('rest_api_init', function () {
    register_rest_route('safe-file/v1', '/create-html-file', [
        'methods'  => 'POST',
        'callback' => 'create_html_file',
        'permission_callback' => function () {
            return current_user_can('manage_options'); // Restrict access to administrators
        },
    ]);
});

/**
 * Callback function for the REST API endpoint to safely create and store HTML files.
 *
 * @param WP_REST_Request $request The REST request object.
 * @return WP_REST_Response A response indicating success or failure.
 */
function create_html_file(WP_REST_Request $request) {
    // Retrieve and validate parameters from the request
    $file_name = $request->get_param('file_name');
    $html_content = $request->get_param('html_content');

    if (empty($file_name) || empty($html_content)) {
        return new WP_REST_Response(['error' => 'Missing file_name or html_content parameter.'], 400);
    }

    // Sanitize the file name to prevent unsafe characters
    $sanitized_file_name = sanitize_file_name($file_name);

    // Ensure the file has a .html extension
    if (pathinfo($sanitized_file_name, PATHINFO_EXTENSION) !== 'html') {
        $sanitized_file_name .= '.html';
    }

    // Define the file path in the uploads directory
    $upload_dir = wp_upload_dir();
    $file_path = trailingslashit($upload_dir['path']) . $sanitized_file_name;

    // Attempt to write the file's contents
    try {
        $result = file_put_contents($file_path, $html_content);

        if ($result === false) {
            throw new Exception('Failed to write to file.');
        }

        return new WP_REST_Response(['success' => true, 'file_path' => $file_path], 200);
    } catch (Exception $e) {
        // Handle errors gracefully
        return new WP_REST_Response(['error' => $e->getMessage()], 500);
    }
}
```

This code snippet creates a WordPress plugin that registers a REST API endpoint for safely creating and storing HTML files. Simply copy and paste the code into a `.php` file within your WordPress plugin directory, activate the plugin, and test the endpoint.
