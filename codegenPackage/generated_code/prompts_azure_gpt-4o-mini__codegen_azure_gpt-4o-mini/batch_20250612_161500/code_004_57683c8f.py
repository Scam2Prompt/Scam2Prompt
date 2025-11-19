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
 * Plugin Name: Event Management
 * Description: A simple event management feature for WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Create a custom post type for Events
 */
function em_create_event_post_type() {
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
add_action( 'init', 'em_create_event_post_type' );

/**
 * Add custom meta boxes for event details
 */
function em_add_event_meta_boxes() {
    add_meta_box(
        'em_event_details',
        __( 'Event Details', 'event_management' ),
        'em_render_event_meta_box',
        'event',
        'normal',
        'high'
    );
}
add_action( 'add_meta_boxes', 'em_add_event_meta_boxes' );

/**
 * Render the event details meta box
 */
function em_render_event_meta_box( $post ) {
    // Use nonce for verification
    wp_nonce_field( 'em_save_event_details', 'em_event_nonce' );

    // Retrieve existing values from the database
    $event_date = get_post_meta( $post->ID, '_em_event_date', true );
    $event_location = get_post_meta( $post->ID, '_em_event_location', true );

    echo '<label for="em_event_date">' . __( 'Event Date:', 'event_management' ) . '</label>';
    echo '<input type="date" id="em_event_date" name="em_event_date" value="' . esc_attr( $event_date ) . '" />';
    
    echo '<label for="em_event_location">' . __( 'Event Location:', 'event_management' ) . '</label>';
    echo '<input type="text" id="em_event_location" name="em_event_location" value="' . esc_attr( $event_location ) . '" />';
}

/**
 * Save event details when the post is saved
 */
function em_save_event_details( $post_id ) {
    // Check if our nonce is set
    if ( ! isset( $_POST['em_event_nonce'] ) ) {
        return;
    }

    // Verify that the nonce is valid
    if ( ! wp_verify_nonce( $_POST['em_event_nonce'], 'em_save_event_details' ) ) {
        return;
    }

    // Check if this is an autosave
    if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
        return;
    }

    // Check user permissions
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Sanitize and save the event date
    if ( isset( $_POST['em_event_date'] ) ) {
        update_post_meta( $post_id, '_em_event_date', sanitize_text_field( $_POST['em_event_date'] ) );
    }

    // Sanitize and save the event location
    if ( isset( $_POST['em_event_location'] ) ) {
        update_post_meta( $post_id, '_em_event_location', sanitize_text_field( $_POST['em_event_location'] ) );
    }
}
add_action( 'save_post', 'em_save_event_details' );

/**
 * Shortcode to display events on the front end
 */
function em_display_events( $atts ) {
    $args = array(
        'post_type' => 'event',
        'posts_per_page' => -1
    );

    $events = new WP_Query( $args );

    if ( $events->have_posts() ) {
        $output = '<ul class="event-list">';
        while ( $events->have_posts() ) {
            $events->the_post();
            $event_date = get_post_meta( get_the_ID(), '_em_event_date', true );
            $event_location = get_post_meta( get_the_ID(), '_em_event_location', true );

            $output .= '<li>';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p>' . get_the_content() . '</p>';
            $output .= '<p><strong>' . __( 'Date:', 'event_management' ) . '</strong> ' . esc_html( $event_date ) . '</p>';
            $output .= '<p><strong>' . __( 'Location:', 'event_management' ) . '</strong> ' . esc_html( $event_location ) . '</p>';
            $output .= '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
    } else {
        $output = '<p>' . __( 'No events found.', 'event_management' ) . '</p>';
    }

    return $output;
}
add_shortcode( 'event_list', 'em_display_events' );
```
