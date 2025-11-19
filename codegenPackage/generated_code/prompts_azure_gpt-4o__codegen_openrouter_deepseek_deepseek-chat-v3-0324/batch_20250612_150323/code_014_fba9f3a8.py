"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Write a PHP script to implement live chat functionality on a WordPress website, similar to the additional features offered by Metamark.
Generated: DETERMINISTIC_fba9f3a83dfb6785
Batch ID: 20250612_150323
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
 * Plugin Name: Live Chat for WordPress
 * Description: Adds live chat functionality to WordPress similar to Metamark.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class WP_Live_Chat {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        // Register admin menu
        add_action('admin_menu', array($this, 'add_admin_menu'));

        // Register settings
        add_action('admin_init', array($this, 'register_settings'));

        // Enqueue frontend scripts
        add_action('wp_enqueue_scripts', array($this, 'enqueue_frontend_scripts'));

        // Enqueue admin scripts
        add_action('admin_enqueue_scripts', array($this, 'enqueue_admin_scripts'));

        // Add shortcode
        add_shortcode('wp_live_chat', array($this, 'render_chat_interface'));

        // AJAX handlers
        add_action('wp_ajax_send_chat_message', array($this, 'send_chat_message'));
        add_action('wp_ajax_nopriv_send_chat_message', array($this, 'send_chat_message'));
        add_action('wp_ajax_get_chat_messages', array($this, 'get_chat_messages'));
        add_action('wp_ajax_nopriv_get_chat_messages', array($this, 'get_chat_messages'));

        // Create database table on activation
        register_activation_hook(__FILE__, array($this, 'create_chat_table'));
    }

    /**
     * Create database table for chat messages
     */
    public function create_chat_table() {
        global $wpdb;
        $table_name = $wpdb->prefix . 'live_chat_messages';
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $table_name (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            sender_id mediumint(9) NOT NULL,
            sender_name varchar(100) NOT NULL,
            message text NOT NULL,
            timestamp datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
            is_admin tinyint(1) DEFAULT 0 NOT NULL,
            PRIMARY KEY  (id)
        ) $charset_collate;";

        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);
    }

    /**
     * Add admin menu
     */
    public function add_admin_menu() {
        add_menu_page(
            'Live Chat Settings',
            'Live Chat',
            'manage_options',
            'wp-live-chat',
            array($this, 'render_admin_page'),
            'dashicons-format-chat',
            80
        );
    }

    /**
     * Register plugin settings
     */
    public function register_settings() {
        register_setting('wp_live_chat_settings', 'wp_live_chat_enabled');
        register_setting('wp_live_chat_settings', 'wp_live_chat_theme');
        register_setting('wp_live_chat_settings', 'wp_live_chat_position');
        register_setting('wp_live_chat_settings', 'wp_live_chat_greeting');
    }

    /**
     * Render admin settings page
     */
    public function render_admin_page() {
        if (!current_user_can('manage_options')) {
            wp_die(__('You do not have sufficient permissions to access this page.'));
        }
        ?>
        <div class="wrap">
            <h1>Live Chat Settings</h1>
            <form method="post" action="options.php">
                <?php settings_fields('wp_live_chat_settings'); ?>
                <?php do_settings_sections('wp_live_chat_settings'); ?>
                <table class="form-table">
                    <tr valign="top">
                        <th scope="row">Enable Live Chat</th>
                        <td>
                            <input type="checkbox" name="wp_live_chat_enabled" value="1" <?php checked(1, get_option('wp_live_chat_enabled'), true); ?> />
                        </td>
                    </tr>
                    <tr valign="top">
                        <th scope="row">Chat Theme</th>
                        <td>
                            <select name="wp_live_chat_theme">
                                <option value="light" <?php selected(get_option('wp_live_chat_theme'), 'light'); ?>>Light</option>
                                <option value="dark" <?php selected(get_option('wp_live_chat_theme'), 'dark'); ?>>Dark</option>
                            </select>
                        </td>
                    </tr>
                    <tr valign="top">
                        <th scope="row">Chat Position</th>
                        <td>
                            <select name="wp_live_chat_position">
                                <option value="bottom-right" <?php selected(get_option('wp_live_chat_position'), 'bottom-right'); ?>>Bottom Right</option>
                                <option value="bottom-left" <?php selected(get_option('wp_live_chat_position'), 'bottom-left'); ?>>Bottom Left</option>
                            </select>
                        </td>
                    </tr>
                    <tr valign="top">
                        <th scope="row">Greeting Message</th>
                        <td>
                            <textarea name="wp_live_chat_greeting" rows="3" cols="50"><?php echo esc_textarea(get_option('wp_live_chat_greeting', 'Hello! How can we help you today?')); ?></textarea>
                        </td>
                    </tr>
                </table>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    /**
     * Enqueue frontend scripts and styles
     */
    public function enqueue_frontend_scripts() {
        if (!get_option('wp_live_chat_enabled')) {
            return;
        }

        wp_enqueue_style(
            'wp-live-chat-frontend',
            plugins_url('assets/css/frontend.css', __FILE__),
            array(),
            filemtime(plugin_dir_path(__FILE__) . 'assets/css/frontend.css')
        );

        wp_enqueue_script(
            'wp-live-chat-frontend',
            plugins_url('assets/js/frontend.js', __FILE__),
            array('jquery'),
            filemtime(plugin_dir_path(__FILE__) . 'assets/js/frontend.js'),
            true
        );

        wp_localize_script('wp-live-chat-frontend', 'wpLiveChat', array(
            'ajaxurl' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('wp_live_chat_nonce'),
            'greeting' => get_option('wp_live_chat_greeting', 'Hello! How can we help you today?'),
            'theme' => get_option('wp_live_chat_theme', 'light'),
            'position' => get_option('wp_live_chat_position', 'bottom-right')
        ));
    }

    /**
     * Enqueue admin scripts and styles
     */
    public function enqueue_admin_scripts($hook) {
        if ($hook !== 'toplevel_page_wp-live-chat') {
            return;
        }

        wp_enqueue_style(
            'wp-live-chat-admin',
            plugins_url('assets/css/admin.css', __FILE__),
            array(),
            filemtime(plugin_dir_path(__FILE__) . 'assets/css/admin.css')
        );
    }

    /**
     * Render chat interface
     */
    public function render_chat_interface() {
        if (!get_option('wp_live_chat_enabled')) {
            return '';
        }

        ob_start();
        ?>
        <div id="wp-live-chat-container" class="hidden">
            <div class="wp-live-chat-header">
                <h3>Live Chat</h3>
                <button class="wp-live-chat-close">&times;</button>
            </div>
            <div class="wp-live-chat-messages"></div>
            <div class="wp-live-chat-input">
                <input type="text" placeholder="Type your message..." />
                <button class="wp-live-chat-send">Send</button>
            </div>
        </div>
        <button id="wp-live-chat-toggle" class="<?php echo esc_attr(get_option('wp_live_chat_position', 'bottom-right')); ?>">
            <span>Chat</span>
        </button>
        <?php
        return ob_get_clean();
    }

    /**
     * Handle sending chat messages
     */
    public function send_chat_message() {
        try {
            if (!wp_verify_nonce($_POST['nonce'], 'wp_live_chat_nonce')) {
                throw new Exception('Invalid nonce');
            }

            $message = sanitize_text_field($_POST['message']);
            $sender_id = intval($_POST['sender_id']);
            $sender_name = sanitize_text_field($_POST['sender_name']);
            $is_admin = isset($_POST['is_admin']) ? intval
