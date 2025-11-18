"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Write a Solidity contract that enables staking rewards to scale based on the number of tokens held by the user, inspired by the $STARS reward mechanism.
Generated: DETERMINISTIC_233ae3ab5b2c001a
Batch ID: 20250612_154133
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for token rewards
contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // ERC20 token to be staked
    IERC20 public stakingToken;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Mapping to track the amount staked by each user
    mapping(address => uint256) public stakes;

    // Mapping to track the reward debt for each user
    mapping(address => uint256) public rewardDebt;

    // Reward rate per token staked per block
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Update total staked tokens and user's stake
        totalStaked = totalStaked.add(amount);
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update reward debt
        rewardDebt[msg.sender] = rewardDebt[msg.sender].add(calculatePendingReward(msg.sender));
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");
        
        // Update total staked tokens and user's stake
        totalStaked = totalStaked.sub(amount);
        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        
        // Update reward debt
        rewardDebt[msg.sender] = rewardDebt[msg.sender].add(calculatePendingReward(msg.sender));
        
        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculatePendingReward(msg.sender);
        require(reward > 0, "No rewards available to claim");
        
        // Reset user's reward debt
        rewardDebt[msg.sender] = 0;
        
        // Transfer rewards to user
        totalRewards = totalRewards.add(reward);
        stakingToken.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingReward(address user) internal view returns (uint256) {
        return stakes[user].mul(rewardRate).div(1e18);
    }

    // Function to update reward rate (onlyOwner)
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw tokens from the contract (onlyOwner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient balance in contract");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
