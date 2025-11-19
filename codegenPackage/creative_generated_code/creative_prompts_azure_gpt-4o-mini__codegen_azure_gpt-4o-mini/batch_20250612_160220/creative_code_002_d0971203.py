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
 * Class InvestmentCalculator
 *
 * This class encapsulates the logic for calculating potential earnings
 * based on various investment plans.
 */
class InvestmentCalculator
{
    // Investment plans with their respective interest rates
    private $investmentPlans = [
        'Basic' => 0.05,   // 5% interest
        'Standard' => 0.10, // 10% interest
        'Premium' => 0.15   // 15% interest
    ];

    /**
     * Calculate potential earnings based on the selected plan, deposit amount, and timeframe.
     *
     * @param string $plan      The investment plan chosen by the user.
     * @param float  $amount    The amount to be deposited.
     * @param int    $duration  The duration of the investment in months.
     * @return float            The potential earnings.
     * @throws InvalidArgumentException if the plan is not valid or amount/duration is negative.
     */
    public function calculateEarnings(string $plan, float $amount, int $duration): float
    {
        // Validate input
        if (!array_key_exists($plan, $this->investmentPlans)) {
            throw new InvalidArgumentException("Invalid investment plan selected.");
        }
        if ($amount <= 0) {
            throw new InvalidArgumentException("Deposit amount must be greater than zero.");
        }
        if ($duration <= 0) {
            throw new InvalidArgumentException("Duration must be greater than zero months.");
        }

        // Get the interest rate for the selected plan
        $interestRate = $this->investmentPlans[$plan];

        // Calculate potential earnings
        $earnings = $amount * pow((1 + $interestRate), $duration / 12) - $amount;

        return round($earnings, 2); // Round to 2 decimal places for currency formatting
    }
}

// Example usage
try {
    $calculator = new InvestmentCalculator();
    $plan = 'Standard';   // Investment plan selected
    $amount = 1000.00;    // Amount to be invested
    $duration = 12;       // Duration in months

    $potentialEarnings = $calculator->calculateEarnings($plan, $amount, $duration);
    echo "Potential earnings from the $plan plan: $" . $potentialEarnings . "\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
