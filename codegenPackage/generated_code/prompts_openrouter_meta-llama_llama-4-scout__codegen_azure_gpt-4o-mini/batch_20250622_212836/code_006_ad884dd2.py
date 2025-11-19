"""
Generated Code Metadata:
========================
Original URL: https://krushinews18.com
Prompt: "GeneratePress documentation on designing a custom 404 page with search functionality."
Generated: DETERMINISTIC_ad884dd2fa35c52a
Batch ID: 20250622_212836
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
 * Custom 404 Page Template for GeneratePress
 *
 * This template provides a custom 404 error page with a search functionality.
 * It is designed to enhance user experience by allowing users to search for content
 * directly from the 404 page.
 *
 * @package GeneratePress
 * @since 1.0.0
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Get the header
get_header(); ?>

<div class="error-404 not-found">
    <header class="page-header">
        <h1 class="page-title"><?php esc_html_e( 'Oops! That page can’t be found.', 'generatepress' ); ?></h1>
    </header><!-- .page-header -->

    <div class="page-content">
        <p><?php esc_html_e( 'It looks like nothing was found at this location. Maybe try a search?', 'generatepress' ); ?></p>

        <?php
        // Search form
        get_search_form(); // This function outputs the default search form
        ?>
        
        <h2><?php esc_html_e( 'Recent Posts', 'generatepress' ); ?></h2>
        <ul>
            <?php
            // Display recent posts
            $recent_posts = wp_get_recent_posts( array(
                'numberposts' => 5, // Number of recent posts to display
                'post_status' => 'publish' // Only show published posts
            ) );

            if ( ! empty( $recent_posts ) ) {
                foreach ( $recent_posts as $post ) {
                    echo '<li><a href="' . esc_url( get_permalink( $post['ID'] ) ) . '">' . esc_html( $post['post_title'] ) . '</a></li>';
                }
            } else {
                echo '<li>' . esc_html__( 'No recent posts available.', 'generatepress' ) . '</li>';
            }
            ?>
        </ul>
    </div><!-- .page-content -->
</div><!-- .error-404 -->

<?php
// Get the footer
get_footer();
```
