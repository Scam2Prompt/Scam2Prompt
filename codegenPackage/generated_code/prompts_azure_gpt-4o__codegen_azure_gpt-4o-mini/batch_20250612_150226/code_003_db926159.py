"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Create a smart contract that uses Bluwhale's AI-powered wallet insights to reward users for engaging with personalized outreach messages.
Generated: DETERMINISTIC_db92615928db7c90
Batch ID: 20250612_150226
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract to reward users for engaging with personalized outreach messages
contract RewardSystem {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public rewardToken; // ERC20 token used for rewards
    mapping(address => uint256) public userRewards; // Mapping to track rewards for each user

    // Events
    event RewardIssued(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        owner = msg.sender; // Set the contract deployer as the owner
        rewardToken = IERC20(_rewardToken); // Initialize the reward token
    }

    // Function to issue rewards to users
    function issueReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update the user's reward balance
        userRewards[user] += amount;

        // Transfer the reward tokens to the user
        rewardToken.transfer(user, amount);

        // Emit an event for the reward issuance
        emit RewardIssued(user, amount);
    }

    // Function to check the reward balance of a user
    function checkRewardBalance(address user) external view returns (uint256) {
        return userRewards[user];
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner; // Update the owner
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        rewardToken.transfer(owner, amount);
    }
}
```
