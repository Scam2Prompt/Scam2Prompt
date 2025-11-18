"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a Solidity contract that implements a treasury system for a token like $GFOX, ensuring it supports staking rewards, token deflation, and liquidity maintenance.
Generated: DETERMINISTIC_cfacb5e36fbf1b09
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Treasury contract to manage staking rewards, token deflation, and liquidity.
contract Treasury is Ownable {
    using SafeMath for uint256;

    // Token to be managed by the treasury
    IERC20 public token;

    // Struct to represent a staker
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastUpdated;
    }

    // Mapping of stakers to their data
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate to distribute
    uint256 public rewardRate; // e.g., 1 token per block

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the treasury contract
    constructor(IERC20 _token, uint256 _rewardRate) {
        require(address(_token) != address(0), "Zero address: token");
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the staker's rewards before changing stakes
        updateRewards(msg.sender);

        // Transfer tokens to the treasury
        token.transferFrom(msg.sender, address(this), amount);

        // Update staker data
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update the staker's rewards before changing stakes
        updateRewards(msg.sender);

        // Transfer tokens back to the staker
        token.transfer(msg.sender, amount);

        // Update staker data
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset the reward debt to zero after claiming
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the staker
        token.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards
    function updateRewards(address account) internal {
        Staker storage staker = stakers[account];
        if (totalStaked > 0) {
            uint256 pendingReward = staker.stakedAmount.mul(rewardRate).mul(block.number - staker.lastUpdated);
            staker.rewardDebt = staker.rewardDebt.add(pendingReward);
        }
        staker.lastUpdated = block.number;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw a specified amount of tokens (for liquidity purposes)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient treasury balance");
        token.transfer(msg.sender, amount);
    }
}
```
