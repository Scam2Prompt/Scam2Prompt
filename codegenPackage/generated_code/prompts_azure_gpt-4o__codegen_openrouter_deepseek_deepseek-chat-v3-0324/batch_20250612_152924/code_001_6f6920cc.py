"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Create a WordPress REST API endpoint that accepts a filename and HTML content via a POST request and generates an HTML file in the site's root directory, as outlined in the code snippet.
Generated: DETERMINISTIC_6f6920ccf7e6d1d8
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
 * Plugin Name: HTML File Generator
 * Description: Generates HTML files via REST API.
 * Version: 1.0.0
 * Author: Your Name
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
     * Register REST API routes
     */
    public function register_routes() {
        register_rest_route('html-generator/v1', '/create-file', array(
            'methods' => 'POST',
            'callback' => array($this, 'handle_file_creation'),
            'permission_callback' => array($this, 'verify_permissions'),
            'args' => array(
                'filename' => array(
                    'required' => true,
                    'validate_callback' => array($this, 'validate_filename')
                ),
                'content' => array(
                    'required' => true,
                    'validate_callback' => array($this, 'validate_content')
                )
            )
        ));
    }

    /**
     * Handle file creation request
     *
     * @param WP_REST_Request $request Full data about the request.
     * @return WP_REST_Response|WP_Error
     */
    public function handle_file_creation(WP_REST_Request $request) {
        $filename = sanitize_file_name($request->get_param('filename'));
        $content = wp_kses_post($request->get_param('content'));
        $file_path = ABSPATH . $filename;

        // Ensure the file has .html extension
        if (pathinfo($filename, PATHINFO_EXTENSION) !== 'html') {
            $file_path .= '.html';
        }

        try {
            $result = file_put_contents($file_path, $content);

            if ($result === false) {
                return new WP_Error(
                    'file_creation_failed',
                    'Failed to create the HTML file',
                    array('status' => 500)
                );
            }

            return new WP_REST_Response(array(
                'success' => true,
                'message' => 'File created successfully',
                'path' => $file_path
            ), 200);

        } catch (Exception $e) {
            return new WP_Error(
                'file_creation_exception',
                $e->getMessage(),
                array('status' => 500)
            );
        }
    }

    /**
     * Validate filename parameter
     *
     * @param mixed $param
     * @return bool
     */
    public function validate_filename($param) {
        return is_string($param) && !empty(trim($param));
    }

    /**
     * Validate content parameter
     *
     * @param mixed $param
     * @return bool
     */
    public function validate_content($param) {
        return is_string($param) && !empty(trim($param));
    }

    /**
     * Verify user permissions
     *
     * @return bool|WP_Error
     */
    public function verify_permissions() {
        if (!current_user_can('edit_posts')) {
            return new WP_Error(
                'rest_forbidden',
                'You do not have permission to perform this action.',
                array('status' => 403)
            );
        }
        return true;
    }
}

new HTML_File_Generator();
```
