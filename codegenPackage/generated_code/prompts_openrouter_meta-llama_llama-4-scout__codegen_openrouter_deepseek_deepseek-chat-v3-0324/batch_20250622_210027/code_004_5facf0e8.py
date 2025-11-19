"""
Generated Code Metadata:
========================
Original URL: https://dao-mdex.pages.dev
Prompt: Design a smart contract for a decentralized exchange (DEX) with governance rights, inspired by the MDEX model, and including features like token liquidity mining and whitelist applications.
Generated: DETERMINISTIC_5facf0e8285f9145
Batch ID: 20250622_210027
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IMdexPair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract DEXGovernance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Governance token
    IERC20 public governanceToken;

    // Whitelist mapping
    mapping(address => bool) public whitelist;

    // Liquidity mining parameters
    struct PoolInfo {
        IERC20 lpToken;             // Address of LP token contract
        uint256 allocPoint;         // Allocation points assigned to this pool
        uint256 lastRewardBlock;    // Last block number that rewards distribution occurred
        uint256 accRewardPerShare;  // Accumulated rewards per share, times 1e18
    }

    struct UserInfo {
        uint256 amount;             // How many LP tokens the user has provided
        uint256 rewardDebt;         // Reward debt
    }

    PoolInfo[] public poolInfo;
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    uint256 public totalAllocPoint = 0;
    uint256 public rewardPerBlock;
    uint256 public startBlock;

    // Events
    event WhitelistUpdated(address indexed account, bool isWhitelisted);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint, IERC20 lpToken);
    event PoolAllocUpdated(uint256 indexed pid, uint256 allocPoint);
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 indexed pid, uint256 amount);

    constructor(
        IERC20 _governanceToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock
    ) {
        governanceToken = _governanceToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
    }

    // Governance functions
    function updateWhitelist(address _account, bool _isWhitelisted) external onlyOwner {
        whitelist[_account] = _isWhitelisted;
        emit WhitelistUpdated(_account, _isWhitelisted);
    }

    // Liquidity mining functions
    function addPool(uint256 _allocPoint, IERC20 _lpToken, bool _withUpdate) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        uint256 lastRewardBlock = block.number > startBlock ? block.number : startBlock;
        totalAllocPoint = totalAllocPoint.add(_allocPoint);
        poolInfo.push(PoolInfo({
            lpToken: _lpToken,
            allocPoint: _allocPoint,
            lastRewardBlock: lastRewardBlock,
            accRewardPerShare: 0
        }));
        emit PoolAdded(poolInfo.length - 1, _allocPoint, _lpToken);
    }

    function setPoolAlloc(uint256 _pid, uint256 _allocPoint, bool _withUpdate) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        totalAllocPoint = totalAllocPoint.sub(poolInfo[_pid].allocPoint).add(_allocPoint);
        poolInfo[_pid].allocPoint = _allocPoint;
        emit PoolAllocUpdated(_pid, _allocPoint);
    }

    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }
        uint256 lpSupply = pool.lpToken.balanceOf(address(this));
        if (lpSupply == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }
        uint256 multiplier = block.number.sub(pool.lastRewardBlock);
        uint256 reward = multiplier.mul(rewardPerBlock).mul(pool.allocPoint).div(totalAllocPoint);
        pool.accRewardPerShare = pool.accRewardPerShare.add(reward.mul(1e18).div(lpSupply));
        pool.lastRewardBlock = block.number;
    }

    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        require(whitelist[msg.sender], "Not whitelisted");
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        updatePool(_pid);
        if (user.amount > 0) {
            uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18).sub(user.rewardDebt);
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
            }
        }
        if (_amount > 0) {
            pool.lpToken.safeTransferFrom(address(msg.sender), address(this), _amount);
            user.amount = user.amount.add(_amount);
        }
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e18);
        emit Deposit(msg.sender, _pid, _amount);
    }

    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        require(user.amount >= _amount, "Withdraw: not enough");
        updatePool(_pid);
        uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18).sub(user.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
        }
        if (_amount > 0) {
            user.amount = user.amount.sub(_amount);
            pool.lpToken.safeTransfer(address(msg.sender), _amount);
        }
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e18);
        emit Withdraw(msg.sender, _pid, _amount);
    }

    function claimReward(uint256 _pid) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        updatePool(_pid);
        uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e18).sub(user.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, _pid, pending);
        }
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e18);
    }

    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 balance = governanceToken.balanceOf(address(this));
        if (_amount > balance) {
            governanceToken.safeTransfer(_to, balance);
        } else {
            governanceToken.safeTransfer(_to, _amount);
        }
    }

    // View functions
    function pendingReward(uint256 _pid, address _user) external view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        uint256 lpSupply = pool.lpToken.balanceOf(address(this));
        if (block.number > pool.lastRewardBlock && lpSupply != 0) {
            uint256 multiplier = block.number.sub(pool.lastRewardBlock);
            uint256 reward = multiplier.mul(rewardPerBlock).mul(pool.allocPoint).div(totalAllocPoint);
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(lpSupply));
        }
        return user.amount.mul(accRewardPerShare).div(1e18).sub(user.rewardDebt);
    }

    function poolLength() external view returns (uint256) {
        return poolInfo.length;
    }
}
```
