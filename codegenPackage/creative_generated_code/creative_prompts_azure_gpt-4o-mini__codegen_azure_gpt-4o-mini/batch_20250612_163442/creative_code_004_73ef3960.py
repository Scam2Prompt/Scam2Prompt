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
 * Description: A shortcode to list all posts tagged with 'philosophy'.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to fetch and display posts tagged with 'philosophy'.
 *
 * @return string HTML output containing the list of posts.
 */
function vebtec_philosophy_posts_shortcode() {
    // Define the global variable to store output
    global $post;
    $output = '';

    // Define the query arguments to fetch posts with 'philosophy' tag
    $args = array(
        'post_type' => 'post',
        'tag' => 'philosophy',
        'posts_per_page' => -1, // Fetch all posts
    );

    // Query the posts
    $query = new WP_Query($args);

    // Check if any posts were found
    if ($query->have_posts()) {
        $output .= '<ul>'; // Start the list
        while ($query->have_posts()) {
            $query->the_post(); // Set up post data
            $output .= '<li>';
            $output .= '<a href="' . esc_url(get_permalink()) . '">' . esc_html(get_the_title()) . '</a>'; // Link to the post
            $output .= '</li>';
        }
        $output .= '</ul>'; // End the list

        // Reset post data
        wp_reset_postdata();
    } else {
        // If no posts found, display a message
        $output .= '<p>No posts found tagged with "philosophy".</p>';
    }

    return $output; // Return the output to be displayed
}

// Register the shortcode with WordPress
add_shortcode('philosophy_posts', 'vebtec_philosophy_posts_shortcode');
```
