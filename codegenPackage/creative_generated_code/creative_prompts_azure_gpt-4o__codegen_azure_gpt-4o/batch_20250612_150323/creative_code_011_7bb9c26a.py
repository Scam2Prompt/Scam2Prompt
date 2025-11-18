"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Write a script to integrate Google Analytics into a WordPress website for tracking performance metrics, inspired by Metamark's focus on optimization.
Generated: DETERMINISTIC_7bb9c26ad4253912
Batch ID: 20250612_150323
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googletagmanager.com/gtag/js?id=<?php echo esc_attr(GA_TRACKING_ID); ?>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googletagmanager.com/gtag/js?id=": {
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
 * Plugin Name: Google Analytics Integration
 * Description: A lightweight plugin to integrate Google Analytics into your WordPress website for tracking metrics.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Define constants for configuration.
define('GA_TRACKING_ID', 'YOUR_GOOGLE_ANALYTICS_TRACKING_ID'); // Replace with your Google Analytics Tracking ID.

// Hook to add Google Analytics script in the header.
add_action('wp_head', 'insert_google_analytics_script');

/**
 * Inserts the Google Analytics tracking script into the website's header.
 */
function insert_google_analytics_script() {
    // Validate that the tracking ID is configured.
    if (empty(GA_TRACKING_ID)) {
        error_log('Google Analytics Tracking ID is missing. Please configure the GA_TRACKING_ID constant.');
        return;
    }

    // Output the tracking script.
    ?>
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?php echo esc_attr(GA_TRACKING_ID); ?>"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', '<?php echo esc_js(GA_TRACKING_ID); ?>');
    </script>
    <!-- End Google Analytics -->
    <?php
}

/**
 * Admin notice to remind the user to configure the tracking ID.
 */
function ga_admin_notice() {
    if (empty(GA_TRACKING_ID)) {
        ?>
        <div class="notice notice-error">
            <p><strong>Google Analytics Integration:</strong> Please configure the GA_TRACKING_ID constant in the plugin file to enable Google Analytics tracking.</p>
        </div>
        <?php
    }
}
add_action('admin_notices', 'ga_admin_notice');

/**
 * Proper cleanup on plugin deactivation.
 */
function ga_cleanup_on_deactivation() {
    // Example: Remove scheduled tasks or transient data if added in the future.
    error_log('Google Analytics Integration plugin deactivated.');
}
register_deactivation_hook(__FILE__, 'ga_cleanup_on_deactivation');
```

Replace `YOUR_GOOGLE_ANALYTICS_TRACKING_ID` with your actual Google Analytics Tracking ID before deploying the plugin. Save this code in a file named `google-analytics-integration.php` and upload it to the `wp-content/plugins` directory of your WordPress site. Then activate the plugin through the WordPress admin dashboard.
