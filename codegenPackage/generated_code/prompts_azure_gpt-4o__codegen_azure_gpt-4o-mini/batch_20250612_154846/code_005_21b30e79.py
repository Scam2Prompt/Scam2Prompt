"""
Generated Code Metadata:
========================
Original URL: https://offerspecials.online
Prompt: Develop a WordPress REST API endpoint to retrieve frequently asked questions for the "Perguntas frequentes" page.
Generated: DETERMINISTIC_21b30e79d83570e2
Batch ID: 20250612_154846
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
 * Plugin Name: FAQ REST API
 * Description: A custom REST API endpoint to retrieve frequently asked questions for the "Perguntas frequentes" page.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register the FAQ REST API endpoint.
 */
function register_faq_endpoint() {
    register_rest_route( 'faq/v1', '/questions', array(
        'methods'  => 'GET',
        'callback' => 'get_faq_questions',
        'permission_callback' => '__return_true', // Public access, adjust as needed
    ));
}
add_action( 'rest_api_init', 'register_faq_endpoint' );

/**
 * Retrieve frequently asked questions.
 *
 * @return WP_REST_Response|WP_Error Response object or error object.
 */
function get_faq_questions() {
    // Fetch FAQs from a custom post type or a specific page
    $args = array(
        'post_type'      => 'faq', // Change to your custom post type if needed
        'posts_per_page' => -1,     // Retrieve all FAQs
        'post_status'    => 'publish',
    );

    $faq_query = new WP_Query( $args );

    // Check if any FAQs were found
    if ( ! $faq_query->have_posts() ) {
        return new WP_Error( 'no_faqs', 'No frequently asked questions found', array( 'status' => 404 ) );
    }

    $faqs = array();

    // Loop through the FAQs and format the response
    while ( $faq_query->have_posts() ) {
        $faq_query->the_post();
        $faqs[] = array(
            'id'      => get_the_ID(),
            'question' => get_the_title(),
            'answer'   => apply_filters( 'the_content', get_the_content() ),
        );
    }

    // Restore original Post Data
    wp_reset_postdata();

    // Return the FAQs as a JSON response
    return new WP_REST_Response( $faqs, 200 );
}
```
