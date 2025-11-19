"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Create a smart contract that mimics Extra Finance's security-focused design, emphasizing audits and robust mechanisms to protect user assets during yield farming.
Generated: DETERMINISTIC_c8a7c45bdf7df197
Batch ID: 20250612_153923
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SecureYieldFarm
 * @dev A security-focused yield farming contract with audit protections and asset safeguards
 */
contract SecureYieldFarm is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to store user information
    struct UserInfo {
        uint256 amount;         // How many LP tokens the user has provided
        uint256 rewardDebt;     // Reward debt (see explanation below)
        uint256 lastDepositTime; // Timestamp of last deposit
    }

    // Struct to store pool information
    struct PoolInfo {
        IERC20 lpToken;         // Address of LP token contract
        uint256 allocPoint;     // Allocation points assigned to this pool
        uint256 lastRewardBlock; // Last block number that rewards distribution occurred
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e12
        uint256 depositFeeBP;   // Deposit fee in basis points
        uint256 lockPeriod;     // Minimum lock period in seconds
        uint256 totalDeposits;  // Total deposits in the pool
    }

    // The reward token
    IERC20 public rewardToken;

    // Reward tokens created per block
    uint256 public rewardPerBlock;

    // Info of each pool
    PoolInfo[] public poolInfo;

    // Info of each user that stakes LP tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;

    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint = 0;

    // The block number when reward mining starts
    uint256 public startBlock;

    // The block number when reward mining ends
    uint256 public endBlock;

    // Maximum deposit fee: 5%
    uint16 public constant MAX_DEPOSIT_FEE = 500;

    // Address where deposit fees are sent
    address public feeAddress;

    // Emergency pause switch
    bool public paused = false;

    // Events
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event SetFeeAddress(address indexed user, address indexed newAddress);
    event SetStartAndEndBlocks(uint256 startBlock, uint256 endBlock);
    event PoolAdded(uint256 allocPoint, IERC20 lpToken, uint256 depositFeeBP, uint256 lockPeriod);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint, uint256 depositFeeBP, uint256 lockPeriod);
    event RewardPerBlockUpdated(uint256 oldRewardPerBlock, uint256 newRewardPerBlock);
    event Paused(address account);
    event Unpaused(address account);

    /**
     * @dev Modifier to check if the contract is not paused
     */
    modifier notPaused() {
        require(!paused, "Contract is paused");
        _;
    }

    /**
     * @dev Constructor
     * @param _rewardToken The reward token address
     * @param _rewardPerBlock Reward tokens created per block
     * @param _startBlock The block number when reward mining starts
     * @param _endBlock The block number when reward mining ends
     * @param _feeAddress Address where deposit fees are sent
     */
    constructor(
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock,
        address _feeAddress
    ) {
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_feeAddress != address(0), "Invalid fee address");
        require(_startBlock > block.number, "Start block must be in future");
        require(_endBlock > _startBlock, "End block must be after start block");

        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
        feeAddress = _feeAddress;
    }

    /**
     * @dev Get number of pools
     */
    function poolLength() external view returns (uint256) {
        return poolInfo.length;
    }

    /**
     * @dev Add a new pool
     * @param _allocPoint Allocation points assigned to this pool
     * @param _lpToken Address of LP token contract
     * @param _depositFeeBP Deposit fee in basis points
     * @param _lockPeriod Minimum lock period in seconds
     * @param _withUpdate Whether to update all pools
     */
    function add(
        uint256 _allocPoint,
        IERC20 _lpToken,
        uint256 _depositFeeBP,
        uint256 _lockPeriod,
        bool _withUpdate
    ) external onlyOwner {
        require(address(_lpToken) != address(0), "Invalid LP token");
        require(_depositFeeBP <= MAX_DEPOSIT_FEE, "Deposit fee too high");

        if (_withUpdate) {
            massUpdatePools();
        }

        uint256 lastRewardBlock = block.number > startBlock ? block.number : startBlock;
        totalAllocPoint = totalAllocPoint.add(_allocPoint);
        poolInfo.push(
            PoolInfo({
                lpToken: _lpToken,
                allocPoint: _allocPoint,
                lastRewardBlock: lastRewardBlock,
                accRewardPerShare: 0,
                depositFeeBP: _depositFeeBP,
                lockPeriod: _lockPeriod,
                totalDeposits: 0
            })
        );

        emit PoolAdded(_allocPoint, _lpToken, _depositFeeBP, _lockPeriod);
    }

    /**
     * @dev Update the given pool's parameters
     * @param _pid Pool ID
     * @param _allocPoint Allocation points assigned to this pool
     * @param _depositFeeBP Deposit fee in basis points
     * @param _lockPeriod Minimum lock period in seconds
     * @param _withUpdate Whether to update all pools
     */
    function set(
        uint256 _pid,
        uint256 _allocPoint,
        uint256 _depositFeeBP,
        uint256 _lockPeriod,
        bool _withUpdate
    ) external onlyOwner {
        require(_pid < poolInfo.length, "Invalid pool ID");
        require(_depositFeeBP <= MAX_DEPOSIT_FEE, "Deposit fee too high");

        if (_withUpdate) {
            massUpdatePools();
        }

        totalAllocPoint = totalAllocPoint.sub(poolInfo[_pid].allocPoint).add(_allocPoint);
        poolInfo[_pid].allocPoint = _allocPoint;
        poolInfo[_pid].depositFeeBP = _depositFeeBP;
        poolInfo[_pid].lockPeriod = _lockPeriod;

        emit PoolUpdated(_pid, _allocPoint, _depositFeeBP, _lockPeriod);
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
     * @param _pid Pool ID
     */
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        uint256 lpSupply = pool.totalDeposits;
        if (lpSupply == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
        uint256 reward = multiplier.mul(rewardPerBlock).mul(pool.allocPoint).div(totalAllocPoint);
        
        // Ensure we don't distribute more rewards than allocated
        uint256 remainingRewards = rewardToken.balanceOf(address(this));
        if (reward > remainingRewards) {
            reward = remainingRewards;
        }

        pool.accRewardPerShare = pool.accRewardPerShare.add(reward.mul(1e12).div(lpSupply));
        pool.lastRewardBlock = block.number;
    }

    /**
     * @dev Calculate reward multiplier over the given _from to _to block
     * @param _from From block number
     * @param _to To block number
     */
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        if (_to <= endBlock) {
