"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Write a smart contract for a yield farming pool on Arbitrum blockchain with AI-powered insights for optimizing investments.
Generated: DETERMINISTIC_5d7ef11d6d2fcab1
Batch ID: 20250622_205751
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// YieldFarm contract for managing a yield farming pool
contract YieldFarm is Ownable {
    using SafeMath for uint256;

    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Struct to hold pool information
    struct PoolInfo {
        IERC20 token;           // Address of the token contract
        uint256 allocPoint;     // Allocation points for this pool
        uint256 lastRewardBlock; // Last block number that rewards were distributed
        uint256 accTokenPerShare; // Accumulated tokens per share
    }

    // State variables
    PoolInfo[] public poolInfo; // Array of pool information
    mapping(uint256 => mapping(address => UserInfo)) public userInfo; // User info mapping
    uint256 public totalAllocPoint = 0; // Total allocation points
    uint256 public tokenPerBlock; // Tokens distributed per block

    // Event for logging deposits
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    // Event for logging withdrawals
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    // Event for logging rewards
    event Harvest(address indexed user, uint256 indexed pid, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _tokenPerBlock) {
        tokenPerBlock = _tokenPerBlock;
    }

    // Function to add a new pool
    function addPool(uint256 _allocPoint, IERC20 _token) external onlyOwner {
        totalAllocPoint = totalAllocPoint.add(_allocPoint);
        poolInfo.push(PoolInfo({
            token: _token,
            allocPoint: _allocPoint,
            lastRewardBlock: block.number,
            accTokenPerShare: 0
        }));
    }

    // Function to update the allocation points of a pool
    function setPool(uint256 _pid, uint256 _allocPoint) external onlyOwner {
        totalAllocPoint = totalAllocPoint.sub(poolInfo[_pid].allocPoint).add(_allocPoint);
        poolInfo[_pid].allocPoint = _allocPoint;
    }

    // Function to deposit tokens into the pool
    function deposit(uint256 _pid, uint256 _amount) external {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        // Update pool rewards
        updatePool(_pid);

        // Transfer tokens from user to the pool
        if (_amount > 0) {
            pool.token.transferFrom(msg.sender, address(this), _amount);
            user.amount = user.amount.add(_amount);
        }

        // Update user's reward debt
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);

        emit Deposit(msg.sender, _pid, _amount);
    }

    // Function to withdraw tokens from the pool
    function withdraw(uint256 _pid, uint256 _amount) external {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        require(user.amount >= _amount, "Withdraw: not enough balance");

        // Update pool rewards
        updatePool(_pid);

        // Transfer tokens back to the user
        if (_amount > 0) {
            user.amount = user.amount.sub(_amount);
            pool.token.transfer(msg.sender, _amount);
        }

        // Update user's reward debt
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Function to harvest rewards
    function harvest(uint256 _pid) external {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        // Update pool rewards
        updatePool(_pid);

        // Calculate pending rewards
        uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e12).sub(user.rewardDebt);

        // Transfer rewards to the user
        if (pending > 0) {
            // Assuming the contract has enough tokens to pay out
            pool.token.transfer(msg.sender, pending);
            emit Harvest(msg.sender, _pid, pending);
        }

        // Update user's reward debt
        user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);
    }

    // Function to update the pool rewards
    function updatePool(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];

        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        uint256 multiplier = block.number.sub(pool.lastRewardBlock);
        uint256 tokenReward = multiplier.mul(tokenPerBlock).mul(pool.allocPoint).div(totalAllocPoint);

        // Update accumulated tokens per share
        if (totalAllocPoint > 0) {
            pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e12).div(totalAllocPoint));
        }

        pool.lastRewardBlock = block.number;
    }

    // Function to set the token per block
    function setTokenPerBlock(uint256 _tokenPerBlock) external onlyOwner {
        tokenPerBlock = _tokenPerBlock;
    }
}
```
