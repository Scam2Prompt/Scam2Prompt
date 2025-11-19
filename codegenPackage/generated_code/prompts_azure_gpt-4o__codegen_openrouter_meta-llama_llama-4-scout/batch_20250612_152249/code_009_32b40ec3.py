"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a Solidity contract to support Zushi farming, allowing users to deposit $ZUSHI tokens and earn rewards based on the staking pool allocation.
Generated: DETERMINISTIC_32b40ec347f27506
Batch ID: 20250612_152249
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
 * @title ZushiFarmingContract
 * @author [Your Name]
 * @notice A contract to support Zushi farming, allowing users to deposit $ZUSHI tokens and earn rewards.
 */
contract ZushiFarmingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user deposit and reward information
    mapping(address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping(uint256 => PoolInfo) public poolInfo;

    // Total allocation points
    uint256 public totalAllocationPoints;

    // ZUSHI token contract
    IERC20 public zushiToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Event emitted when a user deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user withdraws
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when a user harvests rewards
    event Harvest(address indexed user, uint256 indexed pid, uint256 amount);

    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Deposit amount
        uint256 rewardDebt; // Reward debt
    }

    // Struct to store pool information
    struct PoolInfo {
        uint256 allocationPoints; // Allocation points
        uint256 lastRewardTime; // Last reward time
        uint256 accRewardPerShare; // Accumulated reward per share
    }

    /**
     * @notice Constructor
     * @param _zushiToken ZUSHI token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _zushiToken, address _rewardToken) public {
        zushiToken = IERC20(_zushiToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @notice Add a new pool
     * @param _allocationPoints Allocation points
     */
    function addPool(uint256 _allocationPoints) public onlyOwner {
        require(_allocationPoints > 0, "Allocation points must be greater than 0");

        totalAllocationPoints = totalAllocationPoints.add(_allocationPoints);
        poolInfo[uint256(0)] = PoolInfo({
            allocationPoints: _allocationPoints,
            lastRewardTime: block.timestamp,
            accRewardPerShare: 0
        });
    }

    /**
     * @notice Deposit $ZUSHI tokens into a pool
     * @param _pid Pool ID
     * @param _amount Deposit amount
     */
    function deposit(uint256 _pid, uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updateReward(msg.sender, _pid);

        // Deposit
        user.amount = user.amount.add(_amount);
        zushiToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @notice Withdraw $ZUSHI tokens from a pool
     * @param _pid Pool ID
     * @param _amount Withdrawal amount
     */
    function withdraw(uint256 _pid, uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient deposit");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updateReward(msg.sender, _pid);

        // Withdrawal
        user.amount = user.amount.sub(_amount);
        zushiToken.safeTransfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @notice Harvest rewards from a pool
     * @param _pid Pool ID
     */
    function harvest(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update reward
        updateReward(msg.sender, _pid);

        // Harvest
        uint256 reward = user.rewardDebt;
        if (reward > 0) {
            user.rewardDebt = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit Harvest(msg.sender, _pid, reward);
        }
    }

    /**
     * @notice Update reward for a user
     * @param _user User address
     * @param _pid Pool ID
     */
    function updateReward(address _user, uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_user];

        // Calculate accumulated reward per share
        uint256 accRewardPerShare = pool.accRewardPerShare;
        uint256 reward = rewardToken.balanceOf(address(this));
        if (block.timestamp > pool.lastRewardTime && pool.allocationPoints > 0) {
            uint256 totalAllocPoint = totalAllocationPoints;
            uint256 timeElapsed = block.timestamp.sub(pool.lastRewardTime);
            accRewardPerShare = accRewardPerShare.add(
                reward.mul(1e12).mul(pool.allocationPoints).div(totalAllocPoint).div(timeElapsed)
            );
            pool.accRewardPerShare = accRewardPerShare;
            pool.lastRewardTime = block.timestamp;
        }

        // Update user's reward debt
        if (user.amount > 0) {
            user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        }
    }

    /**
     * @notice Update reward for multiple users
     * @param _users User addresses
     * @param _pid Pool ID
     */
    function updateRewards(address[] memory _users, uint256 _pid) public {
        for (uint256 i = 0; i < _users.length; i++) {
            updateReward(_users[i], _pid);
        }
    }
}
```
