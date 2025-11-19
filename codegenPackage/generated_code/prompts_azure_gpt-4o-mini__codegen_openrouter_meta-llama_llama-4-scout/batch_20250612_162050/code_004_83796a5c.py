"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: Explain how to use the WordPress `posts_where` filter to customize post queries, referencing the exclusion of titles as seen in the Residencial Vila da Graça code.
Generated: DETERMINISTIC_83796a5c2b2847fc
Batch ID: 20250612_162050
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
 * Plugin Name: Custom Post Query Filter
 * Description: This plugin demonstrates how to use the WordPress `posts_where` filter to customize post queries.
 * Version: 1.0
 */

// Hook into the posts_where filter
add_filter( 'posts_where', 'custom_posts_where', 10, 2 );

/**
 * Custom posts_where filter callback.
 *
 * This function modifies the WHERE clause of post queries to exclude posts with specific titles.
 *
 * @param string   $where    The current WHERE clause.
 * @param WP_Query $query    The current WP_Query instance.
 *
 * @return string The modified WHERE clause.
 */
function custom_posts_where( $where, $query ) {
    // Define the titles to exclude
    $excluded_titles = array( 'Excluded Title 1', 'Excluded Title 2' );

    // Check if we are in the admin area or on the frontend
    if ( is_admin() || ! is_null( $query->get_queried_object() ) ) {
        // If we are, modify the WHERE clause to exclude the specified titles
        $where .= " AND $query->table_posts.post_title NOT IN ('" . implode( "', '", array_map( 'esc_sql', $excluded_titles ) ) . "')";
    }

    return $where;
}

// Example usage:
// To test the filter, you can use the following code:
// $args = array(
//     'post_type' => 'post',
//     'posts_per_page' => -1,
// );
// $query = new WP_Query( $args );
// if ( $query->have_posts() ) {
//     while ( $query->have_posts() ) {
//         $query->the_post();
//         the_title();
//     }
// }
// wp_reset_postdata();
```
