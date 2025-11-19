"""
Generated Code Metadata:
========================
Original URL: https://steth-pools.pages.dev
Prompt: "Create a code snippet in Solidity to implement a similar staking rewards pool for a different Ethereum token, using the stETH Rewards Pool as a reference."
Generated: DETERMINISTIC_0e689ebb0d2f0f64
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Rewards Pool for a different Ethereum token
 * @author [Your Name]
 * @notice This contract implements a staking rewards pool for a different Ethereum token,
 *          similar to the stETH Rewards Pool.
 */
contract StakingRewardsPool {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token being staked
    IERC20 public stakingToken;

    // Rewards token
    IERC20 public rewardsToken;

    // Staking rewards pool parameters
    uint256 public rewardsPerSecond;
    uint256 public startTime;
    uint256 public endTime;

    // User staking information
    mapping(address => uint256) public userStakedAmounts;
    mapping(address => uint256) public userRewardsEarned;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _stakingToken The token being staked
     * @param _rewardsToken The rewards token
     * @param _rewardsPerSecond The rewards per second
     * @param _startTime The start time of the staking rewards pool
     * @param _endTime The end time of the staking rewards pool
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardsToken,
        uint256 _rewardsPerSecond,
        uint256 _startTime,
        uint256 _endTime
    ) public {
        require(_stakingToken != IERC20(address(0)), "Staking token cannot be zero");
        require(_rewardsToken != IERC20(address(0)), "Rewards token cannot be zero");
        require(_rewardsPerSecond > 0, "Rewards per second must be greater than zero");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be greater than start time");

        stakingToken = _stakingToken;
        rewardsToken = _rewardsToken;
        rewardsPerSecond = _rewardsPerSecond;
        startTime = _startTime;
        endTime = _endTime;
    }

    /**
     * @notice Stake tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Stake amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient staking token balance");

        userStakedAmounts[msg.sender] = userStakedAmounts[msg.sender].add(amount);
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) public {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(userStakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        userStakedAmounts[msg.sender] = userStakedAmounts[msg.sender].sub(amount);
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        uint256 rewardsEarned = calculateRewards(msg.sender);
        require(rewardsEarned > 0, "No rewards earned");

        userRewardsEarned[msg.sender] = userRewardsEarned[msg.sender].add(rewardsEarned);
        rewardsToken.safeTransfer(msg.sender, rewardsEarned);

        emit RewardsClaimed(msg.sender, rewardsEarned);
    }

    /**
     * @notice Calculate rewards earned by a user
     * @param user The user's address
     * @return The rewards earned by the user
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = userStakedAmounts[user];
        uint256 secondsStaked = block.timestamp.sub(startTime);
        if (secondsStaked > endTime.sub(startTime)) {
            secondsStaked = endTime.sub(startTime);
        }

        uint256 rewardsEarned = stakedAmount.mul(rewardsPerSecond).mul(secondsStaked) / 1e18;
        return rewardsEarned.sub(userRewardsEarned[user]);
    }

    /**
     * @notice Update rewards per second
     * @param _rewardsPerSecond The new rewards per second
     */
    function updateRewardsPerSecond(uint256 _rewardsPerSecond) public onlyOwner {
        require(_rewardsPerSecond > 0, "Rewards per second must be greater than zero");

        rewardsPerSecond = _rewardsPerSecond;
    }

    /**
     * @notice Update start time
     * @param _startTime The new start time
     */
    function updateStartTime(uint256 _startTime) public onlyOwner {
        require(_startTime > block.timestamp, "Start time must be in the future");

        startTime = _startTime;
    }

    /**
     * @notice Update end time
     * @param _endTime The new end time
     */
    function updateEndTime(uint256 _endTime) public onlyOwner {
        require(_endTime > startTime, "End time must be greater than start time");

        endTime = _endTime;
    }
}
```
