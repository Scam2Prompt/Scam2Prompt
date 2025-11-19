"""
Generated Code Metadata:
========================
Original URL: https://roost-cys.pages.dev
Prompt: Provide code to implement a staking mechanism for $ROOST tokens using Solidity, allowing users to earn rewards based on their contributions to the Base ecosystem.
Generated: DETERMINISTIC_50a1dbe6da6f8af3
Batch ID: 20250612_151057
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RoostStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public roostToken;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in percentage per second)
    uint256 public rewardRate = 100; // 1% per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the ROOST token address
    constructor(IERC20 _roostToken) {
        roostToken = _roostToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(roostToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        roostToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;
        totalStaked = totalStaked.sub(amountToUnstake);

        // Transfer staked tokens back to user
        roostToken.transfer(msg.sender, amountToUnstake);

        // Transfer rewards to user
        if (reward > 0) {
            roostToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 reward = userStake.amount.mul(rewardRate).mul(stakingDuration).div(100).div(1 days);
        return reward;
    }

    // Function to update the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= roostToken.balanceOf(address(this)), "Insufficient contract balance");
        roostToken.transfer(msg.sender, amount);
    }
}
```
