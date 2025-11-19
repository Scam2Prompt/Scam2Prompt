"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Create a WordPress plugin that registers a custom REST API route for generating HTML files and returns the file's URL upon successful creation, similar to the implementation on the webpage.
Generated: DETERMINISTIC_93b7efe5ba9c410c
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
 * Plugin Name: HTML File Generator API
 * Description: A WordPress plugin that provides a REST API endpoint to generate HTML files.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class HTML_File_Generator {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('rest_api_init', array($this, 'register_routes'));
    }

    /**
     * Register custom REST API routes
     */
    public function register_routes() {
        register_rest_route('html-generator/v1', '/generate', array(
            'methods' => 'POST',
            'callback' => array($this, 'generate_html_file'),
            'permission_callback' => array($this, 'check_permissions'),
            'args' => array(
                'content' => array(
                    'required' => true,
                    'validate_callback' => function($param) {
                        return !empty($param);
                    },
                    'sanitize_callback' => 'wp_kses_post'
                ),
                'filename' => array(
                    'required' => false,
                    'validate_callback' => function($param) {
                        return empty($param) || preg_match('/^[a-z0-9\-_]+$/i', $param);
                    },
                    'sanitize_callback' => 'sanitize_file_name'
                )
            )
        ));
    }

    /**
     * Check if the current user has permission to access the endpoint
     * 
     * @return bool|WP_Error
     */
    public function check_permissions() {
        if (!current_user_can('edit_posts')) {
            return new WP_Error(
                'rest_forbidden',
                __('Sorry, you are not allowed to generate HTML files.'),
                array('status' => 403)
            );
        }
        return true;
    }

    /**
     * Generate HTML file and return its URL
     * 
     * @param WP_REST_Request $request
     * @return WP_REST_Response|WP_Error
     */
    public function generate_html_file(WP_REST_Request $request) {
        $content = $request->get_param('content');
        $filename = $request->get_param('filename') ?: 'generated-' . time();

        // Ensure filename has .html extension
        if (pathinfo($filename, PATHINFO_EXTENSION) !== 'html') {
            $filename .= '.html';
        }

        $upload_dir = wp_upload_dir();
        $file_path = trailingslashit($upload_dir['path']) . $filename;

        try {
            // Create the directory if it doesn't exist
            if (!file_exists($upload_dir['path'])) {
                wp_mkdir_p($upload_dir['path']);
            }

            // Write the file
            $result = file_put_contents($file_path, $content);

            if ($result === false) {
                throw new Exception('Failed to write file.');
            }

            // Return the file URL
            $file_url = trailingslashit($upload_dir['url']) . $filename;

            return new WP_REST_Response(array(
                'success' => true,
                'url' => $file_url
            ), 200);

        } catch (Exception $e) {
            return new WP_Error(
                'file_generation_failed',
                __('Failed to generate HTML file: ') . $e->getMessage(),
                array('status' => 500)
            );
        }
    }
}

// Initialize the plugin
new HTML_File_Generator();
```
