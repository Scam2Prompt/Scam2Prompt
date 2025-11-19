"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Develop a staking incentive program in Solidity that offers higher rewards for early stakers, inspired by DOGE20's early staking incentive feature.
Generated: DETERMINISTIC_4b135f5426183c9b
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingIncentive is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Struct to store staker information
    struct Staker {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    // Token to be staked
    IERC20 public immutable stakingToken;
    // Reward token (can be same as staking token)
    IERC20 public immutable rewardToken;

    // Staking parameters
    uint256 public constant EARLY_STAKING_PERIOD = 30 days;
    uint256 public constant EARLY_STAKING_BONUS = 50; // 50% bonus for early stakers
    uint256 public constant BASE_APR = 1000; // 10% APR (1000 = 10%)
    uint256 public constant BONUS_APR = 1500; // 15% APR during early period (1500 = 15%)

    // Total staked amount
    uint256 public totalStaked;
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Contract deployment time
    uint256 public immutable deploymentTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        deploymentTime = block.timestamp;
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Claim any pending rewards first
        if (stakers[msg.sender].amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker info
        stakers[msg.sender].amount = stakers[msg.sender].amount.add(amount);
        stakers[msg.sender].stakedAt = block.timestamp;
        stakers[msg.sender].lastClaimed = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked balance");

        // Claim rewards first
        _claimRewards();

        // Update staker info
        stakers[msg.sender].amount = stakers[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amount > 0, "No staked balance");
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() private {
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            stakers[msg.sender].lastClaimed = block.timestamp;
            rewardToken.safeTransfer(msg.sender, rewards);
            emit RewardClaimed(msg.sender, rewards);
        }
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param staker Address of the staker
     * @return rewards Amount of pending rewards
     */
    function calculateRewards(address staker) public view returns (uint256 rewards) {
        Staker memory s = stakers[staker];
        if (s.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(s.lastClaimed);
        uint256 stakingStartToNow = block.timestamp.sub(s.stakedAt);

        // Check if staker is eligible for early bonus
        bool isEarlyStaker = stakingStartToNow <= EARLY_STAKING_PERIOD;

        // Calculate APR based on staking time
        uint256 currentAPR = isEarlyStaker ? 
            BASE_APR.add(EARLY_STAKING_BONUS) : 
            BASE_APR;

        // Calculate rewards
        rewards = s.amount
            .mul(currentAPR)
            .mul(stakingDuration)
            .div(365 days)
            .div(10000); // APR is in basis points (10000 = 100%)
    }

    /**
     * @notice Get staker information
     * @param staker Address of the staker
     * @return amount Staked amount
     * @return stakedAt Timestamp when tokens were staked
     * @return lastClaimed Timestamp when rewards were last claimed
     * @return pendingRewards Pending rewards for the staker
     */
    function getStakerInfo(address staker) external view returns (
        uint256 amount,
        uint256 stakedAt,
        uint256 lastClaimed,
        uint256 pendingRewards
    ) {
        Staker memory s = stakers[staker];
        return (
            s.amount,
            s.stakedAt,
            s.lastClaimed,
            calculateRewards(staker)
        );
    }
}
```
