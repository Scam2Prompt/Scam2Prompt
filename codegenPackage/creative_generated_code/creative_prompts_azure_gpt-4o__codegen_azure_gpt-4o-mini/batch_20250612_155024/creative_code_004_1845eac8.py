"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dinamikaplus.ru
Prompt: Write a smart contract in Solidity to enable staking of BELT tokens and distribute rewards based on the mechanisms described in Belt Finance.
Generated: DETERMINISTIC_1845eac8f9ec3e5e
Batch ID: 20250612_155024
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

// Interface for the BELT token contract
interface IBeltToken {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the reward distribution mechanism
interface IRewardDistributor {
    function distributeRewards(address staker, uint256 amount) external;
}

contract BeltStaking {
    // The BELT token contract
    IBeltToken public beltToken;
    // Reward distributor contract
    IRewardDistributor public rewardDistributor;

    // Struct to hold information about each staker
    struct Staker {
        uint256 balance; // Amount of BELT tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping from staker address to their info
    mapping(address => Staker) public stakers;

    // Total amount of BELT tokens staked
    uint256 public totalStaked;

    // Events for logging staking and withdrawing actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with BELT token and reward distributor addresses
    constructor(IBeltToken _beltToken, IRewardDistributor _rewardDistributor) {
        beltToken = _beltToken;
        rewardDistributor = _rewardDistributor;
    }

    // Function to stake BELT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the staker's balance and total staked amount
        Staker storage staker = stakers[msg.sender];
        staker.balance += amount;
        totalStaked += amount;

        // Transfer BELT tokens from the staker to the contract
        require(beltToken.transfer(address(this), amount), "Transfer failed");

        // Emit the staking event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked BELT tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(staker.balance >= amount, "Insufficient balance to withdraw");

        // Update the staker's balance and total staked amount
        staker.balance -= amount;
        totalStaked -= amount;

        // Transfer BELT tokens from the contract to the staker
        require(beltToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to distribute rewards to stakers
    function distributeRewards(uint256 totalReward) external {
        require(totalReward > 0, "Total reward must be greater than zero");

        // Loop through all stakers and distribute rewards
        for (uint256 i = 0; i < totalStaked; i++) {
            // Logic to calculate rewards for each staker
            // This is a placeholder; actual reward calculation logic should be implemented
            uint256 reward = calculateReward(stakers[address(i)], totalReward);
            if (reward > 0) {
                // Update the staker's reward debt
                stakers[address(i)].rewardDebt += reward;
                // Distribute the reward
                rewardDistributor.distributeRewards(address(i), reward);
                emit RewardsDistributed(address(i), reward);
            }
        }
    }

    // Placeholder function to calculate rewards
    function calculateReward(Staker memory staker, uint256 totalReward) internal pure returns (uint256) {
        // Implement reward calculation logic based on staked amount and other parameters
        return (staker.balance * totalReward) / totalStaked; // Example calculation
    }

    // Function to get staker info
    function getStakerInfo(address user) external view returns (uint256 balance, uint256 rewardDebt) {
        Staker storage staker = stakers[user];
        return (staker.balance, staker.rewardDebt);
    }
}
```
