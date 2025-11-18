"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Create a Solidity function to calculate interest on NFT-backed loans, ensuring compatibility with the permissionless smart contract infrastructure described on NFTfi.com.
Generated: DETERMINISTIC_f4abff68c967fece
Batch ID: 20250612_151329
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
 * @title NFTLoanInterestCalculator
 * @dev A contract to calculate interest on NFT-backed loans.
 * Compatible with permissionless smart contract infrastructure like NFTfi.com.
 */
contract NFTLoanInterestCalculator {
    /**
     * @dev Calculates the interest owed on an NFT-backed loan.
     * @param principal The principal amount of the loan in wei (loan value).
     * @param annualInterestRate The annual interest rate as a percentage (e.g., 5% = 500).
     * @param loanDurationInDays The loan duration in days.
     * @return interest The total interest owed in wei.
     */
    function calculateInterest(
        uint256 principal,
        uint256 annualInterestRate,
        uint256 loanDurationInDays
    ) public pure returns (uint256 interest) {
        require(principal > 0, "Principal must be greater than zero");
        require(annualInterestRate > 0, "Interest rate must be greater than zero");
        require(loanDurationInDays > 0, "Loan duration must be greater than zero");

        // Annual interest rate is provided as a percentage (e.g., 5% = 500), so divide by 10000 for calculation
        uint256 dailyInterestRate = (annualInterestRate * 1e16) / 36500;

        // Calculate interest owed
        interest = (principal * dailyInterestRate * loanDurationInDays) / 1e18;

        return interest;
    }
}
```
