"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Create a WordPress plugin to manage and display a portfolio of completed projects, including details like project name, year, and awards received, inspired by Meezan Interior Solutions' "Recent Award Winning Projects."
Generated: DETERMINISTIC_2364729ffc8ac064
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
Plugin Name: Portfolio Manager
Plugin URI: https://example.com
Description: A plugin to manage and display a portfolio of completed projects, including project details like name, year, and awards received.
Version: 1.0
Author: Your Name
Author URI: https://example.com
License: GPL2
*/

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Register custom post type for Portfolio Projects
function pm_register_portfolio_post_type() {
    $labels = array(
        'name'               => _x( 'Portfolio Projects', 'post type general name', 'portfolio-manager' ),
        'singular_name'      => _x( 'Project', 'post type singular name', 'portfolio-manager' ),
        'menu_name'          => _x( 'Portfolio', 'admin menu', 'portfolio-manager' ),
        'name_admin_bar'     => _x( 'Project', 'add new on admin bar', 'portfolio-manager' ),
        'add_new'            => _x( 'Add New', 'project', 'portfolio-manager' ),
        'add_new_item'       => __( 'Add New Project', 'portfolio-manager' ),
        'new_item'           => __( 'New Project', 'portfolio-manager' ),
        'edit_item'          => __( 'Edit Project', 'portfolio-manager' ),
        'view_item'          => __( 'View Project', 'portfolio-manager' ),
        'all_items'          => __( 'All Projects', 'portfolio-manager' ),
        'search_items'       => __( 'Search Projects', 'portfolio-manager' ),
        'parent_item_colon'  => __( 'Parent Projects:', 'portfolio-manager' ),
        'not_found'          => __( 'No projects found.', 'portfolio-manager' ),
        'not_found_in_trash' => __( 'No projects found in Trash.', 'portfolio-manager' )
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'portfolio' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
    );

    register_post_type( 'portfolio', $args );
}
add_action( 'init', 'pm_register_portfolio_post_type' );

// Create custom taxonomy for Awards
function pm_create_award_taxonomy() {
    $labels = array(
        'name'              => _x( 'Awards', 'taxonomy general name', 'portfolio-manager' ),
        'singular_name'     => _x( 'Award', 'taxonomy singular name', 'portfolio-manager' ),
        'search_items'      => __( 'Search Awards', 'portfolio-manager' ),
        'all_items'         => __( 'All Awards', 'portfolio-manager' ),
        'parent_item'       => __( 'Parent Award', 'portfolio-manager' ),
        'parent_item_colon' => __( 'Parent Award:', 'portfolio-manager' ),
        'edit_item'         => __( 'Edit Award', 'portfolio-manager' ),
        'update_item'       => __( 'Update Award', 'portfolio-manager' ),
        'add_new_item'      => __( 'Add New Award', 'portfolio-manager' ),
        'new_item_name'     => __( 'New Award Name', 'portfolio-manager' ),
        'menu_name'         => __( 'Awards', 'portfolio-manager' ),
    );

    $args = array(
        'hierarchical'      => true,
        'labels'            => $labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'award' ),
    );

    register_taxonomy( 'award', array( 'portfolio' ), $args );
}
add_action( 'init', 'pm_create_award_taxonomy' );

// Enqueue styles and scripts
function pm_enqueue_scripts() {
    wp_enqueue_style( 'portfolio-manager-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
    wp_enqueue_script( 'portfolio-manager-script', plugin_dir_url( __FILE__ ) . 'js/script.js', array( 'jquery' ), '', true );
}
add_action( 'wp_enqueue_scripts', 'pm_enqueue_scripts' );

// Shortcode to display portfolio projects
function pm_display_portfolio( $atts ) {
    // Extract shortcode attributes
    $atts = shortcode_atts( array(
        'count' => -1
    ), $atts, 'portfolio' );

    $query_args = array(
        'post_type' => 'portfolio',
        'posts_per_page' => (int) $atts['count']
    );

    $portfolio_query = new WP_Query( $query_args );

    if ( $portfolio_query->have_posts() ) {
        $output = '<div class="portfolio-projects">';
        
        while ( $portfolio_query->have_posts() ) {
            $portfolio_query->the_post();
            $output .= '<div class="project">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<div class="project-content">' . get_the_content() . '</div>';
            $output .= '<div class="project-year">' . get_post_meta( get_the_ID(), 'project_year', true ) . '</div>';
            $output .= '<div class="project-awards">' . get_the_terms( get_the_ID(), 'award' ) ? implode( ', ', wp_list_pluck( get_the_terms( get_the_ID(), 'award' ), 'name' ) ) : 'No awards' . '</div>';
            $output .= '</div>';
        }

        $output .= '</div>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>' . __( 'No projects found.', 'portfolio-manager' ) . '</p>';
    }
}
add_shortcode( 'portfolio', 'pm_display_portfolio' );

// Add meta box for Project Year
function pm_add_project_year_meta_box() {
    add_meta_box(
        'project_year_meta_box',
        __( 'Project Year', 'portfolio-manager' ),
        'pm_render_project_year_meta_box',
        'portfolio',
        'side',
        'default'
    );
}
add_action( 'add_meta_boxes', 'pm_add_project_year_meta_box' );

// Render meta box content
function pm_render_project_year_meta_box( $post ) {
    wp_nonce_field( 'pm_save_project_year_meta', 'pm_project_year_meta_nonce' );
    $value = get_post_meta( $post->ID, 'project_year', true );
    echo '<label for="pm_project_year">' . __( 'Year:', 'portfolio-manager' ) . '</label>';
    echo '<input type="text" id="pm_project_year" name="pm_project_year" value="' . esc_attr( $value ) . '" />';
}

// Save meta box data
function pm_save_project_year_meta( $post_id ) {
    if ( ! isset( $_POST['pm_project_year_meta_nonce'] ) || ! wp_verify_nonce( $_POST['pm_project_year_meta_nonce'], 'pm_save_project_year_meta' ) ) {
        return;
    }

    if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
        return;
    }

    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    if ( isset( $_POST['pm_project_year'] ) ) {
        update_post_meta( $post_id, 'project_year', sanitize_text_field( $_POST['pm_project_year'] ) );
    }
}
add_action( 'save_post', 'pm_save_project_year_meta' );
```

Make sure to create `css/style.css` and `js/script.js` files for styling and functionality as needed. Adjust the plugin URI and author information accordingly.
