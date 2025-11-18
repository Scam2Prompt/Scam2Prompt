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
 * Plugin Name: Custom HTML File Generator API
 * Description: A plugin to register a custom REST API route for generating HTML files and returning their URLs.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Custom_HTML_File_Generator_API {
    public function __construct() {
        add_action( 'rest_api_init', [ $this, 'register_routes' ] );
    }

    /**
     * Registers the custom REST API route.
     */
    public function register_routes() {
        register_rest_route(
            'custom-html-generator/v1',
            '/generate-html',
            [
                'methods'  => 'POST',
                'callback' => [ $this, 'generate_html_file' ],
                'permission_callback' => [ $this, 'permission_callback' ],
            ]
        );
    }

    /**
     * Permission callback to restrict access to the API route.
     * Only logged-in users can access this route.
     *
     * @param WP_REST_Request $request REST API request.
     * @return bool True if user is logged in, false otherwise.
     */
    public function permission_callback( $request ) {
        return is_user_logged_in();
    }

    /**
     * Callback function to generate HTML file and return its URL.
     *
     * @param WP_REST_Request $request REST API request.
     * @return WP_REST_Response REST API response.
     */
    public function generate_html_file( $request ) {
        $params = $request->get_json_params();

        // Validate required parameters.
        if ( ! isset( $params['title'] ) || ! isset( $params['content'] ) ) {
            return new WP_REST_Response(
                [
                    'error'   => 'Missing required parameters: title and content.',
                    'status'  => 400,
                ],
                400
            );
        }

        $title = sanitize_text_field( $params['title'] );
        $content = wp_kses_post( $params['content'] );

        // Generate HTML file content.
        $html = '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>' . esc_html( $title ) . '</title>
</head>
<body>
    ' . $content . '
</body>
</html>';

        // Save HTML file to the uploads directory.
        $upload_dir = wp_upload_dir();
        $file_path = $upload_dir['path'] . '/' . sanitize_file_name( $title ) . '.html';
        $file_url = $upload_dir['url'] . '/' . sanitize_file_name( $title ) . '.html';

        if ( file_put_contents( $file_path, $html ) === false ) {
            return new WP_REST_Response(
                [
                    'error'   => 'Failed to create HTML file.',
                    'status'  => 500,
                ],
                500
            );
        }

        return new WP_REST_Response(
            [
                'message' => 'HTML file created successfully.',
                'file_url' => $file_url,
                'status'  => 200,
            ],
            200
        );
    }
}

// Initialize the plugin.
new Custom_HTML_File_Generator_API();
```
