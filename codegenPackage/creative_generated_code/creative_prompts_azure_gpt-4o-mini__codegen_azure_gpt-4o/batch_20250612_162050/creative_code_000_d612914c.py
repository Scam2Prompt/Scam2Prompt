"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: Generate a code snippet for a WordPress filter that excludes posts based on specific titles, similar to the example provided in the content of the Residencial Vila da Graça website.
Generated: DETERMINISTIC_d612914c6d6ef19d
Batch ID: 20250612_162050
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
 * WordPress filter to exclude posts with specific titles.
 * 
 * This code snippet hooks into the 'posts_where' filter to exclude
 * posts based on specific titles. Add this code to your theme's
 * functions.php file or a custom plugin.
 */

add_filter('posts_where', 'exclude_posts_by_title', 10, 2);

/**
 * Callback function to modify the WHERE clause of the query.
 *
 * @param string   $where The WHERE clause of the query.
 * @param WP_Query $query The WP_Query instance (passed by reference).
 * @return string Filtered WHERE clause.
 */
function exclude_posts_by_title($where, $query) {
    // Titles to exclude; modify this array to include the titles you want excluded.
    $titles_to_exclude = array(
        'Title 1',
        'Title 2',
        'Title 3'
    );

    // Ensure the exclusion applies only to the main query.
    if ($query->is_main_query() && !is_admin()) {
        global $wpdb;

        // Escape the titles for database query.
        $escaped_titles = array_map(function($title) use ($wpdb) {
            return $wpdb->prepare('%s', $title);
        }, $titles_to_exclude);

        // Build the exclusion clause.
        $where .= " AND {$wpdb->posts}.post_title NOT IN (" . implode(',', $escaped_titles) . ")";
    }

    return $where;
}
```

This code snippet is clean, adheres to best practices, and includes inline comments for clarity. Make sure to test it before deploying to production.
