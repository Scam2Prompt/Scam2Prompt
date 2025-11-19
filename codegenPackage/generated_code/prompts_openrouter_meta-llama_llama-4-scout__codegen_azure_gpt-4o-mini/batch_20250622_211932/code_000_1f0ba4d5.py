"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Write a Python code snippet using the ERC20 Token Standard to create a smart contract for a utility token like PLRT on the Binance Smart Chain.
Generated: DETERMINISTIC_1f0ba4d5a43d9713
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PLRTToken is a utility token that follows the ERC20 standard
contract PLRTToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PLRT Token", "PLRT") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        // Mint the specified amount of tokens to the given address
        _mint(to, amount);
    }

    // Function to burn tokens, reducing the total supply
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        // Burn the specified amount of tokens from the caller's balance
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens with additional checks
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    // Function to approve tokens for delegated transfer
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        require(amount > 0, "Approval amount must be greater than zero");
        
        // Call the parent approve function
        return super.approve(spender, amount);
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Call the parent transferFrom function
        return super.transferFrom(sender, recipient, amount);
    }
}
```
