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
 * Class ShippingCalculator
 * This class provides functionality to calculate shipping costs for bulky items based on weight and delivery location.
 */
class ShippingCalculator
{
    // Define shipping cost per kilogram based on location
    private const BASE_COST = 50000; // Base cost in IRR per kilogram
    private const LOCATION_MULTIPLIER = [
        'Tehran' => 1.0,
        'Isfahan' => 1.2,
        'Tabriz' => 1.5,
        'Shiraz' => 1.3,
        'Other' => 1.8,
    ];

    /**
     * Calculate shipping cost for a bulky item.
     *
     * @param float $weight Weight of the item in kilograms.
     * @param string $location Delivery location in Iran.
     * @return float Shipping cost in IRR.
     * @throws InvalidArgumentException If weight is non-positive or location is invalid.
     */
    public function calculateShippingCost(float $weight, string $location): float
    {
        // Validate weight
        if ($weight <= 0) {
            throw new InvalidArgumentException('Weight must be a positive number.');
        }

        // Validate location and get the multiplier
        $multiplier = $this->getLocationMultiplier($location);

        // Calculate the shipping cost
        $cost = self::BASE_COST * $weight * $multiplier;

        return round($cost, 2); // Round to 2 decimal places
    }

    /**
     * Get the cost multiplier based on the delivery location.
     *
     * @param string $location Delivery location.
     * @return float Multiplier for the given location.
     * @throws InvalidArgumentException If location is invalid.
     */
    private function getLocationMultiplier(string $location): float
    {
        $location = ucfirst(strtolower($location)); // Normalize location string

        if (!array_key_exists($location, self::LOCATION_MULTIPLIER)) {
            throw new InvalidArgumentException('Invalid location specified.');
        }

        return self::LOCATION_MULTIPLIER[$location];
    }
}

// Example usage:
try {
    $shippingCalculator = new ShippingCalculator();
    $weight = 150; // Weight in kilograms
    $location = 'Tehran'; // Delivery location
    $shippingCost = $shippingCalculator->calculateShippingCost($weight, $location);
    
    echo "The shipping cost for $weight kg to $location is: " . number_format($shippingCost) . " IRR";
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
```
