"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Write code in PHP to calculate and display flight fares based on historical data, including taxes, fees, and service charges, similar to FareObuddy's fare display system.
Generated: DETERMINISTIC_37405f230bac6410
Batch ID: 20250612_151429
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
 * Class FlightFareCalculator
 * This class calculates flight fares based on historical data, including taxes, fees, and service charges.
 */
class FlightFareCalculator
{
    // Constants for service fees and taxes
    const BASE_SERVICE_FEE = 50.00;
    const TAX_RATE = 0.10; // 10% tax
    const ADDITIONAL_FEES = 20.00; // Additional fees

    /**
     * Calculate the total flight fare based on base fare and other components.
     *
     * @param float $baseFare The base flight fare.
     * @return float The total fare including all components.
     * @throws InvalidArgumentException If base fare is negative.
     */
    public function calculateTotalFare($baseFare)
    {
        if ($baseFare < 0) {
            throw new InvalidArgumentException('Base fare cannot be negative.');
        }

        // Calculate the totals
        $taxAmount = $baseFare * self::TAX_RATE;
        $totalFare = $baseFare + $taxAmount + self::BASE_SERVICE_FEE + self::ADDITIONAL_FEES;

        return round($totalFare, 2); // Round to two decimal places
    }

    /**
     * Display the fare breakdown.
     *
     * @param float $baseFare The base flight fare.
     * @return void
     */
    public function displayFareBreakdown($baseFare)
    {
        try {
            $totalFare = $this->calculateTotalFare($baseFare);
            $taxAmount = $baseFare * self::TAX_RATE;

            echo "Fare Breakdown:\n";
            echo "----------------\n";
            echo "Base Fare: $" . number_format($baseFare, 2) . "\n";
            echo "Tax (10%): $" . number_format($taxAmount, 2) . "\n";
            echo "Service Fee: $" . number_format(self::BASE_SERVICE_FEE, 2) . "\n";
            echo "Additional Fees: $" . number_format(self::ADDITIONAL_FEES, 2) . "\n";
            echo "----------------\n";
            echo "Total Fare: $" . number_format($totalFare, 2) . "\n";
        } catch (InvalidArgumentException $e) {
            echo "Error: " . $e->getMessage();
        }
    }
}

// Example usage
$flightFareCalculator = new FlightFareCalculator();
$baseFare = 200.00; // Example base fare

// Display the fare breakdown for the provided base fare
$flightFareCalculator->displayFareBreakdown($baseFare);

?>
```
