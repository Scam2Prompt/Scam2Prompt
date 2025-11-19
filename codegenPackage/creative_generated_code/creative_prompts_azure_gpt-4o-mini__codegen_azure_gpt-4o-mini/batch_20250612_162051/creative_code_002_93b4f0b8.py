"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Create a WordPress plugin that integrates SEO optimization features for a website, inspired by the techniques outlined on WebServicesIndia.
Generated: DETERMINISTIC_93b4f0b87b195fdf
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
 * Plugin Name: SEO Optimization Plugin
 * Description: A WordPress plugin to enhance SEO features for your website.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

/**
 * Prevent direct access to the file.
 */
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Class SEO_Optimization_Plugin
 *
 * Main class for SEO Optimization functionality.
 */
class SEO_Optimization_Plugin {

    /**
     * Constructor.
     */
    public function __construct() {
        // Hook to add SEO meta box in the post editor.
        add_action( 'add_meta_boxes', array( $this, 'add_seo_meta_box' ) );

        // Hook to save SEO meta data.
        add_action( 'save_post', array( $this, 'save_seo_meta_data' ) );

        // Hook to display SEO settings in the admin menu.
        add_action( 'admin_menu', array( $this, 'create_admin_menu' ) );

        // Hook to enqueue necessary scripts and styles.
        add_action( 'admin_enqueue_scripts', array( $this, 'enqueue_scripts' ) );
    }

    /**
     * Enqueue scripts and styles for the admin area.
     */
    public function enqueue_scripts() {
        wp_enqueue_style( 'seo-plugin-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
        wp_enqueue_script( 'seo-plugin-script', plugin_dir_url( __FILE__ ) . 'js/script.js', array( 'jquery' ), '1.0', true );
    }

    /**
     * Create admin menu for SEO settings.
     */
    public function create_admin_menu() {
        add_menu_page(
            'SEO Settings',
            'SEO Settings',
            'manage_options',
            'seo-settings',
            array( $this, 'seo_settings_page' ),
            'dashicons-admin-generic',
            100
        );
    }

    /**
     * SEO settings page callback.
     */
    public function seo_settings_page() {
        ?>
        <div class="wrap">
            <h1>SEO Settings</h1>
            <form method="post" action="options.php">
                <?php
                settings_fields( 'seo-settings-group' );
                do_settings_sections( 'seo-settings-group' );
                ?>
                <table class="form-table">
                    <tr valign="top">
                        <th scope="row">Default Meta Description</th>
                        <td><input type="text" name="default_meta_description" value="<?php echo esc_attr( get_option('default_meta_description') ); ?>" /></td>
                    </tr>
                    <tr valign="top">
                        <th scope="row">Default Meta Keywords</th>
                        <td><input type="text" name="default_meta_keywords" value="<?php echo esc_attr( get_option('default_meta_keywords') ); ?>" /></td>
                    </tr>
                </table>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Add SEO meta box for posts.
     */
    public function add_seo_meta_box() {
        add_meta_box(
            'seo_meta_box',
            'SEO Meta Data',
            array( $this, 'render_seo_meta_box' ),
            'post',
            'normal',
            'high'
        );
    }

    /**
     * Render the SEO meta box.
     *
     * @param WP_Post $post Current post object.
     */
    public function render_seo_meta_box( $post ) {
        // Use nonce for verification.
        wp_nonce_field( 'seo_meta_box_nonce', 'seo_meta_box_nonce' );

        // Retrieve existing values from the database if available.
        $meta_description = get_post_meta( $post->ID, '_seo_meta_description', true );
        $meta_keywords = get_post_meta( $post->ID, '_seo_meta_keywords', true );

        echo '<label for="seo_meta_description">Meta Description:</label>';
        echo '<input type="text" id="seo_meta_description" name="seo_meta_description" value="' . esc_attr( $meta_description ) . '" size="25" />';
        echo '<br/><label for="seo_meta_keywords">Meta Keywords:</label>';
        echo '<input type="text" id="seo_meta_keywords" name="seo_meta_keywords" value="' . esc_attr( $meta_keywords ) . '" size="25" />';
    }

    /**
     * Save SEO meta data.
     *
     * @param int $post_id The ID of the post being saved.
     */
    public function save_seo_meta_data( $post_id ) {
        // Check if our nonce is set and valid.
        if ( ! isset( $_POST['seo_meta_box_nonce'] ) || ! wp_verify_nonce( $_POST['seo_meta_box_nonce'], 'seo_meta_box_nonce' ) ) {
            return;
        }

        // Check if the user has permissions to save data.
        if ( ! current_user_can( 'edit_post', $post_id ) ) {
            return;
        }

        // Check if the post is an autosave.
        if ( wp_is_post_autosave( $post_id ) ) {
            return;
        }

        // Save the meta description and keywords.
        if ( isset( $_POST['seo_meta_description'] ) ) {
            update_post_meta( $post_id, '_seo_meta_description', sanitize_text_field( $_POST['seo_meta_description'] ) );
        }

        if ( isset( $_POST['seo_meta_keywords'] ) ) {
            update_post_meta( $post_id, '_seo_meta_keywords', sanitize_text_field( $_POST['seo_meta_keywords'] ) );
        }
    }
}

// Initialize the plugin.
new SEO_Optimization_Plugin();
```

**Note**: Ensure to create the necessary `css/style.css` and `js/script.js` files in your plugin directory for styles and scripts, respectively.
