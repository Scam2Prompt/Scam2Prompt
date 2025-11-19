"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Generate a WordPress function that adjusts post counts in the admin panel to exclude posts from a specific author, using `$wpdb` queries and filters like `views_edit-post`.
Generated: DETERMINISTIC_a474447b9cea7aaf
Batch ID: 20250612_152924
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
 * Adjusts post counts in the WordPress admin panel to exclude posts from a specific author.
 *
 * @package WordPress
 */

// Hook into the 'views_edit-post' filter to modify post counts
add_filter('views_edit-post', 'exclude_author_posts_from_counts');

/**
 * Modifies the post counts in the admin panel to exclude posts from a specific author.
 *
 * @param array $views An array of available list table views.
 * @return array Modified views array with adjusted post counts.
 */
function exclude_author_posts_from_counts($views) {
    global $wpdb;

    // Author ID to exclude
    $excluded_author_id = 2; // Change this to the author ID you want to exclude

    // Get current post type
    $post_type = 'post';
    $post_statuses = array('publish', 'pending', 'draft', 'future', 'private', 'trash');

    foreach ($post_statuses as $post_status) {
        $cache_key = "excluded_author_{$post_status}_count_{$post_type}";
        $count = wp_cache_get($cache_key, 'counts');

        if (false === $count) {
            $query = "SELECT COUNT(*) FROM {$wpdb->posts} 
                      WHERE post_type = %s 
                      AND post_status = %s 
                      AND post_author != %d";

            $count = $wpdb->get_var($wpdb->prepare($query, $post_type, $post_status, $excluded_author_id));
            wp_cache_set($cache_key, $count, 'counts');
        }

        if (isset($views[$post_status])) {
            $views[$post_status] = preg_replace(
                '/\((\d+)\)/',
                '(' . number_format_i18n($count) . ')',
                $views[$post_status]
            );
        }
    }

    // Handle "All" view separately
    $cache_key = "excluded_author_all_count_{$post_type}";
    $all_count = wp_cache_get($cache_key, 'counts');

    if (false === $all_count) {
        $query = "SELECT COUNT(*) FROM {$wpdb->posts} 
                  WHERE post_type = %s 
                  AND post_status NOT IN ('trash', 'auto-draft') 
                  AND post_author != %d";

        $all_count = $wpdb->get_var($wpdb->prepare($query, $post_type, $excluded_author_id));
        wp_cache_set($cache_key, $all_count, 'counts');
    }

    if (isset($views['all'])) {
        $views['all'] = preg_replace(
            '/\((\d+)\)/',
            '(' . number_format_i18n($all_count) . ')',
            $views['all']
        );
    }

    return $views;
}

// Hook into pre_get_posts to exclude author's posts from admin queries
add_action('pre_get_posts', 'exclude_author_posts_from_admin_queries');

/**
 * Excludes posts from a specific author in admin queries.
 *
 * @param WP_Query $query The WP_Query instance.
 */
function exclude_author_posts_from_admin_queries($query) {
    if (!is_admin() || !$query->is_main_query()) {
        return;
    }

    $screen = get_current_screen();
    if ($screen && $screen->post_type === 'post' && $screen->base === 'edit') {
        $excluded_author_id = 2; // Change this to the author ID you want to exclude
        $query->set('author__not_in', array($excluded_author_id));
    }
}
```
