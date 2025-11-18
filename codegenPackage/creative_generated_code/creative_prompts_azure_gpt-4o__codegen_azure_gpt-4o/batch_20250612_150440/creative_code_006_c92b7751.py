"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webstarstudio.com
Prompt: Create a configuration file for integrating Split2 analytics into a WordPress site, referencing WebStar Studio's services.
Generated: DETERMINISTIC_c92b7751b966bc55
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.split2.com/analytics.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Split2 Analytics Integration
 * Description: Integrates Split2 analytics into your WordPress site using WebStar Studio's services.
 * Version: 1.0.0
 * Author: WebStar Studio
 * License: GPL-2.0+
 * Text Domain: split2-analytics
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Define constants for the plugin.
define('SPLIT2_ANALYTICS_VERSION', '1.0.0');
define('SPLIT2_ANALYTICS_OPTION_KEY', 'split2_analytics_settings');

/**
 * Enqueues the Split2 Analytics script on the front-end.
 */
function split2_enqueue_analytics_script() {
    // Retrieve the Split2 API Key from the options.
    $options = get_option(SPLIT2_ANALYTICS_OPTION_KEY);
    $api_key = isset($options['api_key']) ? esc_js($options['api_key']) : '';

    // Ensure the API Key is set before enqueueing the script.
    if (!empty($api_key)) {
        wp_enqueue_script(
            'split2-analytics',
            'https://cdn.split2.com/analytics.js', // URL to Split2's analytics script.
            array(), // No dependencies.
            SPLIT2_ANALYTICS_VERSION,
            true // Load in the footer.
        );

        // Add inline script for initializing Split2.
        wp_add_inline_script(
            'split2-analytics',
            "window.split2Config = { apiKey: '{$api_key}' };"
        );
    }
}
add_action('wp_enqueue_scripts', 'split2_enqueue_analytics_script');

/**
 * Adds a settings page to configure Split2 Analytics.
 */
function split2_add_settings_page() {
    add_options_page(
        'Split2 Analytics Settings',
        'Split2 Analytics',
        'manage_options',
        'split2-analytics',
        'split2_render_settings_page'
    );
}
add_action('admin_menu', 'split2_add_settings_page');

/**
 * Renders the settings page for configuring Split2 Analytics.
 */
function split2_render_settings_page() {
    // Check if the user has the required capability.
    if (!current_user_can('manage_options')) {
        return;
    }

    // Handle form submission and save settings.
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && check_admin_referer('split2_settings_save', 'split2_settings_nonce')) {
        $api_key = isset($_POST['api_key']) ? sanitize_text_field($_POST['api_key']) : '';
        update_option(SPLIT2_ANALYTICS_OPTION_KEY, array('api_key' => $api_key));
        echo '<div class="updated"><p>Settings saved successfully.</p></div>';
    }

    // Fetch current settings.
    $options = get_option(SPLIT2_ANALYTICS_OPTION_KEY);
    $api_key = isset($options['api_key']) ? esc_attr($options['api_key']) : '';

    ?>
    <div class="wrap">
        <h1>Split2 Analytics Settings</h1>
        <form method="post">
            <?php wp_nonce_field('split2_settings_save', 'split2_settings_nonce'); ?>
            <table class="form-table">
                <tr>
                    <th scope="row"><label for="api_key">Split2 API Key</label></th>
                    <td>
                        <input type="text" id="api_key" name="api_key" value="<?php echo $api_key; ?>" class="regular-text" required>
                        <p class="description">Enter your Split2 API Key provided by WebStar Studio.</p>
                    </td>
                </tr>
            </table>
            <?php submit_button('Save Changes'); ?>
        </form>
    </div>
    <?php
}

/**
 * Handles plugin activation tasks.
 */
function split2_plugin_activate() {
    if (!get_option(SPLIT2_ANALYTICS_OPTION_KEY)) {
        add_option(SPLIT2_ANALYTICS_OPTION_KEY, array('api_key' => ''));
    }
}
register_activation_hook(__FILE__, 'split2_plugin_activate');

/**
 * Handles plugin deactivation tasks.
 */
function split2_plugin_deactivate() {
    // Optionally clean up options here (commented out to retain settings on deactivation).
    // delete_option(SPLIT2_ANALYTICS_OPTION_KEY);
}
register_deactivation_hook(__FILE__, 'split2_plugin_deactivate');
```
