"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Develop a smart contract that supports staking rewards for multiple meme coins while prioritizing $STARS holders, modeled after the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8ced0b5668554bbe
Batch ID: 20250612_153722
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
 * @title MemeVault
 * @dev A smart contract for staking multiple meme coins with prioritized rewards for $STARS holders
 */
contract MemeVault is Ownable, ReentrancyGuard {
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    struct PoolInfo {
        IERC20 token;
        uint256 allocPoint;
        uint256 lastRewardBlock;
        uint256 accRewardPerShare;
        uint256 totalStaked;
    }

    // The reward token (STARS)
    IERC20 public rewardToken;

    // Reward tokens created per block
    uint256 public rewardPerBlock;

    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint;

    // Info of each pool
    PoolInfo[] public poolInfo;

    // Info of each staker that stakes tokens
    mapping(uint256 => mapping(address => Staker)) public stakers;

    // Mapping to track if token is already added
    mapping(address => bool) public poolExists;

    // STARS holders get multiplier on rewards
    uint256 public starsMultiplier = 2;
    uint256 public constant MULTIPLIER_DECIMALS = 100;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PoolAdded(uint256 indexed pid, address indexed token, uint256 allocPoint);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint);

    /**
     * @dev Constructor
     * @param _rewardToken Address of the reward token (STARS)
     * @param _rewardPerBlock Reward tokens distributed per block
     */
    constructor(IERC20 _rewardToken, uint256 _rewardPerBlock) {
        require(address(_rewardToken) != address(0), "Invalid reward token");
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Add a new meme coin pool
     * @param _token The token to be staked in the pool
     * @param _allocPoint Allocation points assigned to the pool
     */
    function addPool(IERC20 _token, uint256 _allocPoint) external onlyOwner {
        require(address(_token) != address(0), "Invalid token");
        require(!poolExists[address(_token)], "Pool already exists");

        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                token: _token,
                allocPoint: _allocPoint,
                lastRewardBlock: block.number,
                accRewardPerShare: 0,
                totalStaked: 0
            })
        );
        poolExists[address(_token)] = true;

        emit PoolAdded(poolInfo.length - 1, address(_token), _allocPoint);
    }

    /**
     * @dev Update the given pool's allocation point
     * @param _pid The pool id
     * @param _allocPoint New allocation points
     */
    function setPool(uint256 _pid, uint256 _allocPoint) external onlyOwner {
        require(_pid < poolInfo.length, "Invalid pool id");

        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;

        emit PoolUpdated(_pid, _allocPoint);
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
     * @param _pid The pool id
     */
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        if (pool.totalStaked == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = block.number - pool.lastRewardBlock;
        uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;

        pool.accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        pool.lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param _pid The pool id
     * @param _amount Amount of tokens to stake
     */
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool id");
        require(_amount > 0, "Amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        Staker storage staker = stakers[_pid][msg.sender];

        updatePool(_pid);

        if (staker.amount > 0) {
            uint256 pending = (staker.amount * pool.accRewardPerShare) / 1e12 - staker.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
            }
        }

        pool.token.transferFrom(msg.sender, address(this), _amount);
        staker.amount += _amount;
        staker.rewardDebt = (staker.amount * pool.accRewardPerShare) / 1e12;
        staker.lastStakedTime = block.timestamp;
        pool.totalStaked += _amount;

        emit Deposit(msg.sender, _pid, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _pid The pool id
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool id");
        require(_amount > 0, "Amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        Staker storage staker = stakers[_pid][msg.sender];
        require(staker.amount >= _amount, "Insufficient balance");

        updatePool(_pid);

        uint256 pending = (staker.amount * pool.accRewardPerShare) / 1e12 - staker.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
        }

        staker.amount -= _amount;
        staker.rewardDebt = (staker.amount * pool.accRewardPerShare) / 1e12;
        pool.totalStaked -= _amount;

        pool.token.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _pid, _amount);
    }

    /**
     * @dev Claim pending rewards
     * @param _pid The pool id
     */
    function claimReward(uint256 _pid) external nonReentrant {
        require(_pid < poolInfo.length, "Invalid pool id");

        PoolInfo storage pool = poolInfo[_pid];
        Staker storage staker = stakers[_pid][msg.sender];

        updatePool(_pid);

        uint256 pending = (staker.amount * pool.accRewardPerShare) / 1e12 - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = (staker.amount * pool.accRewardPerShare) / 1e12;

        // Apply multiplier for STARS holders
        if (address(pool.token) == address(rewardToken)) {
            pending = (pending * starsMultiplier * MULTIPLIER_DECIMALS) / 100;
        }

        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe reward transfer function
     * @param _to The recipient address
     * @param _amount Amount to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (_amount > balance) {
            rewardToken.transfer(_to, balance);
        } else {
            rewardToken.transfer(_to, _amount);
        }
    }

    /**
     * @dev Set the reward per block
     * @param _rewardPerBlock New reward per block value
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        massUpdatePools();
        rewardPerBlock = _reward
