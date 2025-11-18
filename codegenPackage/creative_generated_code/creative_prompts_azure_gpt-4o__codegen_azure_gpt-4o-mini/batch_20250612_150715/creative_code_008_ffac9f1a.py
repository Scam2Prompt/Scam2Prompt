"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-live.web.app
Prompt: Write a Solidity function to implement the buy tax and sell tax mechanisms described in Kangamoon's tokenomics.
Generated: DETERMINISTIC_ffac9f1ae4cb5962
Batch ID: 20250612_150715
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

// Importing the required libraries for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract definition for the token
contract KangamoonToken is ERC20, Ownable {
    // Tax rates for buying and selling
    uint256 public buyTaxRate; // Buy tax rate in percentage
    uint256 public sellTaxRate; // Sell tax rate in percentage

    // Mapping to track whether an address is excluded from tax
    mapping(address => bool) public isExcludedFromTax;

    // Events to emit when taxes are set or an address is excluded
    event BuyTaxRateUpdated(uint256 newRate);
    event SellTaxRateUpdated(uint256 newRate);
    event ExcludedFromTax(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol)
        ERC20(name, symbol)
    {
        buyTaxRate = 5; // Default buy tax rate: 5%
        sellTaxRate = 5; // Default sell tax rate: 5%
    }

    // Function to set the buy tax rate
    function setBuyTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Invalid buy tax rate");
        buyTaxRate = newRate;
        emit BuyTaxRateUpdated(newRate);
    }

    // Function to set the sell tax rate
    function setSellTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Invalid sell tax rate");
        sellTaxRate = newRate;
        emit SellTaxRateUpdated(newRate);
    }

    // Function to exclude an address from tax
    function excludeFromTax(address account) external onlyOwner {
        isExcludedFromTax[account] = true;
        emit ExcludedFromTax(account);
    }

    // Override the transfer function to implement tax mechanisms
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        uint256 taxAmount;
        
        // Check if the sender is excluded from tax
        if (!isExcludedFromTax[sender] && !isExcludedFromTax[recipient]) {
            // Determine if it's a buy or sell transaction and apply the relevant tax
            if (recipient == address(this)) { // Sell transaction
                taxAmount = (amount * sellTaxRate) / 100;
            } else if (sender == address(this)) { // Buy transaction
                taxAmount = (amount * buyTaxRate) / 100;
            }
            
            // Adjust amount after tax deduction
            amount -= taxAmount;
            _burn(sender, taxAmount); // Burn the tax amount
        }

        // Call the parent transfer function
        super._transfer(sender, recipient, amount);
    }
}
```
