"""
Generated Code Metadata:
========================
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a smart contract in Solidity for staking tokens and distributing rewards, following the Param Network's tokenomics structure.
Generated: DETERMINISTIC_18afe55627ed4d62
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract for staking tokens and distributing rewards.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Token being staked
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Reward accumulator
    uint256 public accRewardPerShare;

    // Staking pool information
    struct UserInfo {
        uint256 amount; // Staked amount
        uint256 rewardDebt; // Reward debt
    }

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Staking: Invalid amount");

        UserInfo storage user = userInfo[msg.sender];

        // Transfer staking tokens from user
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staked amount
        if (user.amount > 0) {
            _updateReward(msg.sender);
        }

        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstaking: Invalid amount");
        require(userInfo[msg.sender].amount >= _amount, "Unstaking: Insufficient staked amount");

        UserInfo storage user = userInfo[msg.sender];

        // Update user's reward debt
        _updateReward(msg.sender);

        // Subtract staked amount
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount);

        totalStaked = totalStaked.sub(_amount);

        // Transfer staking tokens back to user
        stakingToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Update reward for a user
     * @param _user User address
     */
    function _updateReward(address _user) internal {
        UserInfo storage user = userInfo[_user];

        // Calculate accumulated reward
        uint256 pendingReward = _getPendingReward(_user);

        // Update user's reward debt
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e18);

        // Add pending reward to user's balance
        if (pendingReward > 0) {
            rewardToken.safeTransfer(_user, pendingReward);
        }
    }

    /**
     * @notice Get pending reward for a user
     * @param _user User address
     * @return Pending reward amount
     */
    function _getPendingReward(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];

        // Calculate accumulated reward per share
        uint256 currentAccRewardPerShare = accRewardPerShare.add(
            _getRewardAmount().mul(1e18).div(totalStaked)
        );

        // Calculate pending reward
        uint256 pendingReward = user.amount.mul(currentAccRewardPerShare).div(1e18).sub(user.rewardDebt);

        return pendingReward;
    }

    /**
     * @notice Get reward amount from last reward block to current block
     * @return Reward amount
     */
    function _getRewardAmount() internal view returns (uint256) {
        return rewardPerBlock.mul(block.number.sub(lastRewardBlock));
    }

    /**
     * @notice Update reward variables
     */
    function _updateRewardVariables() internal {
        // Update accumulated reward per share
        if (totalStaked > 0) {
            accRewardPerShare = accRewardPerShare.add(
                _getRewardAmount().mul(1e18).div(totalStaked)
            );
        }

        // Update last reward block
        lastRewardBlock = block.number;
    }

    /**
     * @notice Mass update reward variables for all users
     */
    function massUpdateRewards() public {
        _updateRewardVariables();
    }

    /**
     * @notice Update reward for a user and caller
     */
    function updateReward() public {
        _updateReward(msg.sender);
        _updateRewardVariables();
    }

    /**
     * @notice Get user information
     * @param _user User address
     * @return Staked amount, reward debt
     */
    function getUserInfo(address _user) public view returns (uint256, uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount, user.rewardDebt);
    }

    /**
     * @notice Get contract information
     * @return Total staked, reward per block, last reward block
     */
    function getContractInfo() public view returns (uint256, uint256, uint256) {
        return (totalStaked, rewardPerBlock, lastRewardBlock);
    }
}
```
