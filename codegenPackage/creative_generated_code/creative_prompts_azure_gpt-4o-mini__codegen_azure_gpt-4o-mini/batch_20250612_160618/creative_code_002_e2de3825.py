"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Write a function using a library like WooCommerce to handle cart operations for an online arts shop, inspired by the features of the Knox Alliance store.
Generated: DETERMINISTIC_e2de382569dc3ee1
Batch ID: 20250612_160618
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
 * Cart Operations for an Online Arts Shop using WooCommerce
 * 
 * This file contains functions to handle various cart operations 
 * such as adding items, removing items, and updating quantities.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Add item to the cart.
 *
 * @param int $product_id The ID of the product to add.
 * @param int $quantity The quantity of the product to add.
 * @return array|WP_Error Response containing cart data or error message.
 */
function arts_shop_add_to_cart( $product_id, $quantity = 1 ) {
    // Validate product ID
    if ( ! $product_id || ! is_numeric( $product_id ) ) {
        return new WP_Error( 'invalid_product', __( 'Invalid product ID.', 'arts-shop' ) );
    }

    // Validate quantity
    if ( $quantity <= 0 || ! is_numeric( $quantity ) ) {
        return new WP_Error( 'invalid_quantity', __( 'Quantity must be greater than zero.', 'arts-shop' ) );
    }

    // Add product to cart
    $added = WC()->cart->add_to_cart( $product_id, $quantity );

    // Check if product was added successfully
    if ( ! $added ) {
        return new WP_Error( 'add_failed', __( 'Failed to add product to cart.', 'arts-shop' ) );
    }

    return WC()->cart->get_cart();
}

/**
 * Remove item from the cart.
 *
 * @param string $cart_item_key The cart item key for the item to remove.
 * @return array|WP_Error Response containing cart data or error message.
 */
function arts_shop_remove_from_cart( $cart_item_key ) {
    // Validate cart item key
    if ( ! $cart_item_key ) {
        return new WP_Error( 'invalid_cart_item', __( 'Invalid cart item key.', 'arts-shop' ) );
    }

    // Remove item from cart
    $removed = WC()->cart->remove_cart_item( $cart_item_key );

    // Check if product was removed successfully
    if ( ! $removed ) {
        return new WP_Error( 'remove_failed', __( 'Failed to remove product from cart.', 'arts-shop' ) );
    }

    return WC()->cart->get_cart();
}

/**
 * Update item quantity in the cart.
 *
 * @param string $cart_item_key The cart item key for the item to update.
 * @param int $quantity The new quantity for the item.
 * @return array|WP_Error Response containing cart data or error message.
 */
function arts_shop_update_cart_quantity( $cart_item_key, $quantity ) {
    // Validate cart item key
    if ( ! $cart_item_key ) {
        return new WP_Error( 'invalid_cart_item', __( 'Invalid cart item key.', 'arts-shop' ) );
    }

    // Validate quantity
    if ( $quantity < 0 || ! is_numeric( $quantity ) ) {
        return new WP_Error( 'invalid_quantity', __( 'Quantity must be zero or greater.', 'arts-shop' ) );
    }

    // Update item quantity in cart
    $updated = WC()->cart->set_quantity( $cart_item_key, $quantity );

    // Check if quantity was updated successfully
    if ( ! $updated ) {
        return new WP_Error( 'update_failed', __( 'Failed to update product quantity in cart.', 'arts-shop' ) );
    }

    return WC()->cart->get_cart();
}

/**
 * Get the cart contents.
 *
 * @return array The current cart contents.
 */
function arts_shop_get_cart_contents() {
    return WC()->cart->get_cart();
}
```
