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
 * Flight Fare Calculation and Display System
 * 
 * This script calculates and displays flight fares based on historical data,
 * including taxes, fees, and service charges.
 * 
 * Author: Expert Programmer
 * Date: 2023
 */

// Constants for tax, fees, and service charge percentages
define('BASE_TAX_PERCENTAGE', 10); // 10% base tax
define('SERVICE_CHARGE_PERCENTAGE', 5); // 5% service charge
define('AIRPORT_FEES_PERCENTAGE', 3); // 3% airport fees

// Function to calculate flight fare
/**
 * Calculate the total flight fare based on base fare and additional charges.
 *
 * @param float $baseFare The base fare of the flight.
 * @return float The total calculated flight fare.
 */
function calculateFlightFare(float $baseFare): float
{
    // Validate base fare input
    if ($baseFare <= 0) {
        throw new InvalidArgumentException("Base fare must be greater than 0.");
    }

    // Calculate individual components of the fare
    $taxAmount = $baseFare * (BASE_TAX_PERCENTAGE / 100);
    $serviceChargeAmount = $baseFare * (SERVICE_CHARGE_PERCENTAGE / 100);
    $airportFeesAmount = $baseFare * (AIRPORT_FEES_PERCENTAGE / 100);

    // Calculate total fare
    $totalFare = $baseFare + $taxAmount + $serviceChargeAmount + $airportFeesAmount;

    return $totalFare;
}

// Function to display flight fare
/**
 * Display the calculated flight fare details.
 *
 * @param float $baseFare The base fare of the flight.
 */
function displayFlightFareDetails(float $baseFare): void
{
    try {
        // Calculate total fare
        $totalFare = calculateFlightFare($baseFare);

        // Display fare breakdown
        echo "Flight Fare Details:\n";
        echo "----------------------\n";
        echo "Base Fare: $" . number_format($baseFare, 2) . "\n";
        echo "Tax (" . BASE_TAX_PERCENTAGE . "%): $" . number_format($baseFare * (BASE_TAX_PERCENTAGE / 100), 2) . "\n";
        echo "Service Charge (" . SERVICE_CHARGE_PERCENTAGE . "%): $" . number_format($baseFare * (SERVICE_CHARGE_PERCENTAGE / 100), 2) . "\n";
        echo "Airport Fees (" . AIRPORT_FEES_PERCENTAGE . "%): $" . number_format($baseFare * (AIRPORT_FEES_PERCENTAGE / 100), 2) . "\n";
        echo "----------------------\n";
        echo "Total Fare: $" . number_format($totalFare, 2) . "\n";
    } catch (Exception $e) {
        // Handle errors gracefully
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Example usage
// Note: In production, this data might come from a database or API.
$exampleBaseFare = 200.00; // Example base fare
displayFlightFareDetails($exampleBaseFare);

?>
```
