"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Generate code to customize the WordPress admin interface by hiding a specific user's posts from the post count.
Generated: DETERMINISTIC_1408069684ee0c70
Batch ID: 20250622_210443
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
 * Plugin Name: Hide User Posts from Count
 * Description: Customizes the WordPress admin interface by hiding a specific user's posts from the post count.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Hide_User_Posts_From_Count {

    /**
     * The user ID whose posts should be hidden from counts
     * @var int
     */
    private $hidden_user_id;

    /**
     * Initialize the plugin
     */
    public function __construct() {
        $this->hidden_user_id = 1; // Replace with the desired user ID

        add_action('pre_get_posts', array($this, 'modify_post_counts'));
        add_filter('wp_count_posts', array($this, 'adjust_post_counts'), 10, 3);
    }

    /**
     * Modify post queries to exclude hidden user's posts
     * @param WP_Query $query
     */
    public function modify_post_counts($query) {
        if (!is_admin() || !$query->is_main_query()) {
            return;
        }

        $post_type = $query->get('post_type');
        if ($post_type && $post_type !== 'nav_menu_item') {
            $query->set('author__not_in', array($this->hidden_user_id));
        }
    }

    /**
     * Adjust post counts to exclude hidden user's posts
     * @param object $counts
     * @param string $type
     * @param string $perm
     * @return object
     */
    public function adjust_post_counts($counts, $type, $perm) {
        if (!is_admin() || $type === 'nav_menu_item') {
            return $counts;
        }

        global $wpdb;

        $query = "SELECT post_status, COUNT(*) as num_posts 
                  FROM {$wpdb->posts} 
                  WHERE post_type = %s 
                  AND post_author != %d";

        if ('readable' === $perm && is_user_logged_in()) {
            $user_id = get_current_user_id();
            $query .= $wpdb->prepare(
                " AND (post_status = 'publish' OR post_status = 'private' OR (post_status = 'inherit' AND post_parent = 0) OR (post_status = 'inherit' AND post_author = %d))",
                $user_id
            );
        }

        $query .= " GROUP BY post_status";

        $results = $wpdb->get_results($wpdb->prepare($query, $type, $this->hidden_user_id));

        foreach ($results as $row) {
            $counts->{$row->post_status} = $row->num_posts;
        }

        return $counts;
    }
}

new Hide_User_Posts_From_Count();
```
