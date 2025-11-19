"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Create a Solidity function to update the contract's bonus rate based on the total invested balance, using the MinerDog contract's logic of increasing bonuses by 0.05% for every 45 BNB added.
Generated: DETERMINISTIC_8f313b80a515ca20
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Bonus Manager Contract
 * @author [Your Name]
 * @notice This contract manages the bonus rate based on the total invested balance.
 */
contract BonusManager {
    // Constants
    uint256 public constant BONUS_INCREMENT = 0.05 * 10**2; // 0.05%
    uint256 public constant BNB_INCREMENT = 45 * 10**18; // 45 BNB

    // State variables
    uint256 public totalInvestedBalance;
    uint256 public bonusRate;

    /**
     * @notice Initializes the contract with an initial bonus rate of 0%.
     */
    constructor() {
        bonusRate = 0;
    }

    /**
     * @notice Updates the contract's bonus rate based on the total invested balance.
     * @dev Increases the bonus rate by 0.05% for every 45 BNB added to the total invested balance.
     * @param _newBalance The new total invested balance.
     */
    function updateBonusRate(uint256 _newBalance) public {
        // Check if the new balance is greater than the current total invested balance
        require(_newBalance >= totalInvestedBalance, "New balance must be greater than or equal to the current balance");

        // Calculate the increase in balance
        uint256 balanceIncrease = _newBalance - totalInvestedBalance;

        // Calculate the number of 45 BNB increments
        uint256 increments = balanceIncrease / BNB_INCREMENT;

        // Update the bonus rate
        bonusRate = bonusRate + (increments * BONUS_INCREMENT);

        // Update the total invested balance
        totalInvestedBalance = _newBalance;
    }

    /**
     * @notice Gets the current bonus rate.
     * @return The current bonus rate.
     */
    function getBonusRate() public view returns (uint256) {
        return bonusRate;
    }

    /**
     * @notice Gets the total invested balance.
     * @return The total invested balance.
     */
    function getTotalInvestedBalance() public view returns (uint256) {
        return totalInvestedBalance;
    }
}
```
