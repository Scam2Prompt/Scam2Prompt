"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Recommend a WordPress plugin or API to manage service listings for "تلميع سيارات متنقل" and "تركيب زجاج سيكوريت" across different cities, as described on https://www.khadamy.com.
Generated: DETERMINISTIC_6453b8a093e0c06a
Batch ID: 20250612_154239
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
 * Plugin Name: Service Listings Manager
 * Description: A plugin to manage service listings for تلميع سيارات متنقل and تركيب زجاج سيكوريت across different cities.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Custom post type for Service Listings
 */
function slm_create_service_post_type() {
    $labels = array(
        'name'                  => _x( 'Services', 'Post type general name', 'slm' ),
        'singular_name'         => _x( 'Service', 'Post type singular name', 'slm' ),
        'menu_name'             => _x( 'Services', 'Admin Menu text', 'slm' ),
        'name_admin_bar'        => _x( 'Service', 'Add New on Toolbar', 'slm' ),
        'add_new'               => __( 'Add New', 'slm' ),
        'add_new_item'          => __( 'Add New Service', 'slm' ),
        'new_item'              => __( 'New Service', 'slm' ),
        'edit_item'             => __( 'Edit Service', 'slm' ),
        'view_item'             => __( 'View Service', 'slm' ),
        'all_items'             => __( 'All Services', 'slm' ),
        'search_items'          => __( 'Search Services', 'slm' ),
        'not_found'             => __( 'No services found.', 'slm' ),
        'not_found_in_trash'    => __( 'No services found in Trash.', 'slm' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'service' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
    );

    register_post_type( 'service', $args );
}
add_action( 'init', 'slm_create_service_post_type' );

/**
 * Add meta boxes for service details
 */
function slm_add_service_meta_boxes() {
    add_meta_box( 'service_details', __( 'Service Details', 'slm' ), 'slm_render_service_meta_box', 'service' );
}
add_action( 'add_meta_boxes', 'slm_add_service_meta_boxes' );

/**
 * Render the service details meta box
 */
function slm_render_service_meta_box( $post ) {
    // Nonce field for security
    wp_nonce_field( 'slm_save_service_details', 'slm_service_nonce' );

    $cities = get_post_meta( $post->ID, 'service_cities', true );

    echo '<label for="service_cities">' . __( 'Cities (comma-separated)', 'slm' ) . '</label>';
    echo '<input type="text" id="service_cities" name="service_cities" value="' . esc_attr( $cities ) . '" class="widefat" />';
}

/**
 * Save service details
 */
function slm_save_service_details( $post_id ) {
    // Check if nonce is set
    if ( ! isset( $_POST['slm_service_nonce'] ) ) {
        return;
    }

    // Verify nonce
    if ( ! wp_verify_nonce( $_POST['slm_service_nonce'], 'slm_save_service_details' ) ) {
        return;
    }

    // Check if user has permissions to save data
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Sanitize and save the cities data
    if ( isset( $_POST['service_cities'] ) ) {
        $cities = sanitize_text_field( $_POST['service_cities'] );
        update_post_meta( $post_id, 'service_cities', $cities );
    }
}
add_action( 'save_post', 'slm_save_service_details' );

/**
 * Shortcode to display services
 */
function slm_service_list_shortcode( $atts ) {
    $args = array(
        'post_type' => 'service',
        'posts_per_page' => -1,
    );

    $services = new WP_Query( $args );
    $output = '<div class="service-list">';

    if ( $services->have_posts() ) {
        while ( $services->have_posts() ) {
            $services->the_post();
            $cities = get_post_meta( get_the_ID(), 'service_cities', true );

            $output .= '<div class="service-item">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<div>' . get_the_content() . '</div>';
            $output .= '<p><strong>' . __( 'Cities:', 'slm' ) . '</strong> ' . esc_html( $cities ) . '</p>';
            $output .= '</div>';
        }
        wp_reset_postdata();
    } else {
        $output .= '<p>' . __( 'No services found.', 'slm' ) . '</p>';
    }

    $output .= '</div>';
    return $output;
}
add_shortcode( 'service_list', 'slm_service_list_shortcode' );

?>
```
