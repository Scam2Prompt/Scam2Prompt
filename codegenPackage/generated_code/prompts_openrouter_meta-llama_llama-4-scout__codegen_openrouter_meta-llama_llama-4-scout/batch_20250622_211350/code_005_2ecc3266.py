"""
Generated Code Metadata:
========================
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Develop a smart contract code to deploy a similar staking pool on BNB Smart Chain, inspired by the Bitcoin BSC project.
Generated: DETERMINISTIC_2ecc3266125177c3
Batch ID: 20250622_211350
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title StakingPool Contract
 * @author [Your Name]
 * @notice A staking pool contract inspired by Bitcoin BSC, deployed on BNB Smart Chain.
 */
contract StakingPool is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract instance
    IERC20 public token;

    // Staking pool properties
    uint256 public totalStaked;
    uint256 public totalRewards;
    uint256 public stakingDuration; // in seconds
    uint256 public stakingStartTime;
    uint256 public rewardPerSecond;

    // User staking information
    mapping(address => uint256) public userStakedAmounts;
    mapping(address => uint256) public userRewardDebt;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor function
     * @param _token Token contract address
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        IERC20 _token,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) {
        require(
            address(_token) != address(0),
            "Token contract address cannot be zero"
        );
        token = _token;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @dev Stake tokens function
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(
            token.balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );

        // Transfer tokens to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staked amount
        userStakedAmounts[msg.sender] = userStakedAmounts[msg.sender].add(_amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens function
     */
    function unstake() external nonReentrant {
        require(userStakedAmounts[msg.sender] > 0, "No staked tokens to unstake");

        // Calculate user's reward debt
        uint256 rewardDebt = getRewardDebt(msg.sender);

        // Update user's reward debt
        userRewardDebt[msg.sender] = rewardDebt;

        // Transfer staked tokens back to user
        token.transfer(msg.sender, userStakedAmounts[msg.sender]);

        // Reset user's staked amount
        userStakedAmounts[msg.sender] = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(userStakedAmounts[msg.sender]);

        // Emit unstaked event
        emit Unstaked(msg.sender, userStakedAmounts[msg.sender]);
    }

    /**
     * @dev Get reward debt function
     * @param _user User address
     * @return Reward debt
     */
    function getRewardDebt(address _user) public view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(stakingStartTime);
        uint256 rewards = stakedDuration.mul(rewardPerSecond).mul(userStakedAmounts[_user]).div(totalStaked);
        return userRewardDebt[_user].add(rewards);
    }

    /**
     * @dev Claim rewards function
     */
    function claimRewards() external nonReentrant {
        require(userStakedAmounts[msg.sender] > 0, "No staked tokens to claim rewards");

        // Calculate user's reward debt
        uint256 rewardDebt = getRewardDebt(msg.sender);

        // Calculate reward amount
        uint256 rewardAmount = rewardDebt.sub(userRewardDebt[msg.sender]);

        // Update user's reward debt
        userRewardDebt[msg.sender] = rewardDebt;

        // Transfer rewards to user
        token.transfer(msg.sender, rewardAmount);

        // Emit rewards distributed event
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Update reward per second function
     * @param _newRewardPerSecond New reward per second
     */
    function updateRewardPerSecond(uint256 _newRewardPerSecond) external onlyOwner {
        rewardPerSecond = _newRewardPerSecond;
    }

    /**
     * @dev Update staking duration function
     * @param _newStakingDuration New staking duration
     */
    function updateStakingDuration(uint256 _newStakingDuration) external onlyOwner {
        stakingDuration = _newStakingDuration;
    }

    /**
     * @dev Withdraw tokens function
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        token.transfer(msg.sender, _amount);
    }
}
```
