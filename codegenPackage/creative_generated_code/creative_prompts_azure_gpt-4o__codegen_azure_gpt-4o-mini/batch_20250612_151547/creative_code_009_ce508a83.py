"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Write a function in PHP to calculate shipping costs for Brother NZ products based on user-selected currency and location.
Generated: DETERMINISTIC_ce508a83aee88afd
Batch ID: 20250612_151547
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
 *
 * A class to calculate shipping costs for Brother NZ products based on user-selected currency and location.
 */
class ShippingCalculator
{
    // Define shipping rates for different regions in NZD
    private $shippingRates = [
        'NZ' => 10.00, // New Zealand
        'AU' => 30.00, // Australia
        'US' => 50.00, // United States
        'EU' => 60.00  // Europe
    ];

    // Conversion rates to NZD for different currencies
    private $conversionRates = [
        'NZD' => 1.00,  // New Zealand Dollar
        'AUD' => 0.93,  // Australian Dollar
        'USD' => 0.67,  // US Dollar
        'EUR' => 0.59   // Euro
    ];

    /**
     * Calculate shipping cost based on location and currency
     *
     * @param string $location User's location (country code)
     * @param string $currency User's selected currency
     * @return float|null Shipping cost in the selected currency or null if invalid
     */
    public function calculateShippingCost(string $location, string $currency): ?float
    {
        // Validate location and currency
        if (!array_key_exists($location, $this->shippingRates)) {
            throw new InvalidArgumentException("Invalid location provided: $location");
        }

        if (!array_key_exists($currency, $this->conversionRates)) {
            throw new InvalidArgumentException("Invalid currency provided: $currency");
        }

        // Calculate shipping cost in NZD
        $costInNzd = $this->shippingRates[$location];

        // Convert shipping cost to selected currency
        $shippingCost = $costInNzd * $this->conversionRates[$currency];

        return round($shippingCost, 2); // Round to 2 decimal places
    }
}

// Example usage
try {
    $shippingCalculator = new ShippingCalculator();
    $cost = $shippingCalculator->calculateShippingCost('AU', 'AUD');
    echo "Shipping cost: " . $cost . " AUD";
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
