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
 * Shopping Cart Class
 * Represents a simple shopping cart system implementing free shipping eligibility.
 */
class ShoppingCart {
    private $items = [];
    private $totalPrice = 0.0;
    private $shippingThreshold = 100.00; // Define threshold for free shipping

    /**
     * Adds an item to the cart.
     *
     * @param string $itemName Name of the item
     * @param float $itemPrice Price of the item
     * @param int $quantity Quantity to add
     * @throws InvalidArgumentException If item price or quantity is invalid
     */
    public function addItem($itemName, $itemPrice, $quantity) {
        if ($itemPrice < 0 || $quantity < 1) {
            throw new InvalidArgumentException('Item price must be non-negative and quantity must be at least 1.');
        }

        $this->items[$itemName] = [
            'price' => $itemPrice,
            'quantity' => $quantity
        ];

        $this->totalPrice += $itemPrice * $quantity;
    }

    /**
     * Removes an item from the cart.
     *
     * @param string $itemName Name of the item
     * @throws InvalidArgumentException If the item does not exist in the cart
     */
    public function removeItem($itemName) {
        if (!isset($this->items[$itemName])) {
            throw new InvalidArgumentException('Item does not exist in the cart.');
        }

        $this->totalPrice -= $this->items[$itemName]['price'] * $this->items[$itemName]['quantity'];
        unset($this->items[$itemName]);
    }

    /**
     * Calculates the total price of items in the cart.
     *
     * @return float Total price
     */
    public function getTotalPrice() {
        return $this->totalPrice;
    }

    /**
     * Checks if the cart is eligible for free shipping.
     *
     * @return bool True if eligible for free shipping, otherwise false
     */
    public function isEligibleForFreeShipping() {
        return $this->totalPrice >= $this->shippingThreshold;
    }

    /**
     * Displays the items in the cart.
     *
     * @return array Items in the cart
     */
    public function getItems() {
        return $this->items;
    }
}

// Example usage
try {
    // Create a shopping cart instance
    $cart = new ShoppingCart();

    // Add items to the cart
    $cart->addItem('Laptop', 950.00, 1);
    $cart->addItem('Mouse', 25.00, 2);

    // Display total price
    echo "Total Price: $" . number_format($cart->getTotalPrice(), 2) . "\n";

    // Check for free shipping eligibility
    if ($cart->isEligibleForFreeShipping()) {
        echo "You are eligible for free shipping!\n";
    } else {
        echo "You are not eligible for free shipping.\n";
    }

    // Remove an item
    $cart->removeItem('Mouse');

    // Display updated cart items
    print_r($cart->getItems());

} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
