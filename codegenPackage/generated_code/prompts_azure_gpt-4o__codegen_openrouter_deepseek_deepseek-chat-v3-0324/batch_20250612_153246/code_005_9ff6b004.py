"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: Create a WordPress plugin for displaying multi-sized picture frame sets, similar to the product listings on Gvika, with options for adding items to the cart.
Generated: DETERMINISTIC_9ff6b004549625d7
Batch ID: 20250612_153246
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

# Generated Code:
# ===============

```php
<?php
/**
 * Plugin Name: Picture Frame Sets
 * Description: Display multi-sized picture frame sets with cart functionality.
 * Version: 1.0
 * Author: Your Name
 * Author URI: https://example.com
 * License: GPL2
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Picture_Frame_Sets {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('init', array($this, 'register_frame_sets_post_type'));
        add_action('add_meta_boxes', array($this, 'add_frame_sets_meta_boxes'));
        add_action('save_post', array($this, 'save_frame_sets_meta'));
        add_shortcode('frame_sets', array($this, 'frame_sets_shortcode'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_action('wp_ajax_add_frame_to_cart', array($this, 'add_frame_to_cart'));
        add_action('wp_ajax_nopriv_add_frame_to_cart', array($this, 'add_frame_to_cart'));
    }

    /**
     * Register custom post type for frame sets
     */
    public function register_frame_sets_post_type() {
        $labels = array(
            'name'               => 'Frame Sets',
            'singular_name'      => 'Frame Set',
            'menu_name'          => 'Frame Sets',
            'name_admin_bar'     => 'Frame Set',
            'add_new'            => 'Add New',
            'add_new_item'       => 'Add New Frame Set',
            'new_item'           => 'New Frame Set',
            'edit_item'          => 'Edit Frame Set',
            'view_item'          => 'View Frame Set',
            'all_items'          => 'All Frame Sets',
            'search_items'       => 'Search Frame Sets',
            'parent_item_colon'  => 'Parent Frame Sets:',
            'not_found'          => 'No frame sets found.',
            'not_found_in_trash' => 'No frame sets found in Trash.'
        );

        $args = array(
            'labels'             => $labels,
            'public'             => true,
            'publicly_queryable' => true,
            'show_ui'            => true,
            'show_in_menu'       => true,
            'query_var'          => true,
            'rewrite'            => array('slug' => 'frame-sets'),
            'capability_type'    => 'post',
            'has_archive'        => true,
            'hierarchical'       => false,
            'menu_position'      => null,
            'supports'           => array('title', 'editor', 'thumbnail'),
            'menu_icon'          => 'dashicons-format-gallery'
        );

        register_post_type('frame_sets', $args);
    }

    /**
     * Add meta boxes for frame sets
     */
    public function add_frame_sets_meta_boxes() {
        add_meta_box(
            'frame_sets_meta',
            'Frame Set Details',
            array($this, 'render_frame_sets_meta_box'),
            'frame_sets',
            'normal',
            'high'
        );
    }

    /**
     * Render meta box content
     */
    public function render_frame_sets_meta_box($post) {
        wp_nonce_field('frame_sets_meta_box', 'frame_sets_meta_box_nonce');
        
        $frame_sizes = get_post_meta($post->ID, '_frame_sizes', true);
        $frame_prices = get_post_meta($post->ID, '_frame_prices', true);
        $frame_skus = get_post_meta($post->ID, '_frame_skus', true);
        
        ?>
        <div class="frame-sets-meta">
            <p>
                <label for="frame_sizes">Frame Sizes (comma separated):</label>
                <input type="text" id="frame_sizes" name="frame_sizes" value="<?php echo esc_attr($frame_sizes); ?>" class="widefat">
            </p>
            <p>
                <label for="frame_prices">Frame Prices (comma separated):</label>
                <input type="text" id="frame_prices" name="frame_prices" value="<?php echo esc_attr($frame_prices); ?>" class="widefat">
            </p>
            <p>
                <label for="frame_skus">Frame SKUs (comma separated):</label>
                <input type="text" id="frame_skus" name="frame_skus" value="<?php echo esc_attr($frame_skus); ?>" class="widefat">
            </p>
        </div>
        <?php
    }

    /**
     * Save meta box data
     */
    public function save_frame_sets_meta($post_id) {
        if (!isset($_POST['frame_sets_meta_box_nonce']) || 
            !wp_verify_nonce($_POST['frame_sets_meta_box_nonce'], 'frame_sets_meta_box')) {
            return;
        }

        if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
            return;
        }

        if (!current_user_can('edit_post', $post_id)) {
            return;
        }

        if (isset($_POST['frame_sizes'])) {
            update_post_meta($post_id, '_frame_sizes', sanitize_text_field($_POST['frame_sizes']));
        }

        if (isset($_POST['frame_prices'])) {
            update_post_meta($post_id, '_frame_prices', sanitize_text_field($_POST['frame_prices']));
        }

        if (isset($_POST['frame_skus'])) {
            update_post_meta($post_id, '_frame_skus', sanitize_text_field($_POST['frame_skus']));
        }
    }

    /**
     * Enqueue scripts and styles
     */
    public function enqueue_scripts() {
        wp_enqueue_style('frame-sets-style', plugins_url('css/style.css', __FILE__));
        wp_enqueue_script('frame-sets-script', plugins_url('js/script.js', __FILE__), array('jquery'), '1.0', true);
        
        wp_localize_script('frame-sets-script', 'frame_sets_ajax', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('frame_sets_nonce')
        ));
    }

    /**
     * Shortcode to display frame sets
     */
    public function frame_sets_shortcode($atts) {
        $atts = shortcode_atts(array(
            'category' => '',
            'limit' => -1
        ), $atts);

        $args = array(
            'post_type' => 'frame_sets',
            'posts_per_page' => $atts['limit'],
            'post_status' => 'publish'
        );

        if (!empty($atts['category'])) {
            $args['tax_query'] = array(
                array(
                    'taxonomy' => 'category',
                    'field' => 'slug',
                    'terms' => $atts['category']
                )
            );
        }

        $query = new WP_Query($args);
        ob_start();

        if ($query->have_posts()) {
            echo '<div class="frame-sets-container">';
            while ($query->have_posts()) {
                $query->the_post();
                $this->render_frame_set(get_the_ID());
            }
            echo '</div>';
            wp_reset_postdata();
        } else {
            echo '<p>No frame sets found.</p>';
        }

        return ob_get_clean();
    }

    /**
     * Render individual frame set
     */
    private function render_frame_set($post_id) {
        $frame_sizes = explode(',', get_post_meta($post_id, '_frame_sizes', true));
        $frame_prices = explode(',', get_post_meta($post_id, '_frame_prices', true));
        $frame_skus = explode(',', get_post_meta($post_id, '_frame_skus', true));
        
        if (count($frame_sizes) !== count($frame_prices) || count($frame_sizes) !== count($frame_skus)) {
            return '<p>Error: Mismatch in frame set data.</p>';
        }
        
        ?>
        <div class="frame-set" data-post-id="<?php echo esc_attr($post_id); ?>">
            <div class="frame-set-image">
                <?php if (has_post_thumbnail($post_id)): ?>
                    <?php echo get_the_post_thumbnail($post_id, 'medium'); ?>
                <?php endif; ?>
            </div>
            <div class="frame-set-details">
                <h3><?php echo get_the_title($post_id); ?></h3>
                <div class="frame-set-sizes">
                    <?php for ($i = 0; $i < count($frame_sizes); $i++): ?>
                        <div class="frame-size-option">
