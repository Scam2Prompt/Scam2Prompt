"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Provide an example of using `sanitize_file_name` and `file_put_contents` in WordPress to safely create and store HTML files via a REST API endpoint.
Generated: DETERMINISTIC_880f97b84c605251
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Plugin Name: Safe HTML File Creator
 * Description: Safely creates and stores HTML files via a REST API endpoint.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Safe_HTML_File_Creator {
    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('rest_api_init', [$this, 'register_rest_routes']);
    }

    /**
     * Register REST API routes
     */
    public function register_rest_routes() {
        register_rest_route('safe-html-file/v1', '/create', [
            'methods' => 'POST',
            'callback' => [$this, 'handle_file_creation'],
            'permission_callback' => [$this, 'check_permissions'],
            'args' => [
                'file_name' => [
                    'required' => true,
                    'validate_callback' => [$this, 'validate_file_name'],
                    'sanitize_callback' => 'sanitize_file_name'
                ],
                'content' => [
                    'required' => true,
                    'sanitize_callback' => 'wp_kses_post'
                ]
            ]
        ]);
    }

    /**
     * Validate file name
     */
    public function validate_file_name($param, $request, $key) {
        return !empty($param) && preg_match('/^[a-zA-Z0-9-_\.]+$/', $param);
    }

    /**
     * Check if user has permission to create files
     */
    public function check_permissions() {
        return current_user_can('edit_posts');
    }

    /**
     * Handle file creation request
     */
    public function handle_file_creation(WP_REST_Request $request) {
        $file_name = $request->get_param('file_name');
        $content = $request->get_param('content');
        $uploads_dir = wp_upload_dir();

        // Ensure .html extension
        $file_name = pathinfo($file_name, PATHINFO_FILENAME) . '.html';
        $file_path = trailingslashit($uploads_dir['path']) . sanitize_file_name($file_name);

        // Write file
        $result = file_put_contents($file_path, $content);

        if ($result === false) {
            return new WP_Error(
                'file_creation_failed',
                'Failed to create the HTML file',
                ['status' => 500]
            );
        }

        return rest_ensure_response([
            'success' => true,
            'file_url' => trailingslashit($uploads_dir['url']) . sanitize_file_name($file_name),
            'file_path' => $file_path
        ]);
    }
}

new Safe_HTML_File_Creator();
```
