"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: How can I implement a rewards system for an ETH-based application that supports EVM wallets, similar to the one described on de-agent.com?
Generated: DETERMINISTIC_e2e202ab4e6bf13a
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RewardsSystem contract to manage rewards for users
contract RewardsSystem is Ownable {
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Mapping to keep track of user rewards
    mapping(address => uint256) private rewards;

    // The ERC20 token used for rewards
    IERC20 public rewardsToken;

    // Constructor to set the rewards token address
    constructor(IERC20 _rewardsToken) {
        rewardsToken = _rewardsToken;
    }

    // Function to add rewards to a user's balance
    // Only the owner can call this function
    function addRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = rewardsToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    // Function to check the rewards balance of a user
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    // Function to withdraw unwanted tokens from the contract
    // Only the owner can call this function
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
