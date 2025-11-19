"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Generate a smart contract for a meme token similar to MAGA ($MAGA) that has a 0% tax and is community-driven.
Generated: DETERMINISTIC_70e68b63216a9e5d
Batch ID: 20250612_160853
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Meme Token $MAGA
contract MemeToken is ERC20, Ownable {
    // Events for transfer logging
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Meme Token", "MAGA") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Example: 1 million tokens
    }

    // Function to mint new tokens (only owner)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens (only owner)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    // Override the transfer function to ensure no transaction fees are applied
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");

        super._transfer(sender, recipient, amount);
    }
}
```
