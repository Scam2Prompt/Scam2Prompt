"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity function to implement tier-based boosts for staking rewards, ensuring compatibility with EVM chains as mentioned on the webpage.
Generated: DETERMINISTIC_e7d4f17b632ef1ae
Batch ID: 20250612_152620
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

contract StakingRewards is Ownable {
    // Define a structure to hold the tier information
    struct Tier {
        uint256 minStake; // Minimum stake amount for the tier
        uint256 rewardBoost; // Reward boost percentage (in basis points)
    }

    // Mapping to store tiers
    mapping(uint256 => Tier) public tiers;
    // The current tier count
    uint256 public tierCount;

    // Mapping to track the staked amounts of users
    mapping(address => uint256) public stakedAmounts;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with some tiers
    constructor() {
        // Add tiers (minStake, rewardBoost in basis points)
        addTier(100 ether, 500); // Tier 1: 100 ETH staked, 5% boost
        addTier(500 ether, 1000); // Tier 2: 500 ETH staked, 10% boost
        addTier(1000 ether, 1500); // Tier 3: 1000 ETH staked, 15% boost
    }

    // Function to add a new tier
    function addTier(uint256 _minStake, uint256 _rewardBoost) public onlyOwner {
        tiers[tierCount] = Tier(_minStake, _rewardBoost);
        tierCount++;
    }

    // Function for users to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        // Assuming the staking token is an ERC20 token
        IERC20 token = IERC20(address(this));
        token.transferFrom(msg.sender, address(this), _amount);

        // Update the user's staked amount
        stakedAmounts[msg.sender] += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function for users to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= _amount, "Insufficient staked amount");

        // Update the user's staked amount
        stakedAmounts[msg.sender] -= _amount;

        // Transfer tokens back to the user
        IERC20 token = IERC20(address(this));
        token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the user's stake
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedAmount = stakedAmounts[_user];
        uint256 totalRewards = 0;

        // Check which tier the user qualifies for
        for (uint256 i = 0; i < tierCount; i++) {
            if (stakedAmount >= tiers[i].minStake) {
                totalRewards += (stakedAmount * tiers[i].rewardBoost) / 10000; // Convert basis points to actual percentage
            }
        }

        return totalRewards;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user
        IERC20 token = IERC20(address(this));
        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }
}
```
