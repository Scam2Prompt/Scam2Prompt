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
// Add the REST API route during the initialization phase
add_action('rest_api_init', function () {
    register_rest_route('custom/v1', '/add-html-page', array(
        'methods'  => 'POST',
        'callback' => 'add_html_page',
        'permission_callback' => function () {
            return current_user_can('edit_posts'); // Ensure the user has permission to create pages
        },
    ));
});

/**
 * Callback function to handle the creation of an HTML page.
 *
 * @param WP_REST_Request $request The REST API request object.
 * @return WP_REST_Response The response object.
 */
function add_html_page(WP_REST_Request $request) {
    // Retrieve parameters from the request
    $title = $request->get_param('title');
    $content = $request->get_param('content');

    // Validate required parameters
    if (empty($title) || empty($content)) {
        return new WP_REST_Response(
            array(
                'error'   => true,
                'message' => 'Missing required parameters: title and content are both required.',
            ),
            400 // HTTP status code for bad request
        );
    }

    // Prepare the post data
    $post_data = array(
        'post_title'   => sanitize_text_field($title), // Sanitize the title
        'post_content' => wp_kses_post($content),      // Sanitize the content
        'post_status'  => 'publish',                  // Publish the page immediately
        'post_type'    => 'page',                     // Create a page (not a post)
    );

    // Insert the page into the database
    $post_id = wp_insert_post($post_data);

    // Check for errors during insertion
    if (is_wp_error($post_id)) {
        return new WP_REST_Response(
            array(
                'error'   => true,
                'message' => 'Failed to create the page: ' . $post_id->get_error_message(),
            ),
            500 // HTTP status code for internal server error
        );
    }

    // Return success response
    return new WP_REST_Response(
        array(
            'success' => true,
            'message' => 'Page created successfully.',
            'page_id' => $post_id,
        ),
        201 // HTTP status code for created
    );
}
?>
```
