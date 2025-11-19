"""
Generated Code Metadata:
========================
Original URL: https://www.malmobeerweek.se
Prompt: Create a WordPress page template for an event website, similar to Malmö Beer Week's website, using the EventPress theme.
Generated: DETERMINISTIC_bb7b7a2f302592cf
Batch ID: 20250622_210703
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
 * Template Name: Event Page Template
 * Description: A custom page template for event websites similar to Malmö Beer Week.
 * Version: 1.0
 * Author: Your Name
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <?php
        while (have_posts()) :
            the_post();

            // Get event meta data
            $event_date = get_post_meta(get_the_ID(), 'event_date', true);
            $event_location = get_post_meta(get_the_ID(), 'event_location', true);
            $event_tickets = get_post_meta(get_the_ID(), 'event_tickets', true);
            ?>

            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <header class="entry-header">
                    <?php the_title('<h1 class="entry-title">', '</h1>'); ?>
                    
                    <?php if ($event_date || $event_location) : ?>
                        <div class="event-meta">
                            <?php if ($event_date) : ?>
                                <span class="event-date">
                                    <i class="fas fa-calendar-alt"></i> <?php echo esc_html($event_date); ?>
                                </span>
                            <?php endif; ?>
                            
                            <?php if ($event_location) : ?>
                                <span class="event-location">
                                    <i class="fas fa-map-marker-alt"></i> <?php echo esc_html($event_location); ?>
                                </span>
                            <?php endif; ?>
                        </div>
                    <?php endif; ?>
                </header>

                <div class="entry-content">
                    <?php
                    the_content();
                    
                    if ($event_tickets) :
                        echo '<div class="event-tickets">';
                        echo '<a href="' . esc_url($event_tickets) . '" class="button ticket-button">Get Tickets</a>';
                        echo '</div>';
                    endif;
                    ?>
                </div>

                <?php
                // Display event gallery if exists
                $gallery = get_post_meta(get_the_ID(), 'event_gallery', true);
                if ($gallery) :
                    echo '<div class="event-gallery">';
                    echo do_shortcode($gallery);
                    echo '</div>';
                endif;
                ?>

                <footer class="entry-footer">
                    <?php
                    // Event categories
                    $categories = get_the_terms(get_the_ID(), 'event_category');
                    if ($categories && !is_wp_error($categories)) :
                        echo '<div class="event-categories">';
                        echo '<span>' . esc_html__('Categories:', 'eventpress') . '</span>';
                        foreach ($categories as $category) {
                            echo '<a href="' . esc_url(get_term_link($category)) . '">' . esc_html($category->name) . '</a>';
                        }
                        echo '</div>';
                    endif;
                    ?>
                </footer>
            </article>

            <?php
            // If comments are open or we have at least one comment, load up the comment template.
            if (comments_open() || get_comments_number()) :
                comments_template();
            endif;

        endwhile; // End of the loop.
        ?>
    </main>
</div>

<?php
get_sidebar();
get_footer();
```
