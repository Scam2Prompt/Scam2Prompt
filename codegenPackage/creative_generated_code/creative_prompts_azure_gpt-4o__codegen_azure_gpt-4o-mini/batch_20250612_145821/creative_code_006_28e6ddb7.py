"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepeunchained.pages.dev
Prompt: Provide an example of how to implement double staking rewards for $PEPU tokens on Layer 2 using Solidity.
Generated: DETERMINISTIC_28e6ddb74bcb7220
Batch ID: 20250612_145821
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

// Importing the relevant interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for implementing double staking rewards for $PEPU tokens
contract DoubleStakingRewards is Ownable {
    // State variables
    IERC20 public pepuToken; // The PEPU token contract
    uint256 public rewardRate; // Rate of reward per staked token
    mapping(address => uint256) public stakedAmount; // Amount of tokens staked by each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user
    mapping(address => uint256) public lastUpdate; // Last update time for rewards calculation

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the PEPU token address and initial reward rate
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount
        stakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards before claiming
        updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset rewards for user
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        pepuToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(address user) internal {
        // Calculate accumulated rewards
        if (stakedAmount[user] > 0) {
            uint256 newRewards = (block.timestamp - lastUpdate[user]) * rewardRate * stakedAmount[user];
            rewards[user] += newRewards;
        }
        // Update last update time
        lastUpdate[user] = block.timestamp;
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        updateAllRewards();
        rewardRate = newRate;
    }

    // Internal function to update rewards for all users (called when changing reward rate)
    function updateAllRewards() internal {
        for (uint256 i = 0; i < stakedAmount.length; i++) {
            address user = address(i); // Placeholder, you'll need your own method to iterate through users
            updateRewards(user);
        }
    }
}
```
