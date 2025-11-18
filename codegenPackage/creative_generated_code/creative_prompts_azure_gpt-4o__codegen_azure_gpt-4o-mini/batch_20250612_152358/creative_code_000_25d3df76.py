"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Write a smart contract in Solidity for a token with similar tokenomics to Marvin, including features like a 1% tax for burns, a 5% tax for marketing and app development, and a reserved supply for exchange listings and burns.
Generated: DETERMINISTIC_25d3df7651012b2f
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a token with specific tokenomics
contract MarvinToken is ERC20, Ownable {
    // Define tax rates
    uint256 public constant BURN_TAX_RATE = 1;        // 1% tax for burns
    uint256 public constant MARKETING_TAX_RATE = 5;   // 5% tax for marketing and app development

    // Reserved supply for exchange listings and burns
    uint256 public constant RESERVED_SUPPLY = 100000 * 10**18; // 100,000 tokens reserved

    // The total supply of tokens
    uint256 public totalSupplyCap;

    // Mapping to track addresses that have been taxed
    mapping(address => bool) public isTaxed;

    // Event to emit when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);
    
    constructor() ERC20("MarvinToken", "MARVIN") {
        // Set the total supply cap
        totalSupplyCap = 1000000 * 10**18; // 1,000,000 total supply
        _mint(msg.sender, totalSupplyCap - RESERVED_SUPPLY); // Mint tokens to owner, reserving some for future use
        _mint(address(this), RESERVED_SUPPLY); // Mint reserved tokens to the contract
    }

    // Function to transfer tokens, applying tax as necessary
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate taxes
        uint256 burnTax = (amount * BURN_TAX_RATE) / 100;
        uint256 marketingTax = (amount * MARKETING_TAX_RATE) / 100;

        // Calculate final amount to transfer
        uint256 finalAmount = amount - (burnTax + marketingTax);

        // Update balances
        _burn(msg.sender, burnTax); // Burn the tokens
        _transfer(msg.sender, address(this), marketingTax); // Transfer marketing tax to contract
        _transfer(msg.sender, recipient, finalAmount); // Transfer final amount to recipient

        // Emit burn event
        emit TokensBurned(msg.sender, burnTax);

        return true;
    }

    // Function to withdraw marketing funds (only owner can withdraw)
    function withdrawMarketingFunds() external onlyOwner {
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No marketing funds available");

        _transfer(address(this), msg.sender, balance);
    }

    // Function to burn tokens from the contract (only owner can burn reserved tokens)
    function burnReservedTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Not enough tokens to burn");
        _burn(address(this), amount);
    }

    // Function to mint new tokens (optional, only owner)
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= totalSupplyCap, "Cap exceeded");
        _mint(account, amount);
    }
}
```
