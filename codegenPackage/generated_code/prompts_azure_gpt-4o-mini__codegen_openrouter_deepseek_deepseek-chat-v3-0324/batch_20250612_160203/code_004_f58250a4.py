"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: Describe how to set up a staking mechanism for users who hold $EARNM tokens, including vesting periods and reward distribution.
Generated: DETERMINISTIC_f58250a41eebed60
Batch ID: 20250612_160203
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

contract EarnmStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;             // Amount of tokens staked
        uint256 rewardDebt;         // Reward debt for accounting
        uint256 vestingEndTime;     // When vesting period ends
        uint256 lastClaimTime;      // Last time rewards were claimed
    }

    // The EARNM token contract
    IERC20 public immutable earnmToken;
    
    // Reward token (could be same as staked token)
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Vesting period in seconds
    uint256 public vestingPeriod;
    
    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time reward distribution was updated
    uint256 public lastRewardTime;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event VestingPeriodUpdated(uint256 newPeriod);

    constructor(
        address _earnmToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _vestingPeriod
    ) {
        require(_earnmToken != address(0), "EARNM token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        
        earnmToken = IERC20(_earnmToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        vestingPeriod = _vestingPeriod;
        lastRewardTime = block.timestamp;
    }

    // Update reward variables
    function updateReward() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate;
        
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        
        // If already staking, claim pending rewards first
        if (staker.amount > 0) {
            _claimRewards();
        }
        
        // Transfer tokens from user to contract
        earnmToken.safeTransferFrom(msg.sender, address(this), _amount);
        
        // Update staker info
        staker.amount += _amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.vestingEndTime = block.timestamp + vestingPeriod;
        staker.lastClaimTime = block.timestamp;
        
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= staker.vestingEndTime, "Tokens are still vesting");
        
        updateReward();
        
        // Claim any pending rewards first
        _claimRewards();
        
        // Update staker info
        staker.amount -= _amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        
        totalStaked -= _amount;
        
        // Transfer tokens back to user
        earnmToken.safeTransfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    // Internal function to claim rewards
    function _claimRewards() internal {
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        if (staker.amount == 0) return;
        
        uint256 pending = ((staker.amount * accRewardPerShare) / PRECISION) - staker.rewardDebt;
        if (pending == 0) return;
        
        // Update reward debt
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.lastClaimTime = block.timestamp;
        
        // Transfer rewards
        rewardToken.safeTransfer(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        if (staker.amount == 0) return 0;
        
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return ((staker.amount * currentAccRewardPerShare) / PRECISION) - staker.rewardDebt;
    }

    // Owner functions
    function setRewardRate(uint256 _newRate) external onlyOwner {
        updateReward();
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    function setVestingPeriod(uint256 _newPeriod) external onlyOwner {
        vestingPeriod = _newPeriod;
        emit VestingPeriodUpdated(_newPeriod);
    }

    // Emergency withdraw rewards (owner only)
    function emergencyWithdrawRewards(uint256 _amount) external onlyOwner {
        rewardToken.safeTransfer(msg.sender, _amount);
    }
}
```
