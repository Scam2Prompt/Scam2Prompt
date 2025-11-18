"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum, ensuring rewards are distributed proportionally to the staker's percentage of the pool over a two-year period.
Generated: DETERMINISTIC_a145896b94ad283e
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for calculating rewards
    }

    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public totalRewards; // Total rewards to be distributed
    uint256 public startTime; // Staking start time
    uint256 public endTime; // Staking end time

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGE20 token address
    constructor(address _doge20Token, uint256 _totalRewards) {
        doge20Token = IERC20(_doge20Token);
        totalRewards = _totalRewards;
        startTime = block.timestamp;
        endTime = startTime + 730 days; // 2 years
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(block.timestamp < endTime, "Staking period has ended");

        // Transfer DOGE20 tokens from user to contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Update staker information
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to user
        doge20Token.transfer(msg.sender, amount);

        // Transfer rewards to user if applicable
        if (reward > 0) {
            doge20Token.transfer(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate the reward for a staker
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        if (totalStaked == 0) return 0; // No rewards if no tokens staked
        uint256 proportionalReward = (staker.amount * totalRewards) / totalStaked;
        return proportionalReward - staker.rewardDebt; // Reward calculation
    }

    // Function to claim rewards (if necessary)
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update reward debt
        staker.rewardDebt += reward;

        // Transfer rewards to user
        doge20Token.transfer(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw remaining rewards after staking period ends
    function withdrawRemainingRewards() external onlyOwner {
        require(block.timestamp >= endTime, "Staking period is still ongoing");
        uint256 remainingRewards = doge20Token.balanceOf(address(this));
        require(remainingRewards > 0, "No remaining rewards to withdraw");

        // Transfer remaining rewards to the owner
        doge20Token.transfer(owner(), remainingRewards);
    }
}
```
