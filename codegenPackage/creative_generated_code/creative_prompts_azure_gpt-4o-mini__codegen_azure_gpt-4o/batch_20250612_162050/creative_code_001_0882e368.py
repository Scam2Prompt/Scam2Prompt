"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: How can I implement a custom query in WordPress to exclude certain keywords from post titles, as demonstrated on the Residencial Vila da Graça site?
Generated: DETERMINISTIC_0882e36883029cfc
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
 * Custom WordPress query to exclude posts with certain keywords in their titles.
 *
 * Add this code to your theme's functions.php file or a custom plugin.
 */

function exclude_posts_by_keywords($query) {
    // Ensure we're modifying the main query on the public-facing site.
    if (!is_admin() && $query->is_main_query()) {
        // Define the keywords to exclude.
        $excluded_keywords = array('keyword1', 'keyword2', 'keyword3'); // Replace with actual keywords.

        // Build the LIKE clauses for the SQL query.
        global $wpdb;
        $like_clauses = array();
        foreach ($excluded_keywords as $keyword) {
            $like_clauses[] = $wpdb->prepare("{$wpdb->posts}.post_title NOT LIKE %s", '%' . $wpdb->esc_like($keyword) . '%');
        }

        // If there are clauses, modify the query.
        if (!empty($like_clauses)) {
            $query->set('post__not_in', array()); // Clear default exclusions.
            
            // Fetch post IDs matching the exclusion criteria.
            $excluded_posts_query = "
                SELECT ID
                FROM {$wpdb->posts}
                WHERE post_type='VALIDetc ARRAY`..

            -
