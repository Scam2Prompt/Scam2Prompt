"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Write a smart contract in Solidity for staking $MK tokens in Meme Kombat that calculates rewards based on a 250% APY during the presale period. Include functionality for users to stake, withdraw, and check their rewards.
Generated: DETERMINISTIC_e69015a82c1a9043
Batch ID: 20250612_152410
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

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MemeKombatStaking {
    IERC20 public mkToken; // MK token contract
    uint256 public constant APY = 250; // 250% APY
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;
    
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Time when the tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // User stakes
    mapping(address => bool) public hasStaked; // Track if user has staked

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);
    
    // Constructor to set the MK token address
    constructor(IERC20 _mkToken) {
        mkToken = _mkToken;
    }

    // Function to stake MK tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(mkToken.balanceOf(msg.sender) >= _amount, "Insufficient MK token balance");

        // Transfer MK tokens from user to the contract
        mkToken.transferFrom(msg.sender, address(this), _amount);
        
        Stake storage userStake = stakes[msg.sender];
        
        // If user has staked before, calculate existing rewards
        if (hasStaked[msg.sender]) {
            userStake.rewards += calculateRewards(msg.sender);
        } else {
            hasStaked[msg.sender] = true;
        }

        userStake.amount += _amount;
        userStake.startTime = block.timestamp; // Update start time

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens to withdraw");

        uint256 totalRewards = calculateRewards(msg.sender) + userStake.rewards;
        uint256 amountToWithdraw = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewards = 0;

        // Transfer staked tokens back to the user
        require(mkToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");

        // Transfer rewards to the user
        if (totalRewards > 0) {
            require(mkToken.transfer(msg.sender, totalRewards), "Reward transfer failed");
        }

        emit Withdrawn(msg.sender, amountToWithdraw, totalRewards);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime; // Duration in seconds
        uint256 yearlyReward = (userStake.amount * APY) / 100; // Annual rewards
        return (yearlyReward * stakingDuration) / SECONDS_IN_A_YEAR; // Rewards based on time staked
    }

    // Function to check the user's rewards
    function checkRewards() external view returns (uint256) {
        return calculateRewards(msg.sender) + stakes[msg.sender].rewards;
    }
}
```
