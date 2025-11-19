"""
Generated Code Metadata:
========================
Original URL: https://icoprotolcol.com
Prompt: Provide an example of a smart contract for staking tokens that aligns with the features mentioned on the Guildhall platform.
Generated: DETERMINISTIC_648a40dd9fd12b3e
Batch ID: 20250612_162711
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

/**
 * @title Token Staking Contract
 * @notice Allows users to stake ERC20 tokens and earn rewards
 * @dev Implements staking functionality with reward distribution
 */
contract TokenStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The ERC20 token being staked
    IERC20 public stakingToken;
    // The ERC20 reward token
    IERC20 public rewardToken;

    // Reward rate per token per second
    uint256 public rewardRate;
    // Total amount currently staked
    uint256 public totalStaked;
    // Precision factor for reward calculation
    uint256 public constant PRECISION = 1e18;
    // Minimum stake duration in seconds
    uint256 public minStakeDuration;
    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @notice Constructor to initialize the staking contract
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Initial reward rate per token per second
     * @param _minStakeDuration Minimum stake duration in seconds
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
    }

    /**
     * @notice Stake tokens to start earning rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];

        // Claim any pending rewards first
        if (staker.amountStaked > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker's information
        staker.amountStaked += amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;

        // Update reward debt
        staker.rewardDebt = staker.amountStaked * rewardRate * PRECISION;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked balance");

        // Check if minimum stake duration has passed
        require(
            block.timestamp >= staker.lastStakeTime + minStakeDuration,
            "Minimum stake duration not met"
        );

        // Claim rewards first
        _claimRewards();

        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Update reward debt
        staker.rewardDebt = staker.amountStaked * rewardRate * PRECISION;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amountStaked > 0, "No tokens staked");
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and distribute rewards
     */
    function _claimRewards() private {
        Staker storage staker = stakers[msg.sender];
        uint256 pending = calculatePendingRewards(msg.sender);

        if (pending > 0) {
            // Ensure contract has enough reward tokens
            uint256 rewardBalance = rewardToken.balanceOf(address(this));
            require(rewardBalance >= pending, "Insufficient reward tokens");

            // Transfer rewards to staker
            rewardToken.safeTransfer(msg.sender, pending);
            totalRewardsDistributed += pending;

            emit RewardClaimed(msg.sender, pending);
        }

        // Reset reward debt
        staker.rewardDebt = staker.amountStaked * rewardRate * PRECISION;
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return Amount of pending rewards
     */
    function calculatePendingRewards(address stakerAddress) public view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amountStaked == 0) return 0;

        uint256 currentReward = staker.amountStaked * rewardRate * 
            (block.timestamp - staker.lastStakeTime) * PRECISION;
        return currentReward - staker.rewardDebt;
    }

    /**
     * @notice Update the reward rate
     * @param newRate New reward rate per token per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Update the minimum stake duration
     * @param newDuration New minimum stake duration in seconds
     */
    function updateMinStakeDuration(uint256 newDuration) external onlyOwner {
        minStakeDuration = newDuration;
        emit MinStakeDurationUpdated(newDuration);
    }

    /**
     * @notice Emergency withdraw staked tokens without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "No tokens staked");

        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;

        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @notice Recover ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
