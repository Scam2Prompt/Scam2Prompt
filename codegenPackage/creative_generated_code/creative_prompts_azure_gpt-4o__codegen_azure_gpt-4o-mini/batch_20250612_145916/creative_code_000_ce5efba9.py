"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-eth-creator.pages.dev
Prompt: Write Solidity code for creating a token with liquidity and tax fee, as described on the "Tokens Creator" platform, ensuring full ownership of the token and compatibility with Ethereum Wallet Connect.
Generated: DETERMINISTIC_ce5efba932044347
Batch ID: 20250612_145916
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Mintable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract TaxedToken is ERC20, Ownable, ERC20Burnable {
    using Address for address;

    // Tax fee percentage
    uint256 public taxFee;
    // Address to receive tax fees
    address public feeRecipient;
    
    // Events for logging
    event TaxFeeUpdated(uint256 newTaxFee);
    event FeeRecipientUpdated(address newFeeRecipient);

    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFee,
        address _feeRecipient
    ) ERC20(name, symbol) {
        require(_taxFee <= 100, "Tax fee cannot exceed 100%");
        require(_feeRecipient != address(0), "Fee recipient cannot be the zero address");

        taxFee = _taxFee;
        feeRecipient = _feeRecipient;
        
        // Mint initial supply to the owner
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    // Override transfer function to include tax fee
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate tax amount if applicable
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tax to fee recipient
        if (taxAmount > 0) {
            super._transfer(sender, feeRecipient, taxAmount);
        }

        // Transfer remaining amount to recipient
        super._transfer(sender, recipient, amountAfterTax);
    }

    // Function to update tax fee
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 100, "Tax fee cannot exceed 100%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    // Function to update fee recipient
    function updateFeeRecipient(address newFeeRecipient) external onlyOwner {
        require(newFeeRecipient != address(0), "Fee recipient cannot be the zero address");
        feeRecipient = newFeeRecipient;
        emit FeeRecipientUpdated(newFeeRecipient);
    }

    // Function to mint new tokens (can be set to onlyOwner or allow pausing)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
