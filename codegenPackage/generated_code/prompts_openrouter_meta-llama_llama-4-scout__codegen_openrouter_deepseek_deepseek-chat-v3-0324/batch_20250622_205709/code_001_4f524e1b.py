"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Recommend a suitable smart contract platform for building a staking platform similar to Solidus AI Tech, considering EVM chains support.
Generated: DETERMINISTIC_4f524e1b00758322
Batch ID: 20250622_205709
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

/**
 * @title StakingPlatform
 * @dev A staking contract that allows users to stake tokens and earn rewards.
 * Designed for EVM-compatible chains with considerations for gas efficiency.
 */
contract StakingPlatform {
    // Token to be staked (ERC-20)
    IERC20 public stakingToken;
    // Reward token (ERC-20)
    IERC20 public rewardToken;
    
    // Staking period in seconds
    uint256 public stakingPeriod;
    // Reward rate (reward tokens per staked token per second)
    uint256 public rewardRate;
    // When staking starts (timestamp)
    uint256 public stakingStartTime;
    
    // Total staked tokens
    uint256 public totalStaked;
    // Total rewards distributed
    uint256 public totalRewardsDistributed;
    
    // User staking details
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastUpdateTime;
    }
    
    // Mapping of user addresses to their staking details
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor initializes the staking platform
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _stakingPeriod Duration of staking period in seconds
     * @param _rewardRate Reward rate (tokens per staked token per second)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingPeriod,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_stakingPeriod > 0, "Staking period must be greater than 0");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingPeriod = _stakingPeriod;
        rewardRate = _rewardRate;
        stakingStartTime = block.timestamp;
    }
    
    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(block.timestamp < stakingStartTime + stakingPeriod, "Staking period has ended");
        
        // Update rewards before changing stake
        _updateReward(msg.sender);
        
        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update staker's balance and total staked
        stakers[msg.sender].amount += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens from the contract
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked balance");
        
        // Update rewards before changing stake
        _updateReward(msg.sender);
        
        // Update staker's balance and total staked
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        _updateReward(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;
        
        require(reward > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient reward tokens");
        
        stakers[msg.sender].rewardDebt = 0;
        totalRewardsDistributed += reward;
        
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    /**
     * @dev Internal function to update user's reward balance
     * @param user Address of the user to update
     */
    function _updateReward(address user) internal {
        if (stakers[user].amount == 0) return;
        
        uint256 timeElapsed = block.timestamp - stakers[user].lastUpdateTime;
        if (timeElapsed == 0) return;
        
        uint256 reward = stakers[user].amount * rewardRate * timeElapsed;
        stakers[user].rewardDebt += reward;
        stakers[user].lastUpdateTime = block.timestamp;
    }
    
    /**
     * @dev View function to check pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        if (stakers[user].amount == 0) return stakers[user].rewardDebt;
        
        uint256 timeElapsed = block.timestamp - stakers[user].lastUpdateTime;
        return stakers[user].rewardDebt + (stakers[user].amount * rewardRate * timeElapsed);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
