"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Write a smart contract in Solidity for staking $BTCBULL tokens on Ethereum, incorporating dynamic APY adjustments as described on the BTC Bull website.
Generated: DETERMINISTIC_92d37afb884f7c75
Batch ID: 20250612_154757
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

/**
 * @title BTC Bull Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $BTCBULL tokens and earn rewards with dynamic APY adjustments.
 */
contract BTCBullStaking is Ownable {
    using SafeMath for uint256;

    // Token contract instance
    IERC20 public token;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking amount
    uint256 public totalStaked;

    // Dynamic APY parameters
    uint256 public apyAdjustmentInterval; // Time interval for APY adjustments (in seconds)
    uint256 public apyAdjustmentFactor; // Factor for APY adjustments (in basis points)
    uint256 public currentApy; // Current APY (in basis points)

    // Reward token instance
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Reward accumulator
    uint256 public accRewardPerShare;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token $BTCBULL token contract address
     * @param _rewardToken Reward token contract address
     * @param _apyAdjustmentInterval Time interval for APY adjustments (in seconds)
     * @param _apyAdjustmentFactor Factor for APY adjustments (in basis points)
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _apyAdjustmentInterval,
        uint256 _apyAdjustmentFactor,
        uint256 _rewardPerBlock
    ) public {
        token = IERC20(_token);
        rewardToken = IERC20(_rewardToken);
        apyAdjustmentInterval = _apyAdjustmentInterval;
        apyAdjustmentFactor = _apyAdjustmentFactor;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake $BTCBULL tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Update reward debt
        updateRewardDebt(msg.sender);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $BTCBULL tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens to user
        token.transfer(msg.sender, _amount);

        // Update reward debt
        updateRewardDebt(msg.sender);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimReward() external {
        // Update reward debt
        updateRewardDebt(msg.sender);

        // Calculate reward
        uint256 reward = rewardDebt[msg.sender].sub(stakingBalances[msg.sender]).mul(accRewardPerShare).div(1e18);

        // Reset reward debt
        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        // Transfer reward to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Update reward debt
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Update APY
        updateApy();

        // Calculate reward accumulator
        uint256 reward = rewardPerBlock.mul(block.number.sub(lastRewardBlock));
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));

        // Update last reward block
        lastRewardBlock = block.number;

        // Update reward debt
        if (stakingBalances[_user] > 0) {
            rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);
        }
    }

    /**
     * @notice Update APY
     */
    function updateApy() internal {
        // Adjust APY periodically
        if (block.timestamp.sub(lastRewardBlock).div(apyAdjustmentInterval) > 0) {
            currentApy = currentApy.add(apyAdjustmentFactor);
            lastRewardBlock = block.timestamp;
        }
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Update APY adjustment factor
     * @param _newApyAdjustmentFactor New APY adjustment factor (in basis points)
     */
    function updateApyAdjustmentFactor(uint256 _newApyAdjustmentFactor) external onlyOwner {
        apyAdjustmentFactor = _newApyAdjustmentFactor;
    }
}
```
