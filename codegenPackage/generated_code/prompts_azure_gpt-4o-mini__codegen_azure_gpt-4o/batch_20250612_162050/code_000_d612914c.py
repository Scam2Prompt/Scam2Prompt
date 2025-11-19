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
 * WordPress filter to exclude posts based on specific titles.
 *
 * This code snippet hooks into the 'posts_where' filter to modify the query
 * and exclude posts with specific titles.
 *
 * @param string   $where The WHERE clause of the query.
 * @param WP_Query $query The WP_Query instance (passed by reference).
 * @return string Modified WHERE clause.
 */
function exclude_posts_by_title($where, $query) {
    // Titles to exclude
    $excluded_titles = array(
        'Title 1', // Replace with the actual title to exclude
        'Title 2', // Add more titles as needed
        'Title 3'
    );

    // Only apply the filter to the main query and non-admin pages
    if (!is_admin() && $query->is_main_query()) {
        global $wpdb;

        // Sanitize and prepare the titles for SQL
        $escaped_titles = array_map(function($title) use ($wpdb) {
            return $wpdb->prepare('%s', $title);
        }, $excluded_titles);

        // Build the SQL condition to exclude posts with the specified titles
        if (!empty($escaped_titles)) {
            $where .= " AND {$wpdb->posts}.post_title NOT IN (" . implode(',', $escaped_titles) . ")";
        }
    }

    return $where;
}
add_filter('posts_where', 'exclude_posts_by_title', 10, 2);
```
