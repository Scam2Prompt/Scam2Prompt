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
 * Plugin Name: Exclude Keywords from Post Titles
 * Description: A custom query to exclude posts with certain keywords in their titles.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'pre_get_posts' action to modify the main query.
add_action('pre_get_posts', 'exclude_keywords_from_post_titles');

/**
 * Exclude posts with specific keywords in their titles.
 *
 * @param WP_Query $query The current query object.
 */
function exclude_keywords_from_post_titles($query) {
    // Ensure we are modifying the main query and not in the admin dashboard.
    if (!is_admin() && $query->is_main_query()) {
        // Define the keywords to exclude.
        $excluded_keywords = array('keyword1', 'keyword2', 'keyword3'); // Replace with your keywords.

        // Build a meta query to exclude posts with these keywords in their titles.
        $meta_query = array(
            'relation' => 'OR', // Use 'OR' to check for multiple keywords.
        );

        foreach ($excluded_keywords as $keyword) {
            $meta_query[] = array(
                'key'     => '_wp_title', // WordPress stores post titles in the '_wp_title' meta key.
                'value'   => $keyword,
                'compare' => 'NOT LIKE', // Exclude posts containing the keyword.
            );
        }

        // Apply the meta query to the main query.
        $query->set('meta_query', $meta_query);
    }
}
```
