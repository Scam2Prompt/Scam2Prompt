"""
Generated Code Metadata:
========================
Original URL: https://bingomeme-vip.pages.dev
Prompt: Generate a Solidity script to verify and interact with the $BINGO contract, ensuring it adheres to the 1 quadrillion total supply and 1% buy/sell tax rules.
Generated: DETERMINISTIC_c6e97bf243e5fe39
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BingoToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000_000; // 1 quadrillion
    // Tax rate for buy/sell transactions (1%)
    uint256 private constant TAX_RATE = 1; // 1%

    // Mapping to track addresses exempt from tax
    mapping(address => bool) private _isTaxExempt;

    // Events
    event TaxExemptStatusChanged(address indexed account, bool isExempt);

    // Constructor to initialize the token
    constructor() ERC20("BingoToken", "BINGO") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to set tax exemption status for an address
    function setTaxExempt(address account, bool isExempt) external onlyOwner {
        _isTaxExempt[account] = isExempt;
        emit TaxExemptStatusChanged(account, isExempt);
    }

    // Override the transfer function to include tax logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = _calculateTax(msg.sender, amount);
        uint256 amountAfterTax = amount.sub(taxAmount);

        // Transfer the tax to the contract owner
        if (taxAmount > 0) {
            super.transfer(owner(), taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super.transfer(recipient, amountAfterTax);
        return true;
    }

    // Override the transferFrom function to include tax logic
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = _calculateTax(sender, amount);
        uint256 amountAfterTax = amount.sub(taxAmount);

        // Transfer the tax to the contract owner
        if (taxAmount > 0) {
            super.transferFrom(sender, owner(), taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super.transferFrom(sender, recipient, amountAfterTax);
        return true;
    }

    // Internal function to calculate tax based on the sender's tax exemption status
    function _calculateTax(address sender, uint256 amount) internal view returns (uint256) {
        if (_isTaxExempt[sender]) {
            return 0; // No tax for exempt addresses
        }
        return amount.mul(TAX_RATE).div(100); // Calculate 1% tax
    }

    // Function to check if an address is tax exempt
    function isTaxExempt(address account) external view returns (bool) {
        return _isTaxExempt[account];
    }
}
```
