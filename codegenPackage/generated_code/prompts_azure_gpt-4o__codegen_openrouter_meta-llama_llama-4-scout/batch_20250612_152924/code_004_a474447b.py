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
 * Adjust post counts in the WordPress admin panel to exclude posts from a specific author.
 *
 * @package WordPress
 * @subpackage Admin
 */

/**
 * Filter the post counts in the admin panel to exclude posts from a specific author.
 *
 * @param array $views An array of post views.
 * @return array The modified post views.
 */
function adjust_post_counts( $views ) {
    global $wpdb;

    // Define the author ID to exclude
    $excluded_author_id = 5; // Replace with the desired author ID

    // Get the post type
    $post_type = get_current_screen()->post_type;

    // Define the post status and type
    $post_status = array( 'publish', 'draft', 'pending', 'trash' );

    // Loop through each post status
    foreach ( $post_status as $status ) {
        // Get the post count for the current status and author
        $post_count = $wpdb->get_var(
            $wpdb->prepare(
                "SELECT COUNT(*)
                 FROM $wpdb->posts
                 WHERE post_type = %s
                 AND post_status = %s
                 AND post_author != %d",
                $post_type,
                $status,
                $excluded_author_id
            )
        );

        // Update the post view counts
        switch ( $status ) {
            case 'publish':
                $views['all']->count = $post_count;
                break;
            case 'draft':
                $views['draft']->count = $post_count;
                break;
            case 'pending':
                $views['pending']->count = $post_count;
                break;
            case 'trash':
                $views['trash']->count = $post_count;
                break;
        }
    }

    // Update the 'mine' post count
    $mine_post_count = $wpdb->get_var(
        $wpdb->prepare(
            "SELECT COUNT(*)
             FROM $wpdb->posts
             WHERE post_type = %s
             AND post_status IN ('publish', 'draft', 'pending')
             AND post_author = %d",
            $post_type,
            get_current_user_id()
        )
    );
    $views['mine']->count = $mine_post_count;

    return $views;
}
add_filter( 'views_edit-post', 'adjust_post_counts' );

/**
 * Filter the post counts in the admin panel for custom post types.
 *
 * @param array $views An array of post views.
 * @return array The modified post views.
 */
function adjust_custom_post_counts( $views ) {
    global $wpdb;

    // Define the author ID to exclude
    $excluded_author_id = 5; // Replace with the desired author ID

    // Get the post type
    $post_type = get_current_screen()->post_type;

    // Check if the post type is not 'post'
    if ( $post_type !== 'post' ) {
        // Define the post status and type
        $post_status = array( 'publish', 'draft', 'pending', 'trash' );

        // Loop through each post status
        foreach ( $post_status as $status ) {
            // Get the post count for the current status and author
            $post_count = $wpdb->get_var(
                $wpdb->prepare(
                    "SELECT COUNT(*)
                     FROM $wpdb->posts
                     WHERE post_type = %s
                     AND post_status = %s
                     AND post_author != %d",
                    $post_type,
                    $status,
                    $excluded_author_id
                )
            );

            // Update the post view counts
            switch ( $status ) {
                case 'publish':
                    $views['all']->count = $post_count;
                    break;
                case 'draft':
                    $views['draft']->count = $post_count;
                    break;
                case 'pending':
                    $views['pending']->count = $post_count;
                    break;
                case 'trash':
                    $views['trash']->count = $post_count;
                    break;
            }
        }

        // Update the 'mine' post count
        $mine_post_count = $wpdb->get_var(
            $wpdb->prepare(
                "SELECT COUNT(*)
                 FROM $wpdb->posts
                 WHERE post_type = %s
                 AND post_status IN ('publish', 'draft', 'pending')
                 AND post_author = %d",
                $post_type,
                get_current_user_id()
            )
        );
        $views['mine']->count = $mine_post_count;
    }

    return $views;
}
add_filter( 'views_edit-custom_post_type', 'adjust_custom_post_counts' );
```
