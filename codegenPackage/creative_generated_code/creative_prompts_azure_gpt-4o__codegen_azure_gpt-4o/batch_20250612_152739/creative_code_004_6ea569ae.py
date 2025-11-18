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
 * Shopping Cart Calculation Script
 * 
 * This script calculates the total cost of a shopping cart containing off-road accessories.
 * Items, quantities, and prices are hardcoded for demonstration purposes.
 * 
 * Author: Professional Software Developer
 * Date: [Insert Date]
 */

// Define shopping cart items (mock data)
$shoppingCart = [
    ['name' => 'Suspension Kit', 'price' => 1200.00, 'quantity' => 1],
    ['name' => 'Off-Road Tires', 'price' => 250.00, 'quantity' => 4],
    ['name' => 'Recovery Gear', 'price' => 150.00, 'quantity' => 2],
];

/**
 * Function to calculate total cost of the shopping cart
 * 
 * @param array $cart List of items in the shopping cart
 * @return float Total cost of all items in the cart
 */
function calculateTotalCost($cart) {
    $totalCost = 0.0;

    foreach ($cart as $item) {
        // Validate item structure to ensure correct calculation
        if (!isset($item['price']) || !isset($item['quantity'])) {
            throw new Exception("Invalid item structure in cart.");
        }

        // Calculate line cost and add to total
        $lineCost = $item['price'] * $item['quantity'];
        $totalCost += $lineCost;
    }

    return $totalCost;
}

// Error handling for script execution
try {
    // Calculate total cost of the shopping cart
    $totalCost = calculateTotalCost($shoppingCart);

    // Display the total cost
    echo "The total cost of your shopping cart is: $" . number_format($totalCost, 2) . "\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
