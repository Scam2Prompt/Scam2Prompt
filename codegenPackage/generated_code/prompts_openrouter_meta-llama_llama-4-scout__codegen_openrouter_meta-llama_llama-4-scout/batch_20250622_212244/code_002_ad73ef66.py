"""
Generated Code Metadata:
========================
Original URL: https://offerspecials.online
Prompt: Generate code to create a custom WordPress page template for a blog.
Generated: DETERMINISTIC_ad73ef66e79a0261
Batch ID: 20250622_212244
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
 * Template Name: Custom Blog Template
 *
 * This template is used to display a custom blog page.
 *
 * @package WordPress
 * @subpackage [Your Theme Name]
 * @since [Your Theme Version]
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <section class="blog-section">
            <header>
                <h1 class="page-title screen-reader-text"><?php single_post_title(); ?></h1>
            </header>

            <?php
            // Check if there are any posts to display
            if ( have_posts() ) :

                // Start the Loop
                while ( have_posts() ) : the_post();

                    // Include the post format-specific template for the content
                    get_template_part( 'template-parts/content', get_post_format() );

                // End the Loop
                endwhile;

                // Display pagination if there are multiple pages
                if ( get_next_post() || get_previous_post() ) :
                    ?>
                    <div class="pagination">
                        <?php
                        // Previous page link
                        previous_post_link( '%link', '<span class="meta-nav screen-reader-text">Previous Post</span> %title', '', '', 'category' );

                        // Next page link
                        next_post_link( '%link', '%title <span class="meta-nav screen-reader-text">Next Post</span>', '', '', 'category' );
                        ?>
                    </div>
                    <?php
                endif;

            // If no posts are found, display a message
            else :
                ?>
                <p>No posts were found.</p>
            <?php endif; ?>
        </section>
    </main><!-- .site-main -->
</div><!-- .content-area -->

<?php get_footer(); ?>
```
