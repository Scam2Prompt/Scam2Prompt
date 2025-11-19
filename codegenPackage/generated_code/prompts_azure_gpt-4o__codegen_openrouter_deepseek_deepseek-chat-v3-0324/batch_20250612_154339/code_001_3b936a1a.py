"""
Generated Code Metadata:
========================
Original URL: https://hopexchange.online
Prompt: Generate code to integrate WP Guardian with a WordPress site hosted outside of Plesk for health monitoring and updates management.
Generated: DETERMINISTIC_3b936a1a523aec8b
Batch ID: 20250612_154339
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
 * WP Guardian Integration for WordPress
 * 
 * This plugin integrates WP Guardian with a WordPress site for health monitoring
 * and updates management. It provides functionality to check site health,
 * manage updates, and send notifications.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class WP_Guardian_Integration {

    /**
     * Plugin version
     */
    const VERSION = '1.0.0';

    /**
     * Initialize the plugin
     */
    public static function init() {
        $instance = new self();
        $instance->setup_hooks();
    }

    /**
     * Set up WordPress hooks
     */
    private function setup_hooks() {
        // Admin menu
        add_action('admin_menu', array($this, 'add_admin_menu'));

        // Health checks
        add_action('wp_guardian_daily_health_check', array($this, 'perform_health_check'));

        // Update checks
        add_action('wp_guardian_daily_update_check', array($this, 'check_for_updates'));

        // Schedule events
        register_activation_hook(__FILE__, array($this, 'activate'));
        register_deactivation_hook(__FILE__, array($this, 'deactivate'));

        // AJAX handlers
        add_action('wp_ajax_wp_guardian_run_health_check', array($this, 'ajax_run_health_check'));
        add_action('wp_ajax_wp_guardian_run_update_check', array($this, 'ajax_run_update_check'));
    }

    /**
     * Add admin menu items
     */
    public function add_admin_menu() {
        add_menu_page(
            'WP Guardian',
            'WP Guardian',
            'manage_options',
            'wp-guardian',
            array($this, 'render_admin_page'),
            'dashicons-shield',
            80
        );

        add_submenu_page(
            'wp-guardian',
            'Health Monitoring',
            'Health Monitoring',
            'manage_options',
            'wp-guardian-health',
            array($this, 'render_health_page')
        );

        add_submenu_page(
            'wp-guardian',
            'Updates Management',
            'Updates Management',
            'manage_options',
            'wp-guardian-updates',
            array($this, 'render_updates_page')
        );
    }

    /**
     * Render main admin page
     */
    public function render_admin_page() {
        if (!current_user_can('manage_options')) {
            wp_die(__('You do not have sufficient permissions to access this page.'));
        }

        include plugin_dir_path(__FILE__) . 'views/admin-page.php';
    }

    /**
     * Render health monitoring page
     */
    public function render_health_page() {
        if (!current_user_can('manage_options')) {
            wp_die(__('You do not have sufficient permissions to access this page.'));
        }

        $health_status = $this->get_health_status();
        include plugin_dir_path(__FILE__) . 'views/health-page.php';
    }

    /**
     * Render updates management page
     */
    public function render_updates_page() {
        if (!current_user_can('manage_options')) {
            wp_die(__('You do not have sufficient permissions to access this page.'));
        }

        $updates = $this->get_available_updates();
        include plugin_dir_path(__FILE__) . 'views/updates-page.php';
    }

    /**
     * Perform comprehensive health check
     */
    public function perform_health_check() {
        $health_status = array();

        // Core WordPress health
        $health_status['core'] = $this->check_core_health();

        // Database health
        $health_status['database'] = $this->check_database_health();

        // File system health
        $health_status['filesystem'] = $this->check_filesystem_health();

        // Security health
        $health_status['security'] = $this->check_security_health();

        // Performance health
        $health_status['performance'] = $this->check_performance_health();

        // Store results
        update_option('wp_guardian_health_status', $health_status);

        // Send notification if needed
        $this->send_health_notification($health_status);

        return $health_status;
    }

    /**
     * Check for available updates
     */
    public function check_for_updates() {
        wp_version_check();
        wp_update_plugins();
        wp_update_themes();

        $updates = array(
            'core' => $this->get_core_updates(),
            'plugins' => $this->get_plugin_updates(),
            'themes' => $this->get_theme_updates()
        );

        update_option('wp_guardian_available_updates', $updates);

        // Send notification if updates are available
        $this->send_update_notification($updates);

        return $updates;
    }

    /**
     * Get current health status
     */
    public function get_health_status() {
        $health_status = get_option('wp_guardian_health_status', array());
        if (empty($health_status)) {
            $health_status = $this->perform_health_check();
        }
        return $health_status;
    }

    /**
     * Get available updates
     */
    public function get_available_updates() {
        $updates = get_option('wp_guardian_available_updates', array());
        if (empty($updates)) {
            $updates = $this->check_for_updates();
        }
        return $updates;
    }

    /**
     * Check core WordPress health
     */
    private function check_core_health() {
        require_once ABSPATH . 'wp-admin/includes/update.php';
        
        $result = array(
            'status' => 'good',
            'messages' => array()
        );

        // Check WordPress version
        if (!is_blog_installed()) {
            $result['status'] = 'critical';
            $result['messages'][] = 'WordPress is not installed properly.';
        }

        // Check for core updates
        $core_updates = get_core_updates();
        if (!empty($core_updates) && $core_updates[0]->response === 'upgrade') {
            $result['status'] = 'warning';
            $result['messages'][] = 'WordPress core update available.';
        }

        return $result;
    }

    /**
     * Check database health
     */
    private function check_database_health() {
        global $wpdb;

        $result = array(
            'status' => 'good',
            'messages' => array()
        );

        // Check database tables
        $tables = $wpdb->get_col("SHOW TABLES");
        if (empty($tables)) {
            $result['status'] = 'critical';
            $result['messages'][] = 'No database tables found.';
            return $result;
        }

        // Check for database errors
        $wpdb->suppress_errors(false);
        $wpdb->show_errors(false);
        $wpdb->query("SELECT 1");
        if ($wpdb->last_error) {
            $result['status'] = 'critical';
            $result['messages'][] = 'Database error detected: ' . $wpdb->last_error;
        }

        return $result;
    }

    /**
     * Check filesystem health
     */
    private function check_filesystem_health() {
        $result = array(
            'status' => 'good',
            'messages' => array()
        );

        // Check if wp-content is writable
        if (!is_writable(WP_CONTENT_DIR)) {
            $result['status'] = 'warning';
            $result['messages'][] = 'wp-content directory is not writable.';
        }

        // Check uploads directory
        $upload_dir = wp_upload_dir();
        if (!is_writable($upload_dir['path'])) {
            $result['status'] = 'warning';
            $result['messages'][] = 'Uploads directory is not writable.';
        }

        return $result;
    }

    /**
     * Check security health
     */
    private function check_security_health() {
        $result = array(
            'status' => 'good',
            'messages' => array()
        );

        // Check if debug mode is enabled
        if (defined('WP_DEBUG') && WP_DEBUG) {
            $result['status'] = 'warning';
            $result['messages'][] = 'Debug mode is enabled.';
        }

        // Check for default admin username
        if (username_exists('admin')) {
            $result['status'] = 'warning';
            $result['messages'][] = 'Default "admin" username exists.';
        }

        return $result;
    }

    /**
     * Check performance health
     */
    private function check_performance_health() {
        $result = array(
            'status' => 'good',
            'messages' => array()
        );

        // Check for object cache
        if (!wp_using_ext_object_cache()) {
            $result['messages'][] = 'Object cache is not enabled.';
        }

        // Check for too many plugins
        $plugins = get
