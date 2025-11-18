"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Write a function in PHP to calculate the cost of furnishing a room with items from Nội thất Viva, including "tủ góc văn phòng" (office corner cabinets) and "bàn học ngăn kéo" (drawer desks).
Generated: DETERMINISTIC_5c0f4aa340b2fd40
Batch ID: 20250612_153225
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
 * Calculates the total cost of furnishing a room with items from Nội thất Viva.
 * 
 * @param array $items List of items to furnish the room.
 *                     Example format:
 *                     [
 *                         ['name' => 'tủ góc văn phòng', 'price' => 5000000, 'quantity' => 2],
 *                         ['name' => 'bàn học ngăn kéo', 'price' => 3000000, 'quantity' => 1]
 *                     ]
 * @return string Total cost formatted as currency in VND (Việt Nam Đồng).
 * @throws InvalidArgumentException If any item data is invalid.
 */
function calculateFurnishingCost(array $items): string {
    // Validate input data
    foreach ($items as $item) {
        if (!isset($item['name'], $item['price'], $item['quantity'])) {
            throw new InvalidArgumentException('Each item must have a name, price, and quantity.');
        }
        if (!is_string($item['name']) || !is_numeric($item['price']) || !is_int($item['quantity'])) {
            throw new InvalidArgumentException('Invalid item data. Ensure name is a string, price is numeric, and quantity is an integer.');
        }
        if ($item['price'] < 0 || $item['quantity'] <= 0) {
            throw new InvalidArgumentException('Price must be non-negative and quantity must be positive.');
        }
    }

    // Calculate total cost
    $totalCost = 0;
    foreach ($items as $item) {
        $totalCost += $item['price'] * $item['quantity'];
    }

    // Format total cost as currency in VND
    return number_format($totalCost, 0, ',', '.') . ' VND';
}

// Example usage
try {
    $items = [
        ['name' => 'tủ góc văn phòng', 'price' => 5000000, 'quantity' => 2],
        ['name' => 'bàn học ngăn kéo', 'price' => 3000000, 'quantity' => 1],
    ];
    echo calculateFurnishingCost($items); // Outputs: 13,000,000 VND
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
