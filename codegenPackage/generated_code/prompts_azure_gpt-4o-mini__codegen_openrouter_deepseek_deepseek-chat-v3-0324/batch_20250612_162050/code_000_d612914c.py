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
<?php
/**
 * Exclude posts with specific titles from the main query.
 *
 * @param WP_Query $query The WordPress query object.
 */
function exclude_posts_by_title( $query ) {
    // Only modify the main query on the front end
    if ( is_admin() || ! $query->is_main_query() ) {
        return;
    }

    // List of post titles to exclude
    $excluded_titles = array(
        'Unwanted Post Title 1',
        'Another Unwanted Post',
        'Exclude This Post',
    );

    // Get post IDs to exclude based on titles
    $excluded_ids = array();
    foreach ( $excluded_titles as $title ) {
        $post = get_page_by_title( $title, OBJECT, 'post' );
        if ( $post ) {
            $excluded_ids[] = $post->ID;
        }
    }

    // Exclude the posts if any were found
    if ( ! empty( $excluded_ids ) ) {
        $query->set( 'post__not_in', $excluded_ids );
    }
}
add_action( 'pre_get_posts', 'exclude_posts_by_title' );
```
