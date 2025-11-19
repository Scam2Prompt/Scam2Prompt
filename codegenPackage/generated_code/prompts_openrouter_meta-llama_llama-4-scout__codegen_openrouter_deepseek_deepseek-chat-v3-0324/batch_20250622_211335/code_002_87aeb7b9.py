"""
Generated Code Metadata:
========================
Original URL: https://app-sunswap.github.io
Prompt: Generate a smart contract code in Solidity for a sustainable yield farming platform on Tron, inspired by SunSwap's tokenomics and community governance model.
Generated: DETERMINISTIC_87aeb7b92f965e58
Batch ID: 20250622_211335
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
 * @title SustainableYieldFarm
 * @dev A sustainable yield farming platform with community governance inspired by SunSwap
 */
contract SustainableYieldFarm is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent user stake information
    struct UserInfo {
        uint256 amount;     // How many LP tokens the user has provided
        uint256 rewardDebt; // Reward debt for yield calculation
        uint256 lastHarvest; // Timestamp of last harvest
    }

    // Struct to represent pool information
    struct PoolInfo {
        IERC20 lpToken;     // Address of LP token contract
        uint256 allocPoint; // Allocation points assigned to this pool
        uint256 lastRewardBlock; // Last block number where rewards were distributed
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e12
        uint16 depositFeeBP; // Deposit fee in basis points
        uint256 harvestInterval; // Minimum time between harvests in seconds
    }

    // The reward token
    IERC20 public rewardToken;
    // Reward tokens created per block
    uint256 public rewardPerBlock;
    // Max deposit fee: 10%
    uint16 public constant MAX_DEPOSIT_FEE = 1000;
    // Max harvest interval: 1 week
    uint256 public constant MAX_HARVEST_INTERVAL = 7 days;

    // Info of each pool
    PoolInfo[] public poolInfo;
    // Info of each user that stakes LP tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint = 0;
    // The block number when farming starts
    uint256 public startBlock;
    // Total locked rewards
    uint256 public totalLockedRewards;

    // Events
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event Harvest(address indexed user, uint256 indexed pid, uint256 amount);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint, IERC20 lpToken, uint16 depositFeeBP, uint256 harvestInterval);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint, uint16 depositFeeBP, uint256 harvestInterval);
    event RewardPerBlockUpdated(uint256 oldRewardPerBlock, uint256 newRewardPerBlock);
    event SetFeeAddress(address indexed feeAddress);

    // Fee address
    address public feeAddress;

    constructor(
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        address _feeAddress
    ) {
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_feeAddress != address(0), "Invalid fee address");

        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        feeAddress = _feeAddress;
    }

    /**
     * @dev Add a new LP pool
     */
    function add(
        uint256 _allocPoint,
        IERC20 _lpToken,
        uint16 _depositFeeBP,
        uint256 _harvestInterval,
        bool _withUpdate
    ) external onlyOwner {
        require(_depositFeeBP <= MAX_DEPOSIT_FEE, "Invalid deposit fee");
        require(_harvestInterval <= MAX_HARVEST_INTERVAL, "Invalid harvest interval");
        if (_withUpdate) {
            massUpdatePools();
        }
        uint256 lastRewardBlock = block.number > startBlock ? block.number : startBlock;
        totalAllocPoint = totalAllocPoint + _allocPoint;
        poolInfo.push(
            PoolInfo({
                lpToken: _lpToken,
                allocPoint: _allocPoint,
                lastRewardBlock: lastRewardBlock,
                accRewardPerShare: 0,
                depositFeeBP: _depositFeeBP,
                harvestInterval: _harvestInterval
            })
        );
        emit PoolAdded(poolInfo.length - 1, _allocPoint, _lpToken, _depositFeeBP, _harvestInterval);
    }

    /**
     * @dev Update the given pool's parameters
     */
    function set(
        uint256 _pid,
        uint256 _allocPoint,
        uint16 _depositFeeBP,
        uint256 _harvestInterval,
        bool _withUpdate
    ) external onlyOwner {
        require(_depositFeeBP <= MAX_DEPOSIT_FEE, "Invalid deposit fee");
        require(_harvestInterval <= MAX_HARVEST_INTERVAL, "Invalid harvest interval");
        if (_withUpdate) {
            massUpdatePools();
        }
        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;
        poolInfo[_pid].depositFeeBP = _depositFeeBP;
        poolInfo[_pid].harvestInterval = _harvestInterval;
        emit PoolUpdated(_pid, _allocPoint, _depositFeeBP, _harvestInterval);
    }

    /**
     * @dev Update reward per block
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        massUpdatePools();
        emit RewardPerBlockUpdated(rewardPerBlock, _rewardPerBlock);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Update fee address
     */
    function setFeeAddress(address _feeAddress) external {
        require(msg.sender == feeAddress, "setFeeAddress: FORBIDDEN");
        require(_feeAddress != address(0), "Invalid fee address");
        feeAddress = _feeAddress;
        emit SetFeeAddress(_feeAddress);
    }

    /**
     * @dev Return number of pools
     */
    function poolLength() external view returns (uint256) {
        return poolInfo.length;
    }

    /**
     * @dev View function to see pending rewards on frontend
     */
    function pendingReward(uint256 _pid, address _user) external view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        uint256 lpSupply = pool.lpToken.balanceOf(address(this));
        if (block.number > pool.lastRewardBlock && lpSupply != 0) {
            uint256 multiplier = block.number - pool.lastRewardBlock;
            uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;
            accRewardPerShare = accRewardPerShare + (reward * 1e12) / lpSupply;
        }
        return (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
    }

    /**
     * @dev Update reward variables for all pools
     */
    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    /**
     * @dev Update reward variables of the given pool
     */
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }
        uint256 lpSupply = pool.lpToken.balanceOf(address(this));
        if (lpSupply == 0 || pool.allocPoint == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }
        uint256 multiplier = block.number - pool.lastRewardBlock;
        uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;
        totalLockedRewards += reward;
        pool.accRewardPerShare = pool.accRewardPerShare + (reward * 1e12) / lpSupply;
        pool.lastRewardBlock = block.number;
    }

    /**
     * @dev Deposit LP tokens to farm for rewards
     */
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        updatePool(_pid);
        if (user.amount > 0) {
            _harvest(_pid);
        }
        if (_amount > 0) {
            uint256 before = pool.lpToken
