"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-reward.web.app
Prompt: Create a Solidity contract that supports staking rewards for multiple meme coins, with a mechanism to incentivize holding a specific token like $STARS.
Generated: DETERMINISTIC_8c1ebe0345dbfefc
Batch ID: 20250612_154133
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

contract MemeCoinStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct StakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    struct PoolInfo {
        IERC20 stakingToken;
        IERC20 rewardToken;
        uint256 rewardPerBlock;
        uint256 lastRewardBlock;
        uint256 accRewardPerShare;
        uint256 totalStaked;
        uint256 bonusMultiplier; // Multiplier for STARS holders
    }

    // The STARS token address
    IERC20 public immutable starsToken;

    // Minimum STARS balance required for bonus
    uint256 public minStarsForBonus;

    // Info of each pool
    PoolInfo[] public poolInfo;

    // Info of each user that stakes tokens
    mapping(uint256 => mapping(address => StakingInfo)) public stakingInfo;

    // Bonus multiplier for STARS holders (e.g., 150 = 1.5x)
    uint256 public starsBonusMultiplier;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event PoolAdded(uint256 indexed pid, address stakingToken, address rewardToken, uint256 rewardPerBlock);
    event RewardUpdated(uint256 indexed pid, uint256 rewardPerBlock);

    constructor(
        IERC20 _starsToken,
        uint256 _minStarsForBonus,
        uint256 _starsBonusMultiplier
    ) {
        require(address(_starsToken) != address(0), "Invalid STARS token");
        starsToken = _starsToken;
        minStarsForBonus = _minStarsForBonus;
        starsBonusMultiplier = _starsBonusMultiplier;
    }

    function poolLength() external view returns (uint256) {
        return poolInfo.length;
    }

    // Add a new staking pool
    function addPool(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _bonusMultiplier,
        bool _withUpdate
    ) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }

        uint256 lastRewardBlock = block.number;
        poolInfo.push(
            PoolInfo({
                stakingToken: _stakingToken,
                rewardToken: _rewardToken,
                rewardPerBlock: _rewardPerBlock,
                lastRewardBlock: lastRewardBlock,
                accRewardPerShare: 0,
                totalStaked: 0,
                bonusMultiplier: _bonusMultiplier
            })
        );

        emit PoolAdded(poolInfo.length - 1, address(_stakingToken), address(_rewardToken), _rewardPerBlock);
    }

    // Update the given pool's reward per block
    function setRewardPerBlock(uint256 _pid, uint256 _rewardPerBlock, bool _withUpdate) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        poolInfo[_pid].rewardPerBlock = _rewardPerBlock;
        emit RewardUpdated(_pid, _rewardPerBlock);
    }

    // Update bonus multiplier for STARS holders
    function setStarsBonusMultiplier(uint256 _multiplier) external onlyOwner {
        require(_multiplier >= 100, "Multiplier must be >= 100 (1x)");
        starsBonusMultiplier = _multiplier;
    }

    // Update minimum STARS balance for bonus
    function setMinStarsForBonus(uint256 _minStars) external onlyOwner {
        minStarsForBonus = _minStars;
    }

    // Return reward multiplier over the given _from to _to block.
    function getMultiplier(uint256 _from, uint256 _to) public pure returns (uint256) {
        return _to - _from;
    }

    // View function to see pending rewards on frontend.
    function pendingReward(uint256 _pid, address _user) external view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        StakingInfo storage user = stakingInfo[_pid][_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        uint256 totalStaked = pool.totalStaked;

        if (block.number > pool.lastRewardBlock && totalStaked != 0) {
            uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
            uint256 reward = multiplier * pool.rewardPerBlock;
            accRewardPerShare += (reward * 1e12) / totalStaked;
        }

        uint256 pending = (user.stakedAmount * accRewardPerShare) / 1e12 - user.rewardDebt;
        
        // Apply bonus if user holds STARS
        if (starsToken.balanceOf(_user) >= minStarsForBonus) {
            pending = (pending * starsBonusMultiplier) / 100;
        }

        return pending;
    }

    // Update reward variables for all pools
    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    // Update reward variables of the given pool to be up-to-date.
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        uint256 totalStaked = pool.totalStaked;
        if (totalStaked == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
        uint256 reward = multiplier * pool.rewardPerBlock;
        pool.accRewardPerShare += (reward * 1e12) / totalStaked;
        pool.lastRewardBlock = block.number;
    }

    // Stake tokens to earn rewards
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        StakingInfo storage user = stakingInfo[_pid][msg.sender];

        updatePool(_pid);

        if (user.stakedAmount > 0) {
            uint256 pending = (user.stakedAmount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            
            // Apply bonus if user holds STARS
            if (starsToken.balanceOf(msg.sender) >= minStarsForBonus) {
                pending = (pending * starsBonusMultiplier) / 100;
            }

            if (pending > 0) {
                safeRewardTransfer(pool.rewardToken, msg.sender, pending);
            }
        }

        if (_amount > 0) {
            pool.stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.stakedAmount += _amount;
            pool.totalStaked += _amount;
        }

        user.rewardDebt = (user.stakedAmount * pool.accRewardPerShare) / 1e12;
        user.lastStakedTime = block.timestamp;
        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw staked tokens and collect rewards
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        StakingInfo storage user = stakingInfo[_pid][msg.sender];
        require(user.stakedAmount >= _amount, "Withdraw amount exceeds balance");

        updatePool(_pid);

        uint256 pending = (user.stakedAmount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        
        // Apply bonus if user holds STARS
        if (starsToken.balanceOf(msg.sender) >= minStarsForBonus) {
            pending = (pending * starsBonusMultiplier) / 100;
        }

        if (pending > 0) {
            safeRewardTransfer(pool.rewardToken, msg.sender, pending);
        }

        if (_amount > 0) {
            user.stakedAmount -= _amount;
            pool.totalStaked -= _amount;
            pool.stakingToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.stakedAmount * pool.accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw(uint256 _pid) external nonReentrant {
        PoolInfo
