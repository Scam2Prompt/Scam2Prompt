"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: Provide an example of a WordPress filter that adds conditions to exclude posts with specific keywords in their titles, based on the approach used by Residencial Vila da Graça.
Generated: DETERMINISTIC_a66ee3e35bf15825
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
 * Plugin Name: Exclude Posts by Title Keywords
 * Description: A WordPress filter to exclude posts with specific keywords in their titles.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'pre_get_posts' action to modify the main query
add_action('pre_get_posts', 'exclude_posts_by_title_keywords');

/**
 * Exclude posts with specific keywords in their titles from the main query.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function exclude_posts_by_title_keywords($query) {
    // Check if we are in the main query and on the front end
    if (!is_admin() && $query->is_main_query()) {
        // Define the keywords to exclude
        $excluded_keywords = array('keyword1', 'keyword2', 'keyword3');

        // Initialize an array to hold the title exclusion conditions
        $title_exclusions = array();

        // Loop through each keyword and create a condition for exclusion
        foreach ($excluded_keywords as $keyword) {
            $title_exclusions[] = "NOT LIKE '%" . esc_sql($keyword) . "%'";
        }

        // If there are any keywords to exclude, modify the query
        if (!empty($title_exclusions)) {
            // Build the SQL condition string
            $title_condition = implode(' AND ', $title_exclusions);

            // Use the 'posts_where' filter to modify the SQL WHERE clause
            add_filter('posts_where', function($where) use ($title_condition) {
                return $where . " AND (post_title " . $title_condition . ")";
            });
        }
    }
}
```
