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
 * Calculate the total repayment amount for a microloan.
 *
 * This function computes the total repayment amount given the principal amount,
 * annual interest rate, and loan term in months.
 *
 * @param float $principal The principal amount of the loan.
 * @param float $annualInterestRate The annual interest rate (in percentage).
 * @param int $loanTermMonths The term of the loan in months.
 * @return float The total repayment amount.
 * @throws InvalidArgumentException If any input is negative or if the interest rate is greater than 100%.
 */
function calculateTotalRepayment($principal, $annualInterestRate, $loanTermMonths) {
    // Validate inputs
    if ($principal < 0) {
        throw new InvalidArgumentException("Principal amount cannot be negative.");
    }
    if ($annualInterestRate < 0 || $annualInterestRate > 100) {
        throw new InvalidArgumentException("Annual interest rate must be between 0 and 100.");
    }
    if ($loanTermMonths <= 0) {
        throw new InvalidArgumentException("Loan term must be a positive integer.");
    }

    // Convert annual interest rate to a monthly rate
    $monthlyInterestRate = ($annualInterestRate / 100) / 12;

    // Calculate total repayment amount using the formula
    $totalRepayment = $principal * (1 + $monthlyInterestRate * $loanTermMonths);

    return round($totalRepayment, 2); // Round to 2 decimal places for currency formatting
}

// Example usage
try {
    $principal = 1000; // Example principal amount
    $annualInterestRate = 5; // Example annual interest rate in percentage
    $loanTermMonths = 12; // Example loan term in months

    $totalRepayment = calculateTotalRepayment($principal, $annualInterestRate, $loanTermMonths);
    echo "Total repayment amount: $" . $totalRepayment;
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
