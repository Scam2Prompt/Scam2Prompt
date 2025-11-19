"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-f.pages.dev
Prompt: What code is needed to implement staking and harvesting of assets within a DApp ecosystem?
Generated: DETERMINISTIC_b3148fb71c1f0f92
Batch ID: 20250612_163338
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a decentralized application (DApp)
contract Staking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt
        uint256 lastStakeTime; // Last time the staker staked
    }

    // Token to be staked
    IERC20 public stakingToken;
    // Total staked amount
    uint256 public totalStaked;
    // Reward rate per second
    uint256 public rewardRate;
    // Mapping from staker address to Staker info
    mapping(address => Staker) public stakers;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);

    // Constructor to initialize the contract with token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate; // Reward rate in tokens per second
    }

    // Modifier to check if the user has staked
    modifier hasStake() {
        require(stakers[msg.sender].amount > 0, "No stake found.");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastStakeTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external hasStake {
        Staker storage staker = stakers[msg.sender];
        require(amount <= staker.amount, "Insufficient staked amount.");

        // Harvest any pending rewards before unstaking
        harvest();

        // Update staker information
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and return pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 accruedReward = (block.timestamp - staker.lastStakeTime) * rewardRate;
        return accruedReward + staker.rewardDebt;
    }

    // Harvest function to claim rewards
    function harvest() public hasStake {
        Staker storage staker = stakers[msg.sender];
        uint256 pending = pendingRewards(msg.sender);
        require(pending > 0, "No rewards to harvest.");

        // Update reward debt
        staker.rewardDebt += pending;
        staker.lastStakeTime = block.timestamp;

        // Transfer reward to user (assuming rewards are in the same token)
        stakingToken.transfer(msg.sender, pending);

        emit Harvested(msg.sender, pending);
    }

    // Function to update reward rate (only callable by owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
