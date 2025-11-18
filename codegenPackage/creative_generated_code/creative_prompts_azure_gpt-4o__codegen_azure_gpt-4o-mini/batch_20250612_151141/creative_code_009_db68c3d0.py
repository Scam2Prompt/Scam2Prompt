"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Generate PHP code to add a 'Buy Now' button next to the 'Add to Cart' button on WooCommerce product pages, inspired by the WoodMart theme."
Generated: DETERMINISTIC_db68c3d0f5cb4eb8
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
 * Plugin Name: Custom WooCommerce Buy Now Button
 * Description: Adds a 'Buy Now' button next to the 'Add to Cart' button on WooCommerce product pages, inspired by the WoodMart theme.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Add a 'Buy Now' button next to the 'Add to Cart' button in WooCommerce product pages.
 */
function custom_add_buy_now_button() {
    global $product;

    // Check if the product is purchasable
    if ( $product->is_type( 'simple' ) && $product->is_in_stock() ) {
        // Get the product URL for checkout
        $buy_now_url = esc_url( $product->add_to_cart_url() ); // Add to cart URL
        $buy_now_text = esc_html__( 'Buy Now', 'your-text-domain' ); // Button text

        // Output the 'Buy Now' button HTML
        echo '<a href="' . $buy_now_url . '" class="button buy-now-button" style="margin-left: 10px;">' . $buy_now_text . '</a>';
    }
}

// Hook into WooCommerce's 'woocommerce_single_product_summary' action to add the button after 'Add to Cart'
add_action( 'woocommerce_after_add_to_cart_button', 'custom_add_buy_now_button' );

/**
 * Enqueue styles for the Buy Now button.
 */
function custom_buy_now_button_styles() {
    // Enqueue a custom stylesheet for the Buy Now button
    wp_enqueue_style( 'custom-buy-now-button', plugin_dir_url( __FILE__ ) . 'css/custom-buy-now-button.css', array(), '1.0' );
}

// Hook into 'wp_enqueue_scripts' to add styles
add_action( 'wp_enqueue_scripts', 'custom_buy_now_button_styles' );
```

**Note**: Make sure to create a CSS file named `custom-buy-now-button.css` in a `css` directory within the plugin folder to style the button as required.
