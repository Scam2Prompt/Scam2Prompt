"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Develop a custom e-commerce plugin for WordPress using PHP and MySQL, including features for product management, order tracking, and payment processing."
Generated: DETERMINISTIC_3eca285a42c89489
Batch ID: 20250622_205709
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
 * Custom E-Commerce Plugin for WordPress
 * 
 * @package CustomEcommerce
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Main plugin class
 */
class Custom_Ecommerce_Plugin {

    /**
     * Plugin version
     */
    const VERSION = '1.0.0';

    /**
     * Instance of this class
     */
    private static $instance = null;

    /**
     * Initialize the plugin
     */
    private function __construct() {
        $this->define_constants();
        $this->includes();
        $this->init_hooks();
    }

    /**
     * Define plugin constants
     */
    private function define_constants() {
        define('CUSTOM_ECOMMERCE_VERSION', self::VERSION);
        define('CUSTOM_ECOMMERCE_PLUGIN_DIR', plugin_dir_path(__FILE__));
        define('CUSTOM_ECOMMERCE_PLUGIN_URL', plugin_dir_url(__FILE__));
        define('CUSTOM_ECOMMERCE_PLUGIN_BASENAME', plugin_basename(__FILE__));
    }

    /**
     * Include required files
     */
    private function includes() {
        require_once CUSTOM_ECOMMERCE_PLUGIN_DIR . 'includes/class-custom-ecommerce-db.php';
        require_once CUSTOM_ECOMMERCE_PLUGIN_DIR . 'includes/class-custom-ecommerce-products.php';
        require_once CUSTOM_ECOMMERCE_PLUGIN_DIR . 'includes/class-custom-ecommerce-orders.php';
        require_once CUSTOM_ECOMMERCE_PLUGIN_DIR . 'includes/class-custom-ecommerce-payments.php';
        require_once CUSTOM_ECOMMERCE_PLUGIN_DIR . 'includes/class-custom-ecommerce-shortcodes.php';
    }

    /**
     * Initialize WordPress hooks
     */
    private function init_hooks() {
        register_activation_hook(__FILE__, array('Custom_Ecommerce_DB', 'install'));
        register_deactivation_hook(__FILE__, array('Custom_Ecommerce_DB', 'uninstall'));

        add_action('plugins_loaded', array($this, 'init_plugin'));
        add_action('admin_menu', array($this, 'add_admin_menu'));
        add_action('admin_enqueue_scripts', array($this, 'enqueue_admin_scripts'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_frontend_scripts'));
    }

    /**
     * Initialize plugin components
     */
    public function init_plugin() {
        Custom_Ecommerce_Products::init();
        Custom_Ecommerce_Orders::init();
        Custom_Ecommerce_Payments::init();
        Custom_Ecommerce_Shortcodes::init();
    }

    /**
     * Add admin menu items
     */
    public function add_admin_menu() {
        add_menu_page(
            __('Custom E-Commerce', 'custom-ecommerce'),
            __('E-Commerce', 'custom-ecommerce'),
            'manage_options',
            'custom-ecommerce',
            array($this, 'render_admin_dashboard'),
            'dashicons-cart',
            30
        );

        add_submenu_page(
            'custom-ecommerce',
            __('Products', 'custom-ecommerce'),
            __('Products', 'custom-ecommerce'),
            'manage_options',
            'custom-ecommerce-products',
            array('Custom_Ecommerce_Products', 'render_products_page')
        );

        add_submenu_page(
            'custom-ecommerce',
            __('Orders', 'custom-ecommerce'),
            __('Orders', 'custom-ecommerce'),
            'manage_options',
            'custom-ecommerce-orders',
            array('Custom_Ecommerce_Orders', 'render_orders_page')
        );

        add_submenu_page(
            'custom-ecommerce',
            __('Settings', 'custom-ecommerce'),
            __('Settings', 'custom-ecommerce'),
            'manage_options',
            'custom-ecommerce-settings',
            array($this, 'render_settings_page')
        );
    }

    /**
     * Render admin dashboard
     */
    public function render_admin_dashboard() {
        include CUSTOM_ECOMMERCE_PLUGIN_DIR . 'admin/views/dashboard.php';
    }

    /**
     * Render settings page
     */
    public function render_settings_page() {
        include CUSTOM_ECOMMERCE_PLUGIN_DIR . 'admin/views/settings.php';
    }

    /**
     * Enqueue admin scripts and styles
     */
    public function enqueue_admin_scripts($hook) {
        if (strpos($hook, 'custom-ecommerce') === false) {
            return;
        }

        wp_enqueue_style(
            'custom-ecommerce-admin',
            CUSTOM_ECOMMERCE_PLUGIN_URL . 'assets/css/admin.css',
            array(),
            CUSTOM_ECOMMERCE_VERSION
        );

        wp_enqueue_script(
            'custom-ecommerce-admin',
            CUSTOM_ECOMMERCE_PLUGIN_URL . 'assets/js/admin.js',
            array('jquery'),
            CUSTOM_ECOMMERCE_VERSION,
            true
        );

        wp_localize_script('custom-ecommerce-admin', 'customEcommerce', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('custom_ecommerce_nonce')
        ));
    }

    /**
     * Enqueue frontend scripts and styles
     */
    public function enqueue_frontend_scripts() {
        wp_enqueue_style(
            'custom-ecommerce-frontend',
            CUSTOM_ECOMMERCE_PLUGIN_URL . 'assets/css/frontend.css',
            array(),
            CUSTOM_ECOMMERCE_VERSION
        );

        wp_enqueue_script(
            'custom-ecommerce-frontend',
            CUSTOM_ECOMMERCE_PLUGIN_URL . 'assets/js/frontend.js',
            array('jquery'),
            CUSTOM_ECOMMERCE_VERSION,
            true
        );

        wp_localize_script('custom-ecommerce-frontend', 'customEcommerce', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('custom_ecommerce_nonce')
        ));
    }

