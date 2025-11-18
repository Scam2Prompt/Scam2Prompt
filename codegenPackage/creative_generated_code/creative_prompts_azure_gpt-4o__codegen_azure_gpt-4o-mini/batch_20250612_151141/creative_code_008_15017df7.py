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
 * Add SKU and Stock Status to WooCommerce Product Loops
 * This code snippet adds the SKU and stock status to the WooCommerce product archive pages.
 * Place this code in your theme's functions.php file or a custom plugin.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Display SKU and Stock Status in product loops.
 *
 * @param array $args Arguments for the product loops.
 * @return void
 */
function display_sku_and_stock_status_in_loop( $args ) {
    global $product;

    // Check if product is available and is a product object
    if ( ! is_a( $product, 'WC_Product' ) ) {
        return;
    }

    // Get the SKU and stock status
    $sku = $product->get_sku();
    $stock_status = $product->get_stock_status();

    // Check if SKU exists and display it
    if ( ! empty( $sku ) ) {
        echo '<div class="product-sku">SKU: ' . esc_html( $sku ) . '</div>';
    }

    // Check stock status and display it accordingly
    switch ( $stock_status ) {
        case 'instock':
            echo '<div class="product-stock-status">In stock</div>';
            break;
        case 'outofstock':
            echo '<div class="product-stock-status">Out of stock</div>';
            break;
        case 'onbackorder':
            echo '<div class="product-stock-status">Available on backorder</div>';
            break;
    }
}

// Hook into the WooCommerce loop
add_action( 'woocommerce_after_shop_loop_item_title', 'display_sku_and_stock_status_in_loop', 15 );
```

This code snippet will display the SKU and stock status of each product in the WooCommerce product loop. Place the code in your theme's `functions.php` file or within a custom plugin to ensure it runs properly on your WooCommerce site.
