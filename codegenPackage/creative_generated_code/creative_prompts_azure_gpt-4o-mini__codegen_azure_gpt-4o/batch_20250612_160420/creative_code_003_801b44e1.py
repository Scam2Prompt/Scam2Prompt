"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.host
Prompt: Develop a PHP script to manage an online shopping cart for self-care gifts, specifically focusing on items like gemstone jewelry and wellness gift sets.
Generated: DETERMINISTIC_801b44e13eb72828
Batch ID: 20250612_160420
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
 * Shopping Cart Management for Self-Care Gifts
 * 
 * This script provides functionality to manage an online shopping cart 
 * specifically for gemstone jewelry and wellness gift sets. 
 * Includes features for adding, removing, viewing, and calculating totals.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Start session to persist cart data
session_start();

// Initialize the shopping cart if it doesn't exist
if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

/**
 * Function to add an item to the shopping cart.
 *
 * @param string $itemId    Unique identifier for the item.
 * @param string $itemName  Name of the item.
 * @param float  $itemPrice Price of the item.
 * @param int    $itemQty   Quantity of the item.
 * @return void
 */
function addToCart($itemId, $itemName, $itemPrice, $itemQty)
{
    if (isset($_SESSION['cart'][$itemId])) {
        // If item already exists, update the quantity
        $_SESSION['cart'][$itemId]['quantity'] += $itemQty;
    } else {
        // Add new item to the cart
        $_SESSION['cart'][$itemId] = [
            'name' => $itemName,
            'price' => $itemPrice,
            'quantity' => $itemQty
        ];
    }
}

/**
 * Function to remove an item from the shopping cart.
 *
 * @param string $itemId Unique identifier for the item.
 * @return void
 */
function removeFromCart($itemId)
{
    if (isset($_SESSION['cart'][$itemId])) {
        unset($_SESSION['cart'][$itemId]);
    }
}

/**
 * Function to view the shopping cart.
 *
 * @return array Returns the current state of the cart.
 */
function viewCart()
{
    return $_SESSION['cart'];
}

/**
 * Function to calculate the total price of items in the cart.
 *
 * @return float Total price of items in the cart.
 */
function calculateTotal()
{
    $total = 0.0;
    foreach ($_SESSION['cart'] as $item) {
        $total += $item['price'] * $item['quantity'];
    }
    return $total;
}

/**
 * Error handling function to validate inputs.
 *
 * @param mixed $input       The input value to validate.
 * @param string $type       Expected type ('string', 'float', 'int').
 * @param string $fieldName  Name of the field for error message context.
 * @return bool Returns true if valid, throws exception otherwise.
 * @throws Exception
 */
function validateInput($input, $type, $fieldName)
{
    switch ($type) {
        case 'string':
            if (!is_string($input) || empty($input)) {
                throw new Exception("Invalid input for $fieldName. Must be a non-empty string.");
            }
            break;
        case 'float':
            if (!is_float($input) && !is_numeric($input)) {
                throw new Exception("Invalid input for $fieldName. Must be a float.");
            }
            break;
        case 'int':
            if (!is_int($input) && !ctype_digit($input)) {
                throw new Exception("Invalid input for $fieldName. Must be an integer.");
            }
            break;
        default:
            throw new Exception("Unknown validation type for $fieldName.");
    }
    return true;
}

// Sample Usage
try {
    // Adding items to the cart
    validateInput('item1', 'string', 'Item ID');
    validateInput('Gemstone Necklace', 'string', 'Item Name');
    validateInput(49.99, 'float', 'Item Price');
    validateInput(2, 'int', 'Item Quantity');
    addToCart('item1', 'Gemstone Necklace', 49.99, 2);

    validateInput('item2', 'string', 'Item ID');
    validateInput('Wellness Gift Set', 'string', 'Item Name');
    validateInput(29.99, 'float', 'Item Price');
    validateInput(1, 'int', 'Item Quantity');
    addToCart('item2', 'Wellness Gift Set', 29.99, 1);

    // Viewing the cart
    $cart = viewCart();
    echo "Shopping Cart:\n";
    foreach ($cart as $itemId => $item) {
        echo "Item ID: $itemId, Name: {$item['name']}, Price: {$item['price']}, Quantity: {$item['quantity']}\n";
    }

    // Calculating total
    $total = calculateTotal();
    echo "Total Price: $" . number_format($total, 2) . "\n";

    // Removing an item
    removeFromCart('item1');
    echo "Item 'item1' removed.\n";

    // Viewing updated cart
    $updatedCart = viewCart();
    echo "Updated Shopping Cart:\n";
    foreach ($updatedCart as $itemId => $item) {
        echo "Item ID: $itemId, Name: {$item['name']}, Price: {$item['price']}, Quantity: {$item['quantity']}\n";
    }

} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