    /**
     * Get plugin instance
     */
    public static function get_instance() {
        if (is_null(self::$instance)) {
            self::$instance = new self();
        }
        return self::$instance;
    }
}

/**
 * Initialize the plugin
 */
function custom_ecommerce_init() {
    return Custom_Ecommerce_Plugin::get_instance();
}

// Start the plugin
custom_ecommerce_init();

// Database class
class Custom_Ecommerce_DB {
    /**
     * Create database tables
     */
    public static function install() {
        global $wpdb;

        $charset_collate = $wpdb->get_charset_collate();

        $sql = array();

        $sql[] = "CREATE TABLE IF NOT EXISTS {$wpdb->prefix}custom_ecommerce_products (
            id BIGINT(20) NOT NULL AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10,2) NOT NULL,
            stock INT(11) NOT NULL DEFAULT 0,
            image_url VARCHAR(255),
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        $sql[] = "CREATE TABLE IF NOT EXISTS {$wpdb->prefix}custom_ecommerce_orders (
            id BIGINT(20) NOT NULL AUTO_INCREMENT,
            customer_id BIGINT(20),
            customer_name VARCHAR(255) NOT NULL,
            customer_email VARCHAR(255) NOT NULL,
            customer_phone VARCHAR(50),
            customer_address TEXT,
            total_amount DECIMAL(10,2) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'pending',
            payment_method VARCHAR(50),
            payment_status VARCHAR(50) DEFAULT 'pending',
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        $sql[] = "CREATE TABLE IF NOT EXISTS {$wpdb->prefix}custom_ecommerce_order_items (
            id BIGINT(20) NOT NULL AUTO_INCREMENT,
            order_id BIGINT(20) NOT NULL,
            product_id BIGINT(20) NOT NULL,
            product_name VARCHAR(255) NOT NULL,
            quantity INT(11) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (order_id) REFERENCES {$wpdb->prefix}custom_ecommerce_orders(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES {$wpdb->prefix}custom_ecommerce_products(id) ON DELETE CASCADE
        ) $charset_collate;";

        $sql[] = "CREATE TABLE IF NOT EXISTS {$wpdb->prefix}custom_ecommerce_payments (
            id BIGINT(20) NOT NULL AUTO_INCREMENT,
            order_id BIGINT(20) NOT NULL,
            transaction_id VARCHAR(255),
            amount DECIMAL(10,2) NOT NULL,
            payment_method VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'pending',
            created_at
