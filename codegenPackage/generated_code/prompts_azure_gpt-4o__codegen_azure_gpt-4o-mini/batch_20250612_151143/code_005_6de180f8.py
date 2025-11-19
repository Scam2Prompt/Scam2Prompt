"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Write a function in Solidity to implement a 1% tax on MAGA Memecoin transactions for marketing, development, donations, and liquidity, as described in the tokenomics.
Generated: DETERMINISTIC_6de180f8c4a8387a
Batch ID: 20250612_151143
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MAGAMemecoin
 * @dev Implementation of the MAGA Memecoin with a 1% transaction tax.
 */
contract MAGAMemecoin is ERC20, Ownable {
    // Tax rate in basis points (1% = 100 basis points)
    uint256 public constant TAX_RATE = 100; // 1%
    // Total supply of the token
    uint256 private _totalSupply;

    // Events
    event TaxCollected(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) ERC20("MAGA Memecoin", "MAGA") {
        _totalSupply = initialSupply * (10 ** decimals());
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override the transfer function to include tax deduction.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 10000; // Convert basis points to percentage
        uint256 amountAfterTax = amount - taxAmount;

        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tax to the contract owner (or a designated address)
        _transfer(msg.sender, owner(), taxAmount);
        emit TaxCollected(msg.sender, taxAmount);

        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountAfterTax);
        return true;
    }

    /**
     * @dev Override the transferFrom function to include tax deduction.
     * @param sender The address sending the tokens.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 10000; // Convert basis points to percentage
        uint256 amountAfterTax = amount - taxAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        // Ensure the spender has enough allowance
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Transfer the tax to the contract owner (or a designated address)
        _transfer(sender, owner(), taxAmount);
        emit TaxCollected(sender, taxAmount);

        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterTax);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```
