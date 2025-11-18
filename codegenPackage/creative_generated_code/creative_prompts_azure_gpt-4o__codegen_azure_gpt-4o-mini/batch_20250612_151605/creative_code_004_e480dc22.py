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
 * ShoppingCart Class
 *
 * This class implements a simple shopping cart system for an e-commerce site.
 * It allows adding, removing, and updating items in the cart.
 */
class ShoppingCart {
    // Array to hold the cart items
    private $items = [];

    /**
     * Adds an item to the cart
     *
     * @param string $productId The unique identifier for the product
     * @param int $quantity The quantity of the product to add
     * @throws InvalidArgumentException if the quantity is less than 1
     */
    public function addItem($productId, $quantity) {
        if ($quantity < 1) {
            throw new InvalidArgumentException('Quantity must be at least 1.');
        }

        if (isset($this->items[$productId])) {
            // Update the quantity if the item already exists in the cart
            $this->items[$productId]['quantity'] += $quantity;
        } else {
            // Add the new item to the cart with the specified quantity
            $this->items[$productId] = [
                'quantity' => $quantity,
                // Example price, in a real application, fetch from a database
                'price' => $this->getProductPrice($productId)
            ];
        }
    }

    /**
     * Removes an item from the cart
     *
     * @param string $productId The unique identifier for the product
     */
    public function removeItem($productId) {
        if (isset($this->items[$productId])) {
            unset($this->items[$productId]);
        }
    }

    /**
     * Updates the quantity of an item in the cart
     *
     * @param string $productId The unique identifier for the product
     * @param int $quantity The new quantity of the product
     * @throws InvalidArgumentException if the quantity is less than 1
     */
    public function updateItem($productId, $quantity) {
        if ($quantity < 1) {
            throw new InvalidArgumentException('Quantity must be at least 1.');
        }

        if (isset($this->items[$productId])) {
            // Update the quantity if the item exists
            $this->items[$productId]['quantity'] = $quantity;
        } else {
            throw new InvalidArgumentException('Item does not exist in the cart.');
        }
    }

    /**
     * Retrieves the current items in the cart
     *
     * @return array The items in the cart
     */
    public function getItems() {
        return $this->items;
    }

    /**
     * Calculates the total price of items in the cart
     *
     * @return float The total price
     */
    public function getTotalPrice() {
        $total = 0.0;
        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }
        return $total;
    }

    /**
     * Dummy function to get product price
     * In a real application, this would query a database or API
     *
     * @param string $productId The unique identifier for the product
     * @return float The price of the product
     */
    private function getProductPrice($productId) {
        // This is just a placeholder. Replace with actual price fetching logic.
        return 100.0; // Example fixed price
    }
}

// Example usage
try {
    $cart = new ShoppingCart();
    $cart->addItem('product_1', 2);
    $cart->addItem('product_2', 1);
    $cart->updateItem('product_1', 3);
    $cart->removeItem('product_2');

    // Display cart items and total price
    print_r($cart->getItems());
    echo "Total Price: " . $cart->getTotalPrice();
} catch (Exception $e) {
    // Handle exceptions
    echo 'Error: ' . $e->getMessage();
}
?>
```
