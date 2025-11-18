"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a function in PHP to calculate shipping costs for bulky items like "مبل تختخواب شو" and "تخت سنتی" based on weight and delivery location in Iran.
Generated: DETERMINISTIC_678369f3a0eea9ca
Batch ID: 20250612_153517
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
 * Calculate shipping costs for bulky items based on weight and delivery location in Iran.
 *
 * @param string $itemName Name of the item (e.g., "مبل تختخواب شو", "تخت سنتی").
 * @param float $weight Weight of the item in kilograms.
 * @param string $location Delivery location in Iran.
 * @return float|int Shipping cost in Iranian Rial or -1 if an error occurs.
 */
function calculateShippingCost($itemName, $weight, $location)
{
    // Define shipping rates per kilogram for different regions in Iran
    $shippingRates = [
        'Tehran' => 8000,       // Tehran: 8,000 Rial per kg
        'Isfahan' => 7000,      // Isfahan: 7,000 Rial per kg
        'Shiraz' => 7500,       // Shiraz: 7,500 Rial per kg
        'Mashhad' => 6000,      // Mashhad: 6,000 Rial per kg
        'Tabriz' => 6500,       // Tabriz: 6,500 Rial per kg
        'Other' => 9000         // Other locations: 9,000 Rial per kg
    ];

    // Validate weight
    if ($weight <= 0) {
        error_log("Invalid weight: $weight");
        return -1; // Error code for invalid weight
    }

    // Validate location
    if (!array_key_exists($location, $shippingRates)) {
        $location = 'Other'; // Default to 'Other' if the location is not found
    }

    // Calculate base cost
    $baseCost = $weight * $shippingRates[$location];

    // Add an additional bulky item fee (e.g., 20% surcharge)
    $bulkyItemFee = 0.2 * $baseCost;

    // Calculate total shipping cost
    $totalCost = $baseCost + $bulkyItemFee;

    return $totalCost;
}

// Example usage:
$itemName = "مبل تختخواب شو";
$weight = 50.0; // Weight in kilograms
$location = "Tehran";

$shippingCost = calculateShippingCost($itemName, $weight, $location);

if ($shippingCost !== -1) {
    echo "Shipping cost for '$itemName' to '$location' is: " . number_format($shippingCost) . " Rial\n";
} else {
    echo "Error calculating shipping cost.\n";
}
?>
```
