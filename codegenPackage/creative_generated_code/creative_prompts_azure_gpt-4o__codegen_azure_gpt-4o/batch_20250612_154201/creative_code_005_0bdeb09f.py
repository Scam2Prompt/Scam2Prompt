"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaexch.info
Prompt: Provide code to integrate an "Events" calendar into a WordPress blog, as referenced in the site's navigation.
Generated: DETERMINISTIC_0bdeb09f4f683319
Batch ID: 20250612_154201
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
 * Plugin Name: Events Calendar Integration
 * Description: Adds an "Events" calendar to the WordPress blog and links it in the site's navigation.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Register custom post type for Events
function register_events_post_type() {
    $labels = array(
        'name'               => __('Events', 'events-calendar'),
        'singular_name'      => __('Event', 'events-calendar'),
        'menu_name'          => __('Events', 'events-calendar'),
        'name_admin_bar'     => __('Event', 'events-calendar'),
        'add_new'            => __('Add New', 'events-calendar'),
        'add_new_item'       => __('Add New Event', 'events-calendar'),
        'edit_item'          => __('Edit Event', 'events-calendar'),
        'new_item'           => __('New Event', 'events-calendar'),
        'view_item'          => __('View Event', 'events-calendar'),
        'search_items'       => __('Search Events', 'events-calendar'),
        'not_found'          => __('No events found.', 'events-calendar'),
        'not_found_in_trash' => __('No events found in Trash.', 'events-calendar'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'rewrite'            => array('slug' => 'events'),
        'supports'           => array('title', 'editor', 'excerpt', 'custom-fields'),
    );

    register_post_type('event', $args);
}
add_action('init', 'register_events_post_type');

// Add "Events" link to site's navigation
function add_events_to_navigation($items, $args) {
    if ($args->theme_location === 'primary') { // Adjust theme_location as needed
        $events_link = '<li><a href="' . esc_url(get_post_type_archive_link('event')) . '">' . __('Events', 'events-calendar') . '</a></li>';
        $items .= $events_link;
    }
    return $items;
}
add_filter('wp_nav_menu_items', 'add_events_to_navigation', 10, 2);

// Shortcode to display Events calendar
function events_calendar_shortcode() {
    $query = new WP_Query(array(
        'post_type'      => 'event',
        'posts_per_page' => -1,
        'orderby'        => 'meta_value',
        'meta_key'       => 'event_date',
        'order'          => 'ASC',
    ));

    if ($query->have_posts()) {
        $output = '<div class="events-calendar">';
        $output .= '<h2>' . __('Upcoming Events', 'events-calendar') . '</h2>';
        $output .= '<ul>';
        while ($query->have_posts()) {
            $query->the_post();
            $event_date = get_post_meta(get_the_ID(), 'event_date', true);
            $output .= '<li>' . esc_html($event_date) . ' - <a href="' . get_permalink() . '">' . get_the_title() . '</a></li>';
        }
        $output .= '</ul>';
        $output .= '</div>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>' . __('No upcoming events.', 'events-calendar') . '</p>';
    }
}
add_shortcode('events_calendar', 'events_calendar_shortcode');

// Add meta box for event date
function add_event_date_meta_box() {
    add_meta_box(
        'event_date_meta_box',
        __('Event Date', 'events-calendar'),
        'render_event_date_meta_box',
        'event',
        'side',
        'default'
    );
}
add_action('add_meta_boxes', 'add_event_date_meta_box');

// Render meta box for event date
function render_event_date_meta_box($post) {
    $event_date = get_post_meta($post->ID, 'event_date', true);
    wp_nonce_field('event_date_nonce_action', 'event_date_nonce');
    echo '<label for="event_date">' . __('Event Date:', 'events-calendar') . '</label>';
    echo '<input type="date" id="event_date" name="event_date" value="' . esc_attr($event_date) . '" />';
}

// Save event date meta box data
function save_event_date_meta_box_data($post_id) {
    if (!isset($_POST['event_date_nonce']) || !wp_verify_nonce($_POST['event_date_nonce'], 'event_date_nonce_action')) {
        return;
    }

    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    if (isset($_POST['event_date'])) {
        update_post_meta($post_id, 'event_date', sanitize_text_field($_POST['event_date']));
    }
}
add_action('save_post', 'save_event_date_meta_box_data');
?>
```
