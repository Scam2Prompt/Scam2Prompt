"""
Generated Code Metadata:
========================
Original URL: https://i-centergroupe.com
Prompt: Create a website using WordPress and Kubio with a maintenance mode feature.
Generated: DETERMINISTIC_de132d1df9457d70
Batch ID: 20250622_210703
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
 * Plugin Name: Maintenance Mode with Kubio
 * Description: Enables maintenance mode for WordPress sites using Kubio.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

class Kubio_Maintenance_Mode {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('admin_menu', array($this, 'add_admin_menu'));
        add_action('admin_init', array($this, 'settings_init'));
        add_action('wp', array($this, 'maintenance_mode_check'));
    }

    /**
     * Add admin menu item
     */
    public function add_admin_menu() {
        add_options_page(
            'Maintenance Mode',
            'Maintenance Mode',
            'manage_options',
            'kubio_maintenance_mode',
            array($this, 'settings_page')
        );
    }

    /**
     * Initialize settings
     */
    public function settings_init() {
        register_setting('kubio_maintenance_mode', 'kubio_maintenance_settings');

        add_settings_section(
            'kubio_maintenance_mode_section',
            'Maintenance Mode Settings',
            array($this, 'settings_section_callback'),
            'kubio_maintenance_mode'
        );

        add_settings_field(
            'maintenance_mode_enabled',
            'Enable Maintenance Mode',
            array($this, 'enable_field_render'),
            'kubio_maintenance_mode',
            'kubio_maintenance_mode_section'
        );

        add_settings_field(
            'maintenance_mode_message',
            'Custom Message',
            array($this, 'message_field_render'),
            'kubio_maintenance_mode',
            'kubio_maintenance_mode_section'
        );

        add_settings_field(
            'maintenance_mode_allowed_ips',
            'Allowed IPs (comma separated)',
            array($this, 'ips_field_render'),
            'kubio_maintenance_mode',
            'kubio_maintenance_mode_section'
        );
    }

    /**
     * Render enable field
     */
    public function enable_field_render() {
        $options = get_option('kubio_maintenance_settings');
        ?>
        <input type="checkbox" name="kubio_maintenance_settings[maintenance_mode_enabled]" <?php checked($options['maintenance_mode_enabled'], 1); ?> value="1">
        <?php
    }

    /**
     * Render message field
     */
    public function message_field_render() {
        $options = get_option('kubio_maintenance_settings');
        ?>
        <textarea cols="40" rows="5" name="kubio_maintenance_settings[maintenance_mode_message]"><?php echo isset($options['maintenance_mode_message']) ? esc_textarea($options['maintenance_mode_message']) : ''; ?></textarea>
        <?php
    }

    /**
     * Render IPs field
     */
    public function ips_field_render() {
        $options = get_option('kubio_maintenance_settings');
        ?>
        <input type="text" name="kubio_maintenance_settings[maintenance_mode_allowed_ips]" value="<?php echo isset($options['maintenance_mode_allowed_ips']) ? esc_attr($options['maintenance_mode_allowed_ips']) : ''; ?>" class="regular-text">
        <p class="description">Enter IP addresses that should bypass maintenance mode, separated by commas.</p>
        <?php
    }

    /**
     * Settings section callback
     */
    public function settings_section_callback() {
        echo 'Configure maintenance mode settings for your Kubio WordPress site.';
    }

    /**
     * Settings page
     */
    public function settings_page() {
        ?>
        <div class="wrap">
            <h1>Maintenance Mode Settings</h1>
            <form action="options.php" method="post">
                <?php
                settings_fields('kubio_maintenance_mode');
                do_settings_sections('kubio_maintenance_mode');
                submit_button();
                ?>
            </form>
        </div>
        <?php
    }

    /**
     * Check if maintenance mode should be enabled
     */
    public function maintenance_mode_check() {
        $options = get_option('kubio_maintenance_settings');

        if (!isset($options['maintenance_mode_enabled']) || !$options['maintenance_mode_enabled']) {
            return;
        }

        // Check if current user can bypass maintenance mode
        if (current_user_can('manage_options')) {
            return;
        }

        // Check allowed IPs
        $allowed_ips = isset($options['maintenance_mode_allowed_ips']) ? $options['maintenance_mode_allowed_ips'] : '';
        if ($allowed_ips) {
            $allowed_ips = array_map('trim', explode(',', $allowed_ips));
            $user_ip = $_SERVER['REMOTE_ADDR'];
            if (in_array($user_ip, $allowed_ips)) {
                return;
            }
        }

        // Show maintenance page
        $this->show_maintenance_page();
    }

    /**
     * Display maintenance page
     */
    private function show_maintenance_page() {
        $options = get_option('kubio_maintenance_settings');
        $message = isset($options['maintenance_mode_message']) ? $options['maintenance_mode_message'] : 'The site is currently undergoing maintenance. Please check back soon.';

        wp_die(
            '<h1>Site Under Maintenance</h1>' . wpautop($message),
            'Site Under Maintenance',
            array('response' => 503)
        );
    }
}

new Kubio_Maintenance_Mode();
```
