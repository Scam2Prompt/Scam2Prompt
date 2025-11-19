"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a code snippet in PHP to integrate a shipping calculator into an e-commerce platform for pet products, considering factors like weight and destination.
Generated: DETERMINISTIC_31b31dfee0b8ddcb
Batch ID: 20250622_205100
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
 * Shipping Calculator for an E-commerce Platform
 * Calculates shipping cost based on weight and destination.
 */

// Define constants for base rates and weight thresholds
define('BASE_RATE', 5.00); // Base rate in USD
define('WEIGHT_THRESHOLD', 10); // Weight threshold in kilograms
define('ADDITIONAL_RATE_PER_KG', 1.50); // Additional rate per kg above threshold
define('DESTINATION_RATES', [
    'domestic' => 1.0, // Multiplier for domestic shipping
    'international' => 2.5 // Multiplier for international shipping
]);

/**
 * Calculate shipping cost.
 *
 * @param float $weight Weight of the package in kilograms.
 * @param string $destination Destination type ('domestic' or 'international').
 * @return float Shipping cost in USD.
 * @throws InvalidArgumentException If invalid parameters are provided.
 */
function calculateShippingCost(float $weight, string $destination): float
{
    // Validate weight
    if ($weight <= 0) {
        throw new InvalidArgumentException('Weight must be greater than zero.');
    }

    // Validate destination
    if (!array_key_exists($destination, DESTINATION_RATES)) {
        throw new InvalidArgumentException('Invalid destination type. Use "domestic" or "international".');
    }

    // Calculate base cost
    $cost = BASE_RATE;

    // Add additional cost for weight above the threshold
    if ($weight > WEIGHT_THRESHOLD) {
        $additionalWeight = $weight - WEIGHT_THRESHOLD;
        $cost += $additionalWeight * ADDITIONAL_RATE_PER_KG;
    }

    // Apply destination multiplier
    $cost *= DESTINATION_RATES[$destination];

    return round($cost, 2); // Round to 2 decimal places for currency formatting
}

// Example usage
try {
    $weight = 12.5; // Weight in kilograms
    $destination = 'international'; // Destination type

    $shippingCost = calculateShippingCost($weight, $destination);
    echo "The shipping cost is: $" . $shippingCost . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid input errors
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}

?>
```
