"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitetoptrade.com
Prompt: Develop a PHP script that calculates potential profits based on the investment plans offered by Elitetoptrade, including the Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_2ea1988e5fe63c3d
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
 * A class to calculate potential profits based on investment plans.
 */
class InvestmentCalculator {
    // Investment plans with their respective returns
    const PLANS = [
        'silver' => 0.05,  // 5% return
        'gold' => 0.1,     // 10% return
        'premium' => 0.15, // 15% return
    ];

    /**
     * Calculates potential profit based on investment amount and selected plan.
     *
     * @param string $plan The investment plan (silver, gold, premium)
     * @param float $amount The amount to invest
     * @return float|null The potential profit or null on error
     */
    public function calculateProfit($plan, $amount) {
        // Validate the plan
        if (!array_key_exists($plan, self::PLANS)) {
            throw new InvalidArgumentException("Invalid investment plan: $plan. Available plans are: " . implode(', ', array_keys(self::PLANS)));
        }

        // Validate the amount
        if (!is_numeric($amount) || $amount <= 0) {
            throw new InvalidArgumentException("Investment amount must be a positive number. Provided: $amount");
        }

        // Calculate potential profit
        $profit = $amount * self::PLANS[$plan];

        return $profit;
    }
}

/**
 * Main script to execute the investment profit calculation
 */
try {
    // Create an instance of the InvestmentCalculator
    $calculator = new InvestmentCalculator();

    // Example usage
    $plan = 'gold'; // Change this to 'silver' or 'premium' to test other plans
    $amount = 1000; // The investment amount

    // Calculate the profit
    $profit = $calculator->calculateProfit($plan, $amount);

    // Output the result
    echo "The potential profit for the $plan plan on an investment of $$amount is: $$profit\n";
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
