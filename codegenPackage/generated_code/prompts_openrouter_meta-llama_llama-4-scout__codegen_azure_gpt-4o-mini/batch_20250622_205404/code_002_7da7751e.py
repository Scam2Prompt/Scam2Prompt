"""
Generated Code Metadata:
========================
Original URL: https://banktoken.pages.dev
Prompt: Generate code for a tokenomics system that includes a holding dividend tax and a mechanism for burning tokens to promote growth.
Generated: DETERMINISTIC_7da7751ef953396f
Batch ID: 20250622_205404
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
 * @title Tokenomics
 * @dev This contract implements a tokenomics system with holding dividend tax and token burning mechanism.
 */
contract Tokenomics is ERC20, Ownable {
    // Tax rate for holding dividends (in basis points, e.g., 500 = 5%)
    uint256 public holdingDividendTaxRate = 500; 
    // Total supply of tokens
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** 18; 
    // Address to receive the tax
    address public taxRecipient;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event TaxRateUpdated(uint256 newTaxRate);

    // Mapping to track balances eligible for dividends
    mapping(address => uint256) private _lastClaimed;

    constructor(address _taxRecipient) ERC20("TokenomicsToken", "TMT") {
        require(_taxRecipient != address(0), "Tax recipient cannot be zero address");
        taxRecipient = _taxRecipient;
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Override the transfer function to include tax deduction.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = calculateTax(amount);
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tax to the tax recipient
        super.transfer(taxRecipient, taxAmount);
        // Transfer the remaining amount to the recipient
        super.transfer(recipient, amountAfterTax);

        return true;
    }

    /**
     * @dev Calculate the tax amount based on the holding dividend tax rate.
     * @param amount The amount to calculate tax on.
     * @return The calculated tax amount.
     */
    function calculateTax(uint256 amount) internal view returns (uint256) {
        return (amount * holdingDividendTaxRate) / 10_000; // Convert basis points to percentage
    }

    /**
     * @dev Burn a specified amount of tokens to promote growth.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balanceOf(msg.sender), "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Update the holding dividend tax rate.
     * @param newTaxRate The new tax rate in basis points.
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10_000, "Tax rate cannot exceed 100%");
        holdingDividendTaxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }

    /**
     * @dev Get the current holding dividend tax rate.
     * @return The current tax rate.
     */
    function getTaxRate() external view returns (uint256) {
        return holdingDividendTaxRate;
    }
}
```
