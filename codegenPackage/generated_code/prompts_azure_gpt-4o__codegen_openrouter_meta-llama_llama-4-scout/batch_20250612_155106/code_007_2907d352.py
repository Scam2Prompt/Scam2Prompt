"""
Generated Code Metadata:
========================
Original URL: https://kodiak-finance.org
Prompt: Write a Solidity smart contract that incorporates security protocols similar to Kodiak Finance's approach to protecting investors’ assets during yield farming activities.
Generated: DETERMINISTIC_2907d3521a3b6135
Batch ID: 20250612_155106
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Kodiak Finance Yield Farming Contract
 * @author [Your Name]
 * @notice This contract provides a secure yield farming platform for investors,
 *          incorporating security protocols similar to Kodiak Finance's approach.
 */
contract KodiakYieldFarming is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user deposits and rewards
    mapping (address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping (uint256 => PoolInfo) public poolInfo;

    // ERC20 token contract
    IERC20 public token;

    // Total allocated amount
    uint256 public totalAllocated;

    // Number of pools
    uint256 public poolLength;

    // Event emitted when user deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user withdraws
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when rewards are distributed
    event DistributeRewards(address indexed user, uint256 indexed pid, uint256 amount);

    /**
     * @dev User information structure
     */
    struct UserInfo {
        uint256 amount; // Deposit amount
        uint256 rewardDebt; // Reward debt
    }

    /**
     * @dev Pool information structure
     */
    struct PoolInfo {
        IERC20 lpToken; // LP token contract
        uint256 allocPoint; // Allocation points
        uint256 lastRewardTime; // Last reward time
        uint256 accTokenPerShare; // Accumulated token per share
    }

    /**
     * @dev Constructor
     * @param _token ERC20 token contract
     */
    constructor(IERC20 _token) public {
        token = _token;
        totalAllocated = 0;
        poolLength = 0;
    }

    /**
     * @dev Add a new pool
     * @param _allocPoint Allocation points
     * @param _lpToken LP token contract
     */
    function addPool(uint256 _allocPoint, IERC20 _lpToken) public onlyOwner {
        require(address(_lpToken) != address(0), "Invalid LP token");

        poolLength++;
        poolInfo[poolLength - 1] = PoolInfo({
            lpToken: _lpToken,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0
        });

        totalAllocated = totalAllocated.add(_allocPoint);
    }

    /**
     * @dev Deposit LP tokens into a pool
     * @param _pid Pool ID
     * @param _amount Deposit amount
     */
    function deposit(uint256 _pid, uint256 _amount) public nonReentrant {
        require(_pid < poolLength, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Transfer LP tokens to the contract
        pool.lpToken.transferFrom(msg.sender, address(this), _amount);

        // Update user deposit and reward debt
        if (user.amount > 0) {
            uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e18) - user.rewardDebt;
            if (pending > 0) {
                token.transfer(msg.sender, pending);
            }
        }

        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e18);

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @dev Withdraw LP tokens from a pool
     * @param _pid Pool ID
     * @param _amount Withdrawal amount
     */
    function withdraw(uint256 _pid, uint256 _amount) public nonReentrant {
        require(_pid < poolLength, "Invalid pool ID");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient deposit");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Update user reward debt
        uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e18) - user.rewardDebt;
        if (pending > 0) {
            token.transfer(msg.sender, pending);
        }

        // Transfer LP tokens back to the user
        pool.lpToken.transfer(msg.sender, _amount);

        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e18);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @dev Update pool allocation points
     * @param _pid Pool ID
     * @param _allocPoint New allocation points
     */
    function updatePool(uint256 _pid, uint256 _allocPoint) public onlyOwner {
        require(_pid < poolLength, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];

        // Update total allocated amount
        totalAllocated = totalAllocated.sub(pool.allocPoint).add(_allocPoint);

        pool.allocPoint = _allocPoint;
    }

    /**
     * @dev Distribute rewards to users
     * @param _pid Pool ID
     */
    function distributeRewards(uint256 _pid) public {
        require(_pid < poolLength, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];

        // Update pool last reward time and accumulated token per share
        uint256 currentTime = block.timestamp;
        uint256 secondsSinceLastReward = currentTime.sub(pool.lastRewardTime);
        if (secondsSinceLastReward > 0) {
            uint256 tokenReward = secondsSinceLastReward.mul(pool.allocPoint).mul(token.balanceOf(address(this))).div(totalAllocated).div(1e18);
            pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e18).div(userInfo[msg.sender].amount));
            pool.lastRewardTime = currentTime;

            emit DistributeRewards(msg.sender, _pid, tokenReward);
        }
    }
}
```
