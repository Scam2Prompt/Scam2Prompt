"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Generate a smart contract for a token with a burning mechanism, similar to $CORGIAI.
Generated: DETERMINISTIC_e66e146802c517a7
Batch ID: 20250622_205623
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a token with a burning mechanism
contract CorgiAI is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("CorgiAI Token", "CORGIAI") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        // Emit the TokensBurned event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to burn tokens on behalf of another account (only owner)
    function burnFrom(address account, uint256 amount) external onlyOwner {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the specified account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Call the _burn function to burn tokens
        _burn(account, amount);
        // Emit the TokensBurned event
        emit TokensBurned(account, amount);
    }
}
```
