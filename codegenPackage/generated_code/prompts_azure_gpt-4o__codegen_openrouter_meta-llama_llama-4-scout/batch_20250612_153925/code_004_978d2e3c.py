"""
Generated Code Metadata:
========================
Original URL: https://et-erfi-v2.com
Prompt: Create a Solidity function that tracks staking rewards and updates the value of a liquid staking token (eETH) in real-time, inspired by EtherFi’s architecture.
Generated: DETERMINISTIC_978d2e3c44409428
Batch ID: 20250612_153925
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

/**
 * @title Liquid Staking Token (eETH) Rewards Tracker
 * @author [Your Name]
 * @notice Tracks staking rewards and updates the value of eETH in real-time.
 */
contract eETHRewardsTracker {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // eETH token contract
    IERC20 public eETH;

    // Staking reward token contract
    IERC20 public rewardToken;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are updated
    event RewardsUpdated(uint256 accRewardPerShare);

    /**
     * @param _eETH eETH token contract address
     * @param _rewardToken Staking reward token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _eETH,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) public {
        eETH = IERC20(_eETH);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Updates the accumulated reward per share
     */
    function updateRewards() internal {
        uint256 totalStaking = totalStakingBalance;
        if (totalStaking == 0) return;

        uint256 reward = rewardToken.balanceOf(address(this));
        accRewardPerShare = accRewardPerShare.add(
            reward.div(totalStaking)
        );
        emit RewardsUpdated(accRewardPerShare);
    }

    /**
     * @dev Stake eETH tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Update user's reward debt
        uint256 _rewardDebt = rewardDebt[msg.sender];
        uint256 _newRewardDebt = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
        rewardDebt[msg.sender] = _newRewardDebt;

        // Transfer eETH tokens to staking contract
        eETH.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake eETH tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Update user's reward debt
        uint256 _rewardDebt = rewardDebt[msg.sender];
        uint256 _newRewardDebt = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
        rewardDebt[msg.sender] = _newRewardDebt;

        // Transfer eETH tokens to user
        eETH.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() external {
        uint256 _rewardDebt = rewardDebt[msg.sender];
        uint256 _newRewardDebt = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
        uint256 _reward = _newRewardDebt.sub(_rewardDebt);

        // Update user's reward debt
        rewardDebt[msg.sender] = _newRewardDebt;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, _reward);
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external {
        require(msg.sender == owner(), "Only owner can update reward per block");
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @dev Get user's staking balance and reward debt
     * @param _user User address
     * @return staking balance and reward debt
     */
    function getUserInfo(address _user) external view returns (uint256, uint256) {
        return (stakingBalances[_user], rewardDebt[_user]);
    }
}
```
