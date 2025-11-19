"""
Generated Code Metadata:
========================
Original URL: https://thesoftware.online
Prompt: Create a WordPress shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout, similar to the structure found on a site using WooCommerce themes.
Generated: DETERMINISTIC_c9ce351c2ac442d6
Batch ID: 20250612_151611
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
 * Plugin Name: Custom Blog Posts Grid Shortcode
 * Description: A shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode to display blog posts in a grid layout.
 *
 * @return string HTML output of the blog posts grid.
 */
function custom_blog_posts_grid_shortcode() {
    // Define the categories to query
    $categories = array('Decoration', 'Design trends');

    // Set up the query arguments
    $args = array(
        'category_name' => implode(',', $categories),
        'posts_per_page' => 6, // Number of posts to display
        'post_status' => 'publish', // Only show published posts
    );

    // Execute the query
    $query = new WP_Query($args);

    // Check if there are posts
    if ( $query->have_posts() ) {
        // Start output buffering
        ob_start();
        
        // Begin the grid layout
        echo '<div class="custom-blog-posts-grid">';

        // Loop through the posts
        while ( $query->have_posts() ) {
            $query->the_post();
            ?>
            <div class="grid-item">
                <a href="<?php the_permalink(); ?>" title="<?php the_title(); ?>">
                    <?php if ( has_post_thumbnail() ) : ?>
                        <div class="grid-item-thumbnail">
                            <?php the_post_thumbnail('medium'); ?>
                        </div>
                    <?php endif; ?>
                    <h2 class="grid-item-title"><?php the_title(); ?></h2>
                </a>
                <div class="grid-item-excerpt">
                    <?php the_excerpt(); ?>
                </div>
            </div>
            <?php
        }

        // End the grid layout
        echo '</div>';

        // Reset post data
        wp_reset_postdata();

        // Return the buffered content
        return ob_get_clean();
    } else {
        // No posts found message
        return '<p>No posts found in the specified categories.</p>';
    }
}

// Register the shortcode
add_shortcode('blog_posts_grid', 'custom_blog_posts_grid_shortcode');

// Enqueue styles for the grid layout
function custom_blog_posts_grid_styles() {
    ?>
    <style>
        .custom-blog-posts-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px; /* Space between grid items */
        }
        .grid-item {
            flex: 1 1 calc(33.333% - 20px); /* Three items per row */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 10px;
            border-radius: 5px;
            background-color: #fff;
        }
        .grid-item-thumbnail img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        .grid-item-title {
            font-size: 1.2em;
            margin: 10px 0;
        }
        .grid-item-excerpt {
            font-size: 0.9em;
            color: #666;
        }
    </style>
    <?php
}
add_action('wp_head', 'custom_blog_posts_grid_styles');
```
