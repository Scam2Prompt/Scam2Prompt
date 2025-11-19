"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Create a smart contract in Solidity for implementing TG.Casino's buy-back mechanism for `$TGC` tokens as described in the roadmap.
Generated: DETERMINISTIC_46c2d7eb5f1f7e0f
Batch ID: 20250612_150435
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for TG.Casino's buy-back mechanism for $TGC tokens
contract TGCasinoBuyBack is Ownable {
    // Address of the $TGC token contract
    IERC20 public tgcToken;

    // Event emitted when tokens are bought back
    event TokensBoughtBack(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract with the $TGC token address
    constructor(address _tgcToken) {
        require(_tgcToken != address(0), "Invalid token address");
        tgcToken = IERC20(_tgcToken);
    }

    // Function to buy back $TGC tokens from the market
    function buyBackTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the specified amount of $TGC tokens from the contract to the owner
        uint256 balanceBefore = tgcToken.balanceOf(address(this));
        tgcToken.transferFrom(msg.sender, address(this), amount);
        uint256 balanceAfter = tgcToken.balanceOf(address(this));

        // Ensure the transfer was successful
        require(balanceAfter == balanceBefore + amount, "Token transfer failed");

        // Emit an event for the buy-back
        emit TokensBoughtBack(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(tgcToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of $TGC tokens to the owner
        tgcToken.transfer(msg.sender, amount);
    }

    // Function to set a new $TGC token address (only owner can call)
    function setTgcTokenAddress(address _tgcToken) external onlyOwner {
        require(_tgcToken != address(0), "Invalid token address");
        tgcToken = IERC20(_tgcToken);
    }
}
```
