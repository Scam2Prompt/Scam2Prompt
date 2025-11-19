"""
Generated Code Metadata:
========================
Original URL: https://joincommonwealth.net
Prompt: Design a simple staking and unstaking system using Solidity for a cryptocurrency project like Commonwealth.
Generated: DETERMINISTIC_7614d441b4699b02
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A simple staking and unstaking system for a cryptocurrency project.
 */
contract StakingContract {
    // Mapping to track staked balances of users
    mapping(address => uint256) private stakedBalances;

    // Mapping to track the last staking timestamp for users
    mapping(address => uint256) private stakingTimestamps;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Modifier to ensure a valid staking amount
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external validAmount(amount) {
        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;

        // Update the last staking timestamp
        stakingTimestamps[msg.sender] = block.timestamp;

        // Update the total staked amount
        totalStaked += amount;

        // Emit the staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external validAmount(amount) {
        // Ensure the user has enough staked balance
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's staked balance
        stakedBalances[msg.sender] -= amount;

        // Update the total staked amount
        totalStaked -= amount;

        // Emit the unstaking event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the last staking timestamp of a user.
     * @param user The address of the user.
     * @return The last staking timestamp of the user.
     */
    function getLastStakingTimestamp(address user) external view returns (uint256) {
        return stakingTimestamps[user];
    }
}
```
