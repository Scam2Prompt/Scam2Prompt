"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a smart contract in Solidity for a loyalty program that rewards users with CRUDO tokens for frequent gas purchases at affiliated petrol stations.
Generated: DETERMINISTIC_e236accf2ad9d5bb
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface for CRUDO token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LoyaltyProgram contract to manage rewards for gas purchases
contract LoyaltyProgram is Ownable {
    // Event emitted when rewards are issued
    event RewardsIssued(address indexed user, uint256 amount);

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Reference to the CRUDO token contract
    IERC20 public crudoToken;

    // Constructor to initialize the CRUDO token address
    constructor(address _crudoTokenAddress) {
        require(_crudoTokenAddress != address(0), "Invalid token address");
        crudoToken = IERC20(_crudoTokenAddress);
    }

    // Function to reward users for gas purchases
    function rewardUser(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the user's rewards balance
        rewards[user] += amount;

        // Emit an event for the rewards issued
        emit RewardsIssued(user, amount);
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards balance
        rewards[msg.sender] = 0;

        // Transfer CRUDO tokens to the user
        require(crudoToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }

    // Function to check the reward balance of a user
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(crudoToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(crudoToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
