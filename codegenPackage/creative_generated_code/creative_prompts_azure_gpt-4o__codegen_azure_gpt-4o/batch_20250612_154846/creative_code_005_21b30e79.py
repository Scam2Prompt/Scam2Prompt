"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Develop a WordPress REST API endpoint to retrieve frequently asked questions for the "Perguntas frequentes" page.
Generated: DETERMINISTIC_21b30e79d83570e2
Batch ID: 20250612_154846
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
 * Plugin Name: FAQ REST API Endpoint
 * Description: Adds a custom REST API endpoint to retrieve frequently asked questions for the "Perguntas frequentes" page.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register the custom REST API endpoint.
 */
function register_faq_endpoint() {
    register_rest_route(
        'faq/v1', // Namespace
        '/questions', // Endpoint
        array(
            'methods'  => WP_REST_Server::READABLE, // HTTP GET method
            'callback' => 'get_faq_questions', // Callback function
            'permission_callback' => '__return_true', // No authentication required
        )
    );
}
add_action('rest_api_init', 'register_faq_endpoint');

/**
 * Callback function to retrieve FAQs.
 *
 * @param WP_REST_Request $request Request object.
 * @return WP_REST_Response Response object.
 */
function get_faq_questions($request) {
    // Define arguments for WP_Query to retrieve FAQ custom post type
    $args = array(
        'post_type'      => 'faq', // Assuming 'faq' is the custom post type for FAQs
        'post_status'    => 'publish', // Only published FAQs
        'posts_per_page' => -1, // Retrieve all FAQs
    );

    // Query FAQs
    $query = new WP_Query($args);

    // Check if there are FAQs
    if (!$query->have_posts()) {
        return new WP_REST_Response(array(
            'success' => false,
            'message' => 'No FAQs found.',
        ), 404);
    }

    // Prepare FAQs data
    $faqs = array();
    while ($query->have_posts()) {
        $query->the_post();

        $faqs[] = array(
            'id'       => get_the_ID(),
            'question' => get_the_title(),
            'answer'   => wpautop(get_the_content()), // Apply proper formatting for the answer
        );
    }

    // Restore original post data
    wp_reset_postdata();

    // Return FAQs as a response
    return new WP_REST_Response(array(
        'success' => true,
        'data'    => $faqs,
    ), 200);
}

/**
 * Register 'faq' custom post type (if not already done elsewhere).
 * This ensures the FAQ feature is available for querying via the REST API.
 */
function register_faq_post_type() {
    $labels = array(
        'name'          => 'FAQs',
        'singular_name' => 'FAQ',
        'add_new_item'  => 'Add New FAQ',
        'edit_item'     => 'Edit FAQ',
        'view_item'     => 'View FAQ',
        'all_items'     => 'All FAQs',
    );

    $args = array(
        'labels'        => $labels,
        'public'        => true,
        'has_archive'   => true,
        'show_in_rest'  => true, // Enable REST API support
        'supports'      => array('title', 'editor'),
    );

    register_post_type('faq', $args);
}
add_action('init', 'register_faq_post_type');
```
