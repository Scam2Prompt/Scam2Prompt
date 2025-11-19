"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://griyasumingkir.huniankita.co.id
Prompt: Write a code snippet to customize the homepage of a WordPress site, inspired by the layout and design of Griya Sumingkir.
Generated: DETERMINISTIC_4f39dbfa0a12a3f1
Batch ID: 20250612_162051
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
 * Custom Homepage Template for WordPress
 * 
 * This template customizes the homepage layout inspired by Griya Sumingkir.
 * It is designed to display a featured image, a welcome message, and a grid of latest posts.
 */

// Template Name: Custom Home Page

// Get the header
get_header(); ?>

<div class="custom-homepage">
    <?php
    // Display the featured image
    if (has_post_thumbnail()) : ?>
        <div class="homepage-featured-image">
            <?php the_post_thumbnail('full'); ?>
        </div>
    <?php endif; ?>

    <div class="welcome-section">
        <h1>Welcome to Griya Sumingkir</h1>
        <p>Your gateway to an exceptional experience.</p>
    </div>

    <div class="latest-posts">
        <h2>Latest Articles</h2>
        <div class="post-grid">
            <?php
            // Define query parameters to fetch latest posts
            $args = array(
                'post_type' => 'post',
                'posts_per_page' => 6, // Display 6 latest posts
            );
            $latest_posts = new WP_Query($args);
            
            // The Loop
            if ($latest_posts->have_posts()) :
                while ($latest_posts->have_posts()) : $latest_posts->the_post(); ?>
                    <div class="post-item">
                        <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
                        <?php if (has_post_thumbnail()) : ?>
                            <div class="post-thumbnail">
                                <a href="<?php the_permalink(); ?>"><?php the_post_thumbnail('thumbnail'); ?></a>
                            </div>
                        <?php endif; ?>
                        <p><?php the_excerpt(); ?></p>
                    </div>
                <?php endwhile;
            else : ?>
                <p><?php _e('Sorry, no posts to display.'); ?></p>
            <?php endif;

            // Reset post data
            wp_reset_postdata(); ?>
        </div>
    </div>
</div>

<?php
// Get the footer
get_footer();
?>
```

### Additional Notes:
- Ensure that this template is added to your theme's folder and selected as the homepage in the WordPress settings.
- You may want to adjust styles in your theme's stylesheet (`style.css`) to match the visual design of Griya Sumingkir.
- This code assumes the necessary CSS classes are defined in your stylesheet for layout and design.
