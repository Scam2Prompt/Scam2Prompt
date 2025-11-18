"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Generate code to implement a search functionality in a WordPress eCommerce site for keywords like "Bhagalpuri silk saree" and "Cotton saree" using the REST API.
Generated: DETERMINISTIC_75978225fac0f79f
Batch ID: 20250612_150327
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
 * Plugin Name: Custom Saree Search API
 * Description: Adds custom search functionality to an eCommerce WordPress site using REST API.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register the custom REST API route for product search.
 */
function register_saree_search_endpoint() {
    register_rest_route('custom/v1', '/search', array(
        'methods' => WP_REST_Server::READABLE,
        'callback' => 'custom_saree_search',
        'permission_callback' => '__return_true',
        'args' => array(
            'keyword' => array(
                'required' => true,
                'validate_callback' => 'is_string',
            ),
        ),
    ));
}
add_action('rest_api_init', 'register_saree_search_endpoint');

/**
 * Handle the custom search functionality.
 *
 * @param WP_REST_Request $request The REST API request.
 * @return WP_REST_Response The response.
 */
function custom_saree_search($request) {
    // Extract the keyword from the request
    $keyword = sanitize_text_field($request->get_param('keyword'));

    // Ensure keyword is not empty
    if (empty($keyword)) {
        return new WP_REST_Response(
            array(
                'error' => true,
                'message' => 'Keyword parameter is required.'
            ),
            400
        );
    }

    // Arguments for WP_Query to search products
    $args = array(
        'post_type' => 'product',
        'posts_per_page' => 10,
        's' => $keyword, // Search by keyword
        'post_status' => 'publish',
    );

    // Query the products
    $query = new WP_Query($args);

    // Check if results exist
    if (!$query->have_posts()) {
        return new WP_REST_Response(
            array(
                'error' => false,
                'message' => 'No products found for the given keyword.',
                'data' => array()
            ),
            200
        );
    }

    // Prepare the response data
    $products = array();
    while ($query->have_posts()) {
        $query->the_post();

        // Collect basic product information
        $products[] = array(
            'id' => get_the_ID(),
            'title' => get_the_title(),
            'url' => get_permalink(),
            'price' => get_post_meta(get_the_ID(), '_price', true), // WooCommerce price meta key
            'thumbnail' => get_the_post_thumbnail_url(get_the_ID(), 'thumbnail'),
        );
    }

    // Reset post data
    wp_reset_postdata();

    // Return the response
    return new WP_REST_Response(
        array(
            'error' => false,
            'message' => 'Products found.',
            'data' => $products
        ),
        200
    );
}
```

This code snippet creates a WordPress plugin that registers a custom REST API endpoint (`/custom/v1/search`) to search for products by keyword such as "Bhagalpuri silk saree" or "Cotton saree". The endpoint uses `WP_Query` to fetch published products matching the given keyword and returns relevant product data in JSON format.
