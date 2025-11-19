"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Write a Solidity function that updates the current bonus rate based on total investments, reflecting the dynamic profit structure used by MinerDog.
Generated: DETERMINISTIC_2cb2e5fadd6e1518
Batch ID: 20250612_155753
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

contract MinerDog {
    // State variable to hold the current bonus rate
    uint256 public bonusRate;

    // State variable to hold total investments
    uint256 public totalInvestments;

    // Event to log bonus rate updates
    event BonusRateUpdated(uint256 newBonusRate);

    // Constructor to initialize the contract with default values
    constructor() {
        bonusRate = 0; // Initial bonus rate
        totalInvestments = 0; // Initial total investments
    }

    /**
     * @dev Updates the bonus rate based on total investments.
     * The bonus rate increases as total investments cross certain thresholds.
     * @param newInvestment Amount of new investment to add to total investments.
     */
    function updateBonusRate(uint256 newInvestment) external {
        require(newInvestment > 0, "Investment must be greater than zero");

        // Update total investments
        totalInvestments += newInvestment;

        // Update bonus rate based on total investments
        if (totalInvestments < 1 ether) {
            bonusRate = 0; // No bonus for less than 1 ether
        } else if (totalInvestments < 10 ether) {
            bonusRate = 5; // 5% bonus for 1 to 10 ether
        } else if (totalInvestments < 100 ether) {
            bonusRate = 10; // 10% bonus for 10 to 100 ether
        } else {
            bonusRate = 15; // 15% bonus for 100 ether and above
        }

        // Emit event to log the new bonus rate
        emit BonusRateUpdated(bonusRate);
    }

    /**
     * @dev Retrieve the current bonus rate.
     * @return Current bonus rate as a percentage.
     */
    function getBonusRate() external view returns (uint256) {
        return bonusRate;
    }

    /**
     * @dev Retrieve the total investments.
     * @return Total investments in the contract.
     */
    function getTotalInvestments() external view returns (uint256) {
        return totalInvestments;
    }
}
```
