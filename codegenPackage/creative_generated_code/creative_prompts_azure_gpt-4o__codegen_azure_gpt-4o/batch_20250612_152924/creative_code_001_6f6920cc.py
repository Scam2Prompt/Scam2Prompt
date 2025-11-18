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
// Ensure this file is part of the WordPress ecosystem
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Registers a custom REST API endpoint to create an HTML file.
 */
function register_create_html_file_endpoint() {
    register_rest_route(
        'custom-api/v1',
        '/create-html-file',
        array(
            'methods'  => 'POST',
            'callback' => 'handle_create_html_file_request',
            'permission_callback' => 'can_user_create_html_file',
        )
    );
}
add_action('rest_api_init', 'register_create_html_file_endpoint');

/**
 * Handles the creation of the HTML file.
 *
 * @param WP_REST_Request $request The request object.
 * @return WP_REST_Response Response object indicating success or failure.
 */
function handle_create_html_file_request($request) {
    // Extract and validate parameters from the request
    $filename = sanitize_file_name($request->get_param('filename'));
    $html_content = $request->get_param('html_content');

    if (empty($filename) || empty($html_content)) {
        return new WP_REST_Response(
            array(
                'success' => false,
                'message' => 'Both "filename" and "html_content" parameters are required.'
            ),
            400
        );
    }

    // Ensure the filename ends with .html
    if (!str_ends_with($filename, '.html')) {
        $filename .= '.html';
    }

    // Define the path to save the file
    $file_path = ABSPATH . $filename;

    // Attempt to save the HTML content to the file
    try {
        $result = file_put_contents($file_path, $html_content);

        if ($result === false) {
            throw new Exception('Failed to write to file.');
        }

        return new WP_REST_Response(
            array(
                'success' => true,
                'message' => "File created successfully at: $file_path",
            ),
            201
        );
    } catch (Exception $e) {
        return new WP_REST_Response(
            array(
                'success' => false,
                'message' => 'An error occurred while creating the file: ' . $e->getMessage(),
            ),
            500
        );
    }
}

/**
 * Determines whether the current user has permission to create an HTML file.
 *
 * @return bool True if the user has permission, false otherwise.
 */
function can_user_create_html_file() {
    // Check if the user has the 'manage_options' capability (admin role)
    return current_user_can('manage_options');
}
```
