"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: How can I modify WordPress admin views (e.g., user or post counts) to exclude data related to a specific user, using filters like `views_users` and `views_edit-post`?
Generated: DETERMINISTIC_6eeab80baa2f1f7a
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
 * Plugin Name: Exclude Specific User Data from Admin Views
 * Description: Modifies WordPress admin views to exclude data related to a specific user (e.g., user or post counts).
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Exclude specific user's posts from post count in the "All Posts" admin view.
 *
 * @param array $views The existing views in the `Posts` admin page.
 * @return array Modified views.
 */
function exclude_user_posts_from_views( $views ) {
    $excluded_user_id = 123; // Replace 123 with the ID of the user you want to exclude.

    // Adjust the count for each view.
    foreach ( $views as $key => $view ) {
        // Extract the current post count for the view.
        preg_match( '/\((\d+)\)/', $view, $matches );

        if ( isset( $matches[1] ) ) {
            $total_count = (int) $matches[1];

            // Query the number of posts by the excluded user for this view.
            $excluded_count = count(
                get_posts( array(
                    'author'        => $excluded_user_id,
                    'post_status'   => $key === 'trash' ? 'trash' : 'publish',
                    'post_type'     => 'post',
                    'fields'        => 'ids',
                    'posts_per_page'=> -1,
                ) )
            );

            // Subtract the excluded count from the total count.
            $adjusted_count = $total_count - $excluded_count;

            // Replace the count in the view HTML.
            $views[ $key ] = preg_replace(
                '/\(\d+\)/',
                '(' . max( 0, $adjusted_count ) . ')',
                $view
            );
        }
    }

    return $views;
}
add_filter( 'views_edit-post', 'exclude_user_posts_from_views' );

/**
 * Exclude a specific user from the Users list counts in the admin dashboard.
 *
 * @param array $views The existing views in the `Users` admin page.
 * @return array Modified views.
 */
function exclude_user_from_user_views( $views ) {
    $excluded_user_id = 123; // Replace 123 with the ID of the user you want to exclude.

    // Modify the "All" view count.
    if ( isset( $views['all'] ) ) {
        preg_match( '/\((\d+)\)/', $views['all'], $matches );

        if ( isset( $matches[1] ) ) {
            $total_count = (int) $matches[1];

            // Check if the excluded user exists.
            $excluded_count = get_userdata( $excluded_user_id ) ? 1 : 0;

            // Adjust the count.
            $adjusted_count = $total_count - $excluded_count;

            // Replace the count in the view HTML.
            $views['all'] = preg_replace(
                '/\(\d+\)/',
                '(' . max( 0, $adjusted_count ) . ')',
                $views['all']
            );
        }
    }

    return $views;
}
add_filter( 'views_users', 'exclude_user_from_user_views' );

```
