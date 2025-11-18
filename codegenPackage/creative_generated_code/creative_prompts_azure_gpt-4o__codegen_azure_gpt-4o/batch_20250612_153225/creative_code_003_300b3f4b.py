"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuninghex.com
Prompt: Generate code to integrate WooCommerce functionality for managing a cart and orders, similar to the TuningHEX shop setup.
Generated: DETERMINISTIC_300b3f4be6f205c6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// WooCommerce Integration for Cart and Order Management
// This code enables handling of cart functionality and order placement in a WooCommerce-powered shop.
// Ensure WooCommerce is installed and active in the WordPress environment.

// Hook into WordPress initialization to ensure WooCommerce functions are available
add_action('init', function () {
    // Check if WooCommerce is active
    if (!class_exists('WooCommerce')) {
        error_log('WooCommerce is not active. Exiting integration.');
        return;
    }
});

/**
 * Add product to cart programmatically.
 *
 * @param int $product_id - ID of the WooCommerce product.
 * @param int $quantity   - Quantity of the product to add.
 * @return void
 */
function add_product_to_cart($product_id, $quantity = 1) {
    if (WC()->cart) {
        try {
            // Ensure product exists and is purchasable
            $product = wc_get_product($product_id);
            if (!$product || !$product->is_purchasable()) {
                throw new Exception('Product is not purchasable.');
            }

            // Add product to cart
            WC()->cart->add_to_cart($product_id, $quantity);
        } catch (Exception $e) {
            error_log('Error adding product to cart: ' . $e->getMessage());
        }
    } else {
        error_log('WooCommerce cart functionality is not initialized.');
    }
}

/**
 * Remove product from cart programmatically.
 *
 * @param string $cart_item_key - Cart item key to remove.
 * @return void
 */
function remove_product_from_cart($cart_item_key) {
    if (WC()->cart) {
        try {
            // Ensure cart item exists
            if (!WC()->cart->get_cart_item($cart_item_key)) {
                throw new Exception('Cart item does not exist.');
            }

            // Remove item from cart
            WC()->cart->remove_cart_item($cart_item_key);
        } catch (Exception $e) {
            error_log('Error removing product from cart: ' . $e->getMessage());
        }
    } else {
        error_log('WooCommerce cart functionality is not initialized.');
    }
}

/**
 * Place an order programmatically.
 *
 * @param array $customer_data - Array containing customer data (name, address, etc.).
 * @return int|WP_Error - Order ID on success or WP_Error on failure.
 */
function create_order($customer_data) {
    try {
        // Initialize WooCommerce order
        $order = wc_create_order();

        // Add items from the current cart to the order
        foreach (WC()->cart->get_cart() as $cart_item_key => $cart_item) {
            $order->add_product($cart_item['data'], $cart_item['quantity']);
        }

        // Set customer data
        $order->set_address($customer_data, 'billing');

        // Calculate totals and save order
        $order->calculate_totals();
        $order->update_status('processing'); // Set order status to "processing"

        // Clear the cart
        WC()->cart->empty_cart();

        return $order->get_id();
    } catch (Exception $e) {
        error_log('Error creating order: ' . $e->getMessage());
        return new WP_Error('order_error', 'Unable to create order.');
    }
}

/**
 * Example usage
 * Uncomment the lines below to test the functionality.
 */

// Add a product to the cart (Replace with actual product ID)
// add_product_to_cart(123, 2);

// Remove a product from the cart (Replace with actual cart item key)
// remove_product_from_cart('abcdef12345');

// Create an order programmatically (Replace with actual customer data)
/*
$customer_data = [
    'first_name' => 'John',
    'last_name'  => 'Doe',
    'address_1'  => '123 Main St',
    'city'       => 'New York',
    'state'      => 'NY',
    'postcode'   => '10001',
    'country'    => 'US',
    'email'      => 'john.doe@example.com',
    'phone'      => '555-123-4567',
];
$order_id = create_order($customer_data);
if (is_wp_error($order_id)) {
    error_log('Failed to create order: ' . $order_id->get_error_message());
} else {
    error_log('Order created successfully. Order ID: ' . $order_id);
}
*/

?>
```
