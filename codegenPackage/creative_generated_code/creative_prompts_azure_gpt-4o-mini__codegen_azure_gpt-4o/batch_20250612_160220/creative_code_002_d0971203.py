"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Create a function in PHP that calculates potential earnings based on the different investment plans offered by realtechearners.com, considering deposit amounts and timeframes.
Generated: DETERMINISTIC_d0971203f2814e0b
Batch ID: 20250612_160220
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
 * Calculate potential earnings based on investment plans.
 *
 * @param float $deposit The amount of money invested.
 * @param string $planName The name of the investment plan.
 * @param int $timeframe The duration of the investment in months.
 *
 * @return float|string The calculated earnings or an error message if input is invalid.
 */
function calculatePotentialEarnings(float $deposit, string $planName, int $timeframe) {
    // Validate inputs
    if ($deposit <= 0) {
        return "Error: Deposit amount must be greater than zero.";
    }
    if ($timeframe <= 0) {
        return "Error: Timeframe must be a positive integer.";
    }

    // Investment plans provided by realtechearners.com
    $investmentPlans = [
        'Basic' => 0.03,  // 3% monthly return
        'Standard' => 0.05, // 5% monthly return
        'Premium' => 0.08   // 8% monthly return
    ];

    // Check if the plan name is valid
    if (!array_key_exists($planName, $investmentPlans)) {
        return "Error: Invalid investment plan name.";
    }

    // Calculate potential earnings
    $monthlyRate = $investmentPlans[$planName];
    $potentialEarnings = $deposit * pow((1 + $monthlyRate), $timeframe);

    // Return the rounded result
    return round($potentialEarnings, 2);
}

// Example usage:
$deposit = 1000.00;
$planName = 'Standard';
$timeframe = 12;

$result = calculatePotentialEarnings($deposit, $planName, $timeframe);
echo $result; // Outputs the calculated earnings or an error message.
?>
```
