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
 * Shortcode to display blog posts from 'Decoration' and 'Design trends' categories in a grid layout.
 * 
 * Usage: [posts_grid]
 */
function decoration_design_posts_grid_shortcode() {
    ob_start();

    // Query arguments
    $args = array(
        'post_type'      => 'post',
        'posts_per_page' => 6,
        'tax_query'      => array(
            'relation' => 'OR',
            array(
                'taxonomy' => 'category',
                'field'    => 'slug',
                'terms'    => array('decoration', 'design-trends'),
            ),
        ),
    );

    $query = new WP_Query($args);

    if ($query->have_posts()) :
        echo '<div class="posts-grid-container" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">';
        
        while ($query->have_posts()) : $query->the_post();
            ?>
            <div class="post-grid-item" style="border: 1px solid #eee; padding: 15px; border-radius: 5px;">
                <?php if (has_post_thumbnail()) : ?>
                    <div class="post-thumbnail" style="margin-bottom: 15px;">
                        <a href="<?php the_permalink(); ?>">
                            <?php the_post_thumbnail('medium', array('style' => 'width: 100%; height: auto;')); ?>
                        </a>
                    </div>
                <?php endif; ?>
                
                <h3 style="margin: 0 0 10px 0; font-size: 1.2em;">
                    <a href="<?php the_permalink(); ?>" style="text-decoration: none; color: inherit;">
                        <?php the_title(); ?>
                    </a>
                </h3>
                
                <div class="post-excerpt" style="margin-bottom: 10px; font-size: 0.9em;">
                    <?php the_excerpt(); ?>
                </div>
                
                <div class="post-meta" style="font-size: 0.8em; color: #666;">
                    <?php echo get_the_date(); ?>
                </div>
            </div>
            <?php
        endwhile;
        
        echo '</div>';
        
        wp_reset_postdata();
    else :
        echo '<p>No posts found in the specified categories.</p>';
    endif;

    return ob_get_clean();
}
add_shortcode('posts_grid', 'decoration_design_posts_grid_shortcode');
```
