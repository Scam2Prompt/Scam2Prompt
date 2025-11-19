"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dhlinternationalexpress.com
Prompt: Generate a code snippet to create a WordPress blog page using the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_1b23b5ea136a07fb
Batch ID: 20250612_160823
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
 * Template Name: Custom Blog Page
 * Description: A custom template for displaying blog posts in the Twenty Twenty-Five theme.
 *
 * This template fetches and displays a list of blog posts with pagination.
 */

// Prevent direct access to the script.
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

// Get the header of the theme.
get_header(); ?>

<main id="site-content" role="main">
    <div class="post-list">

        <?php
        // Define the query parameters for fetching posts.
        $args = array(
            'post_type'      => 'post',  // We want to fetch posts.
            'posts_per_page' => 10,      // Display 10 posts per page.
            'paged'          => get_query_var( 'paged' ) ? get_query_var( 'paged' ) : 1 // Support pagination.
        );

        // Execute the query.
        $query = new WP_Query( $args );

        // Check if there are posts.
        if ( $query->have_posts() ) :
            // Loop through the posts.
            while ( $query->have_posts() ) : $query->the_post(); ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                    <header class="entry-header">
                        <h2 class="entry-title">
                            <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                        </h2>
                    </header>

                    <div class="entry-content">
                        <?php the_excerpt(); // Display the excerpt of the post. ?>
                    </div>
                </article>
            <?php endwhile; // End the post loop.

            // Pagination for the posts.
            the_posts_pagination(array(
                'mid_size' => 2,
                'prev_text' => __('Previous', 'twentytwentyfive'),
                'next_text' => __('Next', 'twentytwentyfive'),
            ));
        else :
            // Fallback message if no posts are found.
            echo '<p>' . __('No posts found.', 'twentytwentyfive') . '</p>';
        endif;

        // Reset post data after custom query.
        wp_reset_postdata();
        ?>
    </div>
</main>

<?php
// Get the footer of the theme.
get_footer();
```
