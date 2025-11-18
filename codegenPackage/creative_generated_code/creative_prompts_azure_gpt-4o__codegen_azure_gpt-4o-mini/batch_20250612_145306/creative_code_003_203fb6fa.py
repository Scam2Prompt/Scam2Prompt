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
 * Shopping Cart Class
 *
 * This class handles the shopping cart functionalities including calculating
 * the total price, applying discounts, and checking shipping conditions.
 */
class ShoppingCart
{
    // Array to hold items in the cart
    private $items = [];
    
    // Discount percentage (e.g., 10 for 10%)
    private $discountPercentage = 0;

    // Free shipping threshold
    private $freeShippingThreshold = 100.00; // Free shipping for orders over $100

    /**
     * Adds an item to the cart.
     *
     * @param string $itemName The name of the item
     * @param float $price The price of the item
     * @param int $quantity The quantity of the item
     * @throws InvalidArgumentException when quantity is less than 1
     */
    public function addItem($itemName, $price, $quantity = 1)
    {
        if ($quantity < 1) {
            throw new InvalidArgumentException('Quantity must be at least 1.');
        }

        $this->items[] = [
            'name' => $itemName,
            'price' => $price,
            'quantity' => $quantity,
        ];
    }

    /**
     * Sets the discount percentage.
     *
     * @param float $percentage The discount percentage
     * @throws InvalidArgumentException when percentage is less than 0 or greater than 100
     */
    public function setDiscount($percentage)
    {
        if ($percentage < 0 || $percentage > 100) {
            throw new InvalidArgumentException('Discount percentage must be between 0 and 100.');
        }
        
        $this->discountPercentage = $percentage;
    }

    /**
     * Calculates the total price of items in the cart.
     *
     * @return float The total price after applying discounts
     */
    public function calculateTotal()
    {
        $total = 0.0;

        // Sum the price of each item
        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }

        // Apply discount if applicable
        if ($this->discountPercentage > 0) {
            $total -= ($total * $this->discountPercentage / 100);
        }

        return $total;
    }

    /**
     * Determines if free shipping applies based on total price.
     *
     * @param float $total The total price of items
     * @return bool True if free shipping applies, otherwise false
     */
    public function isFreeShipping($total)
    {
        return $total >= $this->freeShippingThreshold;
    }
}

// Example usage
try {
    $cart = new ShoppingCart();
    $cart->addItem('Leather Belt', 35.00, 2);
    $cart->addItem('Canvas Belt', 25.00, 1);
    $cart->setDiscount(10); // Apply a 10% discount

    $totalPrice = $cart->calculateTotal();
    echo "Total Price: $" . number_format($totalPrice, 2) . "\n";

    if ($cart->isFreeShipping($totalPrice)) {
        echo "Congratulations! You qualify for free shipping.\n";
    } else {
        echo "Shipping charges will apply.\n";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage() . "\n";
}

```
