"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Design a WordPress plugin to manage events, including creating, editing, and deleting event listings, using WordPress best practices.
Generated: DETERMINISTIC_e1d19dd492d8a849
Batch ID: 20250622_212519
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
 * Description: A simple plugin to manage events including creating, editing, and deleting event listings.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Register custom post type for Events
function em_register_event_post_type() {
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
add_action( 'init', 'em_register_event_post_type' );

// Add meta boxes for event details
function em_add_event_meta_boxes() {
    add_meta_box( 'event_details', 'Event Details', 'em_event_details_callback', 'event', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'em_add_event_meta_boxes' );

// Callback function for event details meta box
function em_event_details_callback( $post ) {
    // Use nonce for verification
    wp_nonce_field( 'em_save_event_details', 'em_event_nonce' );

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
    if ( isset( $_POST['event_date'] ) ) {
        $event_date = sanitize_text_field( $_POST['event_date'] );
        update_post_meta( $post_id, '_event_date', $event_date );
    }

    // Sanitize and save the event location
    if ( isset( $_POST['event_location'] ) ) {
        $event_location = sanitize_text_field( $_POST['event_location'] );
        update_post_meta( $post_id, '_event_location', $event_location );
    }
}
add_action( 'save_post', 'em_save_event_details' );

// Shortcode to display events
function em_display_events( $atts ) {
    $args = array(
        'post_type' => 'event',
        'posts_per_page' => -1
    );

    $events = new WP_Query( $args );
    $output = '<div class="event-list">';

    if ( $events->have_posts() ) {
        while ( $events->have_posts() ) {
            $events->the_post();
            $event_date = get_post_meta( get_the_ID(), '_event_date', true );
            $event_location = get_post_meta( get_the_ID(), '_event_location', true );

            $output .= '<div class="event-item">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p>Date: ' . esc_html( $event_date ) . '</p>';
            $output .= '<p>Location: ' . esc_html( $event_location ) . '</p>';
            $output .= '</div>';
        }
    } else {
        $output .= '<p>No events found.</p>';
    }

    $output .= '</div>';
    wp_reset_postdata();

    return $output;
}
add_shortcode( 'event_list', 'em_display_events' );

// Enqueue styles and scripts
function em_enqueue_scripts() {
    wp_enqueue_style( 'em-styles', plugin_dir_url( __FILE__ ) . 'css/styles.css' );
}
add_action( 'wp_enqueue_scripts', 'em_enqueue_scripts' );
```

**Note:** Ensure to create a `css/styles.css` file for styling the events as needed.
