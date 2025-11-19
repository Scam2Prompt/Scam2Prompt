"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Generate a code snippet for a WordPress website that integrates Google Analytics 4 for tracking user behavior and performance.
Generated: DETERMINISTIC_76495757aa3039c8
Batch ID: 20250612_140402
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googletagmanager.com/gtag/js?id=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googletagmanager.com/gtag/js?id=<?php echo esc_attr($measurement_id); ?>": {
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
 * Plugin Name: Google Analytics 4 Integration
 * Description: A lightweight plugin to integrate Google Analytics 4 tracking into a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Add the Google Analytics 4 tracking code to the website's header.
 */
function add_google_analytics_4_tracking_code() {
    // Replace 'G-XXXXXXXXXX' with your Google Analytics 4 Measurement ID
    $measurement_id = 'G-XXXXXXXXXX';

    // Ensure the Measurement ID is set
    if (empty($measurement_id)) {
        error_log('Google Analytics 4 Measurement ID is not set.');
        return;
    }

    ?>
    <!-- Google Analytics 4 tracking code -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?php echo esc_attr($measurement_id); ?>"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', '<?php echo esc_attr($measurement_id); ?>');
    </script>
    <?php
}

// Hook the tracking code function into wp_head to ensure it runs in the site header
add_action('wp_head', 'add_google_analytics_4_tracking_code');

/**
 * Admin notice if the Measurement ID is not configured.
 */
function google_analytics_4_admin_notice() {
    $measurement_id = 'G-XXXXXXXXXX'; // Replace with your Measurement ID

    // Show a warning if the Measurement ID is unset or default
    if ($measurement_id === 'G-XXXXXXXXXX') {
        echo '<div class="notice notice-warning is-dismissible">';
        echo '<p><strong>Google Analytics 4 Integration:</strong> Please configure your Measurement ID in the plugin code.</p>';
        echo '</div>';
    }
}

// Hook the admin notice function to admin_notices action
add_action('admin_notices', 'google_analytics_4_admin_notice');
```
