"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements the staking mechanism for $POODL tokens, ensuring it distributes rewards at the specified rate per Ethereum block.
Generated: DETERMINISTIC_b7d31b7d58239734
Batch ID: 20250612_161353
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

/**
 * @title PoodlStakingContract
 * @author [Your Name]
 * @notice A staking contract for $POODL tokens that distributes rewards at a specified rate per Ethereum block.
 */
contract PoodlStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // POODL token contract
    IERC20 public poodlToken;

    // Reward token contract (same as POODL for simplicity)
    IERC20 public rewardToken;

    // Total POODL tokens staked
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Last block number when rewards were distributed
    uint256 public lastRewardBlock;

    // Info for each user that stakes POODL tokens
    struct UserInfo {
        uint256 amount; // How many POODL tokens the user has staked
        uint256 rewardDebt; // Reward debt
    }

    /**
     * @notice Constructor
     * @param _poodlToken POODL token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardRate Reward rate per block
     */
    constructor(
        address _poodlToken,
        address _rewardToken,
        uint256 _rewardRate
    ) public {
        poodlToken = IERC20(_poodlToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake POODL tokens
     * @param _amount Amount of POODL tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            _updateReward(msg.sender);
        }

        poodlToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake POODL tokens
     * @param _amount Amount of POODL tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient staked amount");

        UserInfo storage user = userInfo[msg.sender];
        _updateReward(msg.sender);

        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        poodlToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Update reward for a user
     * @param _user User address
     */
    function _updateReward(address _user) internal {
        UserInfo storage user = userInfo[_user];
        uint256 pendingReward = _getPendingReward(_user);
        if (pendingReward > 0) {
            rewardToken.safeTransfer(_user, pendingReward);
        }
        user.rewardDebt = accRewardPerShare;
    }

    /**
     * @notice Get pending reward for a user
     * @param _user User address
     * @return Pending reward
     */
    function _getPendingReward(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 userRewardDebt = user.rewardDebt;
        uint256 currentAccRewardPerShare = accRewardPerShare;
        uint256 stakedAmount = user.amount;

        if (block.number > lastRewardBlock && totalStaked > 0) {
            uint256 reward = _getReward(lastRewardBlock, block.number);
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));
            currentAccRewardPerShare = accRewardPerShare;
        }

        return stakedAmount.mul(currentAccRewardPerShare.sub(userRewardDebt)).div(1e18);
    }

    /**
     * @notice Get reward from last block to current block
     * @param _fromBlock From block
     * @param _toBlock To block
     * @return Reward
     */
    function _getReward(uint256 _fromBlock, uint256 _toBlock) internal view returns (uint256) {
        return _toBlock.sub(_fromBlock).mul(rewardRate);
    }

    /**
     * @notice Update reward variables
     */
    function _updateRewardVariables() internal {
        if (block.number > lastRewardBlock && totalStaked > 0) {
            uint256 reward = _getReward(lastRewardBlock, block.number);
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));
            lastRewardBlock = block.number;
        }
    }

    /**
     * @notice Get user info
     * @param _user User address
     * @return User info
     */
    function getUserInfo(address _user) external view returns (uint256, uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount, _getPendingReward(_user));
    }
}
```
