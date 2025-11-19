"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract code in Solidity to implement a burning utility for digital assets, similar to the one mentioned on the Clone Force website.
Generated: DETERMINISTIC_e083410b087e282c
Batch ID: 20250622_211758
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

// Importing the OpenZeppelin ERC20 contract for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a burnable ERC20 token
contract BurnableToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to burn tokens on behalf of another account (only owner can call this)
    function burnFrom(address account, uint256 amount) external onlyOwner {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Call the internal burn function
        _burn(account, amount);
        // Emit the burn event
        emit TokensBurned(account, amount);
    }
}
```
