"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoftware.online
Prompt: Create a WordPress shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout, similar to the structure found on a site using WooCommerce themes.
Generated: DETERMINISTIC_c9ce351c2ac442d6
Batch ID: 20250612_151611
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
 * Plugin Name: Custom Blog Posts Grid Shortcode
 * Description: A shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout.
 * Version: 1.0
 * Author: Your Name
 */

// Shortcode to display categorized blog posts in a grid layout
function custom_blog_posts_grid_shortcode($atts) {
    // Attributes and their defaults
    $atts = shortcode_atts(
        array(
            'posts_per_page' => 6, // Number of posts to display
            'columns'        => 3, // Number of columns in the grid
        ),
        $atts,
        'blog_posts_grid'
    );

    // Query arguments
    $args = array(
        'post_type'      => 'post', // Only retrieve posts
        'posts_per_page' => intval($atts['posts_per_page']), // Limit the number of posts
        'category_name'  => 'decoration,design trends', // Categories to filter
        'post_status'    => 'publish', // Only published posts
    );

    // Execute the query
    $query = new WP_Query($args);

    // Start output buffering
    ob_start();

    // Check if there are posts matching the query
    if ($query->have_posts()) :
        echo '<div class="custom-blog-posts-grid" style="display: flex; flex-wrap: wrap; gap: 20px;">';

        // Loop through posts
        while ($query->have_posts()) : $query->the_post();
            echo '<div class="grid-item" style="width: calc(100% / ' . intval($atts['columns']) . ' - 20px); background: #f9f9f9; padding: 15px; border: 1px solid #ddd;">';

            // Display post thumbnail
            if (has_post_thumbnail()) {
                echo '<div class="post-thumbnail" style="margin-bottom: 10px;">';
                the_post_thumbnail('medium', array('style' => 'width: 100%; height: auto;'));
                echo '</div>';
            }

            // Display post title
            echo '<h3 class="post-title" style="font-size: 18px; margin-bottom: 10px;">';
            echo '<a href="' . esc_url(get_permalink()) . '" style="text-decoration: none; color: #333;">';
            the_title();
            echo '</a>';
            echo '</h3>';

            // Display post excerpt
            echo '<div class="post-excerpt" style="font-size: 14px; color: #555;">';
            the_excerpt();
            echo '</div>';

            echo '</div>'; // Close grid item
        endwhile;

        echo '</div>'; // Close grid container
    else :
        // Message if no posts found
        echo '<p>No posts found in the specified categories.</p>';
    endif;

    // Restore original Post Data
    wp_reset_postdata();

    // Get buffer content and clean output buffer
    return ob_get_clean();
}

// Register the shortcode
add_shortcode('blog_posts_grid', 'custom_blog_posts_grid_shortcode');
?>
```
