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
/**
 * Shopping Cart System for Gree Air Conditioners
 * This script allows users to add Gree air conditioner models to a shopping cart
 * and calculates the total price.
 */

// Define a class for the shopping cart
class ShoppingCart {
    // Array to hold items in the cart
    private $items = [];
    // Total price of items in the cart
    private $totalPrice = 0.0;

    /**
     * Adds an item to the shopping cart
     *
     * @param string $model    The model name of the air conditioner
     * @param float $price     The price of the air conditioner
     * @throws InvalidArgumentException if the price is negative
     */
    public function addItem($model, $price) {
        if ($price < 0) {
            throw new InvalidArgumentException("Price cannot be negative.");
        }

        $this->items[$model] = $price;
        $this->totalPrice += $price;
    }

    /**
     * Calculates the total price of items in the cart
     *
     * @return float Total price
     */
    public function getTotalPrice() {
        return $this->totalPrice;
    }

    /**
     * Displays the items in the cart
     *
     * @return array Items in the cart
     */
    public function getItems() {
        return $this->items;
    }

    /**
     * Clears the shopping cart
     */
    public function clearCart() {
        $this->items = [];
        $this->totalPrice = 0.0;
    }
}

// Example Usage
try {
    // Create a new shopping cart instance
    $cart = new ShoppingCart();

    // Add items to the cart
    $cart->addItem("Gree GPH14AL-K3NNA1A", 1200.99);
    $cart->addItem("Gree GU30P/A-K", 899.50);

    // Output the items in the cart
    echo "Items in your cart:\n";
    foreach ($cart->getItems() as $model => $price) {
        echo "- $model: $" . number_format($price, 2) . "\n";
    }

    // Output the total price
    echo "Total Price: $" . number_format($cart->getTotalPrice(), 2) . "\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
