"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Outline a step-by-step guide for implementing a staking feature for the $FROP token, focusing on the two pools mentioned in the Popo project.
Generated: DETERMINISTIC_d750f3ed6b657cee
Batch ID: 20250612_161039
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the $FROP token with two staking pools
contract FROPStaking is Ownable {
    // Define the token contract address
    IERC20 public fropToken;

    // Define the staking pool structure
    struct Pool {
        uint256 totalStaked;
        uint256 rewardRate; // Rewards per staked token per block
        mapping(address => uint256) stakedAmount; // Amount staked by each user
    }
    
    // Create two pools
    Pool public pool1;
    Pool public pool2;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount, uint256 poolId);
    event Unstaked(address indexed user, uint256 amount, uint256 poolId);
    event RewardsClaimed(address indexed user, uint256 rewardAmount, uint256 poolId);

    // Constructor to initialize the contract with the FROP token address
    constructor(address _fropToken) {
        fropToken = IERC20(_fropToken);
        // Initialize pools with reward rates (example values)
        pool1.rewardRate = 1e18; // 1 FROP per block per token
        pool2.rewardRate = 2e18; // 2 FROP per block per token
    }

    // Function to stake tokens in a specified pool
    function stake(uint256 amount, uint256 poolId) external {
        require(poolId == 1 || poolId == 2, "Invalid pool ID");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the tokens from the user to the contract
        require(fropToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staked amount and total staked for the pool
        if (poolId == 1) {
            pool1.stakedAmount[msg.sender] += amount;
            pool1.totalStaked += amount;
        } else {
            pool2.stakedAmount[msg.sender] += amount;
            pool2.totalStaked += amount;
        }

        emit Staked(msg.sender, amount, poolId);
    }

    // Function to unstake tokens from a specified pool
    function unstake(uint256 amount, uint256 poolId) external {
        require(poolId == 1 || poolId == 2, "Invalid pool ID");
        require(amount > 0, "Amount must be greater than zero");

        // Check if the user has staked enough in the specified pool
        if (poolId == 1) {
            require(pool1.stakedAmount[msg.sender] >= amount, "Insufficient staked amount in pool 1");
            pool1.stakedAmount[msg.sender] -= amount;
            pool1.totalStaked -= amount;
        } else {
            require(pool2.stakedAmount[msg.sender] >= amount, "Insufficient staked amount in pool 2");
            pool2.stakedAmount[msg.sender] -= amount;
            pool2.totalStaked -= amount;
        }

        // Transfer the tokens back to the user
        require(fropToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, poolId);
    }

    // Function to calculate rewards (simplified for demonstration)
    function calculateRewards(address user, uint256 poolId) external view returns (uint256) {
        // Here you would implement the actual logic for calculating rewards
        // This is a placeholder return value for demonstration purposes
        return poolId == 1 ? pool1.stakedAmount[user] * pool1.rewardRate : pool2.stakedAmount[user] * pool2.rewardRate;
    }

    // Function to claim rewards (simplified for demonstration)
    function claimRewards(uint256 poolId) external {
        uint256 rewardAmount = calculateRewards(msg.sender, poolId);
        require(rewardAmount > 0, "No rewards available");

        // Transfer the rewards to the user (ensure you have enough tokens to cover rewards)
        require(fropToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount, poolId);
    }
}
```
