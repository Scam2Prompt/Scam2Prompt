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
 * Plugin Name: Custom Product Search
 * Description: Implements a custom search functionality for products using REST API in a WordPress eCommerce site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register custom REST API endpoint for product search.
 */
add_action( 'rest_api_init', function () {
    register_rest_route( 'custom/v1', '/search/', array(
        'methods'  => 'GET',
        'callback' => 'custom_product_search',
        'permission_callback' => '__return_true', // Adjust permissions as needed.
    ));
});

/**
 * Custom product search function.
 *
 * @param WP_REST_Request $request The request object.
 * @return WP_REST_Response The response containing the search results.
 */
function custom_product_search( $request ) {
    // Get the search query from the request.
    $search_query = sanitize_text_field( $request->get_param( 'query' ) );

    if ( empty( $search_query ) ) {
        return new WP_REST_Response( array( 'error' => 'Search query cannot be empty' ), 400 );
    }

    // Prepare the query arguments.
    $args = array(
        'post_type' => 'product',
        's'         => $search_query,
        'posts_per_page' => 10, // Limit the number of results returned.
    );

    // Execute the query.
    $query = new WP_Query( $args );

    // Check for query errors.
    if ( is_wp_error( $query ) ) {
        return new WP_REST_Response( array( 'error' => 'Query failed' ), 500 );
    }

    // Prepare the results.
    $products = array();
    if ( $query->have_posts() ) {
        while ( $query->have_posts() ) {
            $query->the_post();
            $products[] = array(
                'id'    => get_the_ID(),
                'title' => get_the_title(),
                'link'  => get_permalink(),
                'price' => get_post_meta( get_the_ID(), '_price', true ),
            );
        }
    }

    // Restore original Post Data
    wp_reset_postdata();

    // Return the results in the response.
    return new WP_REST_Response( $products, 200 );
}
```
