"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Create a WordPress plugin for managing client portfolios, inspired by the portfolio management features highlighted on Asnet Infotech's website.
Generated: DETERMINISTIC_7449e21d724265d2
Batch ID: 20250612_152924
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
 * Plugin Name: Client Portfolio Manager
 * Description: A WordPress plugin for managing client portfolios.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class ClientPortfolioManager
 * Main class for the Client Portfolio Manager plugin.
 */
class ClientPortfolioManager {

    /**
     * Constructor to initialize the plugin.
     */
    public function __construct() {
        // Register custom post type for portfolios
        add_action( 'init', array( $this, 'register_portfolio_post_type' ) );

        // Register custom taxonomy for portfolio categories
        add_action( 'init', array( $this, 'register_portfolio_taxonomy' ) );

        // Add meta boxes for portfolio details
        add_action( 'add_meta_boxes', array( $this, 'add_portfolio_meta_boxes' ) );

        // Save portfolio meta data
        add_action( 'save_post', array( $this, 'save_portfolio_meta' ) );

        // Enqueue admin scripts and styles
        add_action( 'admin_enqueue_scripts', array( $this, 'enqueue_admin_scripts' ) );
    }

    /**
     * Register the custom post type for portfolios.
     */
    public function register_portfolio_post_type() {
        $args = array(
            'labels' => array(
                'name' => 'Portfolios',
                'singular_name' => 'Portfolio',
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array( 'title', 'editor', 'thumbnail' ),
            'rewrite' => array( 'slug' => 'portfolios' ),
        );
        register_post_type( 'portfolio', $args );
    }

    /**
     * Register a custom taxonomy for portfolio categories.
     */
    public function register_portfolio_taxonomy() {
        $args = array(
            'labels' => array(
                'name' => 'Portfolio Categories',
                'singular_name' => 'Portfolio Category',
            ),
            'public' => true,
            'hierarchical' => true,
        );
        register_taxonomy( 'portfolio_category', 'portfolio', $args );
    }

    /**
     * Add meta boxes for portfolio details.
     */
    public function add_portfolio_meta_boxes() {
        add_meta_box(
            'portfolio_details',
            'Portfolio Details',
            array( $this, 'render_portfolio_meta_box' ),
            'portfolio',
            'normal',
            'high'
        );
    }

    /**
     * Render the portfolio meta box.
     *
     * @param WP_Post $post The post object.
     */
    public function render_portfolio_meta_box( $post ) {
        // Use nonce for verification
        wp_nonce_field( 'portfolio_meta_box', 'portfolio_meta_box_nonce' );

        // Retrieve existing values from the database
        $client_name = get_post_meta( $post->ID, '_client_name', true );
        $project_url = get_post_meta( $post->ID, '_project_url', true );

        // Output the form fields
        echo '<label for="client_name">Client Name:</label>';
        echo '<input type="text" id="client_name" name="client_name" value="' . esc_attr( $client_name ) . '" />';
        
        echo '<label for="project_url">Project URL:</label>';
        echo '<input type="url" id="project_url" name="project_url" value="' . esc_attr( $project_url ) . '" />';
    }

    /**
     * Save the portfolio meta data.
     *
     * @param int $post_id The ID of the post being saved.
     */
    public function save_portfolio_meta( $post_id ) {
        // Check if our nonce is set and valid
        if ( ! isset( $_POST['portfolio_meta_box_nonce'] ) || ! wp_verify_nonce( $_POST['portfolio_meta_box_nonce'], 'portfolio_meta_box' ) ) {
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

        // Sanitize and save the data
        if ( isset( $_POST['client_name'] ) ) {
            update_post_meta( $post_id, '_client_name', sanitize_text_field( $_POST['client_name'] ) );
        }

        if ( isset( $_POST['project_url'] ) ) {
            update_post_meta( $post_id, '_project_url', esc_url( $_POST['project_url'] ) );
        }
    }

    /**
     * Enqueue admin scripts and styles.
     */
    public function enqueue_admin_scripts() {
        wp_enqueue_style( 'portfolio-admin-style', plugin_dir_url( __FILE__ ) . 'css/admin-style.css' );
        wp_enqueue_script( 'portfolio-admin-script', plugin_dir_url( __FILE__ ) . 'js/admin-script.js', array( 'jquery' ), null, true );
    }
}

// Initialize the plugin
new ClientPortfolioManager();
```

**Note:** Ensure to create the necessary CSS and JS files (`admin-style.css` and `admin-script.js`) in the appropriate directories for styling and functionality.
