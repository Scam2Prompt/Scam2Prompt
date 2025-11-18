"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://param-35r.pages.dev
Prompt: Write a function in Solidity to mint tokens for achievements earned in a gaming platform like Param Network.
Generated: DETERMINISTIC_868024d7b9702dc8
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

// Importing OpenZeppelin's ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract for minting achievement tokens
contract AchievementToken is ERC20, Ownable {
    // Mapping to track achievements of each user
    mapping(address => uint256) public achievements;

    // Event to emit when tokens are minted
    event TokensMinted(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("AchievementToken", "ATK") {}

    // Function to mint tokens based on achievements
    // Only callable by the contract owner
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address: zero address");
        require(amount > 0, "Invalid amount: must be greater than zero");

        // Minting new tokens to the specified address
        _mint(to, amount);
        achievements[to] += amount;

        emit TokensMinted(to, amount);
    }

    // Function to check achievements for a user
    function checkAchievements(address user) external view returns (uint256) {
        return achievements[user];
    }

    // Function to burn tokens if necessary (optional)
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Invalid amount: must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens from the sender's balance
        _burn(msg.sender, amount);
    }
}
```
