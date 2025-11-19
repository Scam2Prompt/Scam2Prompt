"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Generate code to implement a search functionality in a WordPress eCommerce site for keywords like "Bhagalpuri silk saree" and "Cotton saree" using the REST API.
Generated: DETERMINISTIC_75978225fac0f79f
Batch ID: 20250612_150327
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
 * Plugin Name: WooCommerce Product Search API
 * Description: Extends WooCommerce REST API for custom product search functionality.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

add_action('rest_api_init', 'register_custom_product_search_endpoint');

/**
 * Registers custom REST API endpoint for product search
 */
function register_custom_product_search_endpoint() {
    register_rest_route('wc/v3', '/products/search', array(
        'methods' => 'GET',
        'callback' => 'handle_product_search_request',
        'permission_callback' => '__return_true',
        'args' => array(
            'query' => array(
                'required' => true,
                'validate_callback' => function($param) {
                    return is_string($param) && !empty(trim($param));
                },
                'sanitize_callback' => 'sanitize_text_field'
            ),
            'per_page' => array(
                'default' => 10,
                'validate_callback' => function($param) {
                    return is_numeric($param) && $param > 0;
                },
                'sanitize_callback' => 'absint'
            ),
            'page' => array(
                'default' => 1,
                'validate_callback' => function($param) {
                    return is_numeric($param) && $param > 0;
                },
                'sanitize_callback' => 'absint'
            )
        )
    ));
}

/**
 * Handles product search request
 * 
 * @param WP_REST_Request $request Full data about the request.
 * @return WP_REST_Response|WP_Error
 */
function handle_product_search_request($request) {
    try {
        $query = $request->get_param('query');
        $per_page = $request->get_param('per_page');
        $page = $request->get_param('page');

        $args = array(
            'post_type' => 'product',
            'posts_per_page' => $per_page,
            'paged' => $page,
            's' => $query,
            'post_status' => 'publish'
        );

        // Search in product title, description and meta fields
        add_filter('posts_where', 'extend_product_search_where', 10, 2);
        $query = new WP_Query($args);
        remove_filter('posts_where', 'extend_product_search_where', 10);

        if (!$query->have_posts()) {
            return new WP_REST_Response(array(
                'success' => true,
                'data' => array(),
                'message' => 'No products found'
            ), 200);
        }

        $products = array();
        while ($query->have_posts()) {
            $query->the_post();
            $product = wc_get_product(get_the_ID());
            
            $products[] = array(
                'id' => $product->get_id(),
                'name' => $product->get_name(),
                'description' => $product->get_description(),
                'price' => $product->get_price(),
                'image' => wp_get_attachment_url($product->get_image_id()),
                'permalink' => get_permalink($product->get_id())
            );
        }

        wp_reset_postdata();

        return new WP_REST_Response(array(
            'success' => true,
            'data' => array(
                'products' => $products,
                'total' => $query->found_posts,
                'pages' => $query->max_num_pages
            )
        ), 200);

    } catch (Exception $e) {
        return new WP_Error(
            'search_error',
            'An error occurred while searching products',
            array('status' => 500)
        );
    }
}

/**
 * Extends product search to include meta fields
 * 
 * @param string $where The WHERE clause of the query.
 * @param WP_Query $wp_query The WP_Query instance.
 * @return string Modified WHERE clause
 */
function extend_product_search_where($where, $wp_query) {
    global $wpdb;
    
    if ($search_term = $wp_query->get('s')) {
        $where .= " OR ({$wpdb->posts}.ID IN (
            SELECT post_id
            FROM {$wpdb->postmeta}
            WHERE meta_key IN ('_sku', '_product_attributes')
            AND meta_value LIKE '%" . esc_sql($search_term) . "%'
        ))";
    }
    
    return $where;
}
```
