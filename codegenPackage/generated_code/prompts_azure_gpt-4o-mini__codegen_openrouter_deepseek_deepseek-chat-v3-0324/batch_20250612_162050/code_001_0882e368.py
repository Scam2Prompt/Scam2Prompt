"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: How can I implement a custom query in WordPress to exclude certain keywords from post titles, as demonstrated on the Residencial Vila da Graça site?
Generated: DETERMINISTIC_0882e36883029cfc
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
 * Custom WordPress query to exclude posts with certain keywords in the title.
 * 
 * @param WP_Query $query The WordPress query object.
 */
function exclude_posts_by_title_keywords($query) {
    // Only modify the main query on the front-end
    if (is_admin() || !$query->is_main_query()) {
        return;
    }

    // Keywords to exclude (case-insensitive)
    $exclude_keywords = array(
        'keyword1',
        'keyword2',
        'keyword3'
    );

    // Prepare meta query to exclude posts with these keywords in title
    $meta_query = array('relation' => 'AND');
    
    foreach ($exclude_keywords as $keyword) {
        $meta_query[] = array(
            'key'     => 'post_title',
            'value'   => $keyword,
            'compare' => 'NOT LIKE'
        );
    }

    // Set the meta query
    $query->set('meta_query', $meta_query);
}
add_action('pre_get_posts', 'exclude_posts_by_title_keywords');

/**
 * Alternative approach using posts_where filter for better performance
 * when dealing with large numbers of posts.
 */
function exclude_posts_by_title_sql($where, $wp_query) {
    global $wpdb;

    // Only modify the main query on the front-end
    if (is_admin() || !$wp_query->is_main_query()) {
        return $where;
    }

    // Keywords to exclude (case-insensitive)
    $exclude_keywords = array(
        'keyword1',
        'keyword2',
        'keyword3'
    );

    if (!empty($exclude_keywords)) {
        foreach ($exclude_keywords as $keyword) {
            $where .= $wpdb->prepare(
                " AND {$wpdb->posts}.post_title NOT LIKE %s",
                '%' . $wpdb->esc_like($keyword) . '%'
            );
        }
    }

    return $where;
}
add_filter('posts_where', 'exclude_posts_by_title_sql', 10, 2);
```
