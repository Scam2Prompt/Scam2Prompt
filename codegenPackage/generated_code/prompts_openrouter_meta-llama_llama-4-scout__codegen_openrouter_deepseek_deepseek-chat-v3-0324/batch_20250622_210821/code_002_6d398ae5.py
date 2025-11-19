"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: "Generate a smart contract code for a liquidity mining-based bond with no Impermanent Loss for LP Farming, similar to iZiSwap's Farm iUSD."
Generated: DETERMINISTIC_6d398ae5a5897f94
Batch ID: 20250622_210821
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

contract LiquidityMiningBond is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user information
    struct UserInfo {
        uint256 amount;     // How many LP tokens the user has provided
        uint256 rewardDebt; // Reward debt (see explanation below)
        uint256 lastClaim;  // Last claim timestamp
    }

    // Struct to store pool information
    struct PoolInfo {
        IERC20 lpToken;           // Address of LP token contract
        uint256 allocPoint;       // Allocation points assigned to this pool
        uint256 lastRewardBlock;  // Last block number that rewards distribution occurred
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e12
        uint256 totalDeposited;    // Total LP tokens deposited
    }

    // The reward token
    IERC20 public rewardToken;
    
    // Reward tokens created per block
    uint256 public rewardPerBlock;
    
    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint = 0;
    
    // The block number when mining starts
    uint256 public startBlock;
    
    // The block number when mining ends
    uint256 public endBlock;
    
    // Info of each pool
    PoolInfo[] public poolInfo;
    
    // Info of each user that stakes LP tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    
    // Events
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint, address lpToken);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint);

    constructor(
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_rewardPerBlock > 0, "Invalid reward per block");
        require(_startBlock >= block.number, "Start block must be in future");
        require(_endBlock > _startBlock, "End block must be after start block");

        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    // Add a new LP pool
    function addPool(uint256 _allocPoint, IERC20 _lpToken) external onlyOwner {
        require(block.number < endBlock, "Mining has ended");
        require(address(_lpToken) != address(0), "Invalid LP token");

        massUpdatePools();
        
        uint256 lastRewardBlock = block.number > startBlock ? block.number : startBlock;
        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                lpToken: _lpToken,
                allocPoint: _allocPoint,
                lastRewardBlock: lastRewardBlock,
                accRewardPerShare: 0,
                totalDeposited: 0
            })
        );

        emit PoolAdded(poolInfo.length - 1, _allocPoint, address(_lpToken));
    }

    // Update the given pool's allocation point
    function setPool(uint256 _pid, uint256 _allocPoint) external onlyOwner {
        require(_pid < poolInfo.length, "Invalid pool ID");
        
        massUpdatePools();
        
        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;
        
        emit PoolUpdated(_pid, _allocPoint);
    }

    // Update reward variables for all pools
    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    // Update reward variables of the given pool to be up-to-date
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }
        
        if (pool.totalDeposited == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }
        
        uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
        if (multiplier == 0) return;
        
        uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;
        
        pool.accRewardPerShare += (reward * 1e12) / pool.totalDeposited;
        pool.lastRewardBlock = block.number;
    }

    // Get multiplier for reward calculation
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        if (_to <= startBlock || _from >= endBlock) {
            return 0;
        }
        if (_to > endBlock) {
            _to = endBlock;
        }
        if (_from < startBlock) {
            _from = startBlock;
        }
        return _to - _from;
    }

    // Deposit LP tokens to earn rewards
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool ID");
        require(_amount > 0, "Amount must be greater than zero");
        
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        updatePool(_pid);
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        pool.lpToken.safeTransferFrom(address(msg.sender), address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        user.lastClaim = block.timestamp;
        pool.totalDeposited += _amount;
        
        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw LP tokens and harvest rewards
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool ID");
        require(_amount > 0, "Amount must be greater than zero");
        
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        
        updatePool(_pid);
        
        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        pool.totalDeposited -= _amount;
        
        pool.lpToken.safeTransfer(address(msg.sender), _amount);
        
        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Withdraw without caring about rewards. EMERGENCY ONLY.
    function emergencyWithdraw(uint256 _pid) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool ID");
        
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        pool.totalDeposited -= amount;
        
        pool.lpToken.safeTransfer(address(msg.sender), amount);
        
        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken
