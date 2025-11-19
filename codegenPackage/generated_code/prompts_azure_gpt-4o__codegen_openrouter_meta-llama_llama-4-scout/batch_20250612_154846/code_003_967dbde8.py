"""
Generated Code Metadata:
========================
Original URL: https://offerspecials.online
Prompt: Create a WordPress shortcode to display upcoming events on the "Eventos" page using custom post types.
Generated: DETERMINISTIC_967dbde88403ceac
Batch ID: 20250612_154846
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
 * Register custom post type for events
 */
function register_event_post_type() {
    register_post_type('event',
        array(
            'labels' => array(
                'name' => __( 'Events' ),
                'singular_name' => __( 'Event' ),
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array('title', 'date', 'editor'),
        )
    );
}
add_action('init', 'register_event_post_type');

/**
 * Create shortcode to display upcoming events
 */
function upcoming_events_shortcode($atts) {
    // Define shortcode attributes
    $atts = shortcode_atts(
        array(
            'posts_per_page' => 5,
        ),
        $atts,
        'upcoming_events'
    );

    // Query upcoming events
    $args = array(
        'post_type' => 'event',
        'posts_per_page' => $atts['posts_per_page'],
        'orderby' => 'meta_value',
        'order' => 'ASC',
        'meta_query' => array(
            array(
                'key' => 'event_date',
                'value' => date('Y-m-d'),
                'compare' => '>=',
            ),
        ),
    );

    $events = new WP_Query($args);

    // Display upcoming events
    if ($events->have_posts()) {
        $output = '<ul class="upcoming-events">';
        while ($events->have_posts()) {
            $events->the_post();
            $event_date = get_post_meta(get_the_ID(), 'event_date', true);
            $output .= '<li>';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p>' . date('F j, Y', strtotime($event_date)) . '</p>';
            $output .= '<p>' . get_the_excerpt() . '</p>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>No upcoming events found.</p>';
    }
}
add_shortcode('upcoming_events', 'upcoming_events_shortcode');

/**
 * Save event date as post meta
 */
function save_event_date($post_id) {
    if (isset($_POST['event_date'])) {
        update_post_meta($post_id, 'event_date', $_POST['event_date']);
    }
}
add_action('save_post_event', 'save_event_date');

/**
 * Add event date field to event post type
 */
function add_event_date_field() {
    add_meta_box(
        'event_date',
        'Event Date',
        'event_date_callback',
        'event',
        'advanced',
        'high'
    );
}
add_action('add_meta_boxes', 'add_event_date_field');

function event_date_callback() {
    $event_date = get_post_meta(get_the_ID(), 'event_date', true);
    ?>
    <input type="date" name="event_date" value="<?php echo $event_date; ?>">
    <?php
}

/**
 * Enqueue admin script for date picker
 */
function enqueue_admin_script() {
    wp_enqueue_script('jquery-ui-datepicker');
    wp_enqueue_style('jquery-ui-datepicker', '//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css');
    wp_enqueue_script('event-date-picker', get_stylesheet_directory_uri() . '/js/event-date-picker.js', array('jquery-ui-datepicker'), '1.0', true);
}
add_action('admin_enqueue_scripts', 'enqueue_admin_script');
```
