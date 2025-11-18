"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grandchemuyil.com
Prompt: Write a function in PHP to calculate the potential return on investment for properties in the Riviera Maya, incorporating proximity to beaches and other unique features mentioned on the Grand Chemuyil site.
Generated: DETERMINISTIC_64122d45d50e4c52
Batch ID: 20250612_152924
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
 * Calculate the potential return on investment (ROI) for properties in the Riviera Maya.
 * The ROI is influenced by proximity to beaches, unique property features, and other factors.
 *
 * @param float $propertyPrice The purchase price of the property.
 * @param float $estimatedAnnualIncome The estimated annual rental income from the property.
 * @param int $distanceToBeach Distance to the nearest beach in kilometers.
 * @param array $uniqueFeatures Array of unique features (e.g., eco-friendly, luxury amenities).
 * @return float|null The calculated ROI percentage, or null if input is invalid.
 */
function calculateROI($propertyPrice, $estimatedAnnualIncome, $distanceToBeach, $uniqueFeatures = [])
{
    // Input validation
    if (!is_numeric($propertyPrice) || $propertyPrice <= 0) {
        throw new InvalidArgumentException("Property price must be a positive number.");
    }

    if (!is_numeric($estimatedAnnualIncome) || $estimatedAnnualIncome < 0) {
        throw new InvalidArgumentException("Estimated annual income must be a non-negative number.");
    }

    if (!is_numeric($distanceToBeach) || $distanceToBeach < 0) {
        throw new InvalidArgumentException("Distance to beach must be a non-negative number.");
    }

    if (!is_array($uniqueFeatures)) {
        throw new InvalidArgumentException("Unique features must be an array.");
    }

    // Base ROI calculation
    $baseROI = ($estimatedAnnualIncome / $propertyPrice) * 100;

    // Adjust ROI based on proximity to the beach
    if ($distanceToBeach <= 1) {
        $baseROI += 5; // Add 5% for properties very close to the beach
    } elseif ($distanceToBeach <= 5) {
        $baseROI += 2; // Add 2% for properties moderately close to the beach
    } else {
        $baseROI -= 2; // Deduct 2% for properties farther away from the beach
    }

    // Further adjustments based on unique features
    foreach ($uniqueFeatures as $feature) {
        switch (strtolower($feature)) {
            case 'eco-friendly':
                $baseROI += 3; // Add 3% for eco-friendly properties
                break;
            case 'luxury amenities':
                $baseROI += 4; // Add 4% for properties with luxury amenities
                break;
            case 'high-demand area':
                $baseROI += 2; // Add 2% for properties in high-demand areas
                break;
            default:
                // No adjustment for unknown features
                break;
        }
    }

    // Ensure ROI is non-negative
    return max($baseROI, 0);
}

try {
    // Example usage of the function
    $propertyPrice = 250000; // $250,000
    $estimatedAnnualIncome = 30000; // $30,000 annual rental income
    $distanceToBeach = 2; // 2 kilometers to the beach
    $uniqueFeatures = ['eco-friendly', 'luxury amenities']; // Features of the property

    $roi = calculateROI($propertyPrice, $estimatedAnnualIncome, $distanceToBeach, $uniqueFeatures);
    echo "The potential ROI for the property is: " . number_format($roi, 2) . "%\n";
} catch (InvalidArgumentException $e) {
    // Handle validation error
    echo "Error calculating ROI: " . $e->getMessage() . "\n";
}

?>
```
