"""
Generated Code Metadata:
========================
Original URL: https://laropaestampada.com
Prompt: "How to use WordPress to create an events page for a printed clothing brand."
Generated: DETERMINISTIC_365c415dae0effe6
Batch ID: 20250622_210316
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
 * Plugin Name: Printed Clothing Brand Events Page
 * Description: A custom WordPress plugin to create an events page for a printed clothing brand.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Register custom post type for Events
function pcb_register_events_post_type() {
    $labels = array(
        'name'               => 'Events',
        'singular_name'      => 'Event',
        'menu_name'          => 'Events',
        'name_admin_bar'     => 'Event',
        'add_new'            => 'Add New',
        'add_new_item'       => 'Add New Event',
        'edit_item'          => 'Edit Event',
        'new_item'           => 'New Event',
        'view_item'          => 'View Event',
        'all_items'          => 'All Events',
        'search_items'       => 'Search Events',
        'not_found'          => 'No events found.',
        'not_found_in_trash' => 'No events found in Trash.',
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'rewrite'            => array('slug' => 'events'),
        'supports'           => array('title', 'editor', 'thumbnail', 'custom-fields'),
        'show_in_rest'       => true, // Enable Gutenberg editor
    );

    register_post_type('pcb_event', $args);
}
add_action('init', 'pcb_register_events_post_type');

// Add custom meta box for event details
function pcb_add_event_meta_boxes() {
    add_meta_box(
        'pcb_event_details',
        'Event Details',
        'pcb_event_details_callback',
        'pcb_event',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'pcb_add_event_meta_boxes');

/**
 * Callback function for the Event Details meta box
 */
function pcb_event_details_callback($post) {
    // Retrieve current values for the meta fields
    $event_date = get_post_meta($post->ID, '_pcb_event_date', true);
    $event_location = get_post_meta($post->ID, '_pcb_event_location', true);

    // Nonce field for security
    wp_nonce_field('pcb_save_event_details', 'pcb_event_details_nonce');

    ?>
    <p>
        <label for="pcb_event_date">Event Date:</label>
        <input type="date" id="pcb_event_date" name="pcb_event_date" value="<?php echo esc_attr($event_date); ?>" />
    </p>
    <p>
        <label for="pcb_event_location">Event Location:</label>
        <input type="text" id="pcb_event_location" name="pcb_event_location" value="<?php echo esc_attr($event_location); ?>" />
    </p>
    <?php
}

// Save custom meta fields
function pcb_save_event_details($post_id) {
    // Check nonce for security
    if (!isset($_POST['pcb_event_details_nonce']) || !wp_verify_nonce($_POST['pcb_event_details_nonce'], 'pcb_save_event_details')) {
        return;
    }

    // Prevent auto-save from overwriting data
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Check user permissions
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // Save event date
    if (isset($_POST['pcb_event_date'])) {
        update_post_meta($post_id, '_pcb_event_date', sanitize_text_field($_POST['pcb_event_date']));
    }

    // Save event location
    if (isset($_POST['pcb_event_location'])) {
        update_post_meta($post_id, '_pcb_event_location', sanitize_text_field($_POST['pcb_event_location']));
    }
}
add_action('save_post', 'pcb_save_event_details');

// Shortcode to display events on a page
function pcb_events_shortcode($atts) {
    $atts = shortcode_atts(array(
        'count' => 10, // Default number of events to display
    ), $atts, 'pcb_events');

    $query = new WP_Query(array(
        'post_type'      => 'pcb_event',
        'posts_per_page' => intval($atts['count']),
        'orderby'        => 'meta_value',
        'meta_key'       => '_pcb_event_date',
        'order'          => 'ASC',
    ));

    if ($query->have_posts()) {
        $output = '<div class="pcb-events">';
        while ($query->have_posts()) {
            $query->the_post();
            $event_date = get_post_meta(get_the_ID(), '_pcb_event_date', true);
            $event_location = get_post_meta(get_the_ID(), '_pcb_event_location', true);

            $output .= '<div class="pcb-event">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p><strong>Date:</strong> ' . esc_html($event_date) . '</p>';
            $output .= '<p><strong>Location:</strong> ' . esc_html($event_location) . '</p>';
            $output .= '<p>' . get_the_excerpt() . '</p>';
            $output .= '</div>';
        }
        $output .= '</div>';
        wp_reset_postdata();
    } else {
        $output = '<p>No events found.</p>';
    }

    return $output;
}
add_shortcode('pcb_events', 'pcb_events_shortcode');
?>
```
