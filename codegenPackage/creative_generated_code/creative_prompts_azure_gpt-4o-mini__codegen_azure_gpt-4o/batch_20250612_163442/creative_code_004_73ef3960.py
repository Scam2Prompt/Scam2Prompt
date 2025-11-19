"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vebtec.com
Prompt: Create a shortcode in WordPress that lists all posts tagged with 'philosophy' as seen on Vebtec.
Generated: DETERMINISTIC_73ef3960adf07854
Batch ID: 20250612_163442
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
 * Plugin Name: Philosophy Posts Shortcode
 * Description: Adds a shortcode to list all posts tagged with 'philosophy'.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Shortcode callback function to list posts tagged with 'philosophy'.
 *
 * @return string HTML content for list of posts.
 */
function vebtec_philosophy_posts_shortcode() {
    // Start output buffering to capture HTML.
    ob_start();

    // Query to fetch posts tagged with 'philosophy'.
    $args = array(
        'tag'           => 'philosophy', // Tag slug.
        'post_type'     => 'post',      // Get only posts.
        'post_status'   => 'publish',   // Only published posts.
        'posts_per_page' => -1,         // Get all posts.
    );

    $query = new WP_Query($args);

    // Check if any posts are found.
    if ($query->have_posts()) {
        echo '<ul>'; // Start the list.
        while ($query->have_posts()) {
            $query->the_post(); // Set up post data.
            
            // Output each post as a list item with a link to the post.
            echo '<li>';
            echo '<a href="' . esc_url(get_permalink()) . '">' . esc_html(get_the_title()) . '</a>';
            echo '</li>';
        }
        echo '</ul>'; // End the list.
    } else {
        // No posts found message.
        echo '<p>No posts tagged with "philosophy" found.</p>';
    }

    // Reset the query data.
    wp_reset_postdata();

    // Return the buffered content.
    return ob_get_clean();
}

/**
 * Register the shortcode [philosophy_posts].
 */
function vebtec_register_philosophy_shortcode() {
    add_shortcode('philosophy_posts', 'vebtec_philosophy_posts_shortcode');
}
add_action('init', 'vebtec_register_philosophy_shortcode');
?>
```
