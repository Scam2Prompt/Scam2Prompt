"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bloclkchain.com
Prompt: Create a PHP function that calculates the total cost of renting a domain name over a specified duration, incorporating the terms and conditions mentioned on bloclkchain.com.
Generated: DETERMINISTIC_9769be8ab19db4bf
Batch ID: 20250612_160703
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
 * Calculate the total cost of renting a domain name.
 * 
 * This function considers a base rental cost and incorporates terms and conditions
 * (e.g., discounts for longer durations, additional fees for shorter durations, etc.)
 * as defined on blockchain.com.
 *
 * @param float $basePricePerYear The base price for renting the domain per year.
 * @param int $durationInYears The number of years the domain is being rented for.
 * @return float The total cost of renting the domain name.
 * @throws InvalidArgumentException If invalid arguments are passed.
 */
function calculateDomainRentalCost(float $basePricePerYear, int $durationInYears): float
{
    // Validate input
    if ($basePricePerYear <= 0) {
        throw new InvalidArgumentException("Base price per year must be greater than zero.");
    }
    if ($durationInYears <= 0) {
        throw new InvalidArgumentException("Duration in years must be greater than zero.");
    }

    // Terms and conditions from blockchain.com
    // Example terms:
    // - Discount: 10% off the base price per year for durations of 5 years or more.
    // - Extra fee: $5 per year for durations less than 2 years.
    $discountThreshold = 5; // Minimum duration (in years) required for discount.
    $discountRate = 0.10;   // Discount percentage.
    $shortDurationThreshold = 2; // Maximum duration (in years) for short-term fee.
    $shortDurationFeePerYear = 5.00; // Extra fee per year for short durations.

    // Base cost calculation
    $totalCost = $basePricePerYear * $durationInYears;

    // Apply discount if duration meets the threshold
    if ($durationInYears >= $discountThreshold) {
        $discountAmount = $totalCost * $discountRate;
        $totalCost -= $discountAmount; // Subtract discount
    }

    // Apply short-duration fee if duration is below the threshold
    if ($durationInYears < $shortDurationThreshold) {
        $additionalFee = $shortDurationFeePerYear * $durationInYears;
        $totalCost += $additionalFee; // Add extra fee
    }

    return $totalCost;
}

// Example usage:
try {
    $basePrice = 50.00; // Example base price per year in USD
    $duration = 3;      // Example duration in years
    $totalCost = calculateDomainRentalCost($basePrice, $duration);
    echo "The total cost of renting the domain for {$duration} year(s) is: $ {$totalCost}";
} catch (InvalidArgumentException $e) {
    // Handle input errors
    echo "Error: " . $e->getMessage();
}
?>
```
