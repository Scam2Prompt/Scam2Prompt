"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hgtrgf45refre.pages.dev
Prompt: Create a smart contract in Solidity that links multiple tokens ($BEN, $PSYOP, $MTRX) into a unified ecosystem, inspired by the $LOYAL Token Global concept.
Generated: DETERMINISTIC_029402c18a343130
Batch ID: 20250612_150226
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

// Importing the OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for linking multiple tokens into a unified ecosystem
contract UnifiedTokenEcosystem is Ownable {
    // Mapping to keep track of token balances for users
    mapping(address => mapping(address => uint256)) public userBalances;

    // Event emitted when a user links tokens
    event TokensLinked(address indexed user, address indexed token, uint256 amount);

    // Function to link tokens to the ecosystem
    // Allows users to deposit their tokens into the contract
    function linkTokens(address tokenAddress, uint256 amount) external {
        // Ensure the token address is valid
        require(tokenAddress != address(0), "Invalid token address");
        
        // Get the token contract
        IERC20 token = IERC20(tokenAddress);
        
        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's balance of the linked token
        userBalances[msg.sender][tokenAddress] += amount;

        // Emit an event for successful linking
        emit TokensLinked(msg.sender, tokenAddress, amount);
    }

    // Function to unlink tokens from the ecosystem
    // Allows users to withdraw their previously linked tokens
    function unlinkTokens(address tokenAddress, uint256 amount) external {
        // Ensure the user has enough balance to unlink
        require(userBalances[msg.sender][tokenAddress] >= amount, "Insufficient balance to unlink");

        // Update the user's balance before transferring tokens
        userBalances[msg.sender][tokenAddress] -= amount;

        // Get the token contract
        IERC20 token = IERC20(tokenAddress);
        
        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to check the balance of a specific token for a user
    function getUserBalance(address user, address tokenAddress) external view returns (uint256) {
        return userBalances[user][tokenAddress];
    }

    // Function to withdraw all tokens from the contract (only callable by the owner)
    function withdrawToken(address tokenAddress, uint256 amount) external onlyOwner {
        // Get the token contract
        IERC20 token = IERC20(tokenAddress);
        
        // Transfer specified amount of tokens to the owner
        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
