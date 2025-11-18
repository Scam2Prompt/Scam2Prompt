"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Create a WordPress shortcode to display upcoming events on the "Eventos" page using custom post types.
Generated: DETERMINISTIC_967dbde88403ceac
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Register a shortcode to display upcoming events on the "Eventos" page
function display_upcoming_events_shortcode($atts) {
    // Extract attributes (if any) passed to the shortcode
    $atts = shortcode_atts(
        array(
            'count' => 5, // Default number of events to display
        ),
        $atts
    );

    // Start output buffering to capture HTML output
    ob_start();

    // Query arguments for fetching upcoming events from the "event" custom post type
    $args = array(
        'post_type'      => 'event', // Custom post type for events
        'posts_per_page' => intval($atts['count']), // Number of events to display
        'meta_key'       => 'event_date', // Meta key for event date
        'orderby'        => 'meta_value', // Order by event date
        'order'          => 'ASC', // Ascending order
        'meta_query'     => array(
            array(
                'key'     => 'event_date',
                'value'   => date('Y-m-d'), // Today's date
                'compare' => '>=', // Only events on or after today
                'type'    => 'DATE',
            ),
        ),
    );

    // Fetch events using WP_Query
    $query = new WP_Query($args);

    // Check if there are upcoming events
    if ($query->have_posts()) {
        echo '<div class="upcoming-events">';
        echo '<h2>Upcoming Events</h2>';
        echo '<ul>';

        // Loop through each event and display its title and date
        while ($query->have_posts()) {
            $query->the_post();

            // Fetch the event date (assuming it's stored as 'event_date' meta field)
            $event_date = get_post_meta(get_the_ID(), 'event_date', true);

            // Format the event date for display
            $formatted_date = date('F j, Y', strtotime($event_date));

            echo '<li>';
            echo '<a href="' . get_the_permalink() . '">' . esc_html(get_the_title()) . '</a>';
            echo ' - <span>' . esc_html($formatted_date) . '</span>';
            echo '</li>';
        }

        echo '</ul>';
        echo '</div>';

        // Restore global post data
        wp_reset_postdata();
    } else {
        // If no upcoming events, display a message
        echo '<p>No upcoming events found.</p>';
    }

    // Return the buffered content as the shortcode output
    return ob_get_clean();
}

// Register the shortcode
add_shortcode('upcoming_events', 'display_upcoming_events_shortcode');
?>
```
