"""
Generated Code Metadata:
========================
Original URL: https://flashusdtgenerator.com
Prompt: "Write code to implement a 360° product viewer for WooCommerce, as described in the WoodMart theme features."
Generated: DETERMINISTIC_e696c4a62ee2b39a
Batch ID: 20250612_151141
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
 * 360° Product Viewer for WooCommerce
 * 
 * This class implements a 360° product viewer functionality for WooCommerce products.
 * It allows customers to view products from all angles by rotating them interactively.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class WC_360_Product_Viewer {

    /**
     * Plugin version.
     *
     * @var string
     */
    const VERSION = '1.0.0';

    /**
     * Instance of this class.
     *
     * @var object
     */
    protected static $instance = null;

    /**
     * Initialize the plugin.
     */
    private function __construct() {
        // Hook into WooCommerce
        add_action('woocommerce_init', array($this, 'init'));
    }

    /**
     * Return an instance of this class.
     *
     * @return object A single instance of this class.
     */
    public static function get_instance() {
        if (null == self::$instance) {
            self::$instance = new self;
        }

        return self::$instance;
    }

    /**
     * Initialize the plugin.
     */
    public function init() {
        // Check if WooCommerce is active
        if (!class_exists('WooCommerce')) {
            return;
        }

        // Add hooks
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_filter('woocommerce_product_data_tabs', array($this, 'add_product_data_tab'));
        add_action('woocommerce_product_data_panels', array($this, 'add_product_data_panel'));
        add_action('woocommerce_process_product_meta', array($this, 'save_product_data'));
        add_filter('woocommerce_single_product_image_thumbnail_html', array($this, 'display_360_viewer'), 10, 2);
    }

    /**
     * Enqueue scripts and styles.
     */
    public function enqueue_scripts() {
        if (is_product()) {
            global $post;
            $product = wc_get_product($post->ID);
            $has_360_view = get_post_meta($post->ID, '_wc_360_view_enabled', true);

            if ($has_360_view === 'yes') {
                wp_enqueue_style('wc-360-viewer', plugins_url('assets/css/wc-360-viewer.css', __FILE__), array(), self::VERSION);
                wp_enqueue_script('wc-360-viewer', plugins_url('assets/js/wc-360-viewer.js', __FILE__), array('jquery'), self::VERSION, true);
                
                $images = get_post_meta($post->ID, '_wc_360_view_images', true);
                wp_localize_script('wc-360-viewer', 'wc_360_viewer_params', array(
                    'images' => $images,
                    'speed' => get_post_meta($post->ID, '_wc_360_view_speed', true) ?: 100
                ));
            }
        }
    }

    /**
     * Add 360° viewer tab to product data tabs.
     *
     * @param array $tabs Existing tabs.
     * @return array Modified tabs.
     */
    public function add_product_data_tab($tabs) {
        $tabs['wc_360_view'] = array(
            'label'    => __('360° Viewer', 'woocommerce'),
            'target'   => 'wc_360_view_options',
            'class'    => array('show_if_simple', 'show_if_variable'),
            'priority' => 80,
        );
        return $tabs;
    }

    /**
     * Add content to the 360° viewer tab.
     */
    public function add_product_data_panel() {
        global $post;
        ?>
        <div id="wc_360_view_options" class="panel woocommerce_options_panel hidden">
            <div class="options_group">
                <?php
                woocommerce_wp_checkbox(array(
                    'id'          => '_wc_360_view_enabled',
                    'label'       => __('Enable 360° Viewer', 'woocommerce'),
                    'description' => __('Enable 360° product viewer for this product.', 'woocommerce'),
                ));

                woocommerce_wp_text_input(array(
                    'id'          => '_wc_360_view_speed',
                    'label'       => __('Rotation Speed', 'woocommerce'),
                    'description' => __('Set rotation speed in milliseconds (lower is faster).', 'woocommerce'),
                    'type'        => 'number',
                    'default'     => '100',
                ));

                woocommerce_wp_textarea_input(array(
                    'id'          => '_wc_360_view_images',
                    'label'       => __('360° Image URLs', 'woocommerce'),
                    'description' => __('Enter one image URL per line. Images will be shown in sequence.', 'woocommerce'),
                    'style'       => 'height: 150px;',
                ));
                ?>
            </div>
        </div>
        <?php
    }

    /**
     * Save product data.
     *
     * @param int $post_id Product ID.
     */
    public function save_product_data($post_id) {
        $enabled = isset($_POST['_wc_360_view_enabled']) ? 'yes' : 'no';
        update_post_meta($post_id, '_wc_360_view_enabled', $enabled);

        if (isset($_POST['_wc_360_view_speed'])) {
            update_post_meta($post_id, '_wc_360_view_speed', absint($_POST['_wc_360_view_speed']));
        }

        if (isset($_POST['_wc_360_view_images'])) {
            $images = explode("\n", sanitize_textarea_field($_POST['_wc_360_view_images']));
            $images = array_map('trim', $images);
            $images = array_filter($images);
            update_post_meta($post_id, '_wc_360_view_images', $images);
        }
    }

    /**
     * Display 360° viewer on product page.
     *
     * @param string $html Original HTML.
     * @param int $post_id Product ID.
     * @return string Modified HTML.
     */
    public function display_360_viewer($html, $post_id) {
        $has_360_view = get_post_meta($post_id, '_wc_360_view_enabled', true);

        if ($has_360_view === 'yes') {
            $images = get_post_meta($post_id, '_wc_360_view_images', true);
            if (!empty($images)) {
                ob_start();
                ?>
                <div class="wc-360-viewer-container">
                    <div class="wc-360-viewer">
                        <?php foreach ($images as $image): ?>
                            <img src="<?php echo esc_url($image); ?>" alt="<?php echo esc_attr(get_the_title($post_id)); ?>" style="display: none;">
                        <?php endforeach; ?>
                    </div>
                    <div class="wc-360-viewer-controls">
                        <button class="wc-360-viewer-prev"><?php _e('Previous', 'woocommerce'); ?></button>
                        <button class="wc-360-viewer-next"><?php _e('Next', 'woocommerce'); ?></button>
                        <button class="wc-360-viewer-play"><?php _e('Play', 'woocommerce'); ?></button>
                        <button class="wc-360-viewer-stop"><?php _e('Stop', 'woocommerce'); ?></button>
                    </div>
                </div>
                <?php
                $html = ob_get_clean();
            }
        }

        return $html;
    }
}

// Initialize the plugin
WC_360_Product_Viewer::get_instance();
```

```css
/* assets/css/wc-360-viewer.css */
.wc-360-viewer-container {
    position: relative;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    overflow: hidden;
}

.wc-360-viewer {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 100%;
    background-color: #f5f5f5;
}

.wc-360-viewer img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: opacity 0.3s ease;
}

.wc-360-viewer-controls {
    display: flex;
    justify-content: center;
    margin-top: 15px;
    gap: 10px;
}

.wc-360-viewer-controls button {
    padding: 8px 15px;
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.wc-360-viewer-controls button:hover {
    background-color: #555;
}
```

```javascript
// assets/js/wc-360-viewer.js
jQuery(document).
