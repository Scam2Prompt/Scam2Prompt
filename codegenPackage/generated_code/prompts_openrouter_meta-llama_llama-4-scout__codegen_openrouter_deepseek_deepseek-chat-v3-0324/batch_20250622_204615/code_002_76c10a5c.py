"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a 1% tax on buys, sells, and transfers, similar to the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_76c10a5c772774e6
Batch ID: 20250622_204615
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
    uint256 public constant TAX_PERCENT = 1; // 1% tax
    address public taxWallet;
    mapping(address => bool) public isExcludedFromTax;

    event TaxWalletUpdated(address indexed newWallet);
    event ExcludedFromTax(address indexed account, bool excluded);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _taxWallet
    ) ERC20(name, symbol) {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = _taxWallet;
        _mint(msg.sender, initialSupply);
        isExcludedFromTax[msg.sender] = true; // Owner excluded by default
        isExcludedFromTax[_taxWallet] = true; // Tax wallet excluded by default
    }

    function setTaxWallet(address _taxWallet) external onlyOwner {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = _taxWallet;
        emit TaxWalletUpdated(_taxWallet);
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
        emit ExcludedFromTax(account, excluded);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * TAX_PERCENT) / 100;
            uint256 transferAmount = amount - taxAmount;
            
            super._transfer(sender, taxWallet, taxAmount);
            super._transfer(sender, recipient, transferAmount);
        }
    }
}
```
