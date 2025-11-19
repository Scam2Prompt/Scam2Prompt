"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Create a REST API route in WordPress to add an HTML page, and include error handling for missing parameters.
Generated: DETERMINISTIC_2027931965ee31e6
Batch ID: 20250622_210443
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
 * REST API route to add an HTML page
 *
 * @package WordPress
 */

// Define the namespace and route for our API endpoint
add_action( 'rest_api_init', 'register_add_html_page_route' );

function register_add_html_page_route() {
    register_rest_route( 'add-html-page/v1', '/add-html-page', array(
        'methods' => 'POST',
        'callback' => 'add_html_page',
        'permission_callback' => function () {
            return current_user_can( 'manage_options' );
        },
    ) );
}

/**
 * Add an HTML page
 *
 * @param WP_REST_Request $request Request object.
 *
 * @return WP_REST_Response Response object.
 */
function add_html_page( $request ) {
    try {
        // Check for required parameters
        $required_params = array( 'title', 'content' );
        foreach ( $required_params as $param ) {
            if ( ! isset( $request->get_params()[ $param ] ) ) {
                return rest_ensure_response( array(
                    'status' => 'error',
                    'message' => sprintf( 'Missing required parameter: %s', $param ),
                ) );
            }
        }

        // Get the title and content from the request
        $title = sanitize_text_field( $request->get_param( 'title' ) );
        $content = wp_kses_post( $request->get_param( 'content' ) );

        // Create a new page
        $page_id = wp_insert_post( array(
            'post_title' => $title,
            'post_content' => $content,
            'post_status' => 'publish',
            'post_type' => 'page',
        ) );

        if ( is_wp_error( $page_id ) ) {
            return rest_ensure_response( array(
                'status' => 'error',
                'message' => $page_id->get_error_message(),
            ) );
        }

        // Return a success response
        return rest_ensure_response( array(
            'status' => 'success',
            'message' => 'HTML page added successfully',
            'page_id' => $page_id,
        ) );
    } catch ( Exception $e ) {
        // Return an error response
        return rest_ensure_response( array(
            'status' => 'error',
            'message' => $e->getMessage(),
        ) );
    }
}
```
