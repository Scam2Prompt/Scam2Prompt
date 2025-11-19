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
 * Class ShippingCalculator
 * This class provides methods to calculate shipping costs based on weight and destination.
 */
class ShippingCalculator
{
    private $baseRate; // Base shipping rate
    private $weightRate; // Rate per weight unit
    private $destinationRates; // Array of destination-specific rates

    /**
     * Constructor to initialize shipping rates.
     *
     * @param float $baseRate Base shipping rate
     * @param float $weightRate Rate per weight unit
     * @param array $destinationRates Array of destination-specific rates
     */
    public function __construct($baseRate, $weightRate, $destinationRates)
    {
        $this->baseRate = $baseRate;
        $this->weightRate = $weightRate;
        $this->destinationRates = $destinationRates;
    }

    /**
     * Calculate the shipping cost based on weight and destination.
     *
     * @param float $weight Weight of the package
     * @param string $destination Destination of the package
     * @return float|false Shipping cost or false on error
     */
    public function calculateShippingCost($weight, $destination)
    {
        // Validate weight
        if ($weight <= 0) {
            throw new InvalidArgumentException("Weight must be a positive number.");
        }

        // Validate destination
        if (!array_key_exists($destination, $this->destinationRates)) {
            throw new InvalidArgumentException("Invalid destination provided.");
        }

        // Calculate shipping cost
        $destinationRate = $this->destinationRates[$destination];
        $shippingCost = $this->baseRate + ($this->weightRate * $weight) + $destinationRate;

        return round($shippingCost, 2); // Round to 2 decimal places
    }
}

// Example usage
try {
    // Initialize shipping calculator with base rate, weight rate, and destination rates
    $baseRate = 5.00; // Base shipping rate
    $weightRate = 1.50; // Rate per weight unit
    $destinationRates = [
        'local' => 2.00,
        'national' => 5.00,
        'international' => 10.00
    ];

    $shippingCalculator = new ShippingCalculator($baseRate, $weightRate, $destinationRates);

    // Example input
    $weight = 10; // Weight in kg
    $destination = 'national'; // Destination

    // Calculate shipping cost
    $cost = $shippingCalculator->calculateShippingCost($weight, $destination);
    echo "Shipping cost: $" . $cost . "\n";

} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
