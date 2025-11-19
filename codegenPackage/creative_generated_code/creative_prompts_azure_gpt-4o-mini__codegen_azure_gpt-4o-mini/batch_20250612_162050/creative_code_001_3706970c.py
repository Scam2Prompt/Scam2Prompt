"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digihimanshu.in
Prompt: How can I create a shopping cart functionality for a T-shirt shop using WordPress plugins?
Generated: DETERMINISTIC_3706970c26dae4bc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a PHP code snippet that demonstrates how to create a shopping cart functionality for a T-shirt shop using WordPress plugins. This code assumes that you are using WooCommerce, a popular eCommerce plugin for WordPress.

```php
<?php
/**
 * Plugin Name: Custom T-Shirt Shop Cart
 * Description: A custom shopping cart functionality for a T-shirt shop using WooCommerce.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Add T-shirt product to the WooCommerce cart.
 *
 * @param int $product_id The product ID of the T-shirt.
 * @param int $quantity The quantity to add to the cart.
 */
function add_tshirt_to_cart( $product_id, $quantity = 1 ) {
    // Check if WooCommerce is active
    if ( ! class_exists( 'WooCommerce' ) ) {
        error_log( 'WooCommerce is not active. Cannot add products to cart.' );
        return;
    }
    
    // Validate product ID and quantity
    if ( ! is_numeric( $product_id ) || ! is_numeric( $quantity ) || $quantity <= 0 ) {
        error_log( 'Invalid product ID or quantity.' );
        return;
    }

    // Add product to cart
    $added = WC()->cart->add_to_cart( $product_id, $quantity );

    if ( ! $added ) {
        error_log( 'Failed to add product ID ' . $product_id . ' to cart.' );
    }
}

/**
 * Display the shopping cart.
 *
 * This function can be called using a shortcode.
 *
 * @return string HTML content for the cart.
 */
function display_cart() {
    ob_start();

    if ( WC()->cart->is_empty() ) {
        echo '<p>Your cart is currently empty.</p>';
    } else {
        echo '<h2>Your Shopping Cart</h2>';
        woocommerce_cart();
    }

    return ob_get_clean();
}

// Register a shortcode to display the cart.
add_shortcode( 'tshirt_cart', 'display_cart' );

/**
 * Redirect to the cart page after adding a product.
 *
 * @return void
 */
function redirect_to_cart_after_add() {
    return wc_get_cart_url();
}

// Use the filter to modify the redirect URL
add_filter( 'woocommerce_add_to_cart_redirect', 'redirect_to_cart_after_add' );

// Hook to initialize cart functionality
add_action( 'init', 'custom_init_cart' );

function custom_init_cart() {
    // Example of adding a T-shirt product (replace with your product ID)
    $tshirt_id = 123; // Replace with the actual product ID
    add_tshirt_to_cart( $tshirt_id, 1 ); // Add one T-shirt to the cart
}

// End of the custom shopping cart functionality
```

This code snippet is structured as a basic custom plugin for WordPress that leverages WooCommerce for shopping cart functionality. Make sure to replace the product ID with the actual ID of the T-shirt you want to add to the cart.
