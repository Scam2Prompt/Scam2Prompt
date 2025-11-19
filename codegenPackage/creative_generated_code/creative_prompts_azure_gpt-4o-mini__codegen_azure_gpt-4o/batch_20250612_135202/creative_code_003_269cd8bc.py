"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Develop a plugin for WordPress that displays a promotional banner for a summer sale on premium silk sarees, highlighting discounts and free shipping.
Generated: DETERMINISTIC_269cd8bc267ba7de
Batch ID: 20250612_135202
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
 * Plugin Name: Summer Sale Silk Sarees Banner
 * Description: Displays a promotional banner for a summer sale on premium silk sarees, highlighting discounts and free shipping.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Prevent direct access to the file.
 */
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue styles for the banner.
 */
function summer_sale_enqueue_styles() {
    wp_enqueue_style('summer-sale-banner-style', plugin_dir_url(__FILE__) . 'css/banner-style.css');
}
add_action('wp_enqueue_scripts', 'summer_sale_enqueue_styles');

/**
 * Display the promotional banner.
 */
function summer_sale_banner() {
    // Banner HTML and content
    ?>
    <div class="summer-sale-banner">
        <h2>🎉 Summer Sale on Premium Silk Sarees! 🎉</h2>
        <p>Enjoy <strong>up to 50% off</strong> and <strong>free shipping</strong> on all purchases!</p>
        <a href="/shop" class="summer-sale-banner-btn">Shop Now</a>
    </div>
    <?php
}

/**
 * Hook the banner display function to WordPress' 'wp_footer' action.
 */
function summer_sale_add_banner_to_footer() {
    // Only display the banner on the frontend (not admin area)
    if (!is_admin()) {
        summer_sale_banner();
    }
}
add_action('wp_footer', 'summer_sale_add_banner_to_footer');

/**
 * Activation hook: Perform necessary setup when plugin is activated.
 */
function summer_sale_activate() {
    // Ensure the plugin folder has the necessary files
    if (!file_exists(plugin_dir_path(__FILE__) . 'css/banner-style.css')) {
        error_log('CSS file for summer sale banner not found!');
    }
}
register_activation_hook(__FILE__, 'summer_sale_activate');

/**
 * Deactivation hook: Clean up if needed when plugin is deactivated.
 */
function summer_sale_deactivate() {
    // Clean up operations (if any)
}
register_deactivation_hook(__FILE__, 'summer_sale_deactivate');

/**
 * Uninstall hook: Clean up completely when the plugin is uninstalled.
 */
function summer_sale_uninstall() {
    // Remove options or settings if stored
}
register_uninstall_hook(__FILE__, 'summer_sale_uninstall');

// CSS for the banner (create a separate banner-style.css file in the plugin directory)
/**
 * Example CSS content (to be placed in banner-style.css):
 *
 * .summer-sale-banner {
 *     background-color: #ffaa00;
 *     color: white;
 *     text-align: center;
 *     padding: 20px;
 *     position: fixed;
 *     bottom: 0;
 *     width: 100%;
 *     z-index: 9999;
 *     box-shadow: 0 -2px 5px rgba(0,0,0,0.5);
 * }
 *
 * .summer-sale-banner h2 {
 *     margin: 0;
 *     font-size: 24px;
 * }
 *
 * .summer-sale-banner p {
 *     margin: 5px 0;
 *     font-size: 18px;
 * }
 *
 * .summer-sale-banner-btn {
 *     display: inline-block;
 *     margin-top: 10px;
 *     padding: 10px 20px;
 *     background-color: white;
 *     color: #ffaa00;
 *     text-decoration: none;
 *     font-weight: bold;
 *     border-radius: 5px;
 * }
 *
 * .summer-sale-banner-btn:hover {
 *     background-color: #ffe5b4;
 * }
 */
```
