"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Write a function in PHP to calculate the total repayment amount for microloans based on interest rates and loan terms, similar to the financial calculations seen on nocreditcheck.online.
Generated: DETERMINISTIC_9004b6ead4c46d2d
Batch ID: 20250612_145727
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
 * Calculate the total repayment amount for microloans based on interest rates and loan terms.
 * 
 * @param float $principal       The initial loan amount (principal).
 * @param float $annualInterest  The annual interest rate as a percentage (e.g., 5.5 for 5.5%).
 * @param int   $loanTermMonths  The loan term in months.
 * 
 * @return float                 The total repayment amount.
 * 
 * @throws InvalidArgumentException If any input is negative or invalid.
 */
function calculateTotalRepayment(float $principal, float $annualInterest, int $loanTermMonths): float
{
    // Validate inputs: principal, annual interest rate, and loan term must be positive
    if ($principal <= 0) {
        throw new InvalidArgumentException('Principal amount must be greater than zero.');
    }
    if ($annualInterest < 0) {
        throw new InvalidArgumentException('Annual interest rate cannot be negative.');
    }
    if ($loanTermMonths <= 0) {
        throw new InvalidArgumentException('Loan term must be greater than zero.');
    }

    // Convert annual interest rate to monthly interest rate (divide by 12 and convert to decimal)
    $monthlyInterestRate = ($annualInterest / 100) / 12;

    // Calculate the total repayment amount using the formula:
    // Total Repayment = Principal * (1 + Monthly Interest Rate * Loan Term (in months))
    $totalRepayment = $principal * (1 + ($monthlyInterestRate * $loanTermMonths));

    // Round the result to 2 decimal places for monetary values
    return round($totalRepayment, 2);
}

// Example usage:
try {
    $principal = 1000;        // $1,000 loan
    $annualInterest = 6.5;    // 6.5% annual interest rate
    $loanTermMonths = 12;     // 12-month loan term

    $totalRepayment = calculateTotalRepayment($principal, $annualInterest, $loanTermMonths);
    echo "Total repayment amount: $" . $totalRepayment . PHP_EOL;
} catch (InvalidArgumentException $e) {
    // Handle invalid input errors
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
