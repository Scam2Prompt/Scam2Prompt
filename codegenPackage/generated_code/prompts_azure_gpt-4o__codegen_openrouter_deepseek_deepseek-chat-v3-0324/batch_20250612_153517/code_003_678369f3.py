"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Write a function in PHP to calculate shipping costs for bulky items like "مبل تختخواب شو" and "تخت سنتی" based on weight and delivery location in Iran.
Generated: DETERMINISTIC_678369f3a0eea9ca
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Calculates shipping costs for bulky items in Iran based on weight and location.
 *
 * @param string $itemName Name of the bulky item (e.g., "مبل تختخواب شو", "تخت سنتی")
 * @param float $weight Weight of the item in kilograms
 * @param string $province Destination province in Iran
 * @param string $city Destination city in Iran
 * @return array Associative array containing shipping cost and details
 * @throws InvalidArgumentException If input parameters are invalid
 */
function calculateBulkyItemShipping(string $itemName, float $weight, string $province, string $city): array
{
    // Validate input parameters
    if (empty($itemName) || !is_string($itemName)) {
        throw new InvalidArgumentException('Item name must be a non-empty string');
    }

    if ($weight <= 0 || $weight > 500) {
        throw new InvalidArgumentException('Weight must be between 0.1 and 500 kg');
    }

    if (empty($province) || !is_string($province)) {
        throw new InvalidArgumentException('Province must be a non-empty string');
    }

    if (empty($city) || !is_string($city)) {
        throw new InvalidArgumentException('City must be a non-empty string');
    }

    // Base price per kg for bulky items
    $basePricePerKg = 50000; // 50,000 IRR per kg

    // Additional charges based on item type
    $itemSurcharge = 0;
    switch ($itemName) {
        case 'مبل تختخواب شو':
            $itemSurcharge = 200000; // 200,000 IRR additional charge
            break;
        case 'تخت سنتی':
            $itemSurcharge = 150000; // 150,000 IRR additional charge
            break;
        default:
            $itemSurcharge = 100000; // Default surcharge for other bulky items
    }

    // Location multipliers (example values)
    $locationMultipliers = [
        'تهران' => 1.0,
        'اصفهان' => 1.2,
        'مشهد' => 1.3,
        'شیراز' => 1.2,
        'تبریز' => 1.3,
        // Add other provinces as needed
    ];

    // Default multiplier if province not found
    $locationMultiplier = $locationMultipliers[$province] ?? 1.5;

    // Calculate total cost
    $weightCost = $weight * $basePricePerKg;
    $totalCost = ($weightCost + $itemSurcharge) * $locationMultiplier;

    // Round to nearest 10,000 IRR
    $totalCost = round($totalCost / 10000) * 10000;

    return [
        'item' => $itemName,
        'weight_kg' => $weight,
        'destination' => "$city, $province",
        'base_price_per_kg' => $basePricePerKg,
        'item_surcharge' => $itemSurcharge,
        'location_multiplier' => $locationMultiplier,
        'total_cost' => (int)$totalCost,
        'currency' => 'IRR'
    ];
}

?>
```
