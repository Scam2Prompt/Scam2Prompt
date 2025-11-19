"""
Generated Code Metadata:
========================
Original URL: https://dapp-d.pages.dev
Prompt: "Create a library recommendation for DApp developers to handle staking and harvesting of assets on the blockchain."
Generated: DETERMINISTIC_271e6513be2ea9ce
Batch ID: 20250622_204615
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
 * @title StakingRewards
 * @dev A contract for staking tokens and earning rewards
 */
contract StakingRewards is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
    }

    // The staking token
    IERC20 public stakingToken;
    // The reward token
    IERC20 public rewardToken;
    // Reward tokens per block
    uint256 public rewardPerBlock;
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Total tokens staked
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Harvest(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardPerBlockUpdated(uint256 oldReward, uint256 newReward);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward tokens per block
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
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

        uint256 multiplier = block.number - lastRewardBlock;
        uint256 reward = multiplier * rewardPerBlock;
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param _amount Amount of tokens to stake
     */
    function deposit(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit Harvest(msg.sender, pending);
            }
        }

        if (_amount > 0) {
            stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            totalStaked += _amount;
            emit Deposit(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
    }

    /**
     * @dev Withdraw staked tokens and harvest rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw: amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit Harvest(msg.sender, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            totalStaked -= _amount;
            stakingToken.safeTransfer(msg.sender, _amount);
            emit Withdraw(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
    }

    /**
     * @dev Harvest rewards without withdrawing staked tokens
     */
    function harvest() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "Harvest: no rewards to claim");

        safeRewardTransfer(msg.sender, pending);
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        emit Harvest(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw staked tokens without harvesting rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "EmergencyWithdraw: no tokens staked");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
     * @param _to Address to transfer rewards to
     * @param _amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Update reward per block
     * @param _rewardPerBlock New reward per block value
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        uint256 oldReward = rewardPerBlock;
        rewardPerBlock = _rewardPerBlock;
        emit RewardPerBlockUpdated(oldReward, _rewardPerBlock);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param _user Address of user
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 multiplier = block.number - lastRewardBlock;
            uint256 reward = multiplier * rewardPerBlock;
            tempAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * tempAccRewardPerShare) / 1e12 - user.rewardDebt;
    }
}
```
