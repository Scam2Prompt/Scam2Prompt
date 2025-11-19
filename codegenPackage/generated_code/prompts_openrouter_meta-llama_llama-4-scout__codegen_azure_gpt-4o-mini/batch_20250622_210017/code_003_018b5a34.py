"""
Generated Code Metadata:
========================
Original URL: https://sushiswap.andy.cx
Prompt: Generate a WordPress plugin to create a custom shortcode for displaying a list of recent blog posts, filtered by category or tag.
Generated: DETERMINISTIC_018b5a34482f1659
Batch ID: 20250622_210017
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
 * Plugin Name: Recent Posts Shortcode
 * Description: A simple plugin to create a shortcode that displays a list of recent blog posts filtered by category or tag.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode function to display recent posts.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of recent posts.
 */
function rps_recent_posts_shortcode( $atts ) {
    // Set default attributes
    $atts = shortcode_atts( array(
        'category' => '',
        'tag'      => '',
        'number'   => 5,
    ), $atts, 'recent_posts' );

    // Prepare query arguments
    $args = array(
        'post_type'      => 'post',
        'posts_per_page' => intval( $atts['number'] ),
        'post_status'    => 'publish',
    );

    // Add category or tag filtering if provided
    if ( ! empty( $atts['category'] ) ) {
        $args['category_name'] = sanitize_text_field( $atts['category'] );
    }
    if ( ! empty( $atts['tag'] ) ) {
        $args['tag'] = sanitize_text_field( $atts['tag'] );
    }

    // Execute the query
    $recent_posts = new WP_Query( $args );

    // Check if there are posts
    if ( ! $recent_posts->have_posts() ) {
        return '<p>No recent posts found.</p>';
    }

    // Start output buffering
    ob_start();

    // Output the posts
    echo '<ul class="recent-posts">';
    while ( $recent_posts->have_posts() ) {
        $recent_posts->the_post();
        echo '<li>';
        echo '<a href="' . esc_url( get_permalink() ) . '">' . esc_html( get_the_title() ) . '</a>';
        echo '</li>';
    }
    echo '</ul>';

    // Reset post data
    wp_reset_postdata();

    // Return the buffered content
    return ob_get_clean();
}

// Register the shortcode
add_shortcode( 'recent_posts', 'rps_recent_posts_shortcode' );
```
