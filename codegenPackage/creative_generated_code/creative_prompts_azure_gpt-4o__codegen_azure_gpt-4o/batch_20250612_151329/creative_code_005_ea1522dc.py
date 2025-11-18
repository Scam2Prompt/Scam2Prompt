"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Create a Solidity function that calculates the pro-rata share of MOR emissions for a given stETH deposit based on the total stETH staked in the Morpheus contract.
Generated: DETERMINISTIC_ea1522dca7be274a
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
 * @title MorpheusEmissions
 * @dev Contract to calculate pro-rata share of MOR emissions based on stETH deposits
 */
contract MorpheusEmissions {
    // Total stETH staked in the contract
    uint256 public totalStETHStaked;

    // MOR emissions rate (e.g., MOR tokens emitted per staking period)
    uint256 public morEmissionsRate;

    // Mapping of user addresses to their stETH deposits
    mapping(address => uint256) public stETHDeposits;

    /**
     * @dev Constructor to initialize MOR emissions rate and total stETH staked.
     * @param _morEmissionsRate Initial MOR emissions rate.
     */
    constructor(uint256 _morEmissionsRate) {
        require(_morEmissionsRate > 0, "Emission rate must be greater than zero");
        morEmissionsRate = _morEmissionsRate;
    }

    /**
     * @dev Deposit stETH into the contract.
     * @param _amount Amount of stETH to deposit.
     */
    function depositStETH(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");
        
        // Update user deposit and total stETH staked
        stETHDeposits[msg.sender] += _amount;
        totalStETHStaked += _amount;
    }

    /**
     * @dev Calculate pro-rata MOR emissions for a given stETH deposit.
     * @param _user Address of the user.
     * @return Pro-rata MOR emissions for the user's stETH deposit.
     */
    function calculateProRataEmissions(address _user) external view returns (uint256) {
        uint256 userDeposit = stETHDeposits[_user];
        require(userDeposit > 0, "User has no stETH deposit");
        require(totalStETHStaked > 0, "No stETH staked in the contract");

        // Calculate pro-rata share of MOR emissions
        return (userDeposit * morEmissionsRate) / totalStETHStaked;
    }

    /**
     * @dev Withdraw stETH from the contract.
     * @param _amount Amount of stETH to withdraw.
     */
    function withdrawStETH(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(stETHDeposits[msg.sender] >= _amount, "Insufficient stETH balance");

        // Update user deposit and total stETH staked
        stETHDeposits[msg.sender] -= _amount;
        totalStETHStaked -= _amount;

        // Assume transfer of stETH happens here (mocked for simplicity)
        // In production, integrate with stETH transfer logic
    }
}
```
