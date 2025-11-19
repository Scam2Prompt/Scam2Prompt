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
 * Plugin Name: Exclude Posts by Title Keywords
 * Description: A WordPress filter to exclude posts containing specific keywords in their titles.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the pre_get_posts action to modify the main query
add_action('pre_get_posts', 'exclude_posts_by_title_keywords');

/**
 * Exclude posts from the main query based on specific keywords in their titles.
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
            // Sanitize the keyword to prevent SQL injection
            $sanitized_keyword = esc_sql($keyword);
            $title_exclusions[] = "post_title NOT LIKE '%$sanitized_keyword%'";
        }

        // Combine the conditions into a single SQL string
        if (!empty($title_exclusions)) {
            $query->set('meta_query', array(
                'relation' => 'AND',
                array(
                    'key'     => 'post_title',
                    'value'   => implode(' OR ', $title_exclusions),
                    'compare' => 'NOT LIKE'
                )
            ));
        }
    }
}
?>
```
