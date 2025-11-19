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
 * This script calculates potential profits based on investment plans provided by Morpha Finance.
 * It includes input validation, error handling, and supports multiple investment plans with daily profit rates.
 */

// Investment plans - Define the plans and their daily profit rates (%)
$investmentPlans = [
    'Basic' => 1.5,  // 1.5% daily profit
    'Standard' => 2.0,  // 2.0% daily profit
    'Premium' => 2.5   // 2.5% daily profit
];

/**
 * Calculate potential profit.
 * 
 * @param float $principal Amount invested.
 * @param int $days Number of days the investment is held.
 * @param float $dailyRate Daily profit rate as a percentage.
 * @return float Total profit earned.
 */
function calculateProfit(float $principal, int $days, float $dailyRate): float
{
    return $principal * ($dailyRate / 100) * $days;
}

// Input parameters
$principal = $_POST['principal'] ?? null; // Investment amount (from user input)
$days = $_POST['days'] ?? null; // Duration of investment (from user input)
$selectedPlan = $_POST['plan'] ?? null; // Selected investment plan (from user input)

// Error handling
$errors = [];
if ($principal === null || !is_numeric($principal) || $principal <= 0) {
    $errors[] = "Invalid investment amount. Please provide a positive number.";
}
if ($days === null || !is_numeric($days) || $days <= 0) {
    $errors[] = "Invalid number of days. Please provide a positive integer.";
}
if ($selectedPlan === null || !array_key_exists($selectedPlan, $investmentPlans)) {
    $errors[] = "Invalid investment plan. Please select a valid plan.";
}

// Display errors if any
if (!empty($errors)) {
    foreach ($errors as $error) {
        echo "<p>Error: $error</p>";
    }
    exit;
}

// Calculate profit
$dailyRate = $investmentPlans[$selectedPlan];
$profit = calculateProfit((float)$principal, (int)$days, $dailyRate);

// Display results
echo "<h2>Profit Calculation</h2>";
echo "<p>Investment Plan: $selectedPlan</p>";
echo "<p>Principal Amount: $" . number_format($principal, 2) . "</p>";
echo "<p>Duration: $days days</p>";
echo "<p>Daily Profit Rate: $dailyRate%</p>";
echo "<p>Total Profit: $" . number_format($profit, 2) . "</p>";

?>
```
