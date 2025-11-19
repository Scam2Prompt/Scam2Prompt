"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magnumrockets.com
Prompt: Create a sample code for a WordPress event management feature inspired by the content on magnumrockets.com.
Generated: DETERMINISTIC_57683c8fee9a1023
Batch ID: 20250612_161500
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
 * Plugin Name: Event Management
 * Description: A simple event management plugin for WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Register custom post type for Events
 */
function em_register_event_post_type() {
    $labels = array(
        'name'                  => _x( 'Events', 'Post Type General Name', 'text_domain' ),
        'singular_name'         => _x( 'Event', 'Post Type Singular Name', 'text_domain' ),
        'menu_name'             => __( 'Events', 'text_domain' ),
        'name_admin_bar'        => __( 'Event', 'text_domain' ),
        'add_new'               => __( 'Add New', 'event' ),
        'add_new_item'          => __( 'Add New Event', 'text_domain' ),
        'new_item'              => __( 'New Event', 'text_domain' ),
        'edit_item'             => __( 'Edit Event', 'text_domain' ),
        'view_item'             => __( 'View Event', 'text_domain' ),
        'all_items'             => __( 'All Events', 'text_domain' ),
        'search_items'          => __( 'Search Events', 'text_domain' ),
        'not_found'             => __( 'No events found.', 'text_domain' ),
        'not_found_in_trash'    => __( 'No events found in Trash.', 'text_domain' ),
    );

    $args = array(
        'label'                 => __( 'Event', 'text_domain' ),
        'labels'                => $labels,
        'supports'              => array( 'title', 'editor', 'thumbnail', 'custom-fields' ),
        'hierarchical'          => false,
        'public'                => true,
        'show_ui'               => true,
        'show_in_menu'          => true,
        'menu_position'         => 5,
        'show_in_admin_bar'     => true,
        'show_in_nav_menus'     => true,
        'can_export'            => true,
        'has_archive'           => true,
        'exclude_from_search'   => false,
        'publicly_queryable'    => true,
        'capability_type'       => 'post',
        'rewrite'               => array( 'slug' => 'events' ),
    );

    register_post_type( 'event', $args );
}
add_action( 'init', 'em_register_event_post_type' );

/**
 * Add Event Meta Boxes
 */
function em_add_event_meta_boxes() {
    add_meta_box(
        'event_details',
        __( 'Event Details', 'text_domain' ),
        'em_render_event_details_meta_box',
        'event',
        'normal',
        'high'
    );
}
add_action( 'add_meta_boxes', 'em_add_event_meta_boxes' );

/**
 * Render Event Details Meta Box
 */
function em_render_event_details_meta_box( $post ) {
    // Nonce field for security
    wp_nonce_field( 'em_event_details_nonce', 'em_event_details_nonce' );

    // Retrieve existing meta values
    $event_date = get_post_meta( $post->ID, '_event_date', true );
    $event_location = get_post_meta( $post->ID, '_event_location', true );

    echo '<label for="event_date">' . __( 'Event Date:', 'text_domain' ) . '</label>';
    echo '<input type="date" id="event_date" name="event_date" value="' . esc_attr( $event_date ) . '" />';
    
    echo '<label for="event_location">' . __( 'Event Location:', 'text_domain' ) . '</label>';
    echo '<input type="text" id="event_location" name="event_location" value="' . esc_attr( $event_location ) . '" />';
}

/**
 * Save Event Meta Data
 */
function em_save_event_meta_data( $post_id ) {
    // Check if nonce is set
    if ( ! isset( $_POST['em_event_details_nonce'] ) ) {
        return;
    }
    // Verify nonce
    if ( ! wp_verify_nonce( $_POST['em_event_details_nonce'], 'em_event_details_nonce' ) ) {
        return;
    }

    // Check the user's permissions
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Save or update meta fields
    if ( isset( $_POST['event_date'] ) ) {
        update_post_meta( $post_id, '_event_date', sanitize_text_field( $_POST['event_date'] ) );
    }
    if ( isset( $_POST['event_location'] ) ) {
        update_post_meta( $post_id, '_event_location', sanitize_text_field( $_POST['event_location'] ) );
    }
}
add_action( 'save_post', 'em_save_event_meta_data' );

/**
 * Shortcode to display upcoming events
 */
function em_upcoming_events_shortcode( $atts ) {
    $args = array(
        'post_type'      => 'event',
        'posts_per_page' => 5,
        'meta_query'     => array(
            array(
                'key'     => '_event_date',
                'value'   => date('Y-m-d'),
                'compare' => '>=',
                'type'    => 'DATE',
            ),
        ),
        'orderby'        => 'meta_value',
        'order'          => 'ASC',
    );

    $events_query = new WP_Query( $args );

    if ( $events_query->have_posts() ) {
        $output = '<ul class="upcoming-events">';
        
        while ( $events_query->have_posts() ) {
            $events_query->the_post();
            
            $event_date = get_post_meta( get_the_ID(), '_event_date', true );
            $event_location = get_post_meta( get_the_ID(), '_event_location', true );

            $output .= '<li>';
            $output .= '<strong>' . get_the_title() . '</strong><br>';
            $output .= '<em>' . esc_html( $event_date ) . '</em><br>';
            $output .= esc_html( $event_location ) . '<br>';
            $output .= '</li>';
        }
        
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = __( 'No upcoming events found.', 'text_domain' );
    }

    return $output;
}
add_shortcode( 'upcoming_events', 'em_upcoming_events_shortcode' );
?>
```
