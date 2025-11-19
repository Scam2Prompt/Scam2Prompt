"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-is.web.app
Prompt: Create a code snippet for a decentralized application (dApp) that allows users to stake $MPEPE tokens in DeFi liquidity pools and earn rewards.
Generated: DETERMINISTIC_859fb319d3054b19
Batch ID: 20250612_155428
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MPEPEStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakeTime; // Timestamp of last stake
    }

    // The $MPEPE token contract
    IERC20 public mpepeToken;
    
    // Reward token contract (could be same as staking token)
    IERC20 public rewardToken;
    
    // Reward rate per block
    uint256 public rewardPerBlock;
    
    // Last block number that reward distribution occurred
    uint256 public lastRewardBlock;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Total tokens staked
    uint256 public totalStaked;
    
    // Staking lock period in seconds
    uint256 public lockPeriod;
    
    // Mapping from user address to user info
    mapping(address => UserInfo) public userInfo;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _mpepeToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _lockPeriod
    ) {
        require(address(_mpepeToken) != address(0), "Invalid token address");
        mpepeToken = _mpepeToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lockPeriod = _lockPeriod;
        lastRewardBlock = block.number;
    }

    // Update reward variables
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }
        
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }
        
        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardPerBlock;
        
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Stake $MPEPE tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        
        UserInfo storage user = userInfo[msg.sender];
        updatePool();
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardPaid(msg.sender, pending);
            }
        }
        
        mpepeToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastStakeTime = block.timestamp;
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(block.timestamp >= user.lastStakeTime + lockPeriod, "Tokens are locked");
        
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardPaid(msg.sender, pending);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;
        
        mpepeToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    // Claim rewards without withdrawing staked tokens
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);
        
        emit RewardPaid(msg.sender, pending);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;
        
        mpepeToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Owner functions
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
    }

    function setLockPeriod(uint256 _lockPeriod) external onlyOwner {
        lockPeriod = _lockPeriod;
    }

    // Recover any ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(mpepeToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
