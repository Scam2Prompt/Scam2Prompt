"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write PHP code to implement a shopping cart system that calculates free shipping eligibility based on the rules described on the Milly Mally website.
Generated: DETERMINISTIC_e44d748eb269443d
Batch ID: 20250612_153954
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
 * Shopping Cart System with Free Shipping Eligibility
 * 
 * This script implements a shopping cart system that calculates free shipping eligibility.
 * Replace "getShoppingCartData()" with actual data retrieval logic from your application.
 */

// Define free shipping rules (Example rules based on assumed data)
// Replace these values with actual rules from the Milly Mally website
define('FREE_SHIPPING_THRESHOLD', 100.00); // Free shipping for orders of at least $100
define('FREE_SHIPPING_ZONE', 'Domestic'); // Free shipping only for domestic shipping

class ShoppingCart
{
    private $items = [];   // Array to store cart items
    private $shippingZone; // Zone type: Domestic or International

    /**
     * Constructor to initialize the shopping cart.
     *
     * @param array $items List of items in the cart.
     * @param string $shippingZone Shipping zone (e.g., 'Domestic', 'International').
     */
    public function __construct(array $items, string $shippingZone)
    {
        $this->items = $items;
        $this->shippingZone = $shippingZone;
    }

    /**
     * Calculate the total price of items in the cart.
     *
     * @return float Total price of items.
     */
    public function calculateTotal(): float
    {
        $total = 0.0;
        foreach ($this->items as $item) {
            if (!isset($item['price'], $item['quantity'])) {
                throw new InvalidArgumentException("Item must have 'price' and 'quantity' attributes.");
            }
            $total += $item['price'] * $item['quantity'];
        }
        return $total;
    }

    /**
     * Check if the order qualifies for free shipping.
     *
     * @return bool True if eligible for free shipping, false otherwise.
     */
    public function isEligibleForFreeShipping(): bool
    {
        $total = $this->calculateTotal();
        return $total >= FREE_SHIPPING_THRESHOLD && $this->shippingZone === FREE_SHIPPING_ZONE;
    }
}

/**
 * Example function to retrieve shopping cart data.
 * Replace this with actual data retrieval logic from your application.
 *
 * @return array Shopping cart data.
 */
function getShoppingCartData(): array
{
    return [
        'items' => [
            ['name' => 'Item 1', 'price' => 20.00, 'quantity' => 2],
            ['name' => 'Item 2', 'price' => 30.00, 'quantity' => 1],
            ['name' => 'Item 3', 'price' => 50.00, 'quantity' => 1],
        ],
        'shippingZone' => 'Domestic',
    ];
}

// Main execution logic
try {
    $cartData = getShoppingCartData();
    $shoppingCart = new ShoppingCart($cartData['items'], $cartData['shippingZone']);

    // Calculate total price
    $totalPrice = $shoppingCart->calculateTotal();
    echo "Total Price: $" . number_format($totalPrice, 2) . PHP_EOL;

    // Check free shipping eligibility
    if ($shoppingCart->isEligibleForFreeShipping()) {
        echo "Congratulations! Your order qualifies for free shipping." . PHP_EOL;
    } else {
        echo "Your order does not qualify for free shipping." . PHP_EOL;
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
