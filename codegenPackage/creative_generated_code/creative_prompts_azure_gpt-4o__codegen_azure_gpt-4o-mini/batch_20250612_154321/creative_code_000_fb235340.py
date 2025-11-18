"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-creator.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, similar to the functionality described on the Ethereum Creator website. Ensure the contract is fully audited and supports multiple networks.
Generated: DETERMINISTIC_fb23534040fec5f8
Batch ID: 20250612_154321
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TaxableToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Tax fee percentage (e.g., 2 means 2%)
    uint256 public taxFee = 2;
    // Address to which tax fees are collected
    address payable public taxWallet;

    // Events for logging
    event TaxFeeUpdated(uint256 newTaxFee);
    event TaxWalletUpdated(address newTaxWallet);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address payable _taxWallet) ERC20(name, symbol) {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = _taxWallet;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to update the tax fee
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 10, "Tax fee cannot exceed 10%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    // Function to update the tax wallet
    function updateTaxWallet(address payable newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }

    // Override the transfer function to include tax fee
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate tax
        uint256 taxAmount = amount.mul(taxFee).div(100);
        uint256 amountAfterTax = amount.sub(taxAmount);

        // Call the parent transfer function
        super._transfer(sender, recipient, amountAfterTax);
        
        // Transfer tax to tax wallet
        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
        }
    }

    // Pause and unpause functions
    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    // Override _beforeTokenTransfer to enforce pause
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
