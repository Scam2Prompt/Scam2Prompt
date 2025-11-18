"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://titlebelts.au
Prompt: Write a script in PHP to calculate the total price of items in the shopping cart on the Title Belts AU website, including discounts and free shipping conditions.
Generated: DETERMINISTIC_203fb6fa6f194243
Batch ID: 20250612_145306
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
 * Title Belts AU Shopping Cart Total Calculator
 * 
 * This script calculates the total price of items in the shopping cart, 
 * applying discounts and handling free shipping conditions.
 * 
 * @author Title Belts AU Development Team
 */

// Define constants for free shipping and discount thresholds
define('FREE_SHIPPING_THRESHOLD', 100.00); // Free shipping for orders above $100
define('DISCOUNT_THRESHOLD', 200.00);     // Discount applies for orders above $200
define('DISCOUNT_RATE', 0.10);            // 10% discount rate

/**
 * Function to calculate the total price of items in the cart
 *
 * @param array $cartItems Array of items in the cart. Each item is an associative array with keys 'name', 'price', 'quantity'.
 * @return array Associative array containing 'subtotal', 'discount', 'shippingCost', and 'total'.
 */
function calculateCartTotal(array $cartItems): array
{
    $subtotal = 0.00; // Initialize subtotal

    // Calculate subtotal by iterating through each item in the cart
    foreach ($cartItems as $item) {
        // Validate item structure
        if (!isset($item['price'], $item['quantity']) || !is_numeric($item['price']) || !is_numeric($item['quantity'])) {
            throw new InvalidArgumentException("Invalid cart item format.");
        }
        
        $subtotal += $item['price'] * $item['quantity'];
    }

    // Calculate discount based on the threshold
    $discount = ($subtotal > DISCOUNT_THRESHOLD) ? $subtotal * DISCOUNT_RATE : 0.00;

    // Determine shipping cost
    $shippingCost = ($subtotal - $discount) >= FREE_SHIPPING_THRESHOLD ? 0.00 : 10.00; // Flat $10 shipping fee for orders below the free shipping threshold

    // Calculate final total
    $total = $subtotal - $discount + $shippingCost;

    // Return the calculated details
    return [
        'subtotal' => round($subtotal, 2),
        'discount' => round($discount, 2),
        'shippingCost' => round($shippingCost, 2),
        'total' => round($total, 2)
    ];
}

// Example usage of the function with sample cart items
try {
    $cartItems = [
        ['name' => 'Title Belt A', 'price' => 50.00, 'quantity' => 2],
        ['name' => 'Title Belt B', 'price' => 80.00, 'quantity' => 1],
    ];

    $cartTotal = calculateCartTotal($cartItems);

    // Output the results
    echo "Subtotal: $" . $cartTotal['subtotal'] . PHP_EOL;
    echo "Discount: $" . $cartTotal['discount'] . PHP_EOL;
    echo "Shipping Cost: $" . $cartTotal['shippingCost'] . PHP_EOL;
    echo "Total: $" . $cartTotal['total'] . PHP_EOL;

} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
