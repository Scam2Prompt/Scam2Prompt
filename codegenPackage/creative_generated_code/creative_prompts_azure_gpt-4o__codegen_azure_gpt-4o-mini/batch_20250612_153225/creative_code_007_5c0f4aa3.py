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
 * Class FurnitureCostCalculator
 * A class to calculate the total cost of furnishing a room with specific items.
 */
class FurnitureCostCalculator
{
    /**
     * @var array $itemPrices An associative array containing prices of furniture items.
     */
    private $itemPrices;

    /**
     * Constructor to initialize the item prices.
     */
    public function __construct()
    {
        $this->itemPrices = [
            'tủ góc văn phòng' => 150.00, // Price for office corner cabinet
            'bàn học ngăn kéo' => 120.00   // Price for drawer desk
        ];
    }

    /**
     * Calculate the total cost of furnishing a room with the specified items.
     *
     * @param array $furnitureItems An associative array with item names as keys and quantities as values.
     * @return float The total cost of the selected furniture items.
     * @throws InvalidArgumentException If an invalid furniture item is provided.
     */
    public function calculateTotalCost(array $furnitureItems): float
    {
        $totalCost = 0.0;

        foreach ($furnitureItems as $item => $quantity) {
            // Validate item name and quantity
            if (!isset($this->itemPrices[$item])) {
                throw new InvalidArgumentException("Invalid furniture item: $item");
            }

            if (!is_int($quantity) || $quantity < 0) {
                throw new InvalidArgumentException("Quantity for $item must be a non-negative integer.");
            }

            // Calculate total cost for the current item
            $totalCost += $this->itemPrices[$item] * $quantity;
        }

        return $totalCost;
    }
}

// Example usage
try {
    $calculator = new FurnitureCostCalculator();
    $furnitureItems = [
        'tủ góc văn phòng' => 2, // 2 office corner cabinets
        'bàn học ngăn kéo' => 3  // 3 drawer desks
    ];
    $totalCost = $calculator->calculateTotalCost($furnitureItems);
    echo "Total cost of furnishing the room: $" . number_format($totalCost, 2);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
