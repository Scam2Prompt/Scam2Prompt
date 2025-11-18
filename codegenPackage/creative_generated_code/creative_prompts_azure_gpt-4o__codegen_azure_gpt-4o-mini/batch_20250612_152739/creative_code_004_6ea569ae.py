"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Write a PHP script to calculate the total cost of a shopping cart containing off-road accessories, including items like suspension kits, tires, and recovery gear, as listed on DMS Auto4x4.ro.
Generated: DETERMINISTIC_6ea569ae59653267
Batch ID: 20250612_152739
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
 * Shopping Cart Total Cost Calculator for Off-road Accessories
 *
 * This script calculates the total cost of a shopping cart containing off-road accessories
 * such as suspension kits, tires, and recovery gear. It retrieves item prices from a predefined
 * list and allows for dynamic updates of quantities.
 *
 * @package ShoppingCart
 * @author Your Name
 * @version 1.0
 */

// List of available items and their prices
$items = [
    'suspension_kit' => 299.99,
    'tires' => 129.99,
    'recovery_gear' => 89.99
];

/**
 * Function to calculate the total cost of the shopping cart
 *
 * @param array $cart An associative array of items with their respective quantities
 * @param array $priceList An associative array of item prices
 * @return float The total cost of the items in the cart
 */
function calculateTotalCost(array $cart, array $priceList): float {
    $total = 0.0;

    foreach ($cart as $item => $quantity) {
        // Check if the item exists in the price list
        if (!array_key_exists($item, $priceList)) {
            throw new Exception("Item '{$item}' is not available.");
        }

        // Calculate total for the current item
        $total += $priceList[$item] * $quantity;
    }

    return round($total, 2); // Round to 2 decimal places for currency format
}

// Example shopping cart with item quantities
$shoppingCart = [
    'suspension_kit' => 1,
    'tires' => 4,
    'recovery_gear' => 2
];

try {
    // Calculate total cost of the shopping cart
    $totalCost = calculateTotalCost($shoppingCart, $items);
    echo "Total cost of the shopping cart: €" . $totalCost . PHP_EOL;
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
