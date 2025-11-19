"""
Generated Code Metadata:
========================
Original URL: https://appscottyclaims.pages.dev
Prompt: Create a Solidity smart contract that allows users to stake $SCOTTY tokens and automatically distribute rewards at a rate of 82.5 $SCOTTY per ETH block.
Generated: DETERMINISTIC_fe99b6e59bc61549
Batch ID: 20250612_161035
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

// Importing the ERC20 interface for the $SCOTTY token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Staking contract for $SCOTTY token
contract ScottyStaking {
    // State variables
    IERC20 public scottyToken; // Reference to the $SCOTTY token contract
    uint256 public rewardRate = 82.5 ether; // Reward rate per ETH block
    uint256 public totalStaked; // Total amount of $SCOTTY tokens staked
    uint256 public lastRewardBlock; // Last block number rewards were distributed

    // Mapping to track user stakes and rewards
    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewards; // User rewards

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $SCOTTY token address
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);
        lastRewardBlock = block.number; // Initialize last reward block
    }

    // Function to stake $SCOTTY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update rewards before staking
        _updateRewards(msg.sender);

        stakes[msg.sender] += amount; // Update user's stake
        totalStaked += amount; // Update total staked amount

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $SCOTTY tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakes[msg.sender] -= amount; // Update user's stake
        totalStaked -= amount; // Update total staked amount

        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender); // Update rewards before claiming

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset user's rewards

        require(scottyToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 blocksPassed = block.number - lastRewardBlock; // Calculate blocks passed
        if (blocksPassed > 0 && totalStaked > 0) {
            uint256 reward = blocksPassed * rewardRate; // Calculate total rewards
            rewards[user] += (reward * stakes[user]) / totalStaked; // Distribute rewards proportionally
        }
        lastRewardBlock = block.number; // Update last reward block
    }

    // Function to view the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to view the user's pending rewards
    function getPendingRewards(address user) external view returns (uint256) {
        uint256 blocksPassed = block.number - lastRewardBlock;
        uint256 reward = blocksPassed * rewardRate;
        return rewards[user] + (reward * stakes[user]) / totalStaked;
    }
}
```
