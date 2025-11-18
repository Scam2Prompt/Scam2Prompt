"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate code to implement staking functionality for the $ZUSHI token, ensuring users can stake their tokens and receive rewards based on the distribution model outlined in the Zushi ecosystem.
Generated: DETERMINISTIC_dbf34574892d1921
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ZUSHI Token contract
interface IZUSHI is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for $ZUSHI token
contract ZushiStaking is ReentrancyGuard, Ownable {
    // Variables for staking
    IZUSHI public zushiToken; // The ZUSHI token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public totalStaked; // Total amount of tokens staked by users

    // User staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for calculating pending rewards
    }
    
    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake information
    mapping(address => uint256) public pendingRewards; // Pending rewards for each user

    // Events for staking activity
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Constructor to initialize the staking contract
    constructor(IZUSHI _zushiToken, uint256 _rewardRate) {
        zushiToken = _zushiToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(zushiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;
        stakes[msg.sender].rewardDebt = calculateRewardDebt(msg.sender);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        // Claim any pending rewards before unstaking
        claimRewards();

        require(zushiToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public nonReentrant {
        uint256 reward = calculatePendingRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset reward debt after claiming
        pendingRewards[msg.sender] = 0;
        stakes[msg.sender].rewardDebt = calculateRewardDebt(msg.sender);
        
        zushiToken.mint(msg.sender, reward); // Mint rewards to the user
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        return stakes[user].amount * rewardRate / 1e18 - stakes[user].rewardDebt;
    }

    // Internal function to calculate reward debt
    function calculateRewardDebt(address user) internal view returns (uint256) {
        return stakes[user].amount * rewardRate / 1e18;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw zushi tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(zushiToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
