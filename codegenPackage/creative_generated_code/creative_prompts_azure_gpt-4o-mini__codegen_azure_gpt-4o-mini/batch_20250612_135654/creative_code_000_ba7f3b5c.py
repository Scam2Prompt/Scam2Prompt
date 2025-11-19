"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Generate a smart contract for a meme coin similar to CUM Coin, focusing on cross-border liquidity and zero tax on transactions.
Generated: DETERMINISTIC_ba7f3b5ca7c71626
Batch ID: 20250612_135654
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

// Importing the OpenZeppelin ERC20 standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin is a simple ERC20 token with no transaction taxes and aimed at cross-border liquidity
contract MemeCoin is ERC20, Ownable {
    // Events for monitoring token transfers
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the meme coin with its name and symbol
    constructor() ERC20("MemeCoin", "MEME") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to mint new tokens, callable only by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens, callable only by the owner
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Override the _transfer function to ensure no transaction fees are deducted
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(from) >= amount, "Insufficient balance for transfer");
        
        super._transfer(from, to, amount);
    }
}
```
