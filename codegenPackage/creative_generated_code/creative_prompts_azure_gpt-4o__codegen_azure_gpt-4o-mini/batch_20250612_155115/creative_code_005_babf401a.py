"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Create a WordPress shortcode to display upcoming events dynamically, as referenced in the "Events" section of the site.
Generated: DETERMINISTIC_babf401aed24d757
Batch ID: 20250612_155115
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
 * Plugin Name: Upcoming Events Shortcode
 * Description: A shortcode to display upcoming events dynamically.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode to display upcoming events.
 *
 * @return string HTML output of upcoming events.
 */
function display_upcoming_events() {
    // Fetch upcoming events from a custom post type 'events'
    $args = array(
        'post_type'      => 'events',
        'posts_per_page' => 5, // Limit to 5 upcoming events
        'meta_query'     => array(
            array(
                'key'     => 'event_date', // Custom field for event date
                'value'   => current_time('Ymd'), // Compare with today's date
                'compare' => '>=', // Get events happening today or in the future
                'type'    => 'NUMERIC'
            ),
        ),
        'orderby'        => 'meta_value_num', // Sort by event date
        'order'          => 'ASC' // Ascending order
    );

    $events_query = new WP_Query( $args );

    // Check if any events were found
    if ( ! $events_query->have_posts() ) {
        return '<p>No upcoming events found.</p>'; // Return message if no events
    }

    // Initialize output variable
    $output = '<div class="upcoming-events"><h2>Upcoming Events</h2><ul>';

    // Loop through events and construct the output
    while ( $events_query->have_posts() ) {
        $events_query->the_post();
        $event_date = get_post_meta( get_the_ID(), 'event_date', true );
        $event_time = get_post_meta( get_the_ID(), 'event_time', true );

        // Format the event date
        $formatted_date = date( 'F j, Y', strtotime($event_date) );
        
        // Add each event to the output
        $output .= '<li>';
        $output .= '<strong>' . get_the_title() . '</strong> - ' . $formatted_date . ' at ' . esc_html($event_time);
        $output .= '<p>' . get_the_excerpt() . '</p>';
        $output .= '</li>';
    }

    // Reset post data after custom query
    wp_reset_postdata();

    $output .= '</ul></div>'; // Close container div

    return $output; // Return the final output
}

// Register the shortcode with WordPress
add_shortcode( 'upcoming_events', 'display_upcoming_events' );
?>
```
