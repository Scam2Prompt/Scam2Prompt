"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-qdclhqzos-miketoken.vercel.app
Prompt: Generate code for creating a staking pool smart contract on the BNBChain, inspired by Mike Token's farming launch roadmap.
Generated: DETERMINISTIC_cf5bf9841bb443b9
Batch ID: 20250612_154432
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
 * @title StakingPool
 * @dev A smart contract for staking ERC20 tokens and earning rewards
 */
contract StakingPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Info of each user
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt (see explanation below)
        uint256 pendingRewards; // Pending rewards to be claimed
    }

    // Info of the pool
    struct PoolInfo {
        IERC20 stakingToken;   // Address of staking token contract
        IERC20 rewardToken;    // Address of reward token contract
        uint256 rewardPerBlock; // Reward tokens per block
        uint256 lastRewardBlock; // Last block number that rewards distribution occurs
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e12
        uint256 totalStaked;   // Total tokens staked in the pool
    }

    PoolInfo public poolInfo;
    mapping(address => UserInfo) public userInfo;

    uint256 public startBlock;
    uint256 public endBlock;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event PoolUpdated(uint256 lastRewardBlock, uint256 totalStaked, uint256 accRewardPerShare);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward tokens per block
     * @param _startBlock Start block for rewards
     * @param _endBlock End block for rewards
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        require(address(_stakingToken) != address(0), "Staking token cannot be zero address");
        require(address(_rewardToken) != address(0), "Reward token cannot be zero address");
        require(_startBlock >= block.number, "Start block must be in future");
        require(_endBlock > _startBlock, "End block must be after start block");

        poolInfo = PoolInfo({
            stakingToken: _stakingToken,
            rewardToken: _rewardToken,
            rewardPerBlock: _rewardPerBlock,
            lastRewardBlock: _startBlock,
            accRewardPerShare: 0,
            totalStaked: 0
        });

        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @dev Update reward variables of the pool
     */
    function updatePool() public {
        PoolInfo storage pool = poolInfo;
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        if (pool.totalStaked == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
        uint256 reward = multiplier * pool.rewardPerBlock;
        pool.accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        pool.lastRewardBlock = block.number;

        emit PoolUpdated(pool.lastRewardBlock, pool.totalStaked, pool.accRewardPerShare);
    }

    /**
     * @dev Get multiplier for reward calculation
     * @param _from Starting block
     * @param _to Ending block
     * @return Multiplier value
     */
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        if (_to <= endBlock) {
            return _to - _from;
        } else if (_from >= endBlock) {
            return 0;
        } else {
            return endBlock - _from;
        }
    }

    /**
     * @dev Deposit staking tokens to earn rewards
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(block.number >= startBlock, "Staking not started yet");
        require(block.number <= endBlock, "Staking period ended");

        PoolInfo storage pool = poolInfo;
        UserInfo storage user = userInfo[msg.sender];

        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }

        pool.stakingToken.safeTransferFrom(address(msg.sender), address(this), _amount);
        user.amount += _amount;
        pool.totalStaked += _amount;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        PoolInfo storage pool = poolInfo;
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }

        user.amount -= _amount;
        pool.totalStaked -= _amount;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;

        pool.stakingToken.safeTransfer(address(msg.sender), _amount);

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claim() external nonReentrant {
        PoolInfo storage pool = poolInfo;
        UserInfo storage user = userInfo[msg.sender];

        updatePool();

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }

        uint256 amountToClaim = user.pendingRewards;
        require(amountToClaim > 0, "No rewards to claim");

        user.pendingRewards = 0;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;

        safeRewardTransfer(msg.sender, amountToClaim);

        emit Claim(msg.sender, amountToClaim);
    }

    /**
     * @dev Emergency withdraw without caring about rewards
     */
    function emergencyWithdraw() external nonReentrant {
        PoolInfo storage pool = poolInfo;
        UserInfo storage user = userInfo[msg.sender];

        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        pool.totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        user.pendingRewards = 0;

        pool.stakingToken.safeTransfer(address(msg.sender), amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
     * @param _to Address to transfer rewards to
     * @param _amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        PoolInfo storage pool = poolInfo;
        uint256 rewardBalance = pool.rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            pool.rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            pool.rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Update reward per block
     * @param _rewardPerBlock New reward per block value
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        require(block.number < startBlock, "Staking has already started");
        poolInfo.rewardPerBlock = _rewardPerBlock
