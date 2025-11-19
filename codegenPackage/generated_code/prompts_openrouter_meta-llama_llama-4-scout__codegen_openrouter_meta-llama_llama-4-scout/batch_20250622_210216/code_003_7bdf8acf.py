"""
Generated Code Metadata:
========================
Original URL: https://hydrofinance-dapp.pages.dev
Prompt: Design a smart contract for a Farming feature that allows users to stake their hINJ LSTs and earn superior yields, using a platform like Injective Network.
Generated: DETERMINISTIC_7bdf8acfc13a56b8
Batch ID: 20250622_210216
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
 * @title Farming Contract
 * @author [Your Name]
 * @notice This contract allows users to stake their hINJ LSTs and earn superior yields.
 */
contract FarmingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping(address => PoolInfo) public poolInfo;

    // Event emitted when a user stakes tokens
    event Stake(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstake(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event ClaimRewards(address indexed user, uint256 amount);

    // Struct to store user information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Struct to store pool information
    struct PoolInfo {
        IERC20 token; // Token contract
        uint256 allocPoint; // Allocation point
        uint256 lastRewardTime; // Last reward time
        uint256 accTokenPerShare; // Accumulated token per share
    }

    // Token contract
    IERC20 public hINJ;

    // Reward token contract
    IERC20 public rewardToken;

    // Total allocation points
    uint256 public totalAllocPoint;

    // Reward per second
    uint256 public rewardPerSecond;

    // Minimum lock-up time
    uint256 public minLockupTime;

    /**
     * @notice Constructor
     * @param _hINJ hINJ token contract
     * @param _rewardToken Reward token contract
     * @param _rewardPerSecond Reward per second
     * @param _minLockupTime Minimum lock-up time
     */
    constructor(
        IERC20 _hINJ,
        IERC20 _rewardToken,
        uint256 _rewardPerSecond,
        uint256 _minLockupTime
    ) public {
        hINJ = _hINJ;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
        minLockupTime = _minLockupTime;
    }

    /**
     * @notice Add a new pool
     * @param _token Token contract
     * @param _allocPoint Allocation point
     */
    function addPool(IERC20 _token, uint256 _allocPoint) public onlyOwner {
        require(address(_token) != address(0), "FarmingContract: token address cannot be 0");

        totalAllocPoint = totalAllocPoint.add(_allocPoint);

        poolInfo[address(_token)] = PoolInfo({
            token: _token,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0
        });
    }

    /**
     * @notice Update a pool
     * @param _token Token contract
     * @param _allocPoint Allocation point
     */
    function updatePool(IERC20 _token, uint256 _allocPoint) public onlyOwner {
        require(address(_token) != address(0), "FarmingContract: token address cannot be 0");

        totalAllocPoint = totalAllocPoint.sub(poolInfo[address(_token)].allocPoint).add(_allocPoint);

        poolInfo[address(_token)].allocPoint = _allocPoint;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "FarmingContract: stake amount must be greater than 0");

        hINJ.safeTransferFrom(msg.sender, address(this), _amount);

        UserInfo storage user = userInfo[msg.sender];

        if (user.amount > 0) {
            uint256 pending = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12) - user.rewardDebt;
            if (pending > 0) {
                rewardToken.safeTransfer(msg.sender, pending);
            }
        }

        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12);

        emit Stake(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "FarmingContract: unstake amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "FarmingContract: unstake amount exceeds staked amount");

        UserInfo storage user = userInfo[msg.sender];

        uint256 pending = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12) - user.rewardDebt;
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
        }

        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12);

        hINJ.safeTransfer(msg.sender, _amount);

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        UserInfo storage user = userInfo[msg.sender];

        uint256 pending = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12) - user.rewardDebt;
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
            user.rewardDebt = user.amount.mul(poolInfo[address(hINJ)].accTokenPerShare).div(1e12);

            emit ClaimRewards(msg.sender, pending);
        }
    }

    /**
     * @notice Update reward per second
     * @param _rewardPerSecond Reward per second
     */
    function updateRewardPerSecond(uint256 _rewardPerSecond) public onlyOwner {
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Mass update pools
     */
    function massUpdatePools() public {
        uint256 length = 1; // Assuming only one pool for simplicity
        for (uint256 i = 0; i < length; i++) {
            updatePool(address(hINJ));
        }
    }

    /**
     * @notice Update pool
     * @param _token Token contract
     */
    function updatePool(address _token) public {
        PoolInfo storage pool = poolInfo[_token];

        uint256 lpSupply = pool.token.balanceOf(address(this));

        if (lpSupply == 0) {
            return;
        }

        uint256 multiplier = getMultiplier(pool.lastRewardTime, block.timestamp);

        uint256 tokenReward = multiplier.mul(rewardPerSecond).mul(pool.allocPoint).div(totalAllocPoint);

        pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e12).div(lpSupply));

        pool.lastRewardTime = block.timestamp;
    }

    /**
     * @notice Get multiplier
     * @param _from Start time
     * @param _to End time
     * @return Multiplier
     */
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        return _to.sub(_from);
    }
}
```
