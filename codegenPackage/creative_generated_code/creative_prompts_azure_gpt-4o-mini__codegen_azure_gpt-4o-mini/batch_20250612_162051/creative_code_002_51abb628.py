"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Create an API that allows users to submit travel experiences and display them on a WordPress site like Rupak Parajuli's.
Generated: DETERMINISTIC_51abb628325b64b9
Batch ID: 20250612_162051
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
 * Plugin Name: Travel Experience Submission
 * Description: A simple API for users to submit their travel experiences and display them on a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register custom post type for travel experiences.
 */
function tes_register_post_type() {
    $labels = array(
        'name'               => 'Travel Experiences',
        'singular_name'      => 'Travel Experience',
        'menu_name'          => 'Travel Experiences',
        'name_admin_bar'     => 'Travel Experience',
        'add_new'            => 'Add New',
        'add_new_item'       => 'Add New Travel Experience',
        'new_item'           => 'New Travel Experience',
        'edit_item'          => 'Edit Travel Experience',
        'view_item'          => 'View Travel Experience',
        'all_items'          => 'All Travel Experiences',
        'search_items'       => 'Search Travel Experiences',
        'not_found'          => 'No travel experiences found.',
        'not_found_in_trash' => 'No travel experiences found in trash.',
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
        'show_in_rest'       => true,
    );

    register_post_type( 'travel_experience', $args );
}
add_action( 'init', 'tes_register_post_type' );

/**
 * Create a REST API endpoint for submitting travel experiences.
 */
function tes_submit_experience( WP_REST_Request $request ) {
    // Validate the input data
    $title   = sanitize_text_field( $request['title'] );
    $content = sanitize_textarea_field( $request['content'] );

    if ( empty( $title ) || empty( $content ) ) {
        return new WP_Error( 'missing_data', 'Title and content are required.', array( 'status' => 400 ) );
    }

    // Prepare the post data
    $post_data = array(
        'post_title'   => $title,
        'post_content' => $content,
        'post_status'  => 'publish',
        'post_type'    => 'travel_experience',
    );

    // Insert the post into the database
    $post_id = wp_insert_post( $post_data );

    if ( is_wp_error( $post_id ) ) {
        return new WP_Error( 'database_error', 'Failed to save travel experience.', array( 'status' => 500 ) );
    }

    return array( 'success' => true, 'post_id' => $post_id );
}

// Register the API route
add_action( 'rest_api_init', function () {
    register_rest_route( 'tes/v1', '/submit/', array(
        'methods'  => 'POST',
        'callback' => 'tes_submit_experience',
        'permission_callback' => '__return_true',
    ) );
});

/**
 * Display travel experiences on the front-end using a shortcode.
 */
function tes_display_experiences() {
    $args = array(
        'post_type' => 'travel_experience',
        'posts_per_page' => -1,
    );

    $experiences = new WP_Query( $args );

    if ( ! $experiences->have_posts() ) {
        return '<p>No travel experiences found.</p>';
    }

    $output = '<div class="travel-experiences">';
    while ( $experiences->have_posts() ) {
        $experiences->the_post();
        $output .= '<div class="experience">';
        $output .= '<h2>' . get_the_title() . '</h2>';
        $output .= '<div>' . get_the_content() . '</div>';
        $output .= '</div>';
    }
    $output .= '</div>';

    // Restore original Post Data
    wp_reset_postdata();

    return $output;
}

// Register shortcode to display experiences
add_shortcode( 'travel_experiences', 'tes_display_experiences' );

?>
```
