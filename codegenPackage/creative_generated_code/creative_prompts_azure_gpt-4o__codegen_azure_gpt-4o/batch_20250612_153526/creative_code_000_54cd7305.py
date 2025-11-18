"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to the staker's share in the pool over a two-year period, as described in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_54cd73054e5d5e8c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DOGE20 Token Staking Contract
 * @dev A smart contract for staking DOGE20 tokens and distributing rewards proportionally to the staker's share in the pool over a two-year period.
 */
contract Doge20Staking {
    // State variables
    IERC20 public immutable doge20Token; // Address of the DOGE20 token contract
    uint256 public immutable stakingStartTime; // Start time of the staking period
    uint256 public immutable stakingEndTime; // End time of the staking period (2 years from start)
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    uint256 public totalRewardPool; // Total reward pool for distribution
    
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards owed to the staker
    }
    
    mapping(address => StakeInfo) public stakes; // Staking information for each staker
    mapping(address => bool) public hasStaked;  // Flag to check if an address has staked

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 rewards);
    event RewardsClaimed(address indexed staker, uint256 rewards);

    // Constructor
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        require(address(_doge20Token) != address(0), "Token address cannot be zero");
        require(_rewardPool > 0, "Reward pool must be greater than zero");
        
        doge20Token = _doge20Token;
        totalRewardPool = _rewardPool;
        stakingStartTime = block.timestamp;
        stakingEndTime = block.timestamp + 2 * 365 days; // Two years duration
    }

    // Modifier to enforce staking period
    modifier onlyDuringStakingPeriod() {
        require(block.timestamp >= stakingStartTime, "Staking has not started yet");
        require(block.timestamp <= stakingEndTime, "Staking period has ended");
        _;
    }

    // Modifier to check staking eligibility
    modifier hasStake(address staker) {
        require(stakes[staker].amount > 0, "No stake found for this address");
        _;
    }

    /**
     * @notice Allows a user to stake DOGE20 tokens into the pool.
     * @param amount The amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external onlyDuringStakingPeriod {
        require(amount > 0, "Stake amount must be greater than zero");
        
        // Transfer DOGE20 tokens from the staker to this contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        if (!hasStaked[msg.sender]) {
            hasStaked[msg.sender] = true;
        }

        // Update stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.rewardDebt += calculatePendingReward(msg.sender); // Update reward debt
        
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        
        // Calculate pending rewards and reset staker's information
        uint256 pendingRewards = calculatePendingReward(msg.sender);
        uint256 stakedAmount = stakeInfo.amount;
        
        stakeInfo.amount = 0;
        stakeInfo.rewardDebt = 0;

        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards back to the staker
        require(doge20Token.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(doge20Token.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit Unstaked(msg.sender, stakedAmount, pendingRewards);
    }

    /**
     * @notice Allows a staker to claim their pending rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 pendingRewards = calculatePendingReward(msg.sender);
        stakes[msg.sender].rewardDebt = pendingRewards; // Update reward debt
        
        require(doge20Token.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Calculates the pending rewards for a staker.
     * @param staker The address of the staker.
     * @return The pending rewards for the staker.
     */
    function calculatePendingReward(address staker) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[staker];
        if (totalStaked == 0 || stakeInfo.amount == 0) {
            return 0;
        }
        
        uint256 rewardShare = (stakeInfo.amount * totalRewardPool) / totalStaked;
        return rewardShare - stakeInfo.rewardDebt;
    }

    /**
     * @notice Gets the current staking pool balance.
     * @return The total balance of tokens staked in the pool.
     */
    function getStakingPoolBalance() external view returns (uint256) {
        return doge20Token.balanceOf(address(this));
    }
}

// Interface for the ERC20 token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
