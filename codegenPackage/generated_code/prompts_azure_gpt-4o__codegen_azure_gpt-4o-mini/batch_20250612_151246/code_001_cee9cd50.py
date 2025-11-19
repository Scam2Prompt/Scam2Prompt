"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Create a Solidity smart contract that integrates gamification features for educational milestones, allowing users to earn IQRA Tokens upon completing specific tasks or quizzes.
Generated: DETERMINISTIC_cee9cd50cb5ad4c3
Batch ID: 20250612_151246
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for IQRA Token
contract IQRAToken is ERC20, Ownable {
    // Mapping to track user milestones
    mapping(address => uint256) public userMilestones;

    // Event to log milestone achievements
    event MilestoneAchieved(address indexed user, uint256 milestoneId, uint256 reward);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("IQRA Token", "IQRA") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to allow users to claim tokens for completing a milestone
    function claimTokens(uint256 milestoneId) external {
        // Check if the milestone is valid (greater than 0)
        require(milestoneId > 0, "Invalid milestone ID");

        // Check if the user has not already claimed this milestone
        require(userMilestones[msg.sender] < milestoneId, "Milestone already claimed");

        // Calculate the reward based on the milestone ID
        uint256 reward = milestoneId * 10 * 10 ** decimals(); // Example: 10 IQRA Tokens per milestone

        // Update the user's milestone status
        userMilestones[msg.sender] = milestoneId;

        // Transfer the reward tokens to the user
        _transfer(owner(), msg.sender, reward);

        // Emit an event for the milestone achievement
        emit MilestoneAchieved(msg.sender, milestoneId, reward);
    }

    // Function to allow the owner to mint new tokens (for future milestones)
    function mintTokens(address to, uint256 amount) external onlyOwner {
        // Ensure the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");

        // Mint new tokens to the specified address
        _mint(to, amount);
    }

    // Function to withdraw tokens from the contract (only for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        // Ensure the contract has enough tokens to withdraw
        require(balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
