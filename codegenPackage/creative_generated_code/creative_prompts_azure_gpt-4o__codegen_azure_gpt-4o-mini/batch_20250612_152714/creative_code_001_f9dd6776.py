"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with the $MPEPE token to allow staking and automatic reward distribution, ensuring compliance with the Ethereum blockchain.
Generated: DETERMINISTIC_f9dd6776db67bab9
Batch ID: 20250612_152714
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

// Interface for the $MPEPE token contract
interface IMPEPEToken {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Staking contract for $MPEPE token
contract MPEPEStaking {
    // Token used for staking
    IMPEPEToken public mpepeToken;

    // Struct to represent each user's stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 reward; // Accumulated rewards
        uint256 timestamp; // Time of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total stakes in the contract
    uint256 public totalStaked;

    // Reward rate (in terms of $MPEPE tokens) per second
    uint256 public rewardRate = 1e18; // Example: 1 MPEPE token per second

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token address
    constructor(address _mpepeToken) {
        mpepeToken = IMPEPEToken(_mpepeToken);
    }

    // Function to stake $MPEPE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(mpepeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];

        // Calculate and update the reward before modifying the stake
        userStake.reward += _calculateReward(msg.sender);
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $MPEPE tokens and claim rewards
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Cannot unstake 0");

        // Calculate and update the reward before modifying the stake
        userStake.reward += _calculateReward(msg.sender);
        userStake.amount -= amount;

        totalStaked -= amount;

        // Transfer the staked amount back to the user
        require(mpepeToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);

        // Pay the accrued rewards
        _payReward(msg.sender);
    }

    // Internal function to calculate rewards for a user
    function _calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return userStake.reward; // No amount staked
        
        uint256 duration = block.timestamp - userStake.timestamp;
        return userStake.reward + (userStake.amount * rewardRate * duration) / 1e18;
    }

    // Internal function to pay out rewards
    function _payReward(address user) internal {
        Stake storage userStake = stakes[user];
        uint256 reward = userStake.reward;

        require(reward > 0, "No rewards to claim");
        userStake.reward = 0; // Reset reward after paying

        // Transfer the reward to the user
        require(mpepeToken.transfer(user, reward), "Reward transfer failed");

        emit RewardPaid(user, reward);
    }

    // Function to view total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to view the stake and rewards of a user
    function getUserStake(address user) external view returns (uint256 amount, uint256 reward) {
        Stake storage userStake = stakes[user];
        amount = userStake.amount;
        reward = _calculateReward(user);
    }
}
```
