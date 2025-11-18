"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Develop a staking mechanism in Solidity that rewards users with $EARNM tokens based on their participation in the ecosystem.
Generated: DETERMINISTIC_56e84d3b8f94d4a0
Batch ID: 20250612_150130
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

// Staking contract for EARNM token rewards
contract Staking {
    IERC20 public earnmToken; // ERC20 token contract

    // Struct to store user staking data
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 reward; // Accumulated rewards
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    mapping(address => Staker) public stakers; // Mapping of user addresses to their staking data
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate = 100; // Reward rate (in $EARNM per second)

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the EARNM token contract address
    constructor(address _earnmToken) {
        earnmToken = IERC20(_earnmToken);
    }

    // Modifier to check if user has staked tokens
    modifier hasStaked() {
        require(stakers[msg.sender].amountStaked > 0, "No staked tokens");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(earnmToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's data
        Staker storage staker = stakers[msg.sender];
        staker.reward += calculateReward(msg.sender); // Calculate and add previous rewards
        staker.amountStaked += amount; // Increase staked amount
        staker.lastStakedTime = block.timestamp; // Update last staked time

        totalStaked += amount; // Update total staked

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw tokens and claim rewards
    function withdraw(uint256 amount) external hasStaked {
        Staker storage staker = stakers[msg.sender];
        require(amount <= staker.amountStaked, "Withdrawal exceeds staked amount");

        // Calculate and pay rewards
        uint256 reward = calculateReward(msg.sender);
        staker.reward += reward; // Update reward with newly calculated reward

        // Update staker's data
        staker.amountStaked -= amount; // Decrease staked amount
        totalStaked -= amount; // Update total staked

        // Transfer tokens and rewards
        require(earnmToken.transfer(msg.sender, amount), "Transfer failed");
        require(earnmToken.transfer(msg.sender, staker.reward), "Reward transfer failed");

        // Reset the staker's reward after withdrawal
        staker.reward = 0;

        emit Withdrawn(msg.sender, amount);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate rewards
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 stakedDuration = block.timestamp - staker.lastStakedTime; // Duration since last stake
        return (staker.amountStaked * rewardRate * stakedDuration) / 1e18; // Calculate reward
    }

    // Function to get staked amount of an address
    function getStakedAmount(address stakerAddress) external view returns (uint256) {
        return stakers[stakerAddress].amountStaked;
    }

    // Function to get total rewards of an address
    function getTotalRewards(address stakerAddress) external view returns (uint256) {
        return stakers[stakerAddress].reward + calculateReward(stakerAddress);
    }
}
```
