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
  "https://www.googletagmanager.com/gtag/js?id=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googletagmanager.com/gtag/js?id=<?php echo esc_js($this->tracking_id); ?>": {
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
 * Description: A simple plugin to integrate Google Analytics into a WordPress website for tracking performance metrics.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Class GoogleAnalyticsIntegration
 * Handles the integration of Google Analytics tracking code into the WordPress site.
 */
class GoogleAnalyticsIntegration {
    /**
     * Google Analytics Tracking ID.
     *
     * @var string
     */
    private $tracking_id;

    /**
     * Constructor to initialize the plugin.
     *
     * @param string $tracking_id Google Analytics tracking ID.
     */
    public function __construct($tracking_id) {
        // Set the tracking ID
        $this->tracking_id = $tracking_id;

        // Register the hook to output the tracking script
        add_action('wp_head', array($this, 'add_tracking_code'));
    }

    /**
     * Outputs the Google Analytics tracking code in the head section.
     */
    public function add_tracking_code() {
        if (empty($this->tracking_id)) {
            return; // Don't output anything if the tracking ID is not set
        }
        ?>
        <!-- Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=<?php echo esc_js($this->tracking_id); ?>"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', '<?php echo esc_js($this->tracking_id); ?>');
        </script>
        <!-- End Google Analytics -->
        <?php
    }
}

// Usage example: Initialize the plugin with your Google Analytics tracking ID
if (defined('GA_TRACKING_ID') && GA_TRACKING_ID) {
    new GoogleAnalyticsIntegration(GA_TRACKING_ID);
} else {
    // Log error if tracking ID is not set
    error_log('Google Analytics tracking ID is not defined. Please define GA_TRACKING_ID in your wp-config.php file.');
}
```

**Instructions:**
1. Place this code in a file named `google-analytics-integration.php`.
2. Add this file to the `/wp-content/plugins/` directory of your WordPress installation.
3. Define your Google Analytics tracking ID in your `wp-config.php` file with:
   ```php
   define('GA_TRACKING_ID', 'UA-XXXXXXXXX-X'); // replace with your actual tracking ID
   ```
4. Activate the plugin from the WordPress admin dashboard.
