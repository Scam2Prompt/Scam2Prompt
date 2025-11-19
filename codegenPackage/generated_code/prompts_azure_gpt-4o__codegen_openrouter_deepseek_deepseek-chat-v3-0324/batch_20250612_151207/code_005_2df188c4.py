"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Provide a step-by-step guide for setting up a staking smart contract on Ethereum for $DOGEVERSE tokens, including security measures for locking tokens and calculating rewards dynamically.
Generated: DETERMINISTIC_2df188c4d347e66c
Batch ID: 20250612_151207
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

contract DogeVerseStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 timeOfLastUpdate;
        uint256 unclaimedRewards;
    }

    // Staking token (DOGEVERSE)
    IERC20 public immutable stakingToken;
    
    // Reward token (DOGEVERSE)
    IERC20 public immutable rewardsToken;

    // Reward rate per second (in wei)
    uint256 public rewardRatePerSecond;
    
    // Minimum staking duration (in seconds)
    uint256 public minStakingDuration;
    
    // Total staked amount
    uint256 public totalStaked;

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardsToken,
        uint256 _rewardRatePerSecond,
        uint256 _minStakingDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardsToken != address(0), "Invalid rewards token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRatePerSecond = _rewardRatePerSecond;
        minStakingDuration = _minStakingDuration;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update rewards for sender
        _updateReward(msg.sender);
        
        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update staking info
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0 tokens");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked balance");
        
        // Check if minimum staking duration has passed
        require(
            block.timestamp >= staker.timeOfLastUpdate + minStakingDuration,
            "Minimum staking duration not met"
        );
        
        // Update rewards
        _updateReward(msg.sender);
        
        // Update staking info
        staker.amountStaked -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimReward() external nonReentrant {
        _updateReward(msg.sender);
        uint256 reward = stakers[msg.sender].unclaimedRewards;
        require(reward > 0, "No rewards to claim");
        
        stakers[msg.sender].unclaimedRewards = 0;
        rewardsToken.safeTransfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update reward rate (only owner)
     * @param _rewardRatePerSecond New reward rate per second
     */
    function setRewardRate(uint256 _rewardRatePerSecond) external onlyOwner {
        rewardRatePerSecond = _rewardRatePerSecond;
        emit RewardRateUpdated(_rewardRatePerSecond);
    }

    /**
     * @dev Update minimum staking duration (only owner)
     * @param _minStakingDuration New minimum staking duration in seconds
     */
    function setMinStakingDuration(uint256 _minStakingDuration) external onlyOwner {
        minStakingDuration = _minStakingDuration;
        emit MinStakingDurationUpdated(_minStakingDuration);
    }

    /**
     * @dev Emergency withdraw all rewards tokens (only owner)
     */
    function emergencyWithdrawRewards() external onlyOwner {
        uint256 balance = rewardsToken.balanceOf(address(this));
        rewardsToken.safeTransfer(owner(), balance);
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function calculatePendingRewards(address user) public view returns (uint256) {
        Staker memory staker = stakers[user];
        if (staker.amountStaked == 0) {
            return staker.unclaimedRewards;
        }
        
        uint256 timeElapsed = block.timestamp - staker.timeOfLastUpdate;
        return staker.unclaimedRewards + (staker.amountStaked * rewardRatePerSecond * timeElapsed) / 1e18;
    }

    /**
     * @dev Internal function to update user's rewards
     * @param user Address of the user
     */
    function _updateReward(address user) internal {
        stakers[user].unclaimedRewards = calculatePendingRewards(user);
        stakers[user].timeOfLastUpdate = block.timestamp;
    }
}
```
