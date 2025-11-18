"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Generate code to integrate WP Guardian with a WordPress site hosted outside of Plesk, ensuring visibility into site health and enabling flexible updates management.
Generated: DETERMINISTIC_a6b7fb0d18443650
Batch ID: 20250612_152526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wp-guardian.com/": {
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
 * Plugin Name: WP Guardian Integration
 * Description: Integrates WP Guardian with a WordPress site, ensuring visibility into site health and enabling flexible updates management.
 * Version: 1.0.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Class WP_Guardian_Integration
 * Handles the communication between WordPress and WP Guardian API.
 */
class WP_Guardian_Integration {
    private $api_url = 'https://api.wp-guardian.com/'; // Replace with actual WP Guardian API URL
    private $api_key = ''; // Set your WP Guardian API key here

    public function __construct() {
        // Hook into admin_init to check site health
        add_action('admin_init', [$this, 'check_site_health']);
        // Hook into update_option for custom update management
        add_action('update_option', [$this, 'manage_updates'], 10, 2);
    }

    /**
     * Checks site health and sends data to WP Guardian
     */
    public function check_site_health() {
        // Collect site health data
        $site_health_data = $this->get_site_health_data();

        // Send health data to WP Guardian
        $this->send_data_to_wp_guardian('site_health', $site_health_data);
    }

    /**
     * Gathers site health data
     *
     * @return array
     */
    private function get_site_health_data() {
        return [
            'site_name' => get_bloginfo('name'),
            'home_url' => get_home_url(),
            'wp_version' => get_bloginfo('version'),
            'php_version' => PHP_VERSION,
            'updates_enabled' => $this->are_updates_enabled(),
            // Additional health data can be added here
        ];
    }

    /**
     * Checks if updates are enabled in WordPress
     *
     * @return bool
     */
    private function are_updates_enabled() {
        return defined('AUTOMATIC_UPDATER_DISABLED') && !AUTOMATIC_UPDATER_DISABLED;
    }

    /**
     * Sends data to WP Guardian API
     *
     * @param string $endpoint
     * @param array $data
     * @return void
     */
    private function send_data_to_wp_guardian($endpoint, $data) {
        $url = $this->api_url . $endpoint;

        // Setup cURL
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $this->api_key,
        ]);

        // Execute the request and handle errors
        $response = curl_exec($ch);
        if (curl_errno($ch)) {
            error_log('WP Guardian API error: ' . curl_error($ch));
        } else {
            $response_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            if ($response_code !== 200) {
                error_log('WP Guardian API returned an error: ' . $response);
            }
        }

        // Close the cURL session
        curl_close($ch);
    }

    /**
     * Manages updates based on WP Guardian recommendations
     *
     * @param string $option
     * @param mixed $value
     * @return void
     */
    public function manage_updates($option, $value) {
        // Implement logic here to manage updates based on WP Guardian's guidance
        // Example: Disable certain updates based on site health
        if ($this->should_disable_update($option)) {
            // Logic to disable update
            add_filter('auto_update_option_' . $option, '__return_false');
        }
    }

    /**
     * Determines if an update should be disabled
     *
     * @param string $option
     * @return bool
     */
    private function should_disable_update($option) {
        // Example logic to disable updates
        // This could check against the site health data or WP Guardian recommendations
        return false; // Replace with actual condition
    }
}

// Initialize the integration
new WP_Guardian_Integration();
```
