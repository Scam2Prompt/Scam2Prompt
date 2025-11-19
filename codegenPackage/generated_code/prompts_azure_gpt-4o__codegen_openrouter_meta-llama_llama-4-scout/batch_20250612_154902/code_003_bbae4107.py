"""
Generated Code Metadata:
========================
Original URL: https://thenafl.org
Prompt: Write a smart contract in Solidity that mimics the liquidity optimization model (ve3,3) used by THENA FI for a decentralized exchange on the BNB Chain.
Generated: DETERMINISTIC_bbae41079c7532b8
Batch ID: 20250612_154902
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

contract Ve3_3_LP_Optimizer is Ownable {
    using SafeMath for uint256;

    // Struct to hold user information
    struct UserInfo {
        uint256 amount; // User deposited amount
        uint256 rewardDebt; // User reward debt
    }

    // Struct to hold pool information
    struct PoolInfo {
        IERC20 lpToken; // LP token contract
        uint256 allocPoint; // Allocation points
        uint256 lastRewardTime; // Last reward time
        uint256 accTokenPerShare; // Accumulated token per share
    }

    // Token reward contract
    IERC20 public rewardToken;

    // Total allocation points
    uint256 public totalAllocPoint;

    // Pool info array
    PoolInfo[] public poolInfo;

    // User info mapping
    mapping(address => mapping(uint256 => UserInfo)) public userInfo;

    // Event emitted when user deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user withdraws
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when emergency withdraws
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when pool is added
    event AddPool(uint256 indexed pid, IERC20 lpToken, uint256 allocPoint);

    // Event emitted when pool is set
    event SetPool(uint256 indexed pid, uint256 allocPoint);

    // Constructor
    constructor(IERC20 _rewardToken) public {
        rewardToken = _rewardToken;
    }

    // Add a new LP to the pool
    function addPool(uint256 _allocPoint, IERC20 _lpToken) public onlyOwner {
        require(address(_lpToken) != address(0), "LP token cannot be zero");
        require(_allocPoint > 0, "Allocation points must be greater than 0");

        totalAllocPoint = totalAllocPoint.add(_allocPoint);
        poolInfo.push(PoolInfo({
            lpToken: _lpToken,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0
        }));

        emit AddPool(poolInfo.length - 1, _lpToken, _allocPoint);
    }

    // Update the allocation points of a pool
    function setPool(uint256 _pid, uint256 _allocPoint) public onlyOwner {
        require(_allocPoint >= 0, "Allocation points must be greater than or equal to 0");

        PoolInfo storage pool = poolInfo[_pid];
        uint256 prevAllocPoint = pool.allocPoint;
        pool.allocPoint = _allocPoint;

        if (prevAllocPoint != _allocPoint) {
            totalAllocPoint = totalAllocPoint.sub(prevAllocPoint).add(_allocPoint);
        }

        emit SetPool(_pid, _allocPoint);
    }

    // Deposit LP tokens to the pool
    function deposit(uint256 _pid, uint256 _amount) public {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        // Update pool
        updatePool(_pid);

        // Transfer LP tokens to the pool
        pool.lpToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount.mul(pool.accTokenPerShare).div(1e12));

        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw LP tokens from the pool
    function withdraw(uint256 _pid, uint256 _amount) public {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        require(user.amount >= _amount, "Not enough LP tokens");

        // Update pool
        updatePool(_pid);

        // Update user info
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount.mul(pool.accTokenPerShare).div(1e12));

        // Transfer LP tokens back to user
        pool.lpToken.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Emergency withdraw LP tokens from the pool
    function emergencyWithdraw(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;

        // Transfer LP tokens back to user
        pool.lpToken.transfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    // Update pool
    function updatePool(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];

        uint256 currentTime = block.timestamp;
        uint256 timeElapsed = currentTime.sub(pool.lastRewardTime);

        if (timeElapsed > 0 && pool.allocPoint != 0) {
            uint256 tokenReward = timeElapsed.mul(rewardToken.balanceOf(address(this))).mul(pool.allocPoint).div(totalAllocPoint);

            // Update accumulated token per share
            pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e12).div(pool.lpToken.balanceOf(address(this))));

            // Update last reward time
            pool.lastRewardTime = currentTime;
        }
    }

    // Update user reward debt
    function updateUserRewardDebt(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);
    }

    // Mass update pools
    function massUpdatePools() public {
        for (uint256 i = 0; i < poolInfo.length; i++) {
            updatePool(i);
        }
    }

    // Get user's pending rewards
    function getPendingReward(uint256 _pid) public view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        uint256 accTokenPerShare = pool.accTokenPerShare;
        uint256 lpSupply = pool.lpToken.balanceOf(address(this));

        if (block.timestamp > pool.lastRewardTime && lpSupply != 0) {
            uint256 timeElapsed = block.timestamp.sub(pool.lastRewardTime);
            uint256 tokenReward = timeElapsed.mul(rewardToken.balanceOf(address(this))).mul(pool.allocPoint).div(totalAllocPoint);

            accTokenPerShare = accTokenPerShare.add(tokenReward.mul(1e12).div(lpSupply));
        }

        return user.amount.mul(accTokenPerShare).div(1e12).sub(user.rewardDebt);
    }
}
```
