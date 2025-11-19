"""
Generated Code Metadata:
========================
Original URL: https://mantle-xyz.pages.dev
Prompt: "Write a Solidity code example for a decentralized application (dApp) built on Mantle Network, utilizing its high-performance and low-fee features."
Generated: DETERMINISTIC_5b7a0e48b98265f8
Batch ID: 20250622_204722
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

// Importing OpenZeppelin's ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a simple token on the Mantle Network
contract MantleToken is ERC20, Ownable {
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MantleToken", "MTK") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to mint new tokens, only callable by the owner
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint the tokens
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens with a fee (for demonstration purposes)
    function transferWithFee(address recipient, uint256 amount, uint256 fee) external returns (bool) {
        require(amount > 0, "Amount must be greater than zero");
        require(fee >= 0, "Fee must be non-negative");
        require(amount + fee <= balanceOf(msg.sender), "Insufficient balance");

        // Transfer the amount minus the fee to the recipient
        _transfer(msg.sender, recipient, amount);
        // Transfer the fee to the owner
        _transfer(msg.sender, owner(), fee);
        
        return true;
    }
}
```
