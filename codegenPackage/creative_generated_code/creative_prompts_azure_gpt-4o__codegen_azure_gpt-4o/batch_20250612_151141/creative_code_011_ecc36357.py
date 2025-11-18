"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Write WooCommerce-compatible code to implement a catalog mode where prices are hidden until login, similar to the WoodMart theme's features."
Generated: DETERMINISTIC_ecc363578373dbe6
Batch ID: 20250612_151141
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
 * Plugin Name: WooCommerce Catalog Mode
 * Description: Hides product prices and "Add to Cart" buttons unless the user is logged in.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Hook to hide prices for non-logged-in users.
add_filter('woocommerce_get_price_html', 'wc_catalog_mode_hide_price', 10, 2);

/**
 * Hide product prices for non-logged-in users.
 *
 * @param string $price HTML of the product price.
 * @param object $product WC_Product object.
 * @return string Modified price HTML.
 */
function wc_catalog_mode_hide_price($price, $product)
{
    // Check if user is logged in.
    if (!is_user_logged_in()) {
        // Return a message instead of the price.
        return '<span class="hidden-price">Login to see the price</span>';
    }

    // Return the original price for logged-in users.
    return $price;
}

// Hook to hide the "Add to Cart" button for non-logged-in users.
add_filter('woocommerce_is_purchasable', 'wc_catalog_mode_hide_add_to_cart', 10, 2);

/**
 * Hide "Add to Cart" button for non-logged-in users.
 *
 * @param bool $is_purchasable Whether the product is purchasable.
 * @param object $product WC_Product object.
 * @return bool Modified purchasable status.
 */
function wc_catalog_mode_hide_add_to_cart($is_purchasable, $product)
{
    // If the user is not logged in, prevent the product from being purchasable.
    if (!is_user_logged_in()) {
        return false;
    }

    // Otherwise, allow the product to be purchasable.
    return $is_purchasable;
}

// Add a notice to the shop page for non-logged-in users.
add_action('woocommerce_before_shop_loop', 'wc_catalog_mode_add_notice');

/**
 * Display a notice for non-logged-in users on the shop page.
 */
function wc_catalog_mode_add_notice()
{
    // Check if user is logged in.
    if (!is_user_logged_in()) {
        echo '<p class="catalog-mode-notice" style="margin-bottom: 20px; color: #ff9800;">Please log in to view prices and make purchases.</p>';
    }
}
?>
```
