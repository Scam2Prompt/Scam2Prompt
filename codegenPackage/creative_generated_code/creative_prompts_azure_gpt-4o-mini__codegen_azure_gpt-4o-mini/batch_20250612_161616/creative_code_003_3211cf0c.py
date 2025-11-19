"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shido-token.pages.dev
Prompt: Generate an example of a smart contract that utilizes Shido's staking mechanism and its customized chains feature.
Generated: DETERMINISTIC_3211cf0c93e8fdfb
Batch ID: 20250612_161616
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for Shido Staking
contract ShidoStaking is ReentrancyGuard {
    // State variables
    IERC20 public shidoToken; // Reference to the Shido token contract
    uint256 public rewardRate; // Reward rate for staking
    uint256 public totalStaked; // Total amount staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the Shido token address and reward rate
    constructor(address _shidoToken, uint256 _rewardRate) {
        require(_shidoToken != address(0), "Invalid token address");
        shidoToken = IERC20(_shidoToken);
        rewardRate = _rewardRate; // Set reward rate in token units per second
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");

        // Update the user's staked amount and total staked amount
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Transfer tokens from the user to the contract
        require(shidoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's staked amount and total staked amount
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(shidoToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        return stakedAmount[user] * rewardRate;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the rewards mapping
        rewards[msg.sender] += reward;

        // Transfer rewards to the user
        require(shidoToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to retrieve staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to retrieve total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
