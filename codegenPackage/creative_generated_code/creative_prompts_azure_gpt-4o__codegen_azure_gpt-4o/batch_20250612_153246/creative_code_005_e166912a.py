"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Write code in PHP to integrate a shopping cart system for Gree air conditioners, allowing users to add models like "Gree GPH14AL-K3NNA1A" and "Gree GU30P/A-K" to their cart and calculate the total price.
Generated: DETERMINISTIC_e166912a4ce681dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// shopping_cart.php

/**
 * Shopping Cart class to manage items in the cart and calculate total price.
 */
class ShoppingCart
{
    private $items = []; // Array to store items in the cart

    /**
     * Add an item to the cart.
     * @param string $model The model name of the product.
     * @param float  $price The price of the product.
     * @param int    $quantity The quantity of the product.
     * @return void
     */
    public function addItem(string $model, float $price, int $quantity = 1): void
    {
        if ($quantity <= 0) {
            throw new InvalidArgumentException("Quantity must be greater than zero.");
        }

        if (!isset($this->items[$model])) {
            $this->items[$model] = ['price' => $price, 'quantity' => $quantity];
        } else {
            $this->items[$model]['quantity'] += $quantity;
        }
    }

    /**
     * Calculate the total price of all items in the cart.
     * @return float Total price.
     */
    public function calculateTotalPrice(): float
    {
        $total = 0.0;

        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }

        return $total;
    }

    /**
     * Get the items in the cart.
     * @return array List of items in the cart.
     */
    public function getItems(): array
    {
        return $this->items;
    }

    /**
     * Clear all items from the cart.
     * @return void
     */
    public function clearCart(): void
    {
        $this->items = [];
    }
}

// Usage example:

try {
    // Create a new ShoppingCart instance
    $cart = new ShoppingCart();

    // Add items to the cart
    $cart->addItem("Gree GPH14AL-K3NNA1A", 1200.00, 2);
    $cart->addItem("Gree GU30P/A-K", 900.00, 1);

    // Display cart items
    echo "Items in the cart:\n";
    foreach ($cart->getItems() as $model => $details) {
        echo "- Model: $model, Price: {$details['price']}, Quantity: {$details['quantity']}\n";
    }

    // Calculate and display the total price
    $totalPrice = $cart->calculateTotalPrice();
    echo "Total Price: $$totalPrice\n";

    // Clear the cart
    $cart->clearCart();
    echo "Cart cleared.\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
```
