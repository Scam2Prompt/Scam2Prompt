"""
Generated Code Metadata:
========================
Original URL: https://aarrto.pages.dev
Prompt: Develop a smart contract to distribute AERO emissions to liquidity providers on Aerodrome Finance. Ensure the contract supports anti-dilution rebases for voters.
Generated: DETERMINISTIC_5af885ae01b4875b
Batch ID: 20250612_150927
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title AERO Emissions Distributor
 * @notice Distributes AERO tokens to liquidity providers with anti-dilution rebases for voters
 * @dev This contract handles the distribution of emissions while accounting for rebases
 */
contract AeroEmissionsDistributor is Ownable, ReentrancyGuard {
    IERC20 public immutable aeroToken;
    uint256 public totalEmission;
    uint256 public emissionRate;
    uint256 public lastDistributionTime;
    uint256 public constant DISTRIBUTION_INTERVAL = 1 weeks;

    // Track rebase factors for anti-dilution
    uint256 public rebaseFactor = 1e18;
    uint256 public lastRebaseTime;

    // Pool information
    struct PoolInfo {
        uint256 allocPoint; // Allocation points for the pool
        uint256 lastRebasedTime; // Last time the pool was rebased
        uint256 accAeroPerShare; // Accumulated AERO per share
        uint256 totalShares; // Total shares in the pool
    }

    // User information
    struct UserInfo {
        uint256 amount; // How many LP tokens the user has provided
        uint256 rewardDebt; // Reward debt for anti-dilution
        uint256 pendingRewards; // Pending rewards to claim
    }

    // Pool ID to PoolInfo mapping
    mapping(uint256 => PoolInfo) public poolInfo;
    // User address => Pool ID => UserInfo
    mapping(address => mapping(uint256 => UserInfo)) public userInfo;

    // Total allocation points. Must be the sum of all allocation points in all pools.
    uint256 public totalAllocPoint;

    event EmissionRateUpdated(uint256 newEmissionRate);
    event Rebased(uint256 newRebaseFactor);
    event Deposited(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdrawn(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint);

    /**
     * @param _aeroToken Address of the AERO token
     * @param _emissionRate Initial emission rate per second
     */
    constructor(address _aeroToken, uint256 _emissionRate) {
        require(_aeroToken != address(0), "Invalid AERO token address");
        aeroToken = IERC20(_aeroToken);
        emissionRate = _emissionRate;
        lastDistributionTime = block.timestamp;
        lastRebaseTime = block.timestamp;
    }

    /**
     * @notice Update emission rate
     * @param _emissionRate New emission rate per second
     */
    function updateEmissionRate(uint256 _emissionRate) external onlyOwner {
        massUpdatePools();
        emissionRate = _emissionRate;
        emit EmissionRateUpdated(_emissionRate);
    }

    /**
     * @notice Add a new pool
     * @param _allocPoint Allocation points for the pool
     */
    function addPool(uint256 _allocPoint) external onlyOwner {
        totalAllocPoint += _allocPoint;
        uint256 pid = getPoolCount();
        poolInfo[pid] = PoolInfo({
            allocPoint: _allocPoint,
            lastRebasedTime: block.timestamp,
            accAeroPerShare: 0,
            totalShares: 0
        });
        emit PoolAdded(pid, _allocPoint);
    }

    /**
     * @notice Update pool allocation points
     * @param _pid Pool ID to update
     * @param _allocPoint New allocation points
     */
    function setPool(uint256 _pid, uint256 _allocPoint) external onlyOwner {
        require(_pid < getPoolCount(), "Invalid pool ID");
        massUpdatePools();
        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;
        emit PoolUpdated(_pid, _allocPoint);
    }

    /**
     * @notice Get number of pools
     * @return Number of pools
     */
    function getPoolCount() public view returns (uint256) {
        // This implementation assumes pools are added sequentially starting from 0
        // In production, you might want to track this differently
        uint256 count = 0;
        while (poolInfo[count].allocPoint != 0 || count == 0) {
            count++;
        }
        return count;
    }

    /**
     * @notice Perform rebase to account for anti-dilution
     * @param _newRebaseFactor New rebase factor (1e18 based)
     */
    function rebase(uint256 _newRebaseFactor) external onlyOwner {
        require(_newRebaseFactor > 0, "Invalid rebase factor");
        massUpdatePools();
        rebaseFactor = _newRebaseFactor;
        lastRebaseTime = block.timestamp;
        emit Rebased(_newRebaseFactor);
    }

    /**
     * @notice Update all pools to account for emissions up to current block
     */
    function massUpdatePools() public {
        uint256 length = getPoolCount();
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    /**
     * @notice Update a specific pool to account for emissions
     * @param _pid Pool ID to update
     */
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.timestamp <= pool.lastRebasedTime) {
            return;
        }

        if (pool.totalShares == 0) {
            pool.lastRebasedTime = block.timestamp;
            return;
        }

        uint256 aeroReward = calculateEmission(_pid);
        if (aeroReward > 0) {
            totalEmission += aeroReward;
            pool.accAeroPerShare += (aeroReward * 1e18) / pool.totalShares;
        }
        pool.lastRebasedTime = block.timestamp;
    }

    /**
     * @notice Calculate emission for a pool since last update
     * @param _pid Pool ID
     * @return aeroReward Amount of AERO to distribute
     */
    function calculateEmission(uint256 _pid) internal view returns (uint256 aeroReward) {
        PoolInfo memory pool = poolInfo[_pid];
        uint256 timeElapsed = block.timestamp - pool.lastRebasedTime;
        uint256 totalEmissionForPeriod = timeElapsed * emissionRate;
        
        if (totalAllocPoint > 0) {
            aeroReward = (totalEmissionForPeriod * pool.allocPoint) / totalAllocPoint;
        }
    }

    /**
     * @notice Deposit LP tokens to earn AERO rewards
     * @param _pid Pool ID
     * @param _amount Amount of LP tokens to deposit
     */
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < getPoolCount(), "Invalid pool ID");
        require(_amount > 0, "Amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];

        updatePool(_pid);

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accAeroPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }

        if (_amount > 0) {
            // In production, you would transfer LP tokens from user to this contract
            // IERC20 lpToken = IERC20(pool.lpToken);
            // lpToken.transferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            pool.totalShares += _amount;
        }

        user.rewardDebt = (user.amount * pool.accAeroPerShare) / 1e18;
        emit Deposited(msg.sender, _pid, _amount);
    }

    /**
     * @notice Withdraw LP tokens and claim rewards
     * @param _pid Pool ID
     * @param _amount Amount of LP tokens to withdraw
     */
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < getPoolCount(), "Invalid pool ID");
        require(_amount > 0, "Amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender][_pid];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool(_pid);

        uint256 pending = (
