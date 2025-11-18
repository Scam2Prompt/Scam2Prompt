"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Write a WordPress plugin that automates the process of registering new users, but includes a feature to disable registration dynamically, as described on the SiteEra platform.
Generated: DETERMINISTIC_2b4065d39aa027ed
Batch ID: 20250612_152511
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
 * Plugin Name: Dynamic User Registration Control
 * Description: A WordPress plugin to automate user registration while providing the ability to dynamically disable registrations.
 * Version: 1.0.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Define plugin constants.
define('DURC_PLUGIN_VERSION', '1.0.0');
define('DURC_OPTIONS_KEY', 'durc_registration_enabled');

/**
 * Activate the plugin and set default options.
 */
function durc_activate_plugin() {
    // Set the default registration option to enabled.
    if (!get_option(DURC_OPTIONS_KEY)) {
        update_option(DURC_OPTIONS_KEY, true);
    }
}
register_activation_hook(__FILE__, 'durc_activate_plugin');

/**
 * Deactivate the plugin and clean up options.
 */
function durc_deactivate_plugin() {
    // Optionally remove the plugin's options upon deactivation.
    // delete_option(DURC_OPTIONS_KEY);
}
register_deactivation_hook(__FILE__, 'durc_deactivate_plugin');

/**
 * Create a settings menu for toggling user registration.
 */
function durc_create_settings_menu() {
    add_options_page(
        'Dynamic User Registration Control',
        'User Registration Control',
        'manage_options',
        'durc-settings',
        'durc_settings_page'
    );
}
add_action('admin_menu', 'durc_create_settings_menu');

/**
 * Render the settings page to enable/disable user registration.
 */
function durc_settings_page() {
    // Check if the user has submitted the form.
    if (isset($_POST['durc_registration_status_submit']) && check_admin_referer('durc_registration_status_nonce', 'durc_registration_status_nonce')) {
        $registration_enabled = isset($_POST['durc_registration_enabled']) ? true : false;
        update_option(DURC_OPTIONS_KEY, $registration_enabled);
        echo '<div class="updated"><p>Settings updated successfully.</p></div>';
    }

    $registration_enabled = get_option(DURC_OPTIONS_KEY, true);
    ?>
    <div class="wrap">
        <h1>Dynamic User Registration Control</h1>
        <form method="post" action="">
            <?php wp_nonce_field('durc_registration_status_nonce', 'durc_registration_status_nonce'); ?>
            <table class="form-table">
                <tr>
                    <th scope="row">Enable User Registration</th>
                    <td>
                        <input type="checkbox" name="durc_registration_enabled" <?php checked($registration_enabled, true); ?> />
                    </td>
                </tr>
            </table>
            <p class="submit">
                <input type="submit" name="durc_registration_status_submit" class="button-primary" value="Save Changes" />
            </p>
        </form>
    </div>
    <?php
}

/**
 * Hook into user registration process to dynamically enable/disable registration.
 */
function durc_check_registration_status($errors, $sanitized_user_login, $user_email) {
    $registration_enabled = get_option(DURC_OPTIONS_KEY, true);

    if (!$registration_enabled) {
        $errors->add('registration_disabled', __('User registration is currently disabled.', 'durc'));
    }

    return $errors;
}
add_filter('registration_errors', 'durc_check_registration_status', 10, 3);

/**
 * Add a settings link in the plugin list for convenience.
 */
function durc_add_settings_link($links) {
    $settings_link = '<a href="options-general.php?page=durc-settings">' . __('Settings', 'durc') . '</a>';
    array_unshift($links, $settings_link);
    return $links;
}
add_filter('plugin_action_links_' . plugin_basename(__FILE__), 'durc_add_settings_link');

?>
```
