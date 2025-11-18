"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokita-dashboard.pages.dev
Prompt: Write a Solidity smart contract that implements staking functionality for Flokita tokens, ensuring compatibility with both Binance Smart Chain (BSC) and Solana (SOL), as mentioned on the Flokita website.
Generated: DETERMINISTIC_b3290736329e40ff
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

/**
 * @title FlokitaTokenStaking
 * @dev A staking contract for Flokita tokens, compatible with Binance Smart Chain (BSC).
 * Note: Solidity is not natively compatible with Solana blockchain. This contract is designed for Ethereum-compatible blockchains like BSC.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract FlokitaTokenStaking {
    // State variables
    IERC20 public flokitaToken; // Flokita token instance
    uint256 public rewardRate; // Reward rate (tokens per second)
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when staking started
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward, uint256 timestamp);

    constructor(address _flokitaToken, uint256 _rewardRate) {
        require(_flokitaToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        flokitaToken = IERC20(_flokitaToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake Flokita tokens.
     * @param amount - The amount of Flokita tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer Flokita tokens from the user to the contract
        bool success = flokitaToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their Flokita tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = userStake.amount * rewardRate * stakingDuration / 1 ether; // Normalize reward calculation

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.startTime = 0;

        // Update total staked tokens
        totalStaked -= amountToUnstake;

        // Transfer staked tokens and rewards to the user
        bool success = flokitaToken.transfer(msg.sender, amountToUnstake + reward);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, reward, block.timestamp);
    }

    /**
     * @dev Returns the total staked balance for a user.
     * @param user - The address of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Returns the staking reward for a user based on the current timestamp.
     * @param user - The address of the user.
     */
    function calculateReward(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = userStake.amount * rewardRate * stakingDuration / 1 ether; // Normalize reward calculation
        return reward;
    }
}
```
