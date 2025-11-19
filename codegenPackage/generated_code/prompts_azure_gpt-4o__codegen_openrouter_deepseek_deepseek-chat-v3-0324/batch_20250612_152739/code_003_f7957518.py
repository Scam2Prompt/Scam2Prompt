"""
Generated Code Metadata:
========================
Original URL: https://stakelayerai.pages.dev
Prompt: Create a smart contract in Solidity for staking $LAI tokens and distributing AI Capsule rewards, ensuring compatibility with ERC-20 and BEP-20 standards as described in the LayerAI documentation.
Generated: DETERMINISTIC_f7957518bac50d34
Batch ID: 20250612_152739
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
 * @title LAIStakingContract
 * @dev A smart contract for staking LAI tokens and earning AI Capsule rewards
 * Compatible with both ERC-20 and BEP-20 standards
 */
contract LAIStakingContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTimestamp;
    }

    // The LAI token contract
    IERC20 public laiToken;
    
    // The AI Capsule token contract
    IERC20 public aiCapsuleToken;
    
    // Reward rate per second per token (in wei)
    uint256 public rewardRate;
    
    // Total amount of LAI tokens staked
    uint256 public totalStaked;
    
    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time the reward distribution was calculated
    uint256 public lastRewardTime;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor function
     * @param _laiToken Address of the LAI token contract
     * @param _aiCapsuleToken Address of the AI Capsule token contract
     * @param _rewardRate Initial reward rate per second per token
     */
    constructor(
        address _laiToken,
        address _aiCapsuleToken,
        uint256 _rewardRate
    ) {
        require(_laiToken != address(0), "LAI token address cannot be zero");
        require(_aiCapsuleToken != address(0), "AI Capsule token address cannot be zero");
        
        laiToken = IERC20(_laiToken);
        aiCapsuleToken = IERC20(_aiCapsuleToken);
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Update the reward variables
     */
    function updateRewardVariables() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate * totalStaked;
        
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stake LAI tokens
     * @param amount Amount of LAI tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        updateRewardVariables();
        
        Staker storage staker = stakers[msg.sender];
        
        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
            if (pending > 0) {
                safeAICapsuleTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        laiToken.safeTransferFrom(msg.sender, address(this), amount);
        
        staker.amountStaked += amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        staker.lastStakedTimestamp = block.timestamp;
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake LAI tokens and claim rewards
     * @param amount Amount of LAI tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        updateRewardVariables();
        
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        
        staker.amountStaked -= amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        totalStaked -= amount;
        
        laiToken.safeTransfer(msg.sender, amount);
        
        if (pending > 0) {
            safeAICapsuleTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked amount");
        
        updateRewardVariables();
        
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        
        safeAICapsuleTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "No staked amount");
        
        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        
        laiToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe AI Capsule transfer function
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function safeAICapsuleTransfer(address to, uint256 amount) internal {
        uint256 aiCapsuleBalance = aiCapsuleToken.balanceOf(address(this));
        if (amount > aiCapsuleBalance) {
            aiCapsuleToken.safeTransfer(to, aiCapsuleBalance);
        } else {
            aiCapsuleToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update the reward rate
     * @param newRate New reward rate per second per token
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        updateRewardVariables();
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev View function to check pending rewards
     * @param user Address of the user
     * @return Pending rewards for the user
     */
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate * totalStaked;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return (staker.amountStaked * currentAccRewardPerShare) / PRECISION - staker.rewardDebt;
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(laiToken), "Cannot withdraw LAI tokens");
        require(tokenAddress != address(aiCapsuleToken), "Cannot withdraw AI Caps
