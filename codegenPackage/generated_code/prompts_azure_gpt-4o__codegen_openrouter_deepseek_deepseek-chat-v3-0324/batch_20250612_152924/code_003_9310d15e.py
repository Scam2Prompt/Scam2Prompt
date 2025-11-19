"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Implement a WordPress REST API route using `register_rest_route` that allows creating HTML files with validation for filename and content, as described in the webpage's code.
Generated: DETERMINISTIC_9310d15e1fc80dd0
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
 * Plugin Name: HTML File Creator
 * Description: A plugin to create HTML files via REST API.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class HTML_File_Creator {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('rest_api_init', array($this, 'register_routes'));
    }

    /**
     * Register REST API routes
     */
    public function register_routes() {
        register_rest_route('html-file-creator/v1', '/create', array(
            'methods' => 'POST',
            'callback' => array($this, 'create_html_file'),
            'permission_callback' => array($this, 'check_permissions'),
            'args' => array(
                'filename' => array(
                    'required' => true,
                    'validate_callback' => array($this, 'validate_filename'),
                    'sanitize_callback' => 'sanitize_file_name',
                ),
                'content' => array(
                    'required' => true,
                    'validate_callback' => array($this, 'validate_content'),
                    'sanitize_callback' => 'wp_kses_post',
                ),
            ),
        ));
    }

    /**
     * Validate filename
     *
     * @param string $filename
     * @return bool
     */
    public function validate_filename($filename) {
        if (empty($filename)) {
            return false;
        }

        // Check for valid file extension
        if (!preg_match('/\.html?$/i', $filename)) {
            return false;
        }

        // Check for invalid characters
        if (preg_match('/[\/\\\?\*:|"<>]/', $filename)) {
            return false;
        }

        return true;
    }

    /**
     * Validate content
     *
     * @param string $content
     * @return bool
     */
    public function validate_content($content) {
        return !empty($content);
    }

    /**
     * Check if user has permission to create files
     *
     * @return bool
     */
    public function check_permissions() {
        return current_user_can('edit_posts');
    }

    /**
     * Create HTML file
     *
     * @param WP_REST_Request $request
     * @return WP_REST_Response
     */
    public function create_html_file(WP_REST_Request $request) {
        $filename = $request->get_param('filename');
        $content = $request->get_param('content');

        $uploads_dir = wp_upload_dir();
        $file_path = trailingslashit($uploads_dir['path']) . $filename;

        try {
            $file_handle = fopen($file_path, 'w');
            if (!$file_handle) {
                throw new Exception('Could not open file for writing.');
            }

            $bytes_written = fwrite($file_handle, $content);
            fclose($file_handle);

            if (false === $bytes_written) {
                throw new Exception('Failed to write to file.');
            }

            return new WP_REST_Response(array(
                'success' => true,
                'message' => 'File created successfully',
                'path' => $file_path,
                'url' => trailingslashit($uploads_dir['url']) . $filename
            ), 200);

        } catch (Exception $e) {
            return new WP_REST_Response(array(
                'success' => false,
                'message' => $e->getMessage()
            ), 500);
        }
    }
}

new HTML_File_Creator();
```
