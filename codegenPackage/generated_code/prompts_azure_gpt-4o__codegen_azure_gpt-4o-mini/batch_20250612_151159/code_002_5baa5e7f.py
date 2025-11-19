"""
Generated Code Metadata:
========================
Original URL: https://neiros.pages.dev
Prompt: Provide a Solidity contract example that could be used to create a token similar to $NEIRO, including features like no tax and a fixed supply of 1 billion tokens.
Generated: DETERMINISTIC_5baa5e7fdcae65d2
Batch ID: 20250612_151159
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NEIRO token
contract NEIRO is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("NEIRO Token", "NEIRO") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, _totalSupply);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        // Mint the specified amount of tokens
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
    }

    // Override the transfer function to ensure no tax is applied
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to ensure no tax is applied
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }
}
```
