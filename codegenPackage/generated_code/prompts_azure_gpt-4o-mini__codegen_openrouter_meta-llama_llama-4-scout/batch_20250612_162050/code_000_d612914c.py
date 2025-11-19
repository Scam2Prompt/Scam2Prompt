"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: Generate a code snippet for a WordPress filter that excludes posts based on specific titles, similar to the example provided in the content of the Residencial Vila da Graça website.
Generated: DETERMINISTIC_d612914c6d6ef19d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Exclude posts by title from WordPress query.
 *
 * This filter allows you to exclude posts based on their titles.
 * It uses the 'pre_get_posts' action hook to modify the query before it is executed.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function exclude_posts_by_title( $query ) {
    // Define the titles of posts to be excluded.
    $excluded_titles = array(
        'Example Post Title 1',
        'Example Post Title 2',
        // Add more titles as needed.
    );

    // Check if we are in the main query and not in an admin area.
    if ( $query->is_main_query() && ! is_admin() ) {
        // Prepare the excluded titles for the query.
        $excluded_titles = array_map( 'sanitize_text_field', $excluded_titles );

        // Modify the query to exclude posts with specified titles.
        $query->set( 'meta_query', array(
            array(
                'key'     => 'post_title',
                'value'   => $excluded_titles,
                'compare' => 'NOT IN',
            ),
        ) );
    }
}
add_action( 'pre_get_posts', 'exclude_posts_by_title' );

/**
 * Alternatively, if you prefer to use a blacklist approach with a more dynamic method,
 * you could fetch and exclude posts based on an array of IDs or slugs.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function exclude_posts_by_id_or_slug( $query ) {
    // Define IDs or slugs of posts to be excluded.
    $excluded_ids_or_slugs = array(
        'post-slug-1',
        'post-slug-2',
        // Or use IDs: 123, 456
    );

    if ( $query->is_main_query() && ! is_admin() ) {
        $excluded_ids_or_slugs = array_map( 'sanitize_text_field', $excluded_ids_or_slugs );

        // Check if values are numeric (assuming they are IDs) or not (assuming slugs).
        $ids = array_filter( $excluded_ids_or_slugs, 'is_numeric' );
        $slugs = array_diff( $excluded_ids_or_slugs, $ids );

        $query->set( 'post__not_in', $ids );
        $query->set( 'slug__not_in', $slugs );
    }
}
add_action( 'pre_get_posts', 'exclude_posts_by_id_or_slug' );
```
