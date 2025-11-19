"""
Generated Code Metadata:
========================
Original URL: https://thesoftware.online
Prompt: Generate PHP code for a WordPress site to dynamically update the "Main menu" location in the header builder based on user preferences, referencing WooCommerce themes like WoodMart.
Generated: DETERMINISTIC_3a959865941b0ff6
Batch ID: 20250612_151611
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
 * Dynamically updates the WordPress menu location based on user preferences.
 * Specifically targets the 'Main menu' location in header builder themes like WoodMart.
 * 
 * @package CustomMenuUpdater
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Custom_Menu_Updater {

    /**
     * Initialize the class and set up hooks.
     */
    public function __construct() {
        add_action('wp_loaded', array($this, 'init'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'));
        add_action('wp_ajax_update_menu_location', array($this, 'handle_ajax_request'));
        add_action('wp_ajax_nopriv_update_menu_location', array($this, 'handle_ajax_request'));
    }

    /**
     * Initialize the menu updater functionality.
     */
    public function init() {
        // Check if WoodMart theme is active
        if ($this->is_woodmart_theme()) {
            add_filter('theme_mod_nav_menu_locations', array($this, 'modify_menu_locations'));
        }
    }

    /**
     * Check if the current theme is WoodMart.
     * 
     * @return bool True if WoodMart theme is active, false otherwise.
     */
    private function is_woodmart_theme() {
        $theme = wp_get_theme();
        return ('WoodMart' === $theme->get('Name') || 'woodmart' === $theme->get('Template'));
    }

    /**
     * Modify menu locations based on user preference.
     * 
     * @param array $locations Current menu locations.
     * @return array Modified menu locations.
     */
    public function modify_menu_locations($locations) {
        $user_preference = $this->get_user_menu_preference();
        
        if ($user_preference && isset($locations['main-menu'])) {
            $locations['main-menu'] = $user_preference;
        }

        return $locations;
    }

    /**
     * Get user's menu preference from cookies or session.
     * 
     * @return int|false Menu ID if preference exists, false otherwise.
     */
    private function get_user_menu_preference() {
        if (isset($_COOKIE['custom_menu_preference'])) {
            return (int) $_COOKIE['custom_menu_preference'];
        }

        if (isset($_SESSION['custom_menu_preference'])) {
            return (int) $_SESSION['custom_menu_preference'];
        }

        return false;
    }

    /**
     * Enqueue necessary JavaScript and CSS.
     */
    public function enqueue_assets() {
        if ($this->is_woodmart_theme()) {
            wp_enqueue_script(
                'custom-menu-updater',
                plugins_url('js/custom-menu-updater.js', __FILE__),
                array('jquery'),
                '1.0.0',
                true
            );

            wp_localize_script(
                'custom-menu-updater',
                'customMenuUpdater',
                array(
                    'ajaxurl' => admin_url('admin-ajax.php'),
                    'nonce' => wp_create_nonce('update_menu_location_nonce')
                )
            );
        }
    }

    /**
     * Handle AJAX request to update menu location.
     */
    public function handle_ajax_request() {
        check_ajax_referer('update_menu_location_nonce', 'nonce');

        if (!isset($_POST['menu_id'])) {
            wp_send_json_error('Menu ID not provided');
        }

        $menu_id = (int) $_POST['menu_id'];

        // Verify menu exists
        $menu_exists = wp_get_nav_menu_object($menu_id);
        if (!$menu_exists) {
            wp_send_json_error('Invalid menu ID');
        }

        // Set cookie for 30 days
        setcookie('custom_menu_preference', $menu_id, time() + (86400 * 30), '/');

        // Also store in session for immediate use
        $_SESSION['custom_menu_preference'] = $menu_id;

        wp_send_json_success('Menu preference updated');
    }
}

// Initialize the class
new Custom_Menu_Updater();
```
