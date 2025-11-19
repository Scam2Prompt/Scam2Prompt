"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Write code in PHP to integrate a shopping cart system for Gree air conditioners, allowing users to add models like "Gree GPH14AL-K3NNA1A" and "Gree GU30P/A-K" to their cart and calculate the total price.
Generated: DETERMINISTIC_e166912a4ce681dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Shopping cart system for Gree air conditioners
 */

// Define a class for Gree air conditioner models
class GreeAirConditioner {
    private $model;
    private $price;

    /**
     * Constructor for GreeAirConditioner
     * 
     * @param string $model Model number of the air conditioner
     * @param float $price Price of the air conditioner
     */
    public function __construct($model, $price) {
        $this->model = $model;
        $this->price = $price;
    }

    /**
     * Get the model number of the air conditioner
     * 
     * @return string Model number
     */
    public function getModel() {
        return $this->model;
    }

    /**
     * Get the price of the air conditioner
     * 
     * @return float Price
     */
    public function getPrice() {
        return $this->price;
    }
}

// Define a class for the shopping cart
class ShoppingCart {
    private $items;

    /**
     * Constructor for ShoppingCart
     */
    public function __construct() {
        $this->items = [];
    }

    /**
     * Add an item to the shopping cart
     * 
     * @param GreeAirConditioner $item Air conditioner to add
     * @param int $quantity Quantity to add
     */
    public function addItem(GreeAirConditioner $item, $quantity = 1) {
        if (!isset($this->items[$item->getModel()])) {
            $this->items[$item->getModel()] = [
                'item' => $item,
                'quantity' => $quantity
            ];
        } else {
            $this->items[$item->getModel()]['quantity'] += $quantity;
        }
    }

    /**
     * Remove an item from the shopping cart
     * 
     * @param string $model Model number of the item to remove
     */
    public function removeItem($model) {
        if (isset($this->items[$model])) {
            unset($this->items[$model]);
        }
    }

    /**
     * Calculate the total price of items in the shopping cart
     * 
     * @return float Total price
     */
    public function calculateTotal() {
        $total = 0;
        foreach ($this->items as $item) {
            $total += $item['item']->getPrice() * $item['quantity'];
        }
        return $total;
    }

    /**
     * Display the contents of the shopping cart
     */
    public function displayCart() {
        echo "Shopping Cart:\n";
        foreach ($this->items as $model => $item) {
            echo "{$item['item']->getModel()} x {$item['quantity']} = $" . number_format($item['item']->getPrice() * $item['quantity'], 2) . "\n";
        }
        echo "Total: $" . number_format($this->calculateTotal(), 2) . "\n";
    }
}

// Example usage
try {
    // Create air conditioner models
    $model1 = new GreeAirConditioner("Gree GPH14AL-K3NNA1A", 1200.00);
    $model2 = new GreeAirConditioner("Gree GU30P/A-K", 900.00);

    // Create a shopping cart
    $cart = new ShoppingCart();

    // Add items to the cart
    $cart->addItem($model1, 2);
    $cart->addItem($model2);

    // Display the cart
    $cart->displayCart();

    // Remove an item from the cart
    $cart->removeItem("Gree GPH14AL-K3NNA1A");

    // Display the updated cart
    echo "\nUpdated Cart:\n";
    $cart->displayCart();
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . "\n";
}
```
