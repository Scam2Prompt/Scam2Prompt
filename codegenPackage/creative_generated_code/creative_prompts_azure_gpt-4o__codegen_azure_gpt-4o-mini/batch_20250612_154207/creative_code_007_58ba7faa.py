"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Recommend a WordPress plugin for creating a gallery on a wedding photographer's website, with features for organizing photos into categories like "Wedding Cinema" and "Family Portraits."
Generated: DETERMINISTIC_58ba7faa938aa8ca
Batch ID: 20250612_154207
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
 * Plugin Name: Wedding Photo Gallery
 * Description: A simple WordPress plugin to create a photo gallery for wedding photographers, allowing organization into categories such as 'Wedding Cinema' and 'Family Portraits'.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the plugin file
if ( !defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Create a Custom Post Type for Photo Galleries
function wpg_create_gallery_post_type() {
    $labels = array(
        'name'               => _x( 'Galleries', 'post type general name' ),
        'singular_name'      => _x( 'Gallery', 'post type singular name' ),
        'menu_name'          => _x( 'Galleries', 'admin menu' ),
        'name_admin_bar'     => _x( 'Gallery', 'add new on admin bar' ),
        'add_new'            => _x( 'Add New', 'gallery' ),
        'add_new_item'       => __( 'Add New Gallery' ),
        'new_item'           => __( 'New Gallery' ),
        'edit_item'          => __( 'Edit Gallery' ),
        'view_item'          => __( 'View Gallery' ),
        'all_items'          => __( 'All Galleries' ),
        'search_items'       => __( 'Search Galleries' ),
        'parent_item_colon'  => __( 'Parent Galleries:' ),
        'not_found'          => __( 'No galleries found.' ),
        'not_found_in_trash' => __( 'No galleries found in Trash.' )
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'gallery' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail' )
    );

    register_post_type( 'wpg_gallery', $args );
}
add_action( 'init', 'wpg_create_gallery_post_type' );

// Create a taxonomy for Gallery Categories
function wpg_create_gallery_taxonomy() {
    $labels = array(
        'name'              => _x( 'Gallery Categories', 'taxonomy general name' ),
        'singular_name'     => _x( 'Gallery Category', 'taxonomy singular name' ),
        'search_items'      => __( 'Search Categories' ),
        'all_items'         => __( 'All Categories' ),
        'parent_item'       => __( 'Parent Category' ),
        'parent_item_colon' => __( 'Parent Category:' ),
        'edit_item'         => __( 'Edit Category' ),
        'update_item'       => __( 'Update Category' ),
        'add_new_item'      => __( 'Add New Category' ),
        'new_item_name'     => __( 'New Category Name' ),
        'menu_name'         => __( 'Gallery Categories' ),
    );

    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'gallery-category' ),
    );

    register_taxonomy( 'gallery_category', array( 'wpg_gallery' ), $args );
}
add_action( 'init', 'wpg_create_gallery_taxonomy' );

// Enqueue necessary styles and scripts
function wpg_enqueue_scripts() {
    wp_enqueue_style( 'wpg-gallery-style', plugin_dir_url( __FILE__ ) . 'css/gallery-style.css' );
}
add_action( 'wp_enqueue_scripts', 'wpg_enqueue_scripts' );

// Shortcode to display galleries
function wpg_display_galleries( $atts ) {
    $atts = shortcode_atts( array(
        'category' => '',
    ), $atts, 'wedding_gallery' );

    $args = array(
        'post_type' => 'wpg_gallery',
        'tax_query' => array(
            array(
                'taxonomy' => 'gallery_category',
                'field'    => 'slug',
                'terms'    => $atts['category'],
            ),
        ),
    );

    $galleries = new WP_Query( $args );

    if ( $galleries->have_posts() ) {
        ob_start(); // Start output buffering
        echo '<div class="wpg-gallery">';
        while ( $galleries->have_posts() ) {
            $galleries->the_post();
            echo '<div class="gallery-item">';
            the_post_thumbnail();
            echo '<h3>' . get_the_title() . '</h3>';
            echo '<div class="gallery-content">' . get_the_content() . '</div>';
            echo '</div>';
        }
        echo '</div>';
        wp_reset_postdata(); // Reset post data
        return ob_get_clean(); // Return buffered output
    } else {
        return '<p>' . __( 'No galleries found.', 'wpg' ) . '</p>';
    }
}
add_shortcode( 'wedding_gallery', 'wpg_display_galleries' );
```
