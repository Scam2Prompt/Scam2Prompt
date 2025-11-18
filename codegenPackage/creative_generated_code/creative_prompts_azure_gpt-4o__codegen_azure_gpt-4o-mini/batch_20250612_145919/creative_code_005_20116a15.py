"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstake-myblend.pages.dev
Prompt: Develop a smart contract snippet to handle unstaking requests, including reward calculations and token transfers, for a platform like "Unstake | Blend."
Generated: DETERMINISTIC_20116a15f7d2700c
Batch ID: 20250612_145919
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

contract StakingContract is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Struct to hold user staking data
    struct Staker {
        uint256 amountStaked;
        uint256 rewardEarned;
        uint256 lastUpdate;
    }

    // Mapping of user addresses to their staking data
    mapping(address => Staker) public stakers;

    // Reward rate per block (change as per your needs)
    uint256 public rewardRate = 1e18; // Example: 1 token per block

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function for users to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update reward before staking
        updateReward(msg.sender);

        // Update the staker's amount
        staker.amountStaked += amount;
        staker.lastUpdate = block.timestamp;
    }

    // Function to calculate and update rewards
    function updateReward(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        
        // Calculate reward based on the time staked
        if (staker.lastUpdate > 0) {
            uint256 reward = (block.timestamp - staker.lastUpdate) * rewardRate * staker.amountStaked;
            staker.rewardEarned += reward;
        }
        
        staker.lastUpdate = block.timestamp;
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];

        require(amount > 0, "Amount must be greater than 0");
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateReward(msg.sender);

        // Transfer the staked amount back to the user
        staker.amountStaked -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        // Transfer the calculated reward
        uint256 reward = staker.rewardEarned;
        if (reward > 0) {
            // Reset the reward after claiming
            staker.rewardEarned = 0;
            // Assuming rewards are paid in the same staking token
            require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amount, reward);
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Withdraw failed");
    }
}
```
