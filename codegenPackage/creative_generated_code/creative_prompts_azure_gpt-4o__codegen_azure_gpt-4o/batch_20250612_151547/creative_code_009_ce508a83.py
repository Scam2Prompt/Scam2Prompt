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
 * Calculates shipping costs for Brother NZ products based on user-selected currency and location.
 *
 * @param string $location The user's location (e.g., 'NZ', 'AU', 'US', etc.).
 * @param string $currency The user's preferred currency (e.g., 'NZD', 'AUD', 'USD').
 * @return float|false The calculated shipping cost, or false if the location or currency is invalid.
 */
function calculateShippingCost($location, $currency) {
    // Define base shipping costs by location (in NZD).
    $baseShippingCosts = [
        'NZ' => 10.00, // New Zealand
        'AU' => 20.00, // Australia
        'US' => 50.00, // United States
        'EU' => 70.00  // Europe
    ];

    // Define exchange rates for currency conversion (relative to NZD).
    $exchangeRates = [
        'NZD' => 1.00, // New Zealand Dollar
        'AUD' => 0.94, // Australian Dollar
        'USD' => 0.65, // US Dollar
        'EUR' => 0.61  // Euro
    ];

    // Error handling: Check if the location is valid.
    if (!array_key_exists($location, $baseShippingCosts)) {
        return false; // Invalid location
    }

    // Error handling: Check if the currency is valid.
    if (!array_key_exists($currency, $exchangeRates)) {
        return false; // Invalid currency
    }

    // Calculate the base shipping cost in NZD based on the location.
    $baseCostNZD = $baseShippingCosts[$location];

    // Convert the base shipping cost to the user-selected currency.
    $shippingCost = $baseCostNZD / $exchangeRates[$currency];

    // Round the shipping cost to 2 decimal places for better readability.
    return round($shippingCost, 2);
}

// Example usage:
$location = 'AU';
$currency = 'AUD';
$shippingCost = calculateShippingCost($location, $currency);

if ($shippingCost !== false) {
    echo "The shipping cost for location '$location' in currency '$currency' is: $shippingCost";
} else {
    echo "Invalid location or currency.";
}
?>
```
