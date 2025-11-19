"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Develop a PHP script that lists the available auto parts, such as batteries and shock absorbers, from Distribution Pièces Service's inventory.
Generated: DETERMINISTIC_beec94269d5b31de
Batch ID: 20250612_140107
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
 * Auto Parts Inventory Script
 * 
 * This script lists the available auto parts from the "Distribution Pièces Service" inventory.
 * The inventory is fetched as a predefined array for demonstration purposes.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Define the inventory of auto parts
$inventory = [
    [
        'part_id' => 1,
        'name' => 'Battery',
        'category' => 'Electrical',
        'price' => 75.99,
        'stock' => 50
    ],
    [
        'part_id' => 2,
        'name' => 'Shock Absorber',
        'category' => 'Suspension',
        'price' => 120.50,
        'stock' => 30
    ],
    [
        'part_id' => 3,
        'name' => 'Alternator',
        'category' => 'Electrical',
        'price' => 95.00,
        'stock' => 10
    ]
];

try {
    // Check if inventory is available
    if (empty($inventory)) {
        throw new Exception('Inventory is empty. No auto parts available.');
    }
    
    // Display available auto parts
    echo "Available Auto Parts:\n";
    echo str_repeat("-", 50) . "\n";
    
    foreach ($inventory as $item) {
        // Validate that required fields exist and are non-empty
        if (!isset($item['part_id'], $item['name'], $item['category'], $item['price'], $item['stock']) ||
            empty($item['name']) || empty($item['category'])) {
            throw new Exception('Invalid inventory data detected for part ID: ' . ($item['part_id'] ?? 'Unknown'));
        }
        
        // Display part details
        echo "Part ID: {$item['part_id']}\n";
        echo "Name: {$item['name']}\n";
        echo "Category: {$item['category']}\n";
        echo "Price: \$" . number_format($item['price'], 2) . "\n";
        echo "Stock: {$item['stock']} units\n";
        echo str_repeat("-", 50) . "\n";
    }
} catch (Exception $e) {
    // Handle errors and display a user-friendly message
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
