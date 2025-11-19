"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: "Generate a code example for a plugin that integrates social media feeds into a WordPress site for an architectural firm, similar to e-book.top's social media links."
Generated: DETERMINISTIC_5a6dd45e17c8f014
Batch ID: 20250622_212059
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/' . esc_attr($atts['twitter_handle']) . ": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/' . esc_attr($atts['instagram_user']) . '/embed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/plugins/page.php?href=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://platform.twitter.com/widgets.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/plugins/page.php?href=' . esc_url($atts['facebook_page']) . '&tabs=timeline&width=500&height=600": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Plugin Name: Architectural Firm Social Media Feed Integration
 * Description: A plugin to integrate social media feeds into a WordPress site for an architectural firm.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Define constants
define('AF_SOCIAL_FEED_PLUGIN_VERSION', '1.0');
define('AF_SOCIAL_FEED_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('AF_SOCIAL_FEED_PLUGIN_URL', plugin_dir_url(__FILE__));

/**
 * Enqueue necessary scripts and styles
 */
function af_social_feed_enqueue_scripts() {
    wp_enqueue_style('af-social-feed-style', AF_SOCIAL_FEED_PLUGIN_URL . 'css/style.css');
    wp_enqueue_script('af-social-feed-script', AF_SOCIAL_FEED_PLUGIN_URL . 'js/script.js', array('jquery'), AF_SOCIAL_FEED_PLUGIN_VERSION, true);
}
add_action('wp_enqueue_scripts', 'af_social_feed_enqueue_scripts');

/**
 * Shortcode to display social media feeds
 *
 * Usage: [af_social_feed]
 */
function af_social_feed_shortcode($atts) {
    // Attributes with default values
    $atts = shortcode_atts(array(
        'facebook_page' => '',
        'twitter_handle' => '',
        'instagram_user' => '',
    ), $atts, 'af_social_feed');

    // Start output buffering
    ob_start();

    // Facebook feed
    if (!empty($atts['facebook_page'])) {
        echo '<div class="af-social-feed facebook-feed">';
        echo '<h3>Facebook Feed</h3>';
        echo '<iframe src="https://www.facebook.com/plugins/page.php?href=' . esc_url($atts['facebook_page']) . '&tabs=timeline&width=500&height=600" width="500" height="600" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true"></iframe>';
        echo '</div>';
    }

    // Twitter feed
    if (!empty($atts['twitter_handle'])) {
        echo '<div class="af-social-feed twitter-feed">';
        echo '<h3>Twitter Feed</h3>';
        echo '<a class="twitter-timeline" href="https://twitter.com/' . esc_attr($atts['twitter_handle']) . '">Tweets by ' . esc_html($atts['twitter_handle']) . '</a>';
        echo '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>';
        echo '</div>';
    }

    // Instagram feed
    if (!empty($atts['instagram_user'])) {
        echo '<div class="af-social-feed instagram-feed">';
        echo '<h3>Instagram Feed</h3>';
        echo '<iframe src="https://www.instagram.com/' . esc_attr($atts['instagram_user']) . '/embed" width="500" height="600" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true"></iframe>';
        echo '</div>';
    }

    // Return the buffered content
    return ob_get_clean();
}
add_shortcode('af_social_feed', 'af_social_feed_shortcode');

/**
 * Plugin activation hook
 */
function af_social_feed_activate() {
    // Perform any necessary setup tasks
    // For example, create custom database tables or set default options
}
register_activation_hook(__FILE__, 'af_social_feed_activate');

/**
 * Plugin deactivation hook
 */
function af_social_feed_deactivate() {
    // Clean up tasks
    // For example, remove custom database tables or options
}
register_deactivation_hook(__FILE__, 'af_social_feed_deactivate');

/**
 * Plugin uninstall hook
 */
function af_social_feed_uninstall() {
    // Remove all plugin data
    // For example, delete custom database tables or options
}
register_uninstall_hook(__FILE__, 'af_social_feed_uninstall');
```

### Notes:
- Create a `css/style.css` file for custom styles and a `js/script.js` file for any JavaScript functionality.
- Replace placeholders like `Your Name` with actual values.
- Ensure proper testing before deploying to production.
