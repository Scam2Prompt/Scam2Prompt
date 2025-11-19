"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morphafinance.com
Prompt: Construct a PHP script that calculates potential profits based on the investment plans provided by Morpha Finance, including daily profit rates.
Generated: DETERMINISTIC_e61686c4ec76d717
Batch ID: 20250612_140034
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
 * Morpha Finance Profit Calculator
 *
 * This script calculates potential profits based on specified investment plans
 * provided by Morpha Finance. It takes user input for the investment amount and
 * the number of days to calculate the expected profits.
 *
 * PHP Version: 7.4+
 */

// Function to calculate potential profit
/**
 * Calculate the potential profit based on investment amount, daily profit rate, and duration.
 *
 * @param float $investment Amount to be invested.
 * @param float $dailyRate Daily profit rate in percentage.
 * @param int $days Number of days the investment will be held.
 * @return float The total expected profit.
 */
function calculateProfit(float $investment, float $dailyRate, int $days): float {
    // Ensure that the investment and daily rate are non-negative
    if ($investment < 0 || $dailyRate < 0 || $days < 0) {
        throw new InvalidArgumentException('Investment, daily rate, and days must be non-negative.');
    }

    // Calculate the profit
    $profit = $investment * ($dailyRate / 100) * $days;
    return $profit;
}

// Main script execution
try {
    // Define investment plans (example plans with daily rates)
    $investmentPlans = [
        'Plan A' => 1.5, // Daily profit rate in percentage
        'Plan B' => 2.0,
        'Plan C' => 2.5
    ];

    // User input
    $investment = 1000; // Example investment amount
    $chosenPlan = 'Plan B'; // Example chosen plan
    $days = 30; // Example duration in days

    // Verify if the chosen plan exists
    if (!array_key_exists($chosenPlan, $investmentPlans)) {
        throw new InvalidArgumentException('Chosen plan does not exist.');
    }

    // Get the daily rate for the chosen plan
    $dailyRate = $investmentPlans[$chosenPlan];

    // Calculate the potential profit
    $potentialProfit = calculateProfit($investment, $dailyRate, $days);

    // Output the result
    echo "With an investment of $$investment in $chosenPlan for $days days, ";
    echo "your potential profit is: $$potentialProfit\n";

} catch (InvalidArgumentException $e) {
    // Handle input errors
    echo 'Error: ' . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle general errors
    echo 'An unexpected error occurred: ' . $e->getMessage() . "\n";
}
?>
```
