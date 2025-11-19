"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: Write a Solidity contract that integrates the SOPH token for staking rewards, following the guidelines provided in the Sophon documentation.
Generated: DETERMINISTIC_6da3afe67190c088
Batch ID: 20250612_152658
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

/**
 * @title SophonStaking
 * @dev A contract for staking SOPH tokens and earning rewards
 */
contract SophonStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // The SOPH token contract
    IERC20 public immutable sophToken;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
    }

    // Reward rate per block
    uint256 public rewardPerBlock;

    // Last block number where rewards were calculated
    uint256 public lastRewardBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Total tokens staked
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _sophToken Address of the SOPH token contract
     * @param _rewardPerBlock Initial reward rate per block
     */
    constructor(address _sophToken, uint256 _rewardPerBlock) {
        require(_sophToken != address(0), "Invalid token address");
        sophToken = IERC20(_sophToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update reward variables to be up-to-date
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardPerBlock;
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Deposit SOPH tokens to contract for staking
     * @param _amount Amount of tokens to stake
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeSophTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        sophToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        totalStaked += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeSophTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        totalStaked -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        sophToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeSophTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe transfer function for rewards
     * @param _to Address to transfer to
     * @param _amount Amount to transfer
     */
    function safeSophTransfer(address _to, uint256 _amount) internal {
        uint256 sophBalance = sophToken.balanceOf(address(this));
        if (_amount > sophBalance) {
            sophToken.safeTransfer(_to, sophBalance);
        } else {
            sophToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Update reward rate per block (only owner)
     * @param _rewardPerBlock New reward rate
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev View function to see pending rewards
     * @param _user Address of user
     * @return Pending rewards for given user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardPerBlock;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    /**
     * @dev Emergency withdraw without claiming rewards (only for emergencies)
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        sophToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }
}
```
