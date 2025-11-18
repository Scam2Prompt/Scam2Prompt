"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Write a PHP script that processes orders for a collectible comic book, including validation for limited stock and exclusive items like signed copies.
Generated: DETERMINISTIC_5172c0c2ca670639
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Comic book inventory configuration
$inventory = [
    "standard" => [
        "price" => 14.99,
        "stock" => 100
    ],
    "exclusive_signed_copy" => [
        "price" => 49.99,
        "stock" => 10
    ]
];

/**
 * Function to process an order
 * 
 * @param string $itemType The type of comic book being ordered (standard/exclusive_signed_copy)
 * @param int $quantity The number of items being ordered
 * @return string Order result message
 */
function processOrder($itemType, $quantity) {
    global $inventory;

    // Validate item type
    if (!isset($inventory[$itemType])) {
        return "Error: Invalid item type.";
    }

    // Validate quantity
    if ($quantity <= 0) {
        return "Error: Quantity must be greater than zero.";
    }

    // Check stock availability
    if ($quantity > $inventory[$itemType]['stock']) {
        return "Error: Insufficient stock. Only {$inventory[$itemType]['stock']} items available.";
    }

    // Calculate total cost
    $totalCost = $inventory[$itemType]['price'] * $quantity;

    // Update inventory stock
    $inventory[$itemType]['stock'] -= $quantity;

    // Return success message
    return "Order successful! You have purchased $quantity '$itemType' comic(s) for a total of \$" . number_format($totalCost, 2) . ". Remaining stock: {$inventory[$itemType]['stock']}.";
}

// Example of processing orders
try {
    // Process a standard comic order
    echo processOrder("standard", 2) . PHP_EOL;

    // Process an exclusive signed copy order
    echo processOrder("exclusive_signed_copy", 1) . PHP_EOL;

    // Handle invalid item type
    echo processOrder("invalid_type", 1) . PHP_EOL;

    // Handle insufficient stock
    echo processOrder("exclusive_signed_copy", 11) . PHP_EOL;

    // Handle invalid quantity
    echo processOrder("standard", 0) . PHP_EOL;
} catch (Exception $e) {
    // Log the error (in a real-world application, log this to a file or monitoring system)
    error_log($e->getMessage());
    echo "An unexpected error occurred. Please try again later.";
}
?>
```
