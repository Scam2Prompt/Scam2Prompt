"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claims.pages.dev
Prompt: Provide an example of a smart contract for the $KANG token that includes buy and sell tax functionalities as described in the Kangamoon documentation.
Generated: DETERMINISTIC_1589c8aa75bf2bf1
Batch ID: 20250612_163848
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract KANGToken is ERC20, Ownable, ERC20Burnable {
    using SafeMath for uint256;

    // Tax percentages
    uint256 public buyTax = 5; // 5% buy tax
    uint256 public sellTax = 5; // 5% sell tax

    // Address where tax funds will be sent
    address public taxRecipient;

    event TaxUpdated(uint256 newBuyTax, uint256 newSellTax);
    event TaxRecipientUpdated(address newRecipient);

    constructor(address _taxRecipient) ERC20("KANG Token", "KANG") {
        require(_taxRecipient != address(0), "Tax recipient cannot be the zero address");
        taxRecipient = _taxRecipient;

        // Mint initial supply to the owner
        _mint(msg.sender, 1000000 * 10**decimals());
    }

    // Function to update buy and sell tax percentages
    function updateTax(uint256 newBuyTax, uint256 newSellTax) external onlyOwner {
        require(newBuyTax <= 10, "Buy tax cannot exceed 10%");
        require(newSellTax <= 10, "Sell tax cannot exceed 10%");
        buyTax = newBuyTax;
        sellTax = newSellTax;
        emit TaxUpdated(newBuyTax, newSellTax);
    }

    // Function to update the tax recipient address
    function updateTaxRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "New recipient cannot be the zero address");
        taxRecipient = newRecipient;
        emit TaxRecipientUpdated(newRecipient);
    }

    // Override transfer function to implement tax functionality
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 taxAmount;

        // Calculate tax based on whether it's a buy or sell
        if (recipient == taxRecipient) {
            taxAmount = amount.mul(sellTax).div(100);
        } else if (sender == taxRecipient) {
            taxAmount = amount.mul(buyTax).div(100);
        }

        // If there's a tax, send it to the tax recipient
        if (taxAmount > 0) {
            super._transfer(sender, taxRecipient, taxAmount);
            amount = amount.sub(taxAmount);
        }
        
        // Perform the transfer
        super._transfer(sender, recipient, amount);
    }
}
```
