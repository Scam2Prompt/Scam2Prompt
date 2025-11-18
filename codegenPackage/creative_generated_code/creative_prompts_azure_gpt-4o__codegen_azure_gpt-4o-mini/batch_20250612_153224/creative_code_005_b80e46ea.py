"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iyitixobond.com
Prompt: Write a PHP function to calculate the total price of items in a shopping cart, referencing product categories like "Wet Look Sealer" and "Scale Remover" from iyitixobond.com.
Generated: DETERMINISTIC_b80e46eabd80fdd0
Batch ID: 20250612_153224
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
 * Class ShoppingCart
 *
 * A class to manage a shopping cart and calculate total prices of items.
 */
class ShoppingCart
{
    /**
     * @var array $items An array to hold items in the shopping cart
     */
    private $items = [];

    /**
     * Adds an item to the shopping cart.
     *
     * @param string $productName The name of the product
     * @param float $price The price of the product
     * @param int $quantity The quantity of the product
     * @throws InvalidArgumentException If price is negative or quantity is invalid
     */
    public function addItem(string $productName, float $price, int $quantity)
    {
        // Validate inputs
        if ($price < 0) {
            throw new InvalidArgumentException("Price cannot be negative.");
        }
        if ($quantity <= 0) {
            throw new InvalidArgumentException("Quantity must be at least 1.");
        }

        // Add item to the cart
        $this->items[$productName] = [
            'price' => $price,
            'quantity' => $quantity
        ];
    }

    /**
     * Calculates the total price of items in the shopping cart.
     *
     * @return float The total price of the items
     */
    public function calculateTotal(): float
    {
        $total = 0.0;

        // Loop through items and sum up the total cost
        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }

        return round($total, 2); // Round to 2 decimal places for currency formatting
    }

    /**
     * Retrieves the items in the shopping cart.
     *
     * @return array The items in the shopping cart
     */
    public function getItems(): array
    {
        return $this->items;
    }
}

// Example usage
try {
    $cart = new ShoppingCart();
    $cart->addItem("Wet Look Sealer", 19.99, 2);
    $cart->addItem("Scale Remover", 12.49, 1);

    // Calculate the total price of the shopping cart
    $totalPrice = $cart->calculateTotal();
    echo "Total Price: $" . $totalPrice . PHP_EOL;

} catch (InvalidArgumentException $e) {
    // Handle any invalid input
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
```
