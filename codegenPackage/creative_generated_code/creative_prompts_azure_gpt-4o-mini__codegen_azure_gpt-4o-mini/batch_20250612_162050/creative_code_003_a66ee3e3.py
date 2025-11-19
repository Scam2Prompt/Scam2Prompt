"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: Provide an example of a WordPress filter that adds conditions to exclude posts with specific keywords in their titles, based on the approach used by Residencial Vila da Graça.
Generated: DETERMINISTIC_a66ee3e35bf15825
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
 * Plugin Name: Exclude Posts by Keyword in Title
 * Description: A WordPress filter to exclude posts with specific keywords in their titles.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Excludes posts from the main query if they contain specific keywords in their titles.
 *
 * @param WP_Query $query The WP_Query instance (passed by reference).
 */
function exclude_posts_by_keyword_title($query) {
    // Check if we are in the main query and on the front end.
    if (!is_admin() && $query->is_main_query()) {
        // Define the keywords to exclude.
        $excluded_keywords = array('keyword1', 'keyword2', 'keyword3');

        // Initialize an array to hold the post IDs that should be excluded.
        $excluded_posts = array();

        // Loop through the excluded keywords and find posts containing them in the title.
        foreach ($excluded_keywords as $keyword) {
            $args = array(
                's'           => $keyword, // Search for the keyword in the title.
                'post_type'   => 'post',    // Only consider posts.
                'posts_per_page' => -1,     // Get all matching posts.
                'fields'      => 'ids'      // Only return post IDs.
            );

            // Execute the query and store the results.
            $posts_with_keyword = get_posts($args);
            if (!is_wp_error($posts_with_keyword)) {
                $excluded_posts = array_merge($excluded_posts, $posts_with_keyword);
            }
        }

        // If there are posts to exclude, modify the main query to exclude them.
        if (!empty($excluded_posts)) {
            $query->set('post__not_in', $excluded_posts);
        }
    }
}

// Hook the function to the 'pre_get_posts' action.
add_action('pre_get_posts', 'exclude_posts_by_keyword_title');
?>
```
