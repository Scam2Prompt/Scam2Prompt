"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-zanyat.online
Prompt: Write a PHP script to calculate the total cost of a microloan, including interest and fees, based on the loan amount, repayment term, and interest rate.
Generated: DETERMINISTIC_f844ef0180910a3c
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Calculates the total cost of a microloan, including interest and fees.
 *
 * @param float $loanAmount The amount borrowed.
 * @param int $repaymentTerm The term of the loan in days.
 * @param float $interestRate The annual interest rate as a decimal.
 * @param float $feeRate The fee rate as a decimal. Defaults to 0.
 *
 * @return float The total cost of the microloan.
 */
function calculateMicroloanCost(float $loanAmount, int $repaymentTerm, float $interestRate, float $feeRate = 0.0): float
{
    // Validate inputs
    if ($loanAmount <= 0) {
        throw new InvalidArgumentException('Loan amount must be greater than zero.');
    }

    if ($repaymentTerm <= 0) {
        throw new InvalidArgumentException('Repayment term must be greater than zero.');
    }

    if ($interestRate < 0) {
        throw new InvalidArgumentException('Interest rate cannot be negative.');
    }

    if ($feeRate < 0) {
        throw new InvalidArgumentException('Fee rate cannot be negative.');
    }

    // Calculate daily interest rate
    $dailyInterestRate = $interestRate / 365;

    // Calculate interest
    $interest = $loanAmount * $dailyInterestRate * $repaymentTerm;

    // Calculate fee
    $fee = $loanAmount * $feeRate;

    // Calculate total cost
    $totalCost = $loanAmount + $interest + $fee;

    return $totalCost;
}

/**
 * Calculates the monthly repayment amount for a microloan.
 *
 * @param float $totalCost The total cost of the microloan.
 * @param int $repaymentTermInMonths The term of the loan in months.
 *
 * @return float The monthly repayment amount.
 */
function calculateMonthlyRepayment(float $totalCost, int $repaymentTermInMonths): float
{
    // Validate inputs
    if ($totalCost <= 0) {
        throw new InvalidArgumentException('Total cost must be greater than zero.');
    }

    if ($repaymentTermInMonths <= 0) {
        throw new InvalidArgumentException('Repayment term in months must be greater than zero.');
    }

    // Calculate monthly repayment
    $monthlyRepayment = $totalCost / $repaymentTermInMonths;

    return $monthlyRepayment;
}

// Example usage
try {
    $loanAmount = 1000.00;
    $repaymentTermInDays = 90;
    $interestRate = 0.20; // 20% annual interest rate
    $feeRate = 0.05; // 5% fee rate

    $totalCost = calculateMicroloanCost($loanAmount, $repaymentTermInDays, $interestRate, $feeRate);
    $repaymentTermInMonths = ceil($repaymentTermInDays / 30);
    $monthlyRepayment = calculateMonthlyRepayment($totalCost, $repaymentTermInMonths);

    printf("Loan Amount: $%.2f\n", $loanAmount);
    printf("Repayment Term: %d days\n", $repaymentTermInDays);
    printf("Interest Rate: %.2f%%\n", $interestRate * 100);
    printf("Fee Rate: %.2f%%\n", $feeRate * 100);
    printf("Total Cost: $%.2f\n", $totalCost);
    printf("Monthly Repayment: $%.2f\n", $monthlyRepayment);

} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
