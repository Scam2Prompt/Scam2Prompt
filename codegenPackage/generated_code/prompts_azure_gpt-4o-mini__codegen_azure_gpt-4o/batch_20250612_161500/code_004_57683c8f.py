"""
Generated Code Metadata:
========================
Original URL: https://magnumrockets.com
Prompt: Create a sample code for a WordPress event management feature inspired by the content on magnumrockets.com.
Generated: DETERMINISTIC_57683c8fee9a1023
Batch ID: 20250612_161500
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
 * Plugin Name: Event Manager
 * Description: A simple WordPress plugin for managing events.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Register custom post type for Events
function em_register_event_post_type() {
    $labels = array(
        'name'               => __('Events', 'event-manager'),
        'singular_name'      => __('Event', 'event-manager'),
        'menu_name'          => __('Events', 'event-manager'),
        'name_admin_bar'     => __('Event', 'event-manager'),
        'add_new'            => __('Add New', 'event-manager'),
        'add_new_item'       => __('Add New Event', 'event-manager'),
        'edit_item'          => __('Edit Event', 'event-manager'),
        'new_item'           => __('New Event', 'event-manager'),
        'view_item'          => __('View Event', 'event-manager'),
        'all_items'          => __('All Events', 'event-manager'),
        'search_items'       => __('Search Events', 'event-manager'),
        'not_found'          => __('No events found.', 'event-manager'),
        'not_found_in_trash' => __('No events found in Trash.', 'event-manager'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'menu_icon'          => 'dashicons-calendar',
        'supports'           => array('title', 'editor', 'thumbnail', 'custom-fields'),
        'rewrite'            => array('slug' => 'events'),
    );

    register_post_type('event', $args);
}
add_action('init', 'em_register_event_post_type');

// Add custom meta box for event details
function em_add_event_meta_boxes() {
    add_meta_box(
        'event_details',
        __('Event Details', 'event-manager'),
        'em_event_details_callback',
        'event',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'em_add_event_meta_boxes');

/**
 * Callback function for the Event Details meta box
 */
function em_event_details_callback($post) {
    // Retrieve existing meta data
    $event_date = get_post_meta($post->ID, '_event_date', true);
    $event_location = get_post_meta($post->ID, '_event_location', true);

    // Nonce field for security
    wp_nonce_field('em_save_event_details', 'em_event_nonce');

    ?>
    <p>
        <label for="event_date"><?php _e('Event Date:', 'event-manager'); ?></label>
        <input type="date" id="event_date" name="event_date" value="<?php echo esc_attr($event_date); ?>" />
    </p>
    <p>
        <label for="event_location"><?php _e('Event Location:', 'event-manager'); ?></label>
        <input type="text" id="event_location" name="event_location" value="<?php echo esc_attr($event_location); ?>" />
    </p>
    <?php
}

/**
 * Save event details meta data
 */
function em_save_event_details($post_id) {
    // Check nonce for security
    if (!isset($_POST['em_event_nonce']) || !wp_verify_nonce($_POST['em_event_nonce'], 'em_save_event_details')) {
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
    if (isset($_POST['event_date'])) {
        update_post_meta($post_id, '_event_date', sanitize_text_field($_POST['event_date']));
    }

    // Save event location
    if (isset($_POST['event_location'])) {
        update_post_meta($post_id, '_event_location', sanitize_text_field($_POST['event_location']));
    }
}
add_action('save_post', 'em_save_event_details');

// Shortcode to display upcoming events
function em_display_upcoming_events($atts) {
    $atts = shortcode_atts(array(
        'count' => 5,
    ), $atts, 'upcoming_events');

    $query = new WP_Query(array(
        'post_type'      => 'event',
        'posts_per_page' => intval($atts['count']),
        'meta_key'       => '_event_date',
        'orderby'        => 'meta_value',
        'order'          => 'ASC',
        'meta_query'     => array(
            array(
                'key'     => '_event_date',
                'value'   => date('Y-m-d'),
                'compare' => '>=',
                'type'    => 'DATE',
            ),
        ),
    ));

    if ($query->have_posts()) {
        $output = '<ul class="upcoming-events">';
        while ($query->have_posts()) {
            $query->the_post();
            $event_date = get_post_meta(get_the_ID(), '_event_date', true);
            $event_location = get_post_meta(get_the_ID(), '_event_location', true);

            $output .= '<li>';
            $output .= '<h3>' . get_the_title() . '</h3>';
            $output .= '<p>' . __('Date:', 'event-manager') . ' ' . esc_html($event_date) . '</p>';
            $output .= '<p>' . __('Location:', 'event-manager') . ' ' . esc_html($event_location) . '</p>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = '<p>' . __('No upcoming events found.', 'event-manager') . '</p>';
    }

    return $output;
}
add_shortcode('upcoming_events', 'em_display_upcoming_events');
?>
```
