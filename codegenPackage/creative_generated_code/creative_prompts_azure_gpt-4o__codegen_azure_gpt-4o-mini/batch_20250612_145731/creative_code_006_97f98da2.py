"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Create a Solidity function for staking MuziKoin tokens, ensuring rewards are distributed fairly to participants in the ecosystem.
Generated: DETERMINISTIC_97f98da21f3ba898
Batch ID: 20250612_145731
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

/// @title MuziKoin Staking Contract
/// @author Your Name
/// @notice This contract allows users to stake MuziKoin tokens and earn rewards
/// @dev This contract is designed to be production-ready with proper error handling

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MuziKoinStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public muziKoin;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per token staked per second
    uint256 public rewardRate = 1e18; // Example reward rate (1 reward token per second per token staked)
    
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(IERC20 _muziKoin) {
        muziKoin = _muziKoin;
    }

    /// @notice Stake MuziKoin tokens
    /// @param _amount The amount of tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        // Transfer tokens from the user to the contract
        muziKoin.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(_amount);
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /// @notice Unstake MuziKoin tokens and claim rewards
    /// @param _amount The amount of tokens to unstake
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Calculate pending rewards before unstaking
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        // Update staker information
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer the unstaked tokens back to the user
        muziKoin.transfer(msg.sender, _amount);
        
        // Transfer rewards to the user, if any
        if (pendingRewards > 0) {
            muziKoin.transfer(msg.sender, pendingRewards);
            emit RewardPaid(msg.sender, pendingRewards);
        }

        emit Unstaked(msg.sender, _amount);
    }

    /// @notice Calculate pending rewards for a staker
    /// @param _staker The staker's address
    /// @return pendingRewards The calculated pending rewards
    function calculatePendingRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 stakedDuration = block.timestamp.sub(staker.lastStakedTime);
        return staker.amountStaked.mul(rewardRate).mul(stakedDuration).div(1e18);
    }

    /// @notice Update the reward rate (only owner)
    /// @param _newRate The new reward rate
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
