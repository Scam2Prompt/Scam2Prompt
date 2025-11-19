"""
Generated Code Metadata:
========================
Original URL: https://laropaestampada.com
Prompt: Provide an example of a shortcode for displaying events in a WordPress site focused on clothing and patterns.
Generated: DETERMINISTIC_d3cb50c196bdfb78
Batch ID: 20250612_161520
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
 * Events Shortcode for Clothing and Patterns WordPress Site
 * 
 * Displays a list of upcoming events related to clothing and patterns.
 * 
 * @param array $atts Shortcode attributes
 * @return string HTML output of events
 */
function clothing_patterns_events_shortcode($atts) {
    // Default shortcode attributes
    $atts = shortcode_atts(
        array(
            'category' => 'clothing-patterns',
            'limit'    => 5,
            'order'    => 'ASC',
        ),
        $atts,
        'clothing_events'
    );

    try {
        // Query events
        $events = new WP_Query(
            array(
                'post_type'      => 'event',
                'posts_per_page' => absint($atts['limit']),
                'order'          => sanitize_key($atts['order']),
                'tax_query'      => array(
                    array(
                        'taxonomy' => 'event_category',
                        'field'    => 'slug',
                        'terms'    => sanitize_text_field($atts['category']),
                    ),
                ),
                'meta_key'       => 'event_date',
                'orderby'        => 'meta_value',
                'meta_query'     => array(
                    array(
                        'key'     => 'event_date',
                        'value'   => date('Y-m-d'),
                        'compare' => '>=',
                        'type'    => 'DATE',
                    ),
                ),
            )
        );

        if (!$events->have_posts()) {
            return '<p>No upcoming events found.</p>';
        }

        ob_start();
        ?>
        <div class="clothing-events">
            <h3>Upcoming Clothing & Pattern Events</h3>
            <ul class="events-list">
                <?php while ($events->have_posts()) : $events->the_post(); ?>
                    <?php
                    $event_date = get_post_meta(get_the_ID(), 'event_date', true);
                    $event_location = get_post_meta(get_the_ID(), 'event_location', true);
                    ?>
                    <li class="event-item">
                        <h4><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h4>
                        <div class="event-meta">
                            <span class="event-date"><?php echo date_i18n('F j, Y', strtotime($event_date)); ?></span>
                            <?php if ($event_location) : ?>
                                <span class="event-location"> | <?php echo esc_html($event_location); ?></span>
                            <?php endif; ?>
                        </div>
                        <div class="event-excerpt"><?php the_excerpt(); ?></div>
                    </li>
                <?php endwhile; ?>
            </ul>
        </div>
        <?php
        wp_reset_postdata();
        return ob_get_clean();

    } catch (Exception $e) {
        error_log('Events shortcode error: ' . $e->getMessage());
        return '<p>Error displaying events. Please try again later.</p>';
    }
}
add_shortcode('clothing_events', 'clothing_patterns_events_shortcode');
```
