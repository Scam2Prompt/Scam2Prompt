"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Create a Solidity contract for a meme token that includes a community reward system, inspired by `$BAMBOO`'s claim reward feature.
Generated: DETERMINISTIC_2080fe14c5693ec8
Batch ID: 20250612_152240
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

// Import OpenZeppelin's ERC20 contract and Ownable for administrative functions
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeToken is a simple ERC20 token with a reward system
contract MemeToken is ERC20, Ownable {
    // Mapping to keep track of user rewards
    mapping(address => uint256) public rewards;
    // Total rewards pool
    uint256 public totalRewards;
    // Reward rate per token
    uint256 public rewardRate;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Set the initial reward rate
        rewardRate = 1e18; // 1 token = 1 reward unit
    }

    // Function to mint tokens to an address
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to set the reward rate; only callable by the owner
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
    }

    // Function to calculate and distribute rewards
    function distributeRewards(address user) external onlyOwner {
        uint256 userBalance = balanceOf(user);
        require(userBalance > 0, "User has no tokens to reward");

        // Calculate rewards based on user's balance
        uint256 userRewards = userBalance * rewardRate;
        totalRewards += userRewards;
        rewards[user] += userRewards;
    }

    // Function for users to claim their accumulated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring tokens
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        _mint(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to check the total rewards pool balance
    function getTotalRewards() external view returns (uint256) {
        return totalRewards;
    }
}
```
