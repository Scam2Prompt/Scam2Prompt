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
 * Plugin Name: Exclude Specific Posts by Title
 * Description: A WordPress filter to exclude posts with specific titles from the main query.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the pre_get_posts action to modify the main query
add_action('pre_get_posts', 'exclude_specific_posts_by_title');

/**
 * Exclude posts with specific titles from the main query.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function exclude_specific_posts_by_title($query) {
    // Check if we are in the main query and on the front end
    if (!is_admin() && $query->is_main_query()) {
        // Array of titles to exclude
        $excluded_titles = array(
            'Title to Exclude 1',
            'Title to Exclude 2',
            'Title to Exclude 3',
        );

        // Prepare an array to hold the IDs of posts to exclude
        $excluded_ids = array();

        // Loop through the excluded titles and get their IDs
        foreach ($excluded_titles as $title) {
            $post = get_page_by_title($title, OBJECT, 'post');
            if ($post) {
                $excluded_ids[] = $post->ID;
            }
        }

        // If there are any IDs to exclude, modify the query
        if (!empty($excluded_ids)) {
            $query->set('post__not_in', $excluded_ids);
        }
    }
}
?>
```
