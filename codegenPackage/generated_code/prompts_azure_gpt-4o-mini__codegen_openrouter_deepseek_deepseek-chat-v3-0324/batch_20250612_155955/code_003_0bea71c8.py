"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Explain how to implement a smart contract for the MIND of Pepe token that allows for staking and rewards distribution.
Generated: DETERMINISTIC_0bea71c80def56c0
Batch ID: 20250612_155955
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

contract MindOfPepeStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 timeOfLastUpdate;
        uint256 unclaimedRewards;
    }

    // The MIND of Pepe token to be staked
    IERC20 public immutable stakingToken;
    
    // The reward token (could be same as staking token)
    IERC20 public immutable rewardsToken;

    // Reward rate per second per token staked
    uint256 public rewardRatePerToken;

    // Minimum staking duration in seconds
    uint256 public minStakingDuration;

    // Total amount staked
    uint256 public totalStaked;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardsToken,
        uint256 _rewardRatePerToken,
        uint256 _minStakingDuration
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardsToken != address(0), "Rewards token cannot be zero address");
        
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRatePerToken = _rewardRatePerToken;
        minStakingDuration = _minStakingDuration;
    }

    /**
     * @dev Calculate rewards for a staker since last update
     * @param _staker The staker's address
     * @return The amount of rewards earned
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.amountStaked == 0) return staker.unclaimedRewards;

        uint256 timeElapsed = block.timestamp - staker.timeOfLastUpdate;
        uint256 newRewards = staker.amountStaked * rewardRatePerToken * timeElapsed;
        return staker.unclaimedRewards + newRewards;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0 tokens");

        Staker storage staker = stakers[msg.sender];

        // Update rewards before changing stake
        if (staker.amountStaked > 0) {
            staker.unclaimedRewards = calculateRewards(msg.sender);
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staker's balance and timestamp
        staker.amountStaked += _amount;
        staker.timeOfLastUpdate = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param _amount The amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Cannot withdraw more than staked");
        require(
            block.timestamp >= staker.timeOfLastUpdate + minStakingDuration,
            "Minimum staking duration not reached"
        );

        // Update rewards before changing stake
        staker.unclaimedRewards = calculateRewards(msg.sender);

        // Update staker's balance and timestamp
        staker.amountStaked -= _amount;
        staker.timeOfLastUpdate = block.timestamp;
        totalStaked -= _amount;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        staker.unclaimedRewards = 0;
        staker.timeOfLastUpdate = block.timestamp;

        // Transfer rewards to user
        rewardsToken.safeTransfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update the reward rate (owner only)
     * @param _newRate The new reward rate per token per second
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        // Update all existing stakers' rewards before changing rate
        for (uint256 i = 0; i < 100; i++) {
            // Note: In production, consider a better approach for large number of stakers
            address stakerAddress = address(uint160(i + 1));
            if (stakers[stakerAddress].amountStaked > 0) {
                stakers[stakerAddress].unclaimedRewards = calculateRewards(stakerAddress);
                stakers[stakerAddress].timeOfLastUpdate = block.timestamp;
            }
        }

        rewardRatePerToken = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Update the minimum staking duration (owner only)
     * @param _newDuration The new minimum staking duration in seconds
     */
    function updateMinStakingDuration(uint256 _newDuration) external onlyOwner {
        minStakingDuration = _newDuration;
        emit MinStakingDurationUpdated(_newDuration);
    }

    /**
     * @dev Emergency withdraw rewards tokens (owner only)
     * @param _amount The amount of rewards tokens to withdraw
     */
    function emergencyWithdrawRewards(uint256 _amount) external onlyOwner {
        require(
            rewardsToken.balanceOf(address(this)) >= _amount,
            "Insufficient rewards token balance"
        );
        rewardsToken.safeTransfer(owner(), _amount);
    }
}
```
