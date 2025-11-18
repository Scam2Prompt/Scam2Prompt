"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-greenbitcoin-xyz.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a gamified staking mechanism similar to Green Bitcoin, allowing users to predict Bitcoin price trends and earn rewards.
Generated: DETERMINISTIC_bba26c35bb5aa7d5
Batch ID: 20250612_153400
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

// Import safe math library to avoid overflow/underflow issues
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GamifiedStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold user information
    struct User {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        bool hasParticipated;
    }

    // Mapping to track users and their data
    mapping(address => User) public users;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewards);

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Stake rewards rate (in basis points, e.g. 100 = 1%)
    uint256 public rewardsRate;

    // Constructor to initialize the rewards rate
    constructor(uint256 _rewardsRate) {
        require(_rewardsRate > 0, "Rewards rate must be positive");
        rewardsRate = _rewardsRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update user's staked amount and total staked in contract
        users[msg.sender].stakedAmount = users[msg.sender].stakedAmount.add(amount);
        totalStaked = totalStaked.add(amount);
        users[msg.sender].hasParticipated = true;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate and distribute rewards
    function distributeRewards() external onlyOwner {
        for (address userAddress : getAllUsers()) {
            User storage user = users[userAddress];
            if (user.hasParticipated) {
                uint256 rewards = user.stakedAmount.mul(rewardsRate).div(10000);
                user.rewardsEarned = user.rewardsEarned.add(rewards);
                emit RewardsDistributed(userAddress, rewards);
            }
        }
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        User storage user = users[msg.sender];
        require(user.stakedAmount > 0, "No staked amount to withdraw");

        uint256 amountToWithdraw = user.stakedAmount.add(user.rewardsEarned);
        user.stakedAmount = 0; // Reset user's staked amount
        user.rewardsEarned = 0; // Reset user's rewards

        // Transfer the total amount to the user (Implement token transfer logic)
        // token.transfer(msg.sender, amountToWithdraw);

        // Reduce total staked amount
        totalStaked = totalStaked.sub(amountToWithdraw);
    }

    // Function to get all users (for rewards distribution)
    function getAllUsers() internal view returns (address[] memory) {
        // Assume we maintain an array of addresses that have participated
        // This would need to be implemented for tracking users correctly
    }

    // Function to set a new rewards rate (onlyOwner)
    function setRewardsRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rewards rate must be positive");
        rewardsRate = newRate;
    }
}
```
