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
 * Class InvestmentCalculator
 * A class to calculate potential return on investment (ROI) for properties in the Riviera Maya.
 */
class InvestmentCalculator
{
    /**
     * Calculate the potential return on investment (ROI).
     *
     * @param float $purchasePrice The purchase price of the property.
     * @param float $annualRent The expected annual rent from the property.
     * @param float $annualAppreciationRate The expected annual appreciation rate of the property as a decimal.
     * @param int $years The number of years the investment will be held.
     * @param float $beachProximityMultiplier A multiplier based on proximity to beaches (1.0 for average, >1.0 for closer).
     * @param float $uniqueFeaturesMultiplier A multiplier for unique features provided by the property (1.0 for average).
     * 
     * @return array An associative array containing the calculated ROI and final property value.
     * 
     * @throws InvalidArgumentException If any of the input values are invalid.
     */
    public function calculateROI($purchasePrice, $annualRent, $annualAppreciationRate, $years, $beachProximityMultiplier, $uniqueFeaturesMultiplier)
    {
        // Input validation
        if ($purchasePrice <= 0 || $annualRent < 0 || $annualAppreciationRate < 0 || $years < 0 ||
            $beachProximityMultiplier <= 0 || $uniqueFeaturesMultiplier <= 0) {
            throw new InvalidArgumentException('All input values must be positive numbers, with purchase price greater than zero.');
        }

        // Calculate the final property value after a certain number of years
        $finalPropertyValue = $purchasePrice * pow((1 + $annualAppreciationRate * $beachProximityMultiplier * $uniqueFeaturesMultiplier), $years);
        
        // Calculate total rental income over the investment period
        $totalRentalIncome = $annualRent * $years;

        // Calculate ROI as the total profit divided by the purchase price
        // ROI = (Final Property Value - Purchase Price + Total Rental Income) / Purchase Price
        $roi = (($finalPropertyValue - $purchasePrice) + $totalRentalIncome) / $purchasePrice;

        return [
            'final_property_value' => round($finalPropertyValue, 2),
            'roi' => round($roi * 100, 2) // Convert to percentage
        ];
    }
}

// Example usage
try {
    $calculator = new InvestmentCalculator();
    $result = $calculator->calculateROI(200000, 18000, 0.05, 10, 1.2, 1.1);
    echo "Final Property Value: $" . $result['final_property_value'] . "\n";
    echo "Return on Investment (ROI): " . $result['roi'] . "%\n";
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
