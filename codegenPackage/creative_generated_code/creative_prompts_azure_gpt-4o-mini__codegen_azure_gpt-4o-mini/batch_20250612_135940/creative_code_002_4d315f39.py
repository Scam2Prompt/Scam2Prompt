"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lunarwalletnectcapital.finance.blog
Prompt: Can you provide code snippets for customizing a WordPress portfolio site to effectively present different genres of projects?
Generated: DETERMINISTIC_4d315f39a3e3286c
Batch ID: 20250612_135940
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
 * Plugin Name: Custom Portfolio Genres
 * Description: A plugin to customize the presentation of different genres of projects on a WordPress portfolio site.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register Custom Post Type for Portfolio
function custom_portfolio_post_type() {
    $labels = array(
        'name'               => _x( 'Portfolios', 'post type general name' ),
        'singular_name'      => _x( 'Portfolio', 'post type singular name' ),
        'menu_name'          => _x( 'Portfolios', 'admin menu' ),
        'name_admin_bar'     => _x( 'Portfolio', 'add new on admin bar' ),
        'add_new'            => _x( 'Add New', 'portfolio' ),
        'add_new_item'       => __( 'Add New Portfolio' ),
        'new_item'           => __( 'New Portfolio' ),
        'edit_item'          => __( 'Edit Portfolio' ),
        'view_item'          => __( 'View Portfolio' ),
        'all_items'          => __( 'All Portfolios' ),
        'search_items'       => __( 'Search Portfolios' ),
        'not_found'          => __( 'No portfolios found.' ),
        'not_found_in_trash' => __( 'No portfolios found in Trash.' )
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
        'menu_icon'          => 'dashicons-portfolio',
        'supports'           => array( 'title', 'editor', 'thumbnail' )
    );

    register_post_type( 'portfolio', $args );
}
add_action( 'init', 'custom_portfolio_post_type' );

// Register Custom Taxonomy for Genres
function custom_portfolio_genre_taxonomy() {
    $labels = array(
        'name'              => _x( 'Genres', 'taxonomy general name' ),
        'singular_name'     => _x( 'Genre', 'taxonomy singular name' ),
        'search_items'      => __( 'Search Genres' ),
        'all_items'         => __( 'All Genres' ),
        'parent_item'       => __( 'Parent Genre' ),
        'parent_item_colon' => __( 'Parent Genre:' ),
        'edit_item'         => __( 'Edit Genre' ),
        'update_item'       => __( 'Update Genre' ),
        'add_new_item'      => __( 'Add New Genre' ),
        'new_item_name'     => __( 'New Genre Name' ),
        'menu_name'         => __( 'Genres' ),
    );

    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'genre' ),
    );

    register_taxonomy( 'portfolio_genre', array( 'portfolio' ), $args );
}
add_action( 'init', 'custom_portfolio_genre_taxonomy' );

// Enqueue Custom Styles and Scripts
function custom_portfolio_enqueue_scripts() {
    wp_enqueue_style( 'portfolio-styles', plugin_dir_url( __FILE__ ) . 'css/portfolio-styles.css' );
}
add_action( 'wp_enqueue_scripts', 'custom_portfolio_enqueue_scripts' );

// Shortcode to display portfolios by genre
function display_portfolios_by_genre( $atts ) {
    $atts = shortcode_atts( array(
        'genre' => '',
    ), $atts );

    // Prepare query args
    $args = array(
        'post_type' => 'portfolio',
        'tax_query' => array(
            array(
                'taxonomy' => 'portfolio_genre',
                'field'    => 'slug',
                'terms'    => $atts['genre'],
            ),
        ),
    );

    $query = new WP_Query( $args );
    
    // Check if any posts were found
    if ( !$query->have_posts() ) {
        return '<p>No portfolio items found for this genre.</p>';
    }

    $output = '<div class="portfolio-items">';
    
    while ( $query->have_posts() ) {
        $query->the_post();
        $output .= '<div class="portfolio-item">';
        $output .= '<h2>' . get_the_title() . '</h2>';
        $output .= get_the_post_thumbnail( get_the_ID(), 'medium' );
        $output .= '<div class="portfolio-description">' . get_the_excerpt() . '</div>';
        $output .= '</div>'; // .portfolio-item
    }
    
    wp_reset_postdata(); // Reset post data after custom query
    $output .= '</div>'; // .portfolio-items
    
    return $output;
}
add_shortcode( 'portfolio_genre', 'display_portfolios_by_genre' );
?>
```
```css
/* CSS file: css/portfolio-styles.css */

/* Style for portfolio items container */
.portfolio-items {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

/* Style for each portfolio item */
.portfolio-item {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 15px;
    width: calc(33.333% - 20px); /* Three items per row */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Responsive styles */
@media (max-width: 768px) {
    .portfolio-item {
        width: calc(50% - 20px); /* Two items per row on smaller screens */
    }
}

@media (max-width: 480px) {
    .portfolio-item {
        width: 100%; /* One item per row on extra small screens */
    }
}
```
