"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Write a Solidity function to calculate and display the boost percentage for a staking pool based on the lock term and compounding rewards, as described on SidusPad.
Generated: DETERMINISTIC_137bf2f074e67ecc
Batch ID: 20250612_152235
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

contract StakingPool {

    // Structure to hold staking details
    struct Stake {
        uint256 amount; // Amount staked
        uint256 lockTerm; // Lock term in seconds
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Event to emit when a stake is created
    event StakeCreated(address indexed user, uint256 amount, uint256 lockTerm);

    // Function to create a new stake
    function createStake(uint256 amount, uint256 lockTerm) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(lockTerm > 0, "Lock term must be greater than zero");

        // Initialize staking details
        stakes[msg.sender] = Stake({
            amount: amount,
            lockTerm: lockTerm,
            startTime: block.timestamp
        });

        emit StakeCreated(msg.sender, amount, lockTerm);
    }

    // Function to calculate the boost percentage based on lock term and compounding rewards
    function calculateBoostPercentage() external view returns (uint256) {
        Stake memory userStake = stakes[msg.sender];

        // Require that the user has a stake
        require(userStake.amount > 0, "No stake found for user");

        // Calculate the elapsed time in seconds
        uint256 elapsedTime = block.timestamp - userStake.startTime;

        // Calculate the total boost percentage based on lock term and elapsed time
        uint256 boostPercentage;
        if (elapsedTime >= userStake.lockTerm) {
            // Full boost if the lock term is reached
            boostPercentage = 100; // 100% boost if fully matured
        } else {
            // Calculate the boost as a percentage of the lock term
            boostPercentage = (elapsedTime * 100) / userStake.lockTerm;
        }
        
        // Return the calculated boost percentage
        return boostPercentage;
    }
}
```
