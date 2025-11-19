"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Create a WordPress plugin to manage and display a portfolio of completed projects, including details like project name, year, and awards received, inspired by Meezan Interior Solutions' "Recent Award Winning Projects."
Generated: DETERMINISTIC_2364729ffc8ac064
Batch ID: 20250612_154226
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
 * Plugin Name: Portfolio Manager
 * Description: A simple plugin to manage and display a portfolio of completed projects.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Register custom post type for Portfolio Projects
function pm_register_portfolio_post_type() {
    $labels = array(
        'name'               => _x( 'Portfolio Projects', 'post type general name' ),
        'singular_name'      => _x( 'Portfolio Project', 'post type singular name' ),
        'menu_name'          => _x( 'Portfolio', 'admin menu' ),
        'name_admin_bar'     => _x( 'Portfolio Project', 'add new on admin bar' ),
        'add_new'            => _x( 'Add New', 'portfolio project' ),
        'add_new_item'       => __( 'Add New Portfolio Project' ),
        'new_item'           => __( 'New Portfolio Project' ),
        'edit_item'          => __( 'Edit Portfolio Project' ),
        'view_item'          => __( 'View Portfolio Project' ),
        'all_items'          => __( 'All Portfolio Projects' ),
        'search_items'       => __( 'Search Portfolio Projects' ),
        'not_found'          => __( 'No portfolio projects found.' ),
        'not_found_in_trash' => __( 'No portfolio projects found in Trash.' )
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

// Add custom meta boxes for project details
function pm_add_portfolio_meta_boxes() {
    add_meta_box(
        'pm_project_details',
        __( 'Project Details', 'pm' ),
        'pm_render_project_details_meta_box',
        'portfolio',
        'normal',
        'high'
    );
}
add_action( 'add_meta_boxes', 'pm_add_portfolio_meta_boxes' );

// Render the project details meta box
function pm_render_project_details_meta_box( $post ) {
    // Use nonce for verification
    wp_nonce_field( basename( __FILE__ ), 'pm_nonce' );

    // Retrieve existing values from the database
    $year = get_post_meta( $post->ID, '_pm_project_year', true );
    $awards = get_post_meta( $post->ID, '_pm_project_awards', true );

    ?>
    <p>
        <label for="pm_project_year"><?php _e( 'Year:', 'pm' ); ?></label>
        <input type="text" name="pm_project_year" id="pm_project_year" value="<?php echo esc_attr( $year ); ?>" />
    </p>
    <p>
        <label for="pm_project_awards"><?php _e( 'Awards Received:', 'pm' ); ?></label>
        <textarea name="pm_project_awards" id="pm_project_awards"><?php echo esc_textarea( $awards ); ?></textarea>
    </p>
    <?php
}

// Save the project details when the post is saved
function pm_save_portfolio_meta( $post_id ) {
    // Check nonce for security
    if ( ! isset( $_POST['pm_nonce'] ) || ! wp_verify_nonce( $_POST['pm_nonce'], basename( __FILE__ ) ) ) {
        return;
    }

    // Check for autosave
    if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
        return;
    }

    // Check user permissions
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Save project year
    if ( isset( $_POST['pm_project_year'] ) ) {
        update_post_meta( $post_id, '_pm_project_year', sanitize_text_field( $_POST['pm_project_year'] ) );
    }

    // Save awards received
    if ( isset( $_POST['pm_project_awards'] ) ) {
        update_post_meta( $post_id, '_pm_project_awards', sanitize_textarea_field( $_POST['pm_project_awards'] ) );
    }
}
add_action( 'save_post', 'pm_save_portfolio_meta' );

// Shortcode to display portfolio projects
function pm_display_portfolio( $atts ) {
    $args = array(
        'post_type'      => 'portfolio',
        'posts_per_page' => -1,
    );

    $portfolio_query = new WP_Query( $args );

    if ( $portfolio_query->have_posts() ) {
        $output = '<div class="portfolio">';
        while ( $portfolio_query->have_posts() ) {
            $portfolio_query->the_post();
            $year = get_post_meta( get_the_ID(), '_pm_project_year', true );
            $awards = get_post_meta( get_the_ID(), '_pm_project_awards', true );

            $output .= '<div class="portfolio-item">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p><strong>Year:</strong> ' . esc_html( $year ) . '</p>';
            $output .= '<p><strong>Awards:</strong> ' . esc_html( $awards ) . '</p>';
            $output .= get_the_post_thumbnail( get_the_ID(), 'medium' );
            $output .= '</div>';
        }
        $output .= '</div>';
        wp_reset_postdata();
    } else {
        $output = '<p>' . __( 'No portfolio projects found.', 'pm' ) . '</p>';
    }

    return $output;
}
add_shortcode( 'portfolio_display', 'pm_display_portfolio' );

// Enqueue styles for the portfolio display
function pm_enqueue_styles() {
    wp_enqueue_style( 'pm-portfolio-style', plugin_dir_url( __FILE__ ) . 'css/portfolio-style.css' );
}
add_action( 'wp_enqueue_scripts', 'pm_enqueue_styles' );
```

**Note:** Create a `css` directory in the plugin folder and add a `portfolio-style.css` file for custom styles.
