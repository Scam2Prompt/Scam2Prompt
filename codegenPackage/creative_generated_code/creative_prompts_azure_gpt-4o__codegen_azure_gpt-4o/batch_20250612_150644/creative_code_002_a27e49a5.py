"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sublime.finance
Prompt: Generate code to calculate interest rates for loans using smart contracts, referencing features typically found in platforms like Sublime Finance.
Generated: DETERMINISTIC_a27e49a5d0a400cc
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title LoanInterestCalculator
 * @dev Smart contract to calculate interest rates for loans.
 * Similar to platforms like Sublime Finance, featuring variable interest rates and loan terms.
 */
contract LoanInterestCalculator {
    // Struct to store loan details
    struct Loan {
        uint256 principal; // Loan principal amount
        uint256 annualInterestRate; // Annual interest rate in basis points (1% = 100 basis points)
        uint256 durationInDays; // Loan duration in days
    }

    // Event to emit loan calculation details
    event LoanCalculated(
        uint256 principal,
        uint256 annualInterestRate,
        uint256 durationInDays,
        uint256 interestAmount
    );

    /**
     * @notice Calculates the interest amount for a given loan.
     * @param principal The principal amount of the loan.
     * @param annualInterestRate The annual interest rate (in basis points).
     * @param durationInDays The duration of the loan in days.
     * @return interestAmount The calculated interest amount for the loan.
     */
    function calculateInterest(
        uint256 principal,
        uint256 annualInterestRate,
        uint256 durationInDays
    ) public pure returns (uint256 interestAmount) {
        // Validate inputs
        require(principal > 0, "Principal must be greater than zero.");
        require(
            annualInterestRate > 0 && annualInterestRate <= 10000,
            "Interest rate must be between 0 and 10000 basis points."
        );
        require(durationInDays > 0, "Duration must be greater than zero.");

        // Calculate interest
        uint256 dailyInterestRate = annualInterestRate / 365; // Convert annual rate to daily basis points
        interestAmount = (principal * dailyInterestRate * durationInDays) / 10000; // Calculate interest
    }

    /**
     * @notice Public function to calculate interest and emit details.
     * @dev This function can be used to log loan details on-chain.
     * @param principal The principal amount of the loan.
     * @param annualInterestRate The annual interest rate (in basis points).
     * @param durationInDays The duration of the loan in days.
     */
    function calculateAndLogInterest(
        uint256 principal,
        uint256 annualInterestRate,
        uint256 durationInDays
    ) external {
        // Calculate interest
        uint256 interestAmount = calculateInterest(
            principal,
            annualInterestRate,
            durationInDays
        );

        // Emit event with loan details
        emit LoanCalculated(
            principal,
            annualInterestRate,
            durationInDays,
            interestAmount
        );
    }
}
```
