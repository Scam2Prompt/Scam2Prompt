"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "How can I configure WooCommerce to show SKU and stock status on product loops, similar to the WoodMart theme?"
Generated: DETERMINISTIC_15017df762a986fb
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
 * Plugin Name: WooCommerce SKU and Stock in Product Loops
 * Description: Adds SKU and stock status to product loops in WooCommerce.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Hook into WooCommerce product loops to display SKU and stock status.
 */
function add_sku_and_stock_to_product_loop() {
    add_action('woocommerce_after_shop_loop_item_title', 'display_sku_and_stock_in_loops', 10);
}

/**
 * Display SKU and stock status.
 *
 * @hooked woocommerce_after_shop_loop_item_title
 */
function display_sku_and_stock_in_loops() {
    global $product;

    // Ensure $product is valid.
    if (!$product instanceof WC_Product) {
        return;
    }

    // Get product SKU.
    $sku = $product->get_sku();
    // Get stock status.
    $stock_status = $product->is_in_stock() ? __('In Stock', 'woocommerce') : __('Out of Stock', 'woocommerce');

    echo '<div class="woocommerce-product-meta">';
    
    // Display SKU if available.
    if (!empty($sku)) {
        echo '<p class="sku"><strong>' . __('SKU:', 'woocommerce') . '</strong> ' . esc_html($sku) . '</p>';
    }

    // Display stock status.
    echo '<p class="stock-status"><strong>' . __('Stock Status:', 'woocommerce') . '</strong> ' . esc_html($stock_status) . '</p>';
    
    echo '</div>';
}

// Hook into WooCommerce after theme setup.
add_action('after_setup_theme', 'add_sku_and_stock_to_product_loop');
?>
```
