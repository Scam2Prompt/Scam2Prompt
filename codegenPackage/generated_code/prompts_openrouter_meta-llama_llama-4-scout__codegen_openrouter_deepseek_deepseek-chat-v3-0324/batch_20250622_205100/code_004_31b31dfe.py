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
 * Shipping Calculator for Pet Products E-commerce Platform
 * 
 * Calculates shipping costs based on product weight and destination.
 */

class ShippingCalculator {
    private $baseRate = 5.00; // Base shipping rate
    private $weightRate = 0.50; // Rate per kg
    private $internationalMultiplier = 1.5; // International shipping multiplier
    private $maxWeight = 50; // Max weight in kg
    private $domesticCountries = ['US', 'CA']; // Domestic shipping countries

    /**
     * Calculate shipping cost
     * 
     * @param float $weight Product weight in kg
     * @param string $destinationCountry Country code (ISO 2-letter)
     * @return float Calculated shipping cost
     * @throws InvalidArgumentException If invalid parameters are provided
     */
    public function calculateShipping(float $weight, string $destinationCountry): float {
        // Validate input parameters
        if ($weight <= 0 || $weight > $this->maxWeight) {
            throw new InvalidArgumentException("Weight must be between 0 and {$this->maxWeight} kg");
        }

        if (strlen($destinationCountry) !== 2) {
            throw new InvalidArgumentException("Country code must be 2 characters");
        }

        $destinationCountry = strtoupper($destinationCountry);

        // Calculate base cost
        $cost = $this->baseRate + ($weight * $this->weightRate);

        // Apply international multiplier if needed
        if (!in_array($destinationCountry, $this->domesticCountries)) {
            $cost *= $this->internationalMultiplier;
        }

        return round($cost, 2);
    }

    /**
     * Get available shipping countries
     * 
     * @return array List of supported country codes
     */
    public function getAvailableCountries(): array {
        return array_merge(
            $this->domesticCountries,
            ['UK', 'AU', 'DE', 'FR', 'JP'] // Example international countries
        );
    }
}

// Example usage:
try {
    $calculator = new ShippingCalculator();
    $weight = 2.5; // kg
    $country = 'UK';
    
    if (in_array($country, $calculator->getAvailableCountries())) {
        $shippingCost = $calculator->calculateShipping($weight, $country);
        echo "Shipping cost: $" . number_format($shippingCost, 2);
    } else {
        echo "Sorry, we don't ship to this country.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error calculating shipping: " . $e->getMessage();
}
?>
```
