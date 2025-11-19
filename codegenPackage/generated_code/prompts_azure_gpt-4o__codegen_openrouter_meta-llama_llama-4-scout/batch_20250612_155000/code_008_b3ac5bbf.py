"""
Generated Code Metadata:
========================
Original URL: https://asterdex.vercel.app
Prompt: Create a Solidity-based staking contract for USDF tokens that offers optimized returns and diversified income strategies, as described in the Astherus documentation.
Generated: DETERMINISTIC_b3ac5bbfbd8835ab
Batch ID: 20250612_155000
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title Astherus Staking Contract
 * @author [Your Name]
 * @notice This contract provides a staking mechanism for USDF tokens, offering optimized returns and diversified income strategies.
 */
contract AstherusStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // USDF token contract
    IERC20 public usdfToken;

    // Staking token reward contract
    IERC20 public rewardToken;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward per share
    uint256 public rewardPerShare;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward distribution interval (in seconds)
    uint256 public rewardDistributionInterval;

    // Timestamp of last reward distribution
    uint256 public lastRewardDistribution;

    // Reward amount per interval
    uint256 public rewardAmountPerInterval;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _usdfToken USDF token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardDistributionInterval Reward distribution interval (in seconds)
     * @param _rewardAmountPerInterval Reward amount per interval
     */
    constructor(
        address _usdfToken,
        address _rewardToken,
        uint256 _rewardDistributionInterval,
        uint256 _rewardAmountPerInterval
    ) public {
        usdfToken = IERC20(_usdfToken);
        rewardToken = IERC20(_rewardToken);
        rewardDistributionInterval = _rewardDistributionInterval;
        rewardAmountPerInterval = _rewardAmountPerInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Stake USDF tokens
     * @param _amount Amount of USDF tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer USDF tokens from user to contract
        usdfToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update total staking balance
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Emit staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake USDF tokens
     * @param _amount Amount of USDF tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Update total staking balance
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer USDF tokens from contract to user
        usdfToken.transfer(msg.sender, _amount);

        // Emit unstaked event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward variables
     */
    function updateRewardVariables() internal {
        uint256 currentTimestamp = block.timestamp;
        uint256 intervalElapsed = currentTimestamp.sub(lastRewardDistribution);

        if (intervalElapsed >= rewardDistributionInterval) {
            uint256 reward = rewardAmountPerInterval.mul(intervalElapsed.div(rewardDistributionInterval));

            // Update accumulated reward per share
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStakingBalance));

            // Update last reward distribution timestamp
            lastRewardDistribution = currentTimestamp;
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        updateRewardVariables();

        // Calculate user's reward debt
        uint256 userRewardDebt = rewardDebt[msg.sender];

        // Calculate user's reward
        uint256 userReward = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18).sub(userRewardDebt);

        // Update user's reward debt
        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, userReward);

        // Emit rewards distributed event
        emit RewardsDistributed(msg.sender, userReward);
    }

    /**
     * @notice Withdraw stuck tokens
     * @param _token Token contract address
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawStuckTokens(address _token, uint256 _amount) external onlyOwner nonReentrant {
        IERC20 token = IERC20(_token);
        token.transfer(msg.sender, _amount);
    }
}
```
