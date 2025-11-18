"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbiusclaim.pages.dev
Prompt: Provide an example of how to use the veMULTI token in a staking contract, referencing Multichain's documentation.
Generated: DETERMINISTIC_c8a7e30ec1b33c3e
Batch ID: 20250612_153244
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
 * @title veMULTI Staking Contract
 * @notice This contract allows users to stake veMULTI tokens and earn rewards.
 * @dev References Multichain's documentation for veMULTI token integration.
 */
interface IveMULTI {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract veMULTIStaking {
    // Address of the veMULTI token contract
    IveMULTI public veMULTIToken;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;
    // Mapping to track reward balances
    mapping(address => uint256) public rewardBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Contract constructor to initialize the veMULTI token address
    constructor(address _veMULTITokenAddress) {
        require(_veMULTITokenAddress != address(0), "Invalid veMULTI token address");
        veMULTIToken = IveMULTI(_veMULTITokenAddress);
    }

    /**
     * @notice Stake veMULTI tokens in the contract.
     * @param amount The number of veMULTI tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer veMULTI tokens from the sender to the contract
        bool transferred = veMULTIToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed");

        // Update the staked balance
        stakedBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked veMULTI tokens.
     * @param amount The number of veMULTI tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer veMULTI tokens back to the sender
        bool transferred = veMULTIToken.transferFrom(address(this), msg.sender, amount);
        require(transferred, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim rewards earned through staking.
     */
    function claimRewards() external {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Update reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the sender
        // Note: This assumes rewards are distributed in veMULTI tokens; update as necessary.
        bool transferred = veMULTIToken.transferFrom(address(this), msg.sender, rewards);
        require(transferred, "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @notice View the staked balance of a user.
     * @param user The address of the user.
     * @return The amount of staked veMULTI tokens.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @notice View the reward balance of a user.
     * @param user The address of the user.
     * @return The amount of rewards owed to the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
