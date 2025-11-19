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
 * Create HTML file via WordPress REST API
 *
 * @package WordPress
 */

// Ensure the file is being accessed through WordPress
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

// Include necessary WordPress functions
require_once ABSPATH . 'wp-load.php';

// Define the namespace and route for the REST API
$namespace = 'html-file/v1';
$route = '/create-html-file';

// Register the REST API route
register_rest_route($namespace, $route, array(
    'methods' => 'POST',
    'callback' => 'create_html_file_callback',
    'permission_callback' => function () {
        return current_user_can('manage_options');
    },
    'args' => array(
        'filename' => array(
            'required' => true,
            'type' => 'string',
            'sanitize_callback' => 'sanitize_file_name',
        ),
        'content' => array(
            'required' => true,
            'type' => 'string',
        ),
    ),
));

/**
 * Create an HTML file
 *
 * @param WP_REST_Request $request The request object.
 *
 * @return WP_REST_Response
 */
function create_html_file_callback($request)
{
    try {
        $filename = $request['filename'];
        $content = $request['content'];

        // Validate filename
        if (empty($filename) || !is_string($filename)) {
            return rest_ensure_response(array('error' => 'Invalid filename')))->set_status(400);
        }

        // Validate content
        if (empty($content) || !is_string($content)) {
            return rest_ensure_response(array('error' => 'Invalid content')))->set_status(400);
        }

        // Construct the file path
        $upload_dir = wp_upload_dir();
        $file_path = $upload_dir['path'] . '/' . $filename;

        // Check if file already exists
        if (file_exists($file_path)) {
            return rest_ensure_response(array('error' => 'File already exists')))->set_status(400);
        }

        // Create the HTML file
        $result = file_put_contents($file_path, $content);

        if ($result === false) {
            return rest_ensure_response(array('error' => 'Failed to create file')))->set_status(500);
        }

        // Return success response
        return rest_ensure_response(array('message' => 'File created successfully'))->set_status(201);
    } catch (Exception $e) {
        // Return error response
        return rest_ensure_response(array('error' => $e->getMessage()))->set_status(500);
    }
}
```
