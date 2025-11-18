"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write PHP code to implement a shopping cart system for an e-commerce site like "Poly-Market.hu," including the ability to add, remove, and update items.
Generated: DETERMINISTIC_e480dc2248c06d5e
Batch ID: 20250612_151605
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
 * Shopping Cart System for an E-commerce Site
 * Features: Add, Remove, Update items in the cart
 */

/**
 * Class ShoppingCart
 * Handles cart operations such as adding, removing, and updating items
 */
class ShoppingCart
{
    private $items = []; // Stores cart items

    /**
     * Add an item to the cart
     *
     * @param string $itemId ID of the item
     * @param string $itemName Name of the item
     * @param float $price Price of the item
     * @param int $quantity Quantity of the item
     * @return void
     */
    public function addItem(string $itemId, string $itemName, float $price, int $quantity = 1): void
    {
        if ($quantity <= 0) {
            throw new InvalidArgumentException('Quantity must be greater than zero.');
        }

        if (isset($this->items[$itemId])) {
            // If item already exists, update the quantity
            $this->items[$itemId]['quantity'] += $quantity;
        } else {
            // Add new item
            $this->items[$itemId] = [
                'name' => $itemName,
                'price' => $price,
                'quantity' => $quantity,
            ];
        }
    }

    /**
     * Remove an item from the cart
     *
     * @param string $itemId ID of the item
     * @return void
     */
    public function removeItem(string $itemId): void
    {
        if (!isset($this->items[$itemId])) {
            throw new InvalidArgumentException('Item not found in the cart.');
        }

        unset($this->items[$itemId]);
    }

    /**
     * Update the quantity of an item in the cart
     *
     * @param string $itemId ID of the item
     * @param int $quantity New quantity of the item
     * @return void
     */
    public function updateItemQuantity(string $itemId, int $quantity): void
    {
        if ($quantity < 0) {
            throw new InvalidArgumentException('Quantity cannot be negative.');
        }

        if (!isset($this->items[$itemId])) {
            throw new InvalidArgumentException('Item not found in the cart.');
        }

        if ($quantity === 0) {
            // If quantity is zero, remove the item
            $this->removeItem($itemId);
        } else {
            // Update quantity
            $this->items[$itemId]['quantity'] = $quantity;
        }
    }

    /**
     * Get all items in the cart
     *
     * @return array List of items in the cart
     */
    public function getItems(): array
    {
        return $this->items;
    }

    /**
     * Get the total price of items in the cart
     *
     * @return float Total price
     */
    public function getTotalPrice(): float
    {
        $total = 0.0;

        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }

        return $total;
    }

    /**
     * Clear the cart
     *
     * @return void
     */
    public function clearCart(): void
    {
        $this->items = [];
    }
}

/** Example usage */
try {
    $cart = new ShoppingCart();

    // Add items to the cart
    $cart->addItem('item1', 'Laptop', 999.99, 1);
    $cart->addItem('item2', 'Mouse', 19.99, 2);

    // Update item quantity
    $cart->updateItemQuantity('item2', 3);

    // Remove an item
    $cart->removeItem('item1');

    // Display all items
    print_r($cart->getItems());

    // Display total price
    echo "Total Price: " . $cart->getTotalPrice() . PHP_EOL;

    // Clear the cart
    $cart->clearCart();
    print_r($cart->getItems());
} catch (Exception $e) {
    // Handle errors
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
