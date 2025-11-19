"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Generate a WordPress filter function similar to the one used on residencialviladagraca.com.br to exclude posts containing specific keywords in their titles."
Generated: DETERMINISTIC_dfd8e3a32c815ce6
Batch ID: 20250622_210650
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
 * Filter WordPress query to exclude posts with specific keywords in their titles.
 *
 * This function hooks into the 'posts_where' filter to modify the SQL WHERE clause
 * and exclude posts containing certain keywords in their titles.
 *
 * @param string   $where The existing WHERE clause of the query.
 * @param WP_Query $query The WP_Query instance (passed by reference).
 * @return string Modified WHERE clause.
 */
function exclude_posts_with_keywords_in_title($where, $query) {
    // Define the keywords to exclude.
    $excluded_keywords = array('keyword1', 'keyword2', 'keyword3'); // Replace with your keywords.

    // Only apply the filter to the main query and not in admin area.
    if (!is_admin() && $query->is_main_query()) {
        global $wpdb;

        // Build the SQL condition to exclude posts with the specified keywords in their titles.
        $keyword_conditions = array();
        foreach ($excluded_keywords as $keyword) {
            $keyword_conditions[] = $wpdb->prepare("{$wpdb->posts}.post_title NOT LIKE %s", '%' . $wpdb->esc_like($keyword) . '%');
        }

        // Append the conditions to the WHERE clause.
        if (!empty($keyword_conditions)) {
            $where .= ' AND (' . implode(' AND ', $keyword_conditions) . ')';
        }
    }

    return $where;
}

// Add the filter to modify the query.
add_filter('posts_where', 'exclude_posts_with_keywords_in_title', 10, 2);
?>
```
