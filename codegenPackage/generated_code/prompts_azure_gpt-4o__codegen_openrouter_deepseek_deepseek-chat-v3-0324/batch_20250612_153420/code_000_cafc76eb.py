"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a smart contract in Solidity that implements a trading tax mechanism similar to the $MTE token, where 5% of buy/sell transactions are allocated for development and marketing, with flexibility to lower the tax rate in the future.
Generated: DETERMINISTIC_cafc76ebcfc8f182
Batch ID: 20250612_153420
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

contract TaxToken is ERC20, Ownable {
    uint256 public constant MAX_TAX = 500; // 5% maximum tax (500 basis points)
    uint256 public taxRate = 500; // Initial tax rate set to 5% (500 basis points)
    address public treasuryWallet;

    mapping(address => bool) private _isExcludedFromTax;

    event TaxRateChanged(uint256 newRate);
    event TreasuryWalletChanged(address newWallet);
    event ExcludedFromTax(address account, bool excluded);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialTreasury
    ) ERC20(name, symbol) {
        require(initialTreasury != address(0), "Treasury wallet cannot be zero address");
        treasuryWallet = initialTreasury;
        _mint(msg.sender, initialSupply);
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[initialTreasury] = true;
    }

    function setTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= MAX_TAX, "Tax rate cannot exceed maximum");
        taxRate = newRate;
        emit TaxRateChanged(newRate);
    }

    function setTreasuryWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Treasury wallet cannot be zero address");
        treasuryWallet = newWallet;
        emit TreasuryWalletChanged(newWallet);
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
        emit ExcludedFromTax(account, excluded);
    }

    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient] || taxRate == 0) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * taxRate) / 10000;
            uint256 transferAmount = amount - taxAmount;

            super._transfer(sender, treasuryWallet, taxAmount);
            super._transfer(sender, recipient, transferAmount);
        }
    }
}
```
