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
 * Plugin Name: Simple Event Manager
 * Description: A simple WordPress plugin to create and manage events.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Register custom post type for Events
function sem_register_event_post_type() {
    $labels = array(
        'name'               => _x( 'Events', 'post type general name' ),
        'singular_name'      => _x( 'Event', 'post type singular name' ),
        'menu_name'          => _x( 'Events', 'admin menu' ),
        'name_admin_bar'     => _x( 'Event', 'add new on admin bar' ),
        'add_new'            => _x( 'Add New', 'event' ),
        'add_new_item'       => __( 'Add New Event' ),
        'new_item'           => __( 'New Event' ),
        'edit_item'          => __( 'Edit Event' ),
        'view_item'          => __( 'View Event' ),
        'all_items'          => __( 'All Events' ),
        'search_items'       => __( 'Search Events' ),
        'not_found'          => __( 'No events found.' ),
        'not_found_in_trash' => __( 'No events found in Trash.' )
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'event' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail', 'custom-fields' )
    );

    register_post_type( 'event', $args );
}
add_action( 'init', 'sem_register_event_post_type' );

// Add meta boxes for event details
function sem_add_event_meta_boxes() {
    add_meta_box( 'event_details', 'Event Details', 'sem_event_details_callback', 'event', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'sem_add_event_meta_boxes' );

// Callback function for event details meta box
function sem_event_details_callback( $post ) {
    // Use nonce for verification
    wp_nonce_field( 'sem_save_event_details', 'sem_event_nonce' );

    // Retrieve existing values
    $event_date = get_post_meta( $post->ID, '_event_date', true );
    $event_location = get_post_meta( $post->ID, '_event_location', true );

    // Display fields
    echo '<label for="event_date">Event Date:</label>';
    echo '<input type="date" id="event_date" name="event_date" value="' . esc_attr( $event_date ) . '" />';
    
    echo '<label for="event_location">Event Location:</label>';
    echo '<input type="text" id="event_location" name="event_location" value="' . esc_attr( $event_location ) . '" />';
}

// Save event details
function sem_save_event_details( $post_id ) {
    // Check nonce for security
    if ( ! isset( $_POST['sem_event_nonce'] ) || ! wp_verify_nonce( $_POST['sem_event_nonce'], 'sem_save_event_details' ) ) {
        return;
    }

    // Check if user has permission to save data
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Save event date
    if ( isset( $_POST['event_date'] ) ) {
        update_post_meta( $post_id, '_event_date', sanitize_text_field( $_POST['event_date'] ) );
    }

    // Save event location
    if ( isset( $_POST['event_location'] ) ) {
        update_post_meta( $post_id, '_event_location', sanitize_text_field( $_POST['event_location'] ) );
    }
}
add_action( 'save_post', 'sem_save_event_details' );

// Shortcode to display events
function sem_display_events( $atts ) {
    $args = array(
        'post_type' => 'event',
        'posts_per_page' => -1
    );

    $events = new WP_Query( $args );

    if ( $events->have_posts() ) {
        $output = '<ul class="event-list">';
        while ( $events->have_posts() ) {
            $events->the_post();
            $event_date = get_post_meta( get_the_ID(), '_event_date', true );
            $event_location = get_post_meta( get_the_ID(), '_event_location', true );

            $output .= '<li>';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p>Date: ' . esc_html( $event_date ) . '</p>';
            $output .= '<p>Location: ' . esc_html( $event_location ) . '</p>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = '<p>No events found.</p>';
    }

    return $output;
}
add_shortcode( 'events', 'sem_display_events' );
```
