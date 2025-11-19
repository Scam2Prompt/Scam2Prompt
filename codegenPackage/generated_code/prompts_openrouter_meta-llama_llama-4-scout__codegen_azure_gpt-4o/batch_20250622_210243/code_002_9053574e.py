"""
Generated Code Metadata:
========================
Original URL: https://magnumrockets.com
Prompt: Generate code for a simple WordPress plugin that allows users to create and manage events, similar to the "Events" section mentioned on the site.
Generated: DETERMINISTIC_9053574e4cc5aa07
Batch ID: 20250622_210243
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
 * Plugin Name: Simple Events Manager
 * Description: A simple WordPress plugin to create and manage events.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Define constants
define('SIMPLE_EVENTS_MANAGER_VERSION', '1.0');
define('SIMPLE_EVENTS_MANAGER_PLUGIN_DIR', plugin_dir_path(__FILE__));

// Register custom post type for Events
function sem_register_event_post_type() {
    $labels = array(
        'name'               => __('Events', 'simple-events-manager'),
        'singular_name'      => __('Event', 'simple-events-manager'),
        'menu_name'          => __('Events', 'simple-events-manager'),
        'name_admin_bar'     => __('Event', 'simple-events-manager'),
        'add_new'            => __('Add New', 'simple-events-manager'),
        'add_new_item'       => __('Add New Event', 'simple-events-manager'),
        'edit_item'          => __('Edit Event', 'simple-events-manager'),
        'new_item'           => __('New Event', 'simple-events-manager'),
        'view_item'          => __('View Event', 'simple-events-manager'),
        'all_items'          => __('All Events', 'simple-events-manager'),
        'search_items'       => __('Search Events', 'simple-events-manager'),
        'not_found'          => __('No events found.', 'simple-events-manager'),
        'not_found_in_trash' => __('No events found in Trash.', 'simple-events-manager'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'menu_icon'          => 'dashicons-calendar',
        'supports'           => array('title', 'editor', 'thumbnail'),
        'show_in_rest'       => true,
    );

    register_post_type('event', $args);
}
add_action('init', 'sem_register_event_post_type');

// Add custom meta box for event details
function sem_add_event_meta_boxes() {
    add_meta_box(
        'event_details_meta_box',
        __('Event Details', 'simple-events-manager'),
        'sem_event_details_meta_box_callback',
        'event',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'sem_add_event_meta_boxes');

// Meta box callback function
function sem_event_details_meta_box_callback($post) {
    // Add nonce for security
    wp_nonce_field('sem_save_event_details', 'sem_event_details_nonce');

    // Retrieve existing values
    $event_date = get_post_meta($post->ID, '_event_date', true);
    $event_location = get_post_meta($post->ID, '_event_location', true);

    ?>
    <p>
        <label for="event_date"><?php _e('Event Date:', 'simple-events-manager'); ?></label>
        <input type="date" id="event_date" name="event_date" value="<?php echo esc_attr($event_date); ?>" />
    </p>
    <p>
        <label for="event_location"><?php _e('Event Location:', 'simple-events-manager'); ?></label>
        <input type="text" id="event_location" name="event_location" value="<?php echo esc_attr($event_location); ?>" />
    </p>
    <?php
}

// Save event details
function sem_save_event_details($post_id) {
    // Check nonce for security
    if (!isset($_POST['sem_event_details_nonce']) || !wp_verify_nonce($_POST['sem_event_details_nonce'], 'sem_save_event_details')) {
        return;
    }

    // Check if the user has permission to edit
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
add_action('save_post', 'sem_save_event_details');

// Shortcode to display events
function sem_events_shortcode($atts) {
    $atts = shortcode_atts(array(
        'count' => 5,
    ), $atts, 'events');

    $query = new WP_Query(array(
        'post_type'      => 'event',
        'posts_per_page' => intval($atts['count']),
    ));

    if ($query->have_posts()) {
        $output = '<ul class="events-list">';
        while ($query->have_posts()) {
            $query->the_post();
            $event_date = get_post_meta(get_the_ID(), '_event_date', true);
            $event_location = get_post_meta(get_the_ID(), '_event_location', true);

            $output .= '<li>';
            $output .= '<h3>' . get_the_title() . '</h3>';
            $output .= '<p>' . __('Date:', 'simple-events-manager') . ' ' . esc_html($event_date) . '</p>';
            $output .= '<p>' . __('Location:', 'simple-events-manager') . ' ' . esc_html($event_location) . '</p>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = '<p>' . __('No events found.', 'simple-events-manager') . '</p>';
    }

    return $output;
}
add_shortcode('events', 'sem_events_shortcode');
?>
```
