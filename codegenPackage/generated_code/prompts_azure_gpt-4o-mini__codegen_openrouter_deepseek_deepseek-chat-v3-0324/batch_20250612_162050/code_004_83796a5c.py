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
 * Customize WordPress post queries using the 'posts_where' filter.
 * This example demonstrates excluding posts with specific titles from the query.
 */

/**
 * Add filter to modify the WHERE clause of the post query.
 */
add_filter('posts_where', 'custom_posts_where_filter', 10, 2);

/**
 * Custom posts_where filter callback.
 * Excludes posts with specific titles from the query.
 *
 * @param string $where The current WHERE clause.
 * @param WP_Query $query The WP_Query instance.
 * @return string Modified WHERE clause.
 */
function custom_posts_where_filter($where, $query) {
    // Only modify the query if it's the main query and not in admin area
    if ($query->is_main_query() && !is_admin()) {
        global $wpdb;
        
        // List of post titles to exclude
        $excluded_titles = array(
            'Unwanted Post 1',
            'Unwanted Post 2',
            'Residencial Vila da Graça'
        );
        
        // Sanitize and prepare titles for SQL
        $escaped_titles = array_map(function($title) use ($wpdb) {
            return $wpdb->prepare('%s', $title);
        }, $excluded_titles);
        
        // Add condition to exclude posts with these titles
        if (!empty($escaped_titles)) {
            $where .= " AND {$wpdb->posts}.post_title NOT IN (" . implode(',', $escaped_titles) . ")";
        }
    }
    
    return $where;
}
```
