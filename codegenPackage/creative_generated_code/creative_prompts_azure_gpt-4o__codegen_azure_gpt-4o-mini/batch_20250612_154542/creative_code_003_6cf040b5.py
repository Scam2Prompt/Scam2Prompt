"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://broccoliclaim.web.app
Prompt: Create a smart contract for managing token rewards distribution, inspired by the Broccoli platform's single-transaction claim functionality.
Generated: DETERMINISTIC_6cf040b545fec229
Batch ID: 20250612_154542
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenRewardDistributor contract for managing token rewards distribution
contract TokenRewardDistributor is Ownable {
    // Mapping to keep track of user balances
    mapping(address => uint256) private _rewards;

    // ERC20 token interface
    IERC20 public token;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    // Function to distribute rewards to a user
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the contract to the user
        _rewards[user] += amount;
        emit RewardsDistributed(user, amount);
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 amount = _rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Resetting the user's reward balance
        _rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    // Function to check the rewards balance of a user
    function getRewardsBalance(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }
}
```
