"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Write a smart contract in Solidity for a staking pool that operates on the Linea network, supports compounding rewards, and adjusts investor tiers based on staking duration, similar to the pools described on SidusPad.
Generated: DETERMINISTIC_4d26f8820ab267d3
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's IERC20 interface for ERC20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract definition
contract StakingPool is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount;        // Amount staked
        uint256 rewardDebt;    // Reward debt for compounding
        uint256 lastStakedAt;  // Last time staked
        uint256 tier;          // Staking tier based on duration
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount in the pool
    uint256 public totalStaked;
    
    // Reward token
    IERC20 public rewardToken;

    // Annual percentage yield for rewards (APY)
    uint256 public annualRewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken, uint256 _annualRewardRate) {
        rewardToken = _rewardToken;
        annualRewardRate = _annualRewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        require(rewardToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating the state
        _updateRewards(msg.sender);

        // Update staker information
        staker.amount += _amount;
        staker.lastStakedAt = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Calculate pending rewards before updating the state
        _updateRewards(msg.sender);

        // Decrease staker's amount and total staked
        staker.amount -= _amount;
        totalStaked -= _amount;

        require(rewardToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset reward debt to zero
        staker.rewardDebt = 0;

        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit Claimed(msg.sender, reward);
    }

    // Internal function to update rewards for a staker
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        
        // Calculate the duration staked in years
        uint256 duration = (block.timestamp - staker.lastStakedAt) / 365 days;
        
        // Calculate tier based on staking duration
        staker.tier = _calculateTier(duration);
        
        // Calculate the pending rewards
        uint256 pendingRewards = (staker.amount * annualRewardRate * duration) / 100;

        // Update the reward debt
        staker.rewardDebt += pendingRewards;
        
        // Update the last staked timestamp
        staker.lastStakedAt = block.timestamp;
    }

    // Function to calculate staking tier based on duration
    function _calculateTier(uint256 duration) internal pure returns (uint256) {
        if (duration < 1) return 0;
        if (duration < 2) return 1;
        if (duration < 3) return 2;
        return 3; // Tier 3 for 3 years or more
    }

    // Function to set a new reward rate (only callable by owner)
    function setAnnualRewardRate(uint256 _annualRewardRate) external onlyOwner {
        annualRewardRate = _annualRewardRate;
    }
}
```
