"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-oriviumio.pages.dev
Prompt: Create a Solidity smart contract for staking ORI tokens on the Orivium platform, incorporating the “Play & Earn” model.
Generated: DETERMINISTIC_cb1321ba4191a6ca
Batch ID: 20250612_162325
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for ORI tokens with Play & Earn model
contract OriviumStaking is Ownable {
    // State variables
    IERC20 public oriToken; // Address of the ORI token contract
    uint256 public totalStaked; // Total amount of ORI tokens staked
    uint256 public rewardRate; // Reward rate for stakers
    mapping(address => uint256) public balances; // Staking balance of each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdated; // Last update timestamp for rewards

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _oriToken, uint256 _rewardRate) {
        oriToken = _oriToken;
        rewardRate = _rewardRate;
    }

    // Function to stake ORI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(oriToken.balanceOf(msg.sender) >= amount, "Insufficient ORI balance");

        // Update user rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        oriToken.transferFrom(msg.sender, address(this), amount);

        // Update state variables
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ORI tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user rewards before unstaking
        updateRewards(msg.sender);

        // Transfer tokens back to user
        oriToken.transfer(msg.sender, amount);

        // Update state variables
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for user
        rewards[msg.sender] = 0;

        // Transfer rewards to user
        oriToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        if (timeElapsed > 0) {
            uint256 earnedReward = (balances[user] * rewardRate * timeElapsed) / 1e18; // Assuming rewardRate is in wei
            rewards[user] += earnedReward;
            lastUpdated[user] = block.timestamp; // Update last updated time
        }
    }

    // Function to set reward rate, only callable by owner
    function setRewardRate(uint256 newRate) external onlyOwner {
        updateRewards(msg.sender); // Update rewards for owner before changing the rate
        rewardRate = newRate;
    }

    // Function to view staked balance of a user
    function stakedBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to view pending rewards of a user
    function pendingRewards(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        uint256 earnedReward = (balances[user] * rewardRate * timeElapsed) / 1e18;
        return rewards[user] + earnedReward;
    }
}
```
