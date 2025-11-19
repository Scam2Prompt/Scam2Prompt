"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Design a simple staking system using Solidity for the Oracle Meme token (OMEME) on the Binance Smart Chain, offering a 652% reward based on dynamic percentage.
Generated: DETERMINISTIC_2ebce7eaa8a2fd41
Batch ID: 20250622_205836
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
 * @title Oracle Meme Token Staking Contract
 * @dev A simple staking system for the Oracle Meme token (OMEME) on Binance Smart Chain.
 * Users can stake OMEME tokens and earn rewards based on a dynamic percentage (652% annual reward).
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract OMEMEStaking {
    // Token being staked
    IERC20 public immutable omemeToken;

    // Annual reward percentage (652%)
    uint256 public constant ANNUAL_REWARD_PERCENTAGE = 652;

    // Seconds in a year (used for reward calculation)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract with the OMEME token address.
     * @param _omemeToken Address of the OMEME token contract.
     */
    constructor(IERC20 _omemeToken) {
        require(address(_omemeToken) != address(0), "Invalid token address");
        omemeToken = _omemeToken;
    }

    /**
     * @dev Stake OMEME tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(omemeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate reward based on staking duration and annual reward percentage
        uint256 reward = (userStake.amount * ANNUAL_REWARD_PERCENTAGE * stakingDuration) / (100 * SECONDS_IN_YEAR);

        // Transfer staked tokens and reward to the user
        uint256 totalAmount = userStake.amount + reward;
        require(omemeToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset user's staking information
        userStake.amount = 0;
        userStake.startTime = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Get the current reward for a user based on their staking duration.
     * @param _user Address of the user.
     * @return reward Amount of reward tokens.
     */
    function calculateReward(address _user) external view returns (uint256 reward) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate reward based on staking duration and annual reward percentage
        reward = (userStake.amount * ANNUAL_REWARD_PERCENTAGE * stakingDuration) / (100 * SECONDS_IN_YEAR);
    }
}
```
