"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Create a step-by-step guide for integrating BTCMTX token staking functionality into an existing Ethereum dApp.
Generated: DETERMINISTIC_fbaf83b81a205bee
Batch ID: 20250612_153420
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
 * @dev This contract allows users to stake BTCMTX tokens in an Ethereum dApp.
 *      It includes functionality for staking, withdrawing, and claiming rewards.
 */

interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

contract BTCMTXStaking {
    // Token used for staking (BTCMTX).
    IERC20 public btcmtxToken;

    // Reward rate per second (e.g., 1 token per day = 1 / 86400).
    uint256 public rewardRate;

    // Tracks staked balances of users.
    mapping(address => uint256) public stakedBalances;

    // Tracks when users last interacted with the staking functionality.
    mapping(address => uint256) public lastUpdated;

    // Tracks accumulated rewards for users.
    mapping(address => uint256) public rewards;

    // Event emitted when a user stakes tokens.
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked tokens.
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards.
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Initializes the contract with the BTCMTX token address and reward rate.
     * @param _btcmtxToken Address of the BTCMTX ERC20 token.
     * @param _rewardRate Rate of rewards per second.
     */
    constructor(IERC20 _btcmtxToken, uint256 _rewardRate) {
        btcmtxToken = _btcmtxToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake BTCMTX tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update the user's rewards before changing the staked amount.
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract.
        require(
            btcmtxToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update staked balance and last interaction time.
        stakedBalances[msg.sender] += amount;
        lastUpdated[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked BTCMTX tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(
            stakedBalances[msg.sender] >= amount,
            "Insufficient staked balance"
        );

        // Update the user's rewards before changing the staked amount.
        _updateRewards(msg.sender);

        // Reduce the user's staked balance.
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user.
        require(
            btcmtxToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        lastUpdated[msg.sender] = block.timestamp;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards for staking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset the user's reward balance.
        rewards[msg.sender] = 0;

        // Transfer rewards to the user.
        require(
            btcmtxToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user whose rewards should be updated.
     */
    function _updateRewards(address user) internal {
        uint256 timeDifference = block.timestamp - lastUpdated[user];
        uint256 pendingRewards = stakedBalances[user] * rewardRate * timeDifference;

        // Accumulate rewards for the user.
        rewards[user] += pendingRewards;

        // Update the last interaction time.
        lastUpdated[user] = block.timestamp;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return The amount of pending rewards for the user.
     */
    function calculateRewards(address user) external view returns (uint256) {
        uint256 timeDifference = block.timestamp - lastUpdated[user];
        uint256 pendingRewards = stakedBalances[user] * rewardRate * timeDifference;
        return rewards[user] + pendingRewards;
    }
}
```
