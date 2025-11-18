"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magiccraft-migrate.pages.dev
Prompt: Develop a decentralized application (DApp) that allows users to pledge $MCRT tokens and track their contributions within the MagicCraft ecosystem.
Generated: DETERMINISTIC_e098679dd512e3ff
Batch ID: 20250612_145626
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the main contract for the MagicCraft Pledge DApp
contract MagicCraftPledge is Ownable {
    // State variables
    IERC20 public mcrtToken; // ERC20 token contract
    mapping(address => uint256) public contributions; // Mapping to track user contributions
    uint256 public totalPledged; // Total amount pledged in MCRT tokens

    // Event emitted when a user pledges tokens
    event Pledged(address indexed user, uint256 amount);
    // Event emitted when a user withdraws their pledge
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the MCRT token address
    constructor(address _mcrtTokenAddress) {
        require(_mcrtTokenAddress != address(0), "Invalid token address");
        mcrtToken = IERC20(_mcrtTokenAddress);
    }

    // Function to pledge MCRT tokens
    function pledge(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(mcrtToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        contributions[msg.sender] += amount; // Update user's contribution
        totalPledged += amount; // Update total pledged amount

        emit Pledged(msg.sender, amount); // Emit pledge event
    }

    // Function to withdraw pledged tokens
    function withdraw(uint256 amount) external {
        require(contributions[msg.sender] >= amount, "Insufficient balance to withdraw");

        contributions[msg.sender] -= amount; // Update user's contribution
        totalPledged -= amount; // Update total pledged amount

        require(mcrtToken.transfer(msg.sender, amount), "Token transfer failed"); // Transfer tokens back to user
        emit Withdrawn(msg.sender, amount); // Emit withdrawal event
    }

    // Function to get the pledge details of a user
    function getPledgeDetails(address user) external view returns (uint256) {
        return contributions[user]; // Return user's pledged amount
    }

    // Function to retrieve the total amount pledged
    function getTotalPledged() external view returns (uint256) {
        return totalPledged; // Return total pledged amount
    }

    // Owner-only function to withdraw any ERC20 tokens accidentally sent to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(mcrtToken), "Cannot withdraw MCRT token");
        IERC20(tokenAddress).transfer(msg.sender, amount); // Transfer tokens to owner
    }
}
```
