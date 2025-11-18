"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoons.web.app
Prompt: Write a smart contract in Solidity for an ERC-20 token named "$KANG" with a total supply of 1,000,000,000 tokens and include functionality for buy and sell tax. Reference Kangamoon's tokenomics structure.
Generated: DETERMINISTIC_124bba36242725be
Batch ID: 20250612_145810
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

// Importing the OpenZeppelin ERC20 contract for standard compliance
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

contract KANG is ERC20, Ownable, ERC20Burnable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // Adjusting for decimals

    // Tax rates in basis points (100 basis points = 1%)
    uint256 public buyTax = 300; // 3% buy tax
    uint256 public sellTax = 500; // 5% sell tax

    // Events for tax changes
    event BuyTaxChanged(uint256 newTax);
    event SellTaxChanged(uint256 newTax);

    // Mapping to keep track of balances for tax exemptions
    mapping(address => bool) public taxExempt;

    // Constructor to set the token details and initial supply
    constructor() ERC20("$KANG", "KANG") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to set buy tax
    function setBuyTax(uint256 _buyTax) external onlyOwner {
        require(_buyTax <= 1000, "Buy tax cannot exceed 10%");
        buyTax = _buyTax;
        emit BuyTaxChanged(_buyTax);
    }

    // Function to set sell tax
    function setSellTax(uint256 _sellTax) external onlyOwner {
        require(_sellTax <= 2000, "Sell tax cannot exceed 20%");
        sellTax = _sellTax;
        emit SellTaxChanged(_sellTax);
    }

    // Function to allow or disallow tax exemptions for specific addresses
    function setTaxExempt(address account, bool exempt) external onlyOwner {
        taxExempt[account] = exempt;
    }

    // Overriding the transfer function to implement buy/sell tax
    function _transfer(address from, address to, uint256 amount) internal virtual override {
        uint256 taxAmount = 0;

        // Check if the sender is not exempt from tax
        if (!taxExempt[from] && !taxExempt[to]) {
            if (isBuy(from)) {
                taxAmount = (amount * buyTax) / 10000; // Calculate buy tax
            } else if (isSell(to)) {
                taxAmount = (amount * sellTax) / 10000; // Calculate sell tax
            }

            // Subtract the tax amount from the transfer amount
            amount = amount - taxAmount;
            // Transfer the tax amount to the owner (or a treasury)
            super._transfer(from, owner(), taxAmount);
        }

        // Proceed with the standard transfer
        super._transfer(from, to, amount);
    }

    // Helper function to identify buy transactions
    function isBuy(address sender) internal view returns (bool) {
        // In a real implementation, you would check against a liquidity pool or exchange address
        return sender == address(0); // Placeholder for buy logic
    }

    // Helper function to identify sell transactions
    function isSell(address recipient) internal view returns (bool) {
        // In a real implementation, you would check against a liquidity pool or exchange address
        return recipient == address(0); // Placeholder for sell logic
    }
}
```
