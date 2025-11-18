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

// Interface for the Morpheus contract to interact with stETH deposits
interface IMorpheus {
    function totalStaked() external view returns (uint256);
    function calculateMORShare(uint256 stETHDeposit) external view returns (uint256);
}

contract MorpheusEmissionCalculator {
    IMorpheus public morpheusContract;

    // Event to log the calculation of pro-rata MOR emissions
    event MORShareCalculated(address indexed user, uint256 stETHDeposit, uint256 morShare);

    // Constructor to set the address of the Morpheus contract
    constructor(address _morpheusContractAddress) {
        require(_morpheusContractAddress != address(0), "Invalid Morpheus contract address");
        morpheusContract = IMorpheus(_morpheusContractAddress);
    }

    /**
     * @notice Calculate the pro-rata share of MOR emissions for a given stETH deposit
     * @param stETHDeposit The amount of stETH deposited by the user
     * @return morShare The amount of MOR emissions allocated to the user's stETH deposit
     */
    function calculateProRataMORShare(uint256 stETHDeposit) external view returns (uint256 morShare) {
        // Ensure the stETH deposit is greater than zero
        require(stETHDeposit > 0, "stETH deposit must be greater than zero");

        // Fetch the total staked amount in the Morpheus contract
        uint256 totalStakedAmount = morpheusContract.totalStaked();

        // Ensure that total staked amount is not zero to prevent division by zero
        require(totalStakedAmount > 0, "Total staked amount must be greater than zero");

        // Calculate the pro-rata share of MOR emissions
        morShare = (stETHDeposit * morpheusContract.calculateMORShare(stETHDeposit)) / totalStakedAmount;

        // Emit the event with the calculated share
        emit MORShareCalculated(msg.sender, stETHDeposit, morShare);
    }
}
```
