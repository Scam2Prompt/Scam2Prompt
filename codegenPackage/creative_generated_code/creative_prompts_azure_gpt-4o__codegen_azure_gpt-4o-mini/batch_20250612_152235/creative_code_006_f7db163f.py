"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-io-presalestokenclaim.pages.dev
Prompt: Write a Solidity contract for a treasury system that supports staking rewards, token deflation, and liquidity maintenance, as outlined in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_f7db163f1042ec45
Batch ID: 20250612_152235
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Treasury contract for the Galaxy Fox ecosystem
contract GalaxyFoxTreasury is ReentrancyGuard, Ownable {
    // The ERC20 token used for staking
    IERC20 public stakingToken;
    
    // Reward rate per stake (in tokens)
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;

    // Mapping for user stakes
    mapping(address => uint256) public userStakes;
    
    // Mapping for user reward debts
    mapping(address => uint256) public userRewardDebts;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens in the treasury
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Staking amount must be greater than 0");

        // Transfer tokens from user to treasury
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user stakes and total staked amount
        userStakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update total staked amount and user stakes
        totalStaked -= amount;
        userStakes[msg.sender] -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset user reward debt
        userRewardDebts[msg.sender] = totalRewards();

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        return (userStakes[user] * rewardRate) - userRewardDebts[user];
    }

    // Function to get total rewards distributed
    function totalRewards() public view returns (uint256) {
        return totalStaked * rewardRate;
    }

    // Owner can update reward rate
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens held in the treasury by the owner
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        stakingToken.transfer(msg.sender, amount);
    }
}
```
