"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-3zc.pages.dev
Prompt: Provide an example of a smart contract for managing token farming pools, inspired by the "Farm" tab functionality on the Sophon platform.
Generated: DETERMINISTIC_0f4595e4e59b18e0
Batch ID: 20250612_151143
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

// Importing OpenZeppelin libraries for safe math operations and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenFarmingPool contract allows users to stake tokens and earn rewards
contract TokenFarmingPool is Ownable {
    // Struct to represent a user's stake information
    struct UserStake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their stake information
    mapping(address => UserStake) public userStakes;

    // The token being staked
    IERC20 public stakingToken;
    // Total accumulated rewards
    uint256 public totalRewards;
    // Total staked amount
    uint256 public totalStaked;

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token and total rewards
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient stake amount");

        // Update user stake and total staked amount
        userStake.amount -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        UserStake storage userStake = userStakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(reward > 0, "No rewards available");

        // Update user's reward debt
        userStake.rewardDebt += reward;
        totalRewards -= reward;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        UserStake storage userStake = userStakes[user];
        return (userStake.amount * totalRewards) / totalStaked - userStake.rewardDebt;
    }

    // Function for the owner to distribute rewards
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        totalRewards += amount;

        // Transfer rewards to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
    }

    // View function to get user's stake information
    function getUserStake(address user) external view returns (uint256 amount, uint256 rewards) {
        UserStake storage userStake = userStakes[user];
        return (userStake.amount, calculateReward(user));
    }
}
```
