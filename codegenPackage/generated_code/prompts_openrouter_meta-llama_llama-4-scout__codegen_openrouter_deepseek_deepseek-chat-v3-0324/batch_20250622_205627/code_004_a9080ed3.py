"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Design a basic decentralized application (dApp) on Telos EVM for a gaming launchpad, incorporating features like staking and rewards.
Generated: DETERMINISTIC_a9080ed3d8b9fa0e
Batch ID: 20250622_205627
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GamingLaunchpad is Ownable, ReentrancyGuard {
    // Struct to store staker information
    struct Staker {
        uint256 amount;
        uint256 stakeTime;
        uint256 lastClaimTime;
        uint256 totalRewards;
    }

    // Token used for staking
    IERC20 public stakingToken;
    
    // Reward token
    IERC20 public rewardToken;
    
    // Reward rate per second per token (in wei)
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    
    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Reward rate per second per token (in wei)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }
    
    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards first
        if (staker.amount > 0) {
            _claimRewards();
        }
        
        // Transfer tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        // Update staker info
        staker.amount += amount;
        staker.stakeTime = block.timestamp;
        staker.lastClaimTime = block.timestamp;
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        
        // Claim any pending rewards first
        _claimRewards();
        
        // Update staker info
        staker.amount -= amount;
        
        totalStaked -= amount;
        
        // Transfer tokens back to user
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");
        
        _claimRewards();
    }
    
    /**
     * @dev Internal function to calculate and claim rewards
     */
    function _claimRewards() internal {
        Staker storage staker = stakers[msg.sender];
        
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            require(
                rewardToken.balanceOf(address(this)) >= reward,
                "Insufficient reward tokens"
            );
            
            staker.lastClaimTime = block.timestamp;
            staker.totalRewards += reward;
            
            require(
                rewardToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            
            emit RewardClaimed(msg.sender, reward);
        }
    }
    
    /**
     * @dev Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return reward Pending reward amount
     */
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amount == 0) {
            return 0;
        }
        
        uint256 timeElapsed = block.timestamp - staker.lastClaimTime;
        return staker.amount * timeElapsed * rewardRate;
    }
    
    /**
     * @dev Update reward rate (only owner)
     * @param newRate New reward rate per second per token (in wei)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate != rewardRate, "Same as current rate");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }
    
    /**
     * @dev Withdraw excess reward tokens (only owner)
     * @param amount Amount to withdraw
     */
    function withdrawExcessRewards(uint256 amount) external onlyOwner {
        require(
            rewardToken.balanceOf(address(this)) >= totalPendingRewards() + amount,
            "Cannot withdraw staked rewards"
        );
        
        require(
            rewardToken.transfer(owner(), amount),
            "Reward transfer failed"
        );
    }
    
    /**
     * @dev Calculate total pending rewards for all stakers
     * @return total Total pending rewards
     */
    function totalPendingRewards() public view returns (uint256 total) {
        total = 0;
        // Note: In production, you might want to use a different approach
        // to avoid potential gas issues with large number of stakers
        // This is simplified for demonstration purposes
        address[] memory stakerAddresses = getAllStakers();
        for (uint256 i = 0; i < stakerAddresses.length; i++) {
            total += calculateReward(stakerAddresses[i]);
        }
    }
    
    /**
     * @dev Get all staker addresses (for demonstration purposes)
     * @return Array of staker addresses
     * Note: In production, you would implement a more efficient tracking mechanism
     */
    function getAllStakers() public pure returns (address[] memory) {
        // Implementation note: In a real dApp, you would maintain a list of stakers
        // This is simplified for demonstration purposes
        revert("Not implemented - use a proper staker tracking mechanism");
    }
}
```
