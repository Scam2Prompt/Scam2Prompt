"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Generate a WordPress function that adjusts post counts in the admin panel to exclude posts from a specific author, using `$wpdb` queries and filters like `views_edit-post`.
Generated: DETERMINISTIC_a474447b9cea7aaf
Batch ID: 20250612_152924
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
 * Plugin Name: Adjust Admin Post Counts
 * Description: Exclude posts from a specific author in the admin panel post counts.
 * Version: 1.0
 * Author: Your Name
 */

// Define the author ID to exclude.
define('EXCLUDED_AUTHOR_ID', 2); // Replace 2 with the actual author ID you want to exclude.

/**
 * Adjust post count in the "All" filter in the admin posts list.
 *
 * @param array $views Array of views in the admin posts list.
 * @return array Modified views array.
 */
function adjust_admin_post_counts($views) {
    global $wpdb;

    // Get counts for all posts excluding those from the specified author.
    $total_posts_query = "
        SELECT COUNT(ID)
        FROM {$wpdb->posts} 
        WHERE post_type = 'post'
        AND post_status = 'publish'
        AND post_author != %d
    ";
    
    $total_posts = $wpdb->get_var($wpdb->prepare($total_posts_query, EXCLUDED_AUTHOR_ID));
    
    // Modify the "All" posts count link.
    if (isset($views['all'])) {
        $views['all'] = preg_replace('/\(.+\)/', '(' . $total_posts . ')', $views['all']);
    }

    return $views;
}
add_filter('views_edit-post', 'adjust_admin_post_counts');

/**
 * Adjust admin queries to exclude posts from the specified author.
 *
 * @param WP_Query $query The current query object.
 * @return void
 */
function exclude_author_posts_from_admin($query) {
    if (is_admin() && $query->is_main_query() && $query->get('post_type') === 'post') {
        $meta_query = $query->get('meta_query');

        // Exclude posts from the specified author.
        $query->set('author__not_in', array(EXCLUDED_AUTHOR_ID));

        if (!empty($meta_query)) {
            $query->set('meta_query', $meta_query);
        }
    }
}
add_action('pre_get_posts', 'exclude_author_posts_from_admin');
```
