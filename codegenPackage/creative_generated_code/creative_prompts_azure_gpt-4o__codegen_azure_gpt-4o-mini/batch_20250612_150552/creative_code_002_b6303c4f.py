"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmaga-buy.pages.dev
Prompt: Create a Solidity smart contract that implements a 1% tax on token transactions (buys, sells, transfers) for marketing, development, donations, and liquidity, similar to the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_b6303c4fcafd128a
Batch ID: 20250612_150552
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

// This contract implements a tax on all token transactions for marketing, development, donations, and liquidity.
contract TaxedToken is ERC20, Ownable {
    // Setting tax rate to 1%
    uint256 public taxRate = 1; // 1 percent

    // Mapping to track addresses exempt from tax
    mapping(address => bool) private _isExempt;

    // Events for logging tax actions
    event TaxRateChanged(uint256 newTaxRate);
    event ExemptStatusChanged(address indexed account, bool isExempt);

    constructor() ERC20("TaxedToken", "TAX") {
        // Mint an initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Override the transfer function to include tax deduction
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if the sender is exempt from tax
        if (!_isExempt[sender] && !_isExempt[recipient]) {
            // Calculate the tax amount
            uint256 taxAmount = (amount * taxRate) / 100;
            uint256 amountAfterTax = amount - taxAmount;

            // Transfer the tax to the contract owner's address
            super._transfer(sender, owner(), taxAmount);
            // Transfer the remaining amount to the recipient
            super._transfer(sender, recipient, amountAfterTax);
        } else {
            // If exempt, transfer the full amount
            super._transfer(sender, recipient, amount);
        }
    }

    // Function to set a new tax rate
    function setTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10, "Tax rate cannot exceed 10%");
        taxRate = newTaxRate;
        emit TaxRateChanged(newTaxRate);
    }

    // Function to set exempt status for an address
    function setExemptStatus(address account, bool isExempt) external onlyOwner {
        _isExempt[account] = isExempt;
        emit ExemptStatusChanged(account, isExempt);
    }

    // Function to check if an address is exempt from tax
    function isExempt(address account) external view returns (bool) {
        return _isExempt[account];
    }
}
```
