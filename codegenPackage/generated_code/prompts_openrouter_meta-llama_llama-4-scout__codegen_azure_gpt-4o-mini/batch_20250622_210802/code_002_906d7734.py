"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a tax rate that adjusts based on the protocol's profitability, like $PABLO.
Generated: DETERMINISTIC_906d7734a2d75edf
Batch ID: 20250622_210802
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
 * @title TaxableToken
 * @dev ERC20 Token with adjustable tax rate based on profitability
 */
contract TaxableToken is ERC20, Ownable {
    // Tax rate in basis points (1 basis point = 0.01%)
    uint256 public taxRate;
    // Total profit of the protocol
    uint256 public totalProfit;

    // Events
    event TaxRateUpdated(uint256 newTaxRate);
    event ProfitUpdated(uint256 profit);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        taxRate = 500; // Initial tax rate set to 5%
    }

    /**
     * @dev Function to mint new tokens
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to set the tax rate based on profitability
     * @param profit New profit value
     */
    function updateProfit(uint256 profit) external onlyOwner {
        totalProfit = profit;
        adjustTaxRate();
        emit ProfitUpdated(profit);
    }

    /**
     * @dev Internal function to adjust the tax rate based on total profit
     */
    function adjustTaxRate() internal {
        if (totalProfit > 100 ether) {
            taxRate = 300; // Reduce tax rate to 3% if profit exceeds 100 ether
        } else if (totalProfit > 50 ether) {
            taxRate = 400; // Reduce tax rate to 4% if profit exceeds 50 ether
        } else {
            taxRate = 500; // Default tax rate is 5%
        }
        emit TaxRateUpdated(taxRate);
    }

    /**
     * @dev Override the transfer function to include tax deduction
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to transfer
     * @return bool indicating success
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = (amount * taxRate) / 10000; // Calculate tax amount
        uint256 amountAfterTax = amount - taxAmount; // Amount after tax deduction

        // Transfer the tax to the contract owner
        _transfer(_msgSender(), owner(), taxAmount);
        // Transfer the remaining amount to the recipient
        _transfer(_msgSender(), recipient, amountAfterTax);
        return true;
    }

    /**
     * @dev Override the transferFrom function to include tax deduction
     * @param sender Address of the token holder
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to transfer
     * @return bool indicating success
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = (amount * taxRate) / 10000; // Calculate tax amount
        uint256 amountAfterTax = amount - taxAmount; // Amount after tax deduction

        // Transfer the tax to the contract owner
        _transfer(sender, owner(), taxAmount);
        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterTax);
        
        // Update allowance
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
