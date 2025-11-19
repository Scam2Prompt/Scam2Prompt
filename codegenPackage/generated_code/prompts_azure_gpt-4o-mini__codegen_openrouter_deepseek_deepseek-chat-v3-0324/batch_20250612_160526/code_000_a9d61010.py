"""
Generated Code Metadata:
========================
Original URL: https://zeccashclaim.finance.blog
Prompt: Generate a code snippet for a WordPress plugin that allows users to manage cookie consent on their site.
Generated: DETERMINISTIC_a9d61010939dcaf7
Batch ID: 20250612_160526
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
 * Plugin Name: Cookie Consent Manager
 * Description: A simple plugin to manage cookie consent on your WordPress site.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 * Text Domain: cookie-consent-manager
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

class Cookie_Consent_Manager {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        // Register admin menu
        add_action('admin_menu', array($this, 'add_admin_menu'));
        
        // Register settings
        add_action('admin_init', array($this, 'register_settings'));
        
        // Enqueue frontend scripts and styles
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        
        // Add cookie consent banner to footer
        add_action('wp_footer', array($this, 'display_cookie_consent_banner'));
        
        // Handle AJAX consent
        add_action('wp_ajax_set_cookie_consent', array($this, 'handle_cookie_consent'));
        add_action('wp_ajax_nopriv_set_cookie_consent', array($this, 'handle_cookie_consent'));
    }

    /**
     * Add admin menu item
     */
    public function add_admin_menu() {
        add_options_page(
            __('Cookie Consent Settings', 'cookie-consent-manager'),
            __('Cookie Consent', 'cookie-consent-manager'),
            'manage_options',
            'cookie-consent-settings',
            array($this, 'render_settings_page')
        );
    }

    /**
     * Register plugin settings
     */
    public function register_settings() {
        register_setting('cookie_consent_settings', 'cookie_consent_options');

        add_settings_section(
            'cookie_consent_main',
            __('Cookie Consent Settings', 'cookie-consent-manager'),
            array($this, 'render_settings_section'),
            'cookie-consent-settings'
        );

        add_settings_field(
            'banner_text',
            __('Banner Text', 'cookie-consent-manager'),
            array($this, 'render_banner_text_field'),
            'cookie-consent-settings',
            'cookie_consent_main'
        );

        add_settings_field(
            'accept_button_text',
            __('Accept Button Text', 'cookie-consent-manager'),
            array($this, 'render_accept_button_text_field'),
            'cookie-consent-settings',
            'cookie_consent_main'
        );

        add_settings_field(
            'reject_button_text',
            __('Reject Button Text', 'cookie-consent-manager'),
            array($this, 'render_reject_button_text_field'),
            'cookie-consent-settings',
            'cookie_consent_main'
        );

        add_settings_field(
            'cookie_expiry',
            __('Cookie Expiry (days)', 'cookie-consent-manager'),
            array($this, 'render_cookie_expiry_field'),
            'cookie-consent-settings',
            'cookie_consent_main'
        );
    }

    /**
     * Render settings section
     */
    public function render_settings_section() {
        echo '<p>' . __('Configure your cookie consent settings below.', 'cookie-consent-manager') . '</p>';
    }

    /**
     * Render banner text field
     */
    public function render_banner_text_field() {
        $options = get_option('cookie_consent_options');
        echo '<textarea id="banner_text" name="cookie_consent_options[banner_text]" rows="3" cols="50">' . esc_textarea($options['banner_text'] ?? '') . '</textarea>';
        echo '<p class="description">' . __('The text displayed in the cookie consent banner.', 'cookie-consent-manager') . '</p>';
    }

    /**
     * Render accept button text field
     */
    public function render_accept_button_text_field() {
        $options = get_option('cookie_consent_options');
        echo '<input type="text" id="accept_button_text" name="cookie_consent_options[accept_button_text]" value="' . esc_attr($options['accept_button_text'] ?? '') . '" />';
        echo '<p class="description">' . __('The text for the accept button.', 'cookie-consent-manager') . '</p>';
    }

    /**
     * Render reject button text field
     */
    public function render_reject_button_text_field() {
        $options = get_option('cookie_consent_options');
        echo '<input type="text" id="reject_button_text" name="cookie_consent_options[reject_button_text]" value="' . esc_attr($options['reject_button_text'] ?? '') . '" />';
        echo '<p class="description">' . __('The text for the reject button.', 'cookie-consent-manager') . '</p>';
    }

    /**
     * Render cookie expiry field
     */
    public function render_cookie_expiry_field() {
        $options = get_option('cookie_consent_options');
        echo '<input type="number" id="cookie_expiry" name="cookie_consent_options[cookie_expiry]" value="' . esc_attr($options['cookie_expiry'] ?? 30) . '" min="1" />';
        echo '<p class="description">' . __('Number of days before the cookie expires.', 'cookie-consent-manager') . '</p>';
    }

    /**
     * Render settings page
     */
    public function render_settings_page() {
        if (!current_user_can('manage_options')) {
            return;
        }
        ?>
        <div class="wrap">
            <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
            <form action="options.php" method="post">
                <?php
                settings_fields('cookie_consent_settings');
                do_settings_sections('cookie-consent-settings');
                submit_button(__('Save Settings', 'cookie-consent-manager'));
                ?>
            </form>
        </div>
        <?php
    }

    /**
     * Enqueue frontend scripts and styles
     */
    public function enqueue_scripts() {
        wp_enqueue_style(
            'cookie-consent-style',
            plugin_dir_url(__FILE__) . 'assets/css/style.css',
            array(),
            '1.0.0'
        );

        wp_enqueue_script(
            'cookie-consent-script',
            plugin_dir_url(__FILE__) . 'assets/js/script.js',
            array('jquery'),
            '1.0.0',
            true
        );

        wp_localize_script(
            'cookie-consent-script',
            'cookieConsentData',
            array(
                'ajaxurl' => admin_url('admin-ajax.php'),
                'nonce' => wp_create_nonce('cookie_consent_nonce')
            )
        );
    }

    /**
     * Display cookie consent banner
     */
    public function display_cookie_consent_banner() {
        if (isset($_COOKIE['cookie_consent'])) {
            return;
        }

        $options = get_option('cookie_consent_options');
        ?>
        <div id="cookie-consent-banner" class="cookie-consent-banner" style="display: none;">
            <div class="cookie-consent-content">
                <p><?php echo esc_html($options['banner_text'] ?? __('We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.', 'cookie-consent-manager')); ?></p>
                <div class="cookie-consent-buttons">
                    <button id="cookie-consent-accept" class="cookie-consent-button">
                        <?php echo esc_html($options['accept_button_text'] ?? __('Accept', 'cookie-consent-manager')); ?>
                    </button>
                    <button id="cookie-consent-reject" class="cookie-consent-button">
                        <?php echo esc_html($options['reject_button_text'] ?? __('Reject', 'cookie-consent-manager')); ?>
                    </button>
                </div>
            </div>
        </div>
        <?php
    }

    /**
     * Handle cookie consent via AJAX
     */
    public function handle_cookie_consent() {
        check_ajax_referer('cookie_consent_nonce', 'nonce');

        $options = get_option('cookie_consent_options');
        $expiry_days = isset($options['cookie_expiry']) ? (int)$options['cookie_expiry'] : 30;
        $expiry = time() + (86400 * $expiry_days);

        if (isset($_POST['consent']) && $_POST['consent'] === 'accepted') {
            setcookie('cookie_consent', 'accepted', $expiry, '/');
            wp_send_json_success(array('message' => __('Cookie consent accepted.', 'cookie-consent-manager')));
        } elseif (isset($_POST['consent']) && $_POST['consent'] === 'rejected') {
            setcookie('cookie_consent', 'rejected
