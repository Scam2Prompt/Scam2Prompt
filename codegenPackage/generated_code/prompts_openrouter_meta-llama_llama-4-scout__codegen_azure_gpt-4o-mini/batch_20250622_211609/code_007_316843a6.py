"""
Generated Code Metadata:
========================
Original URL: https://fomo-radar.web.app
Prompt: Write a smart contract to interact with FOMO's portfolio tracking features on a blockchain like Ethereum or Polygon.
Generated: DETERMINISTIC_316843a699d86942
Batch ID: 20250622_211609
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

// FOMO Portfolio Tracker Smart Contract
contract FomoPortfolioTracker {
    // Struct to represent a user's portfolio
    struct Portfolio {
        uint256 totalValue; // Total value of the portfolio in wei
        mapping(address => uint256) tokenBalances; // Mapping of token addresses to their balances
    }

    // Mapping of user addresses to their portfolios
    mapping(address => Portfolio) private portfolios;

    // Event emitted when a user adds tokens to their portfolio
    event TokensAdded(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user removes tokens from their portfolio
    event TokensRemoved(address indexed user, address indexed token, uint256 amount);

    // Function to add tokens to the user's portfolio
    function addTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's portfolio
        portfolios[msg.sender].tokenBalances[token] += amount;
        portfolios[msg.sender].totalValue += amount; // Assuming 1 token = 1 wei for simplicity

        emit TokensAdded(msg.sender, token, amount);
    }

    // Function to remove tokens from the user's portfolio
    function removeTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(portfolios[msg.sender].tokenBalances[token] >= amount, "Insufficient token balance");

        // Update the user's portfolio
        portfolios[msg.sender].tokenBalances[token] -= amount;
        portfolios[msg.sender].totalValue -= amount; // Assuming 1 token = 1 wei for simplicity

        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        emit TokensRemoved(msg.sender, token, amount);
    }

    // Function to get the total value of the user's portfolio
    function getTotalValue() external view returns (uint256) {
        return portfolios[msg.sender].totalValue;
    }

    // Function to get the balance of a specific token in the user's portfolio
    function getTokenBalance(address token) external view returns (uint256) {
        return portfolios[msg.sender].tokenBalances[token];
    }
}
```
