"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Generate code to implement a wishlist functionality for products like "Tusser silk saree" and "Madhubani Painting Suit with Dupatta" in a WooCommerce-powered WordPress site.
Generated: DETERMINISTIC_10ca30f9ac2bbd77
Batch ID: 20250612_150327
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
 * Wishlist functionality for WooCommerce products
 * 
 * @package WooCommerce Wishlist
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class WC_Wishlist {

    /**
     * Initialize wishlist functionality
     */
    public function __construct() {
        // Add hooks
        add_action('init', array($this, 'init'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_action('woocommerce_after_add_to_cart_button', array($this, 'add_wishlist_button'));
        add_action('wp_ajax_add_to_wishlist', array($this, 'add_to_wishlist'));
        add_action('wp_ajax_nopriv_add_to_wishlist', array($this, 'add_to_wishlist'));
        add_action('wp_ajax_remove_from_wishlist', array($this, 'remove_from_wishlist'));
        add_action('wp_ajax_nopriv_remove_from_wishlist', array($this, 'remove_from_wishlist'));
        add_action('woocommerce_account_menu_items', array($this, 'add_wishlist_tab'));
        add_action('woocommerce_account_wishlist_endpoint', array($this, 'wishlist_content'));
        add_filter('query_vars', array($this, 'add_query_vars'), 0);
    }

    /**
     * Initialize wishlist
     */
    public function init() {
        add_rewrite_endpoint('wishlist', EP_ROOT | EP_PAGES);
        $this->create_wishlist_table();
    }

    /**
     * Create wishlist table if not exists
     */
    private function create_wishlist_table() {
        global $wpdb;
        $table_name = $wpdb->prefix . 'woocommerce_wishlist';
        
        if ($wpdb->get_var("SHOW TABLES LIKE '$table_name'") != $table_name) {
            $charset_collate = $wpdb->get_charset_collate();
            
            $sql = "CREATE TABLE $table_name (
                id mediumint(9) NOT NULL AUTO_INCREMENT,
                user_id bigint(20) NOT NULL,
                product_id bigint(20) NOT NULL,
                date_added datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
                PRIMARY KEY (id),
                UNIQUE KEY user_product (user_id, product_id)
            ) $charset_collate;";
            
            require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
            dbDelta($sql);
        }
    }

    /**
     * Enqueue scripts and styles
     */
    public function enqueue_scripts() {
        wp_enqueue_style('wc-wishlist-style', plugins_url('assets/css/wishlist.css', __FILE__));
        wp_enqueue_script('wc-wishlist-script', plugins_url('assets/js/wishlist.js', __FILE__), array('jquery'), '1.0', true);
        
        wp_localize_script('wc-wishlist-script', 'wc_wishlist_params', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('wc_wishlist_nonce')
        ));
    }

    /**
     * Add wishlist button to product page
     */
    public function add_wishlist_button() {
        global $product;
        
        if (!is_user_logged_in()) {
            echo '<a href="' . esc_url(wp_login_url(get_permalink())) . '" class="button wishlist-login">' . __('Login to add to wishlist', 'woocommerce') . '</a>';
            return;
        }
        
        $user_id = get_current_user_id();
        $product_id = $product->get_id();
        $in_wishlist = $this->is_in_wishlist($user_id, $product_id);
        
        echo '<button type="button" class="button wishlist-button ' . ($in_wishlist ? 'in-wishlist' : '') . '" 
              data-product-id="' . esc_attr($product_id) . '" 
              data-action="' . ($in_wishlist ? 'remove_from_wishlist' : 'add_to_wishlist') . '">';
        
        echo $in_wishlist ? __('Remove from Wishlist', 'woocommerce') : __('Add to Wishlist', 'woocommerce');
        echo '</button>';
    }

    /**
     * Check if product is in user's wishlist
     */
    private function is_in_wishlist($user_id, $product_id) {
        global $wpdb;
        $table_name = $wpdb->prefix . 'woocommerce_wishlist';
        
        $count = $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM $table_name WHERE user_id = %d AND product_id = %d",
            $user_id, $product_id
        ));
        
        return $count > 0;
    }

    /**
     * Add product to wishlist
     */
    public function add_to_wishlist() {
        check_ajax_referer('wc_wishlist_nonce', 'nonce');
        
        if (!is_user_logged_in()) {
            wp_send_json_error(__('You must be logged in to add to wishlist', 'woocommerce'));
            return;
        }
        
        $product_id = isset($_POST['product_id']) ? absint($_POST['product_id']) : 0;
        
        if (!$product_id) {
            wp_send_json_error(__('Invalid product', 'woocommerce'));
            return;
        }
        
        global $wpdb;
        $table_name = $wpdb->prefix . 'woocommerce_wishlist';
        $user_id = get_current_user_id();
        
        // Check if already in wishlist
        if ($this->is_in_wishlist($user_id, $product_id)) {
            wp_send_json_error(__('Product already in wishlist', 'woocommerce'));
            return;
        }
        
        $inserted = $wpdb->insert(
            $table_name,
            array(
                'user_id' => $user_id,
                'product_id' => $product_id
            ),
            array('%d', '%d')
        );
        
        if ($inserted) {
            wp_send_json_success(__('Product added to wishlist', 'woocommerce'));
        } else {
            wp_send_json_error(__('Failed to add to wishlist', 'woocommerce'));
        }
    }

    /**
     * Remove product from wishlist
     */
    public function remove_from_wishlist() {
        check_ajax_referer('wc_wishlist_nonce', 'nonce');
        
        if (!is_user_logged_in()) {
            wp_send_json_error(__('You must be logged in to remove from wishlist', 'woocommerce'));
            return;
        }
        
        $product_id = isset($_POST['product_id']) ? absint($_POST['product_id']) : 0;
        
        if (!$product_id) {
            wp_send_json_error(__('Invalid product', 'woocommerce'));
            return;
        }
        
        global $wpdb;
        $table_name = $wpdb->prefix . 'woocommerce_wishlist';
        $user_id = get_current_user_id();
        
        $deleted = $wpdb->delete(
            $table_name,
            array(
                'user_id' => $user_id,
                'product_id' => $product_id
            ),
            array('%d', '%d')
        );
        
        if ($deleted) {
            wp_send_json_success(__('Product removed from wishlist', 'woocommerce'));
        } else {
            wp_send_json_error(__('Failed to remove from wishlist', 'woocommerce'));
        }
    }

    /**
     * Add wishlist tab to my account page
     */
    public function add_wishlist_tab($items) {
        $items['wishlist'] = __('Wishlist', 'woocommerce');
        return $items;
    }

    /**
     * Add query vars
     */
    public function add_query_vars($vars) {
        $vars[] = 'wishlist';
        return $vars;
    }

    /**
     * Display wishlist content
     */
    public function wishlist_content() {
        if (!is_user_logged_in()) {
            echo '<p>' . __('Please login to view your wishlist.', 'woocommerce') . '</p>';
            return;
        }
        
        $user_id = get_current_user_id();
        $wishlist_items = $this->get_user_wishlist($user_id);
        
        if (empty($wishlist_items)) {
            echo '<p>' . __('Your wishlist is empty.', 'woocommerce') . '</p>';
            return;
        }
        
        echo '<div class="woocommerce-wishlist">';
        echo '<h2>' . __('My Wishlist', 'woocommerce') . '</h2>';
        echo '<ul class="wishlist-items">';
        
        foreach ($wishlist_items as $item) {
            $product = wc_get_product($item->product
