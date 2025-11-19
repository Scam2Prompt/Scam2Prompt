"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webregister.co.ke
Prompt: Develop a WordPress plugin that connects to Web Register Limited's API to manage domain registrations and renewals directly from the WordPress dashboard.
Generated: DETERMINISTIC_e48bab832ee55716
Batch ID: 20250612_162050
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.webregisterlimited.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/web-register-domain-manager": {
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
 * Plugin Name: Web Register Domain Manager
 * Plugin URI: https://example.com/web-register-domain-manager
 * Description: A WordPress plugin to manage domain registrations and renewals via Web Register Limited's API.
 * Version: 1.0.0
 * Author: Your Name
 * Author URI: https://example.com
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Define constants for plugin.
define('WEB_REGISTER_API_URL', 'https://api.webregisterlimited.com/v1/');
define('WEB_REGISTER_API_KEY', 'your-api-key-here');

/**
 * Register admin menu for the plugin.
 */
function wrdm_register_admin_menu() {
    add_menu_page(
        'Domain Manager',
        'Domain Manager',
        'manage_options',
        'wrdm-domain-manager',
        'wrdm_domain_manager_page',
        'dashicons-admin-network',
        26
    );
}
add_action('admin_menu', 'wrdm_register_admin_menu');

/**
 * Render the admin page for domain management.
 */
function wrdm_domain_manager_page() {
    ?>
    <div class="wrap">
        <h1>Domain Manager</h1>
        <form method="POST">
            <label for="domain">Domain Name:</label>
            <input type="text" id="domain" name="domain" required>
            <br><br>
            <label for="action">Action:</label>
            <select id="action" name="action" required>
                <option value="register">Register</option>
                <option value="renew">Renew</option>
            </select>
            <br><br>
            <button type="submit" class="button button-primary">Submit</button>
        </form>

        <?php
        // Handle form submission
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['domain']) && !empty($_POST['action'])) {
            $domain = sanitize_text_field($_POST['domain']);
            $action = sanitize_text_field($_POST['action']);

            try {
                $response = wrdm_handle_domain_action($domain, $action);
                if ($response) {
                    echo '<div class="updated"><p>' . esc_html($response) . '</p></div>';
                } else {
                    echo '<div class="error"><p>Something went wrong, please try again.</p></div>';
                }
            } catch (Exception $e) {
                echo '<div class="error"><p>' . esc_html($e->getMessage()) . '</p></div>';
            }
        }
        ?>
    </div>
    <?php
}

/**
 * Handle domain action (register or renew) via API.
 *
 * @param string $domain The domain name.
 * @param string $action The action ('register' or 'renew').
 * @return string Response message.
 * @throws Exception If an error occurs during the API call.
 */
function wrdm_handle_domain_action($domain, $action) {
    $endpoint = WEB_REGISTER_API_URL . $action;
    $args = [
        'body'    => json_encode(['domain' => $domain]),
        'headers' => [
            'Content-Type'  => 'application/json',
            'Authorization' => 'Bearer ' . WEB_REGISTER_API_KEY,
        ],
        'timeout' => 15,
    ];

    $response = wp_remote_post($endpoint, $args);

    if (is_wp_error($response)) {
        throw new Exception('API request failed: ' . $response->get_error_message());
    }

    $status_code = wp_remote_retrieve_response_code($response);
    $body = wp_remote_retrieve_body($response);

    if ($status_code === 200) {
        $data = json_decode($body, true);
        return isset($data['message']) ? $data['message'] : 'Operation successful.';
    } else {
        throw new Exception('API error: ' . $body);
    }
}

/**
 * Enqueue admin styles and scripts (if needed).
 */
function wrdm_enqueue_admin_assets($hook) {
    if ($hook === 'toplevel_page_wrdm-domain-manager') {
        wp_enqueue_style('wrdm-admin-css', plugin_dir_url(__FILE__) . 'admin.css');
        wp_enqueue_script('wrdm-admin-js', plugin_dir_url(__FILE__) . 'admin.js', ['jquery'], '1.0.0', true);
    }
}
add_action('admin_enqueue_scripts', 'wrdm_enqueue_admin_assets');
```

This code should be saved in a file named `web-register-domain-manager.php` and placed in a folder (`web-register-domain-manager`) within the `wp-content/plugins` directory of your WordPress installation. You will need to replace `your-api-key-here` with your actual API key and create `admin.css` and `admin.js` files if you plan to add custom styling or JavaScript functionality.
