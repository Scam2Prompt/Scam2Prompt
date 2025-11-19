"""
Generated Code Metadata:
========================
Original URL: https://berrycoinerc.vip
Prompt: Create a Solidity contract that mimics the $BERRY token features, including a 0% tax on transactions and a total supply of 420,690,000 tokens.
Generated: DETERMINISTIC_234ba378de2601ea
Batch ID: 20250612_162913
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

// BERRY token contract
contract BERRY is ERC20, Ownable {
    // Total supply of the BERRY token
    uint256 private constant TOTAL_SUPPLY = 420690000 * 10 ** 18; // 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("BERRY Token", "BERRY") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Override the transfer function to ensure 0% tax on transactions
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to ensure 0% tax on transactions
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
