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
 * Function to sanitize user input and safely write a `.html` file to the server's root directory.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response A response indicating success or failure.
 */
function sanitize_and_save_html_file(WP_REST_Request $request) {
    // Ensure the 'filename' parameter is provided in the request.
    $filename = $request->get_param('filename');
    $content = $request->get_param('content');

    // Validate if filename and content are provided.
    if (empty($filename) || empty($content)) {
        return new WP_REST_Response(['message' => 'Filename and content are required.'], 400);
    }

    // Sanitize filename to remove unwanted characters.
    $sanitized_filename = sanitize_file_name($filename);

    // Ensure the filename ends with '.html'.
    if (substr($sanitized_filename, -5) !== '.html') {
        return new WP_REST_Response(['message' => 'Filename must end with .html.'], 400);
    }

    // Define the full path to the server's root directory.
    $file_path = ABSPATH . $sanitized_filename;

    // Ensure no directory traversal attacks.
    if (strpos(realpath($file_path), ABSPATH) !== 0) {
        return new WP_REST_Response(['message' => 'Invalid filename.'], 403);
    }

    // Safely write content to the file.
    try {
        $result = file_put_contents($file_path, $content);

        // Check if the file was written successfully.
        if ($result === false) {
            throw new Exception('Failed to write file.');
        }

        return new WP_REST_Response(['message' => 'File saved successfully.', 'file' => $sanitized_filename], 200);
    } catch (Exception $e) {
        // Handle errors gracefully.
        return new WP_REST_Response(['message' => 'An error occurred: ' . $e->getMessage()], 500);
    }
}

/**
 * Register the REST API endpoint.
 */
function register_sanitize_and_save_html_endpoint() {
    register_rest_route('custom/v1', '/save-html', [
        'methods'  => 'POST',
        'callback' => 'sanitize_and_save_html_file',
        'permission_callback' => function () {
            // Only allow logged-in users to access this endpoint.
            return is_user_logged_in();
        },
    ]);
}
add_action('rest_api_init', 'register_sanitize_and_save_html_endpoint');
```
