"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Generate code for a staking rewards system that distributes both platform tokens and stablecoins as airdrops, modeled after the $BCB staking mechanism described on Blockchain Bets.
Generated: DETERMINISTIC_a2741bcbe85dcea4
Batch ID: 20250612_153420
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

contract StakingRewards is Ownable, ReentrancyGuard {
    // Struct to store user staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for platform tokens
        uint256 stableDebt; // Reward debt for stablecoins
        uint256 lastStakeTime; // Last time user staked
    }

    // Staking token (BCB in this case)
    IERC20 public stakingToken;
    
    // Reward tokens
    IERC20 public platformToken;
    IERC20 public stablecoin;
    
    // Reward rates
    uint256 public platformTokenPerBlock;
    uint256 public stablecoinPerBlock;
    
    // Precision factor for accurate division
    uint256 public constant PRECISION_FACTOR = 1e18;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accPlatformTokenPerShare;
    uint256 public accStablecoinPerShare;
    
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    
    // Staking duration in blocks
    uint256 public stakingDuration;
    
    // Minimum staking amount
    uint256 public minStakeAmount;
    
    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 platformAmount, uint256 stableAmount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    
    constructor(
        IERC20 _stakingToken,
        IERC20 _platformToken,
        IERC20 _stablecoin,
        uint256 _platformTokenPerBlock,
        uint256 _stablecoinPerBlock,
        uint256 _stakingDuration,
        uint256 _minStakeAmount
    ) {
        stakingToken = _stakingToken;
        platformToken = _platformToken;
        stablecoin = _stablecoin;
        platformTokenPerBlock = _platformTokenPerBlock;
        stablecoinPerBlock = _stablecoinPerBlock;
        stakingDuration = _stakingDuration;
        minStakeAmount = _minStakeAmount;
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
        
        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 platformTokenReward = blocksSinceLastReward * platformTokenPerBlock;
        uint256 stablecoinReward = blocksSinceLastReward * stablecoinPerBlock;
        
        accPlatformTokenPerShare += (platformTokenReward * PRECISION_FACTOR) / totalStaked;
        accStablecoinPerShare += (stablecoinReward * PRECISION_FACTOR) / totalStaked;
        
        lastRewardBlock = block.number;
    }
    
    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount >= minStakeAmount, "Amount below minimum stake");
        
        UserInfo storage user = userInfo[msg.sender];
        updatePool();
        
        if (user.amount > 0) {
            uint256 pendingPlatform = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR - user.rewardDebt;
            uint256 pendingStable = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR - user.stableDebt;
            
            if (pendingPlatform > 0) {
                safeTransfer(platformToken, msg.sender, pendingPlatform);
            }
            if (pendingStable > 0) {
                safeTransfer(stablecoin, msg.sender, pendingStable);
            }
        }
        
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR;
        user.stableDebt = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR;
        user.lastStakeTime = block.timestamp;
        
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }
    
    // Unstake tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastStakeTime + stakingDuration, "Staking duration not reached");
        
        updatePool();
        
        uint256 pendingPlatform = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR - user.rewardDebt;
        uint256 pendingStable = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR - user.stableDebt;
        
        if (pendingPlatform > 0) {
            safeTransfer(platformToken, msg.sender, pendingPlatform);
        }
        if (pendingStable > 0) {
            safeTransfer(stablecoin, msg.sender, pendingStable);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR;
        user.stableDebt = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR;
        
        stakingToken.transfer(msg.sender, _amount);
        totalStaked -= _amount;
        
        emit Unstaked(msg.sender, _amount);
        emit RewardClaimed(msg.sender, pendingPlatform, pendingStable);
    }
    
    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked amount");
        
        updatePool();
        
        uint256 pendingPlatform = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR - user.rewardDebt;
        uint256 pendingStable = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR - user.stableDebt;
        
        require(pendingPlatform > 0 || pendingStable > 0, "No rewards to claim");
        
        if (pendingPlatform > 0) {
            safeTransfer(platformToken, msg.sender, pendingPlatform);
        }
        if (pendingStable > 0) {
            safeTransfer(stablecoin, msg.sender, pendingStable);
        }
        
        user.rewardDebt = (user.amount * accPlatformTokenPerShare) / PRECISION_FACTOR;
        user.stableDebt = (user.amount * accStablecoinPerShare) / PRECISION_FACTOR;
        
        emit RewardClaimed(msg.sender, pendingPlatform, pendingStable);
    }
    
    // Emergency withdraw without rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        user.amount = 0;
        user.rewardDebt = 0;
        user.stableDebt = 0;
        
        stakingToken.transfer(msg.sender, amount);
        totalStaked -= amount;
        
        emit EmergencyWithdraw(msg.sender, amount);
    }
    
    // Safe transfer function to handle insufficient balance
    function safeTransfer(IERC20 token, address to, uint256 amount) internal {
        uint256 balance = token.balanceOf(address(this));
        if (amount > balance) {
            token.transfer(to, balance);
        } else {
            token.transfer(to, amount);
        }
    }
    
    // Admin functions
    function updateRewardRates(uint256 _platformTokenPerBlock, uint256 _stablecoinPerBlock) external onlyOwner {
        updatePool();
        platformTokenPerBlock = _platformTokenPerBlock;
        stablecoinPerBlock = _stablecoinPerBlock;
    }
    
    function updateStakingDuration(uint256 _stakingDuration) external onlyOwner {
        stakingDuration = _stakingDuration;
    }
    
    function updateMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        minStakeAmount = _minStakeAmount;
    }
    
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address
