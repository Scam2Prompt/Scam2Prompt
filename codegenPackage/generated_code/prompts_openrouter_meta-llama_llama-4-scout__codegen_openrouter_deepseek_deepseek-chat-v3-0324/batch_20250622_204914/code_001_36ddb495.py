"""
Generated Code Metadata:
========================
Original URL: https://renzo-apps.medium.com
Prompt: "Explain the process of restaking tokens in the Renzo Protocol and its benefits."
Generated: DETERMINISTIC_36ddb4956ba73678
Batch ID: 20250622_204914
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RenzoRestaking
 * @dev Contract for restaking tokens in Renzo Protocol
 */
contract RenzoRestaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token to be staked
    IERC20 public stakingToken;
    
    // Reward token
    IERC20 public rewardToken;
    
    // Staking period in blocks
    uint256 public stakingPeriod;
    
    // Reward rate per block
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Mapping of user addresses to their staked amount
    mapping(address => uint256) public stakedBalances;
    
    // Mapping of user addresses to their last stake time
    mapping(address => uint256) public lastStakeTime;
    
    // Mapping of user addresses to their pending rewards
    mapping(address => uint256) public pendingRewards;

    event Staked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _stakingPeriod Staking period in blocks
     * @param _rewardRate Reward rate per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingPeriod,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_stakingPeriod > 0, "Staking period must be greater than 0");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingPeriod = _stakingPeriod;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update pending rewards before staking
        _updateRewards(msg.sender);
        
        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update staked balance
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        
        // Update last stake time
        lastStakeTime[msg.sender] = block.number;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Restake tokens (compound rewards)
     */
    function restake() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 rewardAmount = pendingRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to restake");
        
        // Reset pending rewards
        pendingRewards[msg.sender] = 0;
        
        // Add rewards to staked balance
        stakedBalances[msg.sender] += rewardAmount;
        totalStaked += rewardAmount;
        
        // Update last stake time
        lastStakeTime[msg.sender] = block.number;
        
        emit Restaked(msg.sender, rewardAmount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 rewardAmount = pendingRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        
        // Reset pending rewards
        pendingRewards[msg.sender] = 0;
        
        // Transfer rewards to user
        rewardToken.safeTransfer(msg.sender, rewardAmount);
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        _updateRewards(msg.sender);
        
        // Update staked balance
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Update rewards for a user
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        if (stakedBalances[user] == 0) {
            lastStakeTime[user] = block.number;
            return;
        }
        
        uint256 blocksSinceLastStake = block.number - lastStakeTime[user];
        uint256 reward = (stakedBalances[user] * blocksSinceLastStake * rewardRate) / 1e18;
        
        pendingRewards[user] += reward;
        lastStakeTime[user] = block.number;
    }

    /**
     * @dev Get pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards amount
     */
    function getPendingRewards(address user) external view returns (uint256) {
        if (stakedBalances[user] == 0) {
            return pendingRewards[user];
        }
        
        uint256 blocksSinceLastStake = block.number - lastStakeTime[user];
        uint256 reward = (stakedBalances[user] * blocksSinceLastStake * rewardRate) / 1e18;
        
        return pendingRewards[user] + reward;
    }

    /**
     * @dev Update reward rate (only owner)
     * @param newRate New reward rate per block
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
    }

    /**
     * @dev Emergency withdraw all rewards (only owner)
     */
    function emergencyWithdrawRewards() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        rewardToken.safeTransfer(owner(), balance);
    }
}
```
