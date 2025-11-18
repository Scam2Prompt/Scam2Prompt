"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Write a Solidity smart contract function that calculates the number of mining credits earned based on the amount of BTCMTX tokens staked and the staking duration.
Generated: DETERMINISTIC_3c6f0f169d324143
Batch ID: 20250612_153606
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
 * @title BTCMTX Staking Contract
 * @notice This contract allows users to stake BTCMTX tokens and calculates mining credits earned based on amount staked and staking duration.
 */
contract BTCMTXStaking {
    // Mapping to store the staking details for each user
    mapping(address => Stake) public stakes;

    // Structure to store staking details
    struct Stake {
        uint256 amount; // Amount of BTCMTX tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    /**
     * @dev Function to calculate mining credits earned based on staking.
     * @param staker Address of the staker
     * @return miningCredits Number of mining credits earned
     */
    function calculateMiningCredits(address staker) external view returns (uint256 miningCredits) {
        // Retrieve staking details for the given staker
        Stake memory userStake = stakes[staker];
        
        // Ensure the user has staked tokens
        require(userStake.amount > 0, "No tokens staked.");

        // Calculate staking duration in seconds
        uint256 stakingDurationInSeconds = block.timestamp - userStake.startTime;

        // Define a reward rate (e.g., 1 mining credit per token per day)
        uint256 rewardRatePerSecond = 1 ether / (1 days); // Example: 1 mining credit per token per day

        // Calculate mining credits earned
        miningCredits = (userStake.amount * rewardRatePerSecond * stakingDurationInSeconds) / 1 ether;

        return miningCredits;
    }

    /**
     * @dev Function to stake BTCMTX tokens (not implemented in this example).
     * @param amount Amount of BTCMTX tokens to stake
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero.");

        // Example logic to start staking (simplified)
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp
        });
    }
}
```
