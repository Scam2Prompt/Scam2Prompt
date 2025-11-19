"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Create a smart contract in Solidity for staking $MIND tokens with dynamic APY rewards, ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_0e0905590dc23301
Batch ID: 20250612_153954
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MindTokenStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Staker {
        uint256 amountStaked;
        uint256 timeOfLastUpdate;
        uint256 unclaimedRewards;
    }

    // The token to be staked
    IERC20 public immutable stakingToken;
    
    // Reward parameters
    uint256 public rewardRate; // APY percentage (e.g., 1000 = 10%)
    uint256 public rewardInterval; // Interval for reward calculation (in seconds)
    uint256 public minStakingDuration; // Minimum staking duration (in seconds)
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        uint256 _rewardRate,
        uint256 _rewardInterval,
        uint256 _minStakingDuration
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        rewardInterval = _rewardInterval;
        minStakingDuration = _minStakingDuration;
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        // Update rewards before staking new amount
        if (staker.amountStaked > 0) {
            staker.unclaimedRewards += calculateRewards(msg.sender);
        }
        
        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update staking details
        staker.amountStaked += amount;
        staker.timeOfLastUpdate = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= staker.timeOfLastUpdate + minStakingDuration,
            "Minimum staking duration not reached"
        );
        
        // Calculate and update rewards
        uint256 rewards = calculateRewards(msg.sender);
        staker.unclaimedRewards += rewards;
        
        // Update staking details
        staker.amountStaked -= amount;
        staker.timeOfLastUpdate = block.timestamp;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender) + stakers[msg.sender].unclaimedRewards;
        require(rewards > 0, "No rewards to claim");
        
        // Reset unclaimed rewards and update last update time
        stakers[msg.sender].unclaimedRewards = 0;
        stakers[msg.sender].timeOfLastUpdate = block.timestamp;
        
        // Transfer rewards
        stakingToken.safeTransfer(msg.sender, rewards);
        
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return rewards The calculated rewards
     */
    function calculateRewards(address stakerAddress) public view returns (uint256 rewards) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amountStaked == 0) return 0;
        
        uint256 timeElapsed = block.timestamp - staker.timeOfLastUpdate;
        rewards = (staker.amountStaked * rewardRate * timeElapsed) / (rewardInterval * 10000);
    }

    /**
     * @notice Update the reward rate (only owner)
     * @param newRate New APY percentage (e.g., 1000 = 10%)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Update the minimum staking duration (only owner)
     * @param newDuration New minimum duration in seconds
     */
    function updateMinStakingDuration(uint256 newDuration) external onlyOwner {
        minStakingDuration = newDuration;
        emit MinStakingDurationUpdated(newDuration);
    }

    /**
     * @notice Emergency withdraw tokens from contract (only owner)
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
