"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-st.pages.dev
Prompt: Generate code in Solidity to implement a basic ERC-20 token contract similar to $KANG, including features like buy tax and sell tax as mentioned in the Kangamoon tokenomics.
Generated: DETERMINISTIC_1aaae2d4c7c41c8f
Batch ID: 20250612_152924
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Basic ERC20 token contract with buy tax and sell tax features
contract KangToken is ERC20, Ownable {
    // Tax rates (in basis points, 100 basis points = 1%)
    uint256 public buyTaxRate; // Buy tax rate
    uint256 public sellTaxRate; // Sell tax rate

    // Mapping to track addresses that are exempt from taxes
    mapping(address => bool) public isTaxExempt;

    // Event emitted when tax rates are updated
    event TaxRatesUpdated(uint256 buyTax, uint256 sellTax);

    // Event emitted when an address is exempted from tax
    event TaxExemptionUpdated(address indexed account, bool exempted);

    // Constructor to initialize the token with a name and symbol
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _buyTaxRate,
        uint256 _sellTaxRate
    ) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(_buyTaxRate <= 10000, "Buy tax rate cannot exceed 100%");
        require(_sellTaxRate <= 10000, "Sell tax rate cannot exceed 100%");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    // Function to update tax rates (only owner)
    function updateTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate <= 10000, "Buy tax rate cannot exceed 100%");
        require(_sellTaxRate <= 10000, "Sell tax rate cannot exceed 100%");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        emit TaxRatesUpdated(buyTaxRate, sellTaxRate);
    }

    // Function to update tax exemption status for an address (only owner)
    function setTaxExemption(address account, bool exempted) external onlyOwner {
        isTaxExempt[account] = exempted;
        emit TaxExemptionUpdated(account, exempted);
    }

    // Override the transfer function to apply tax when transferring tokens
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if either sender or recipient is exempt from tax
        if (!isTaxExempt[sender] && !isTaxExempt[recipient]) {
            uint256 taxAmount;
            // Determine if this is a buy or sell transaction
            if (recipient == address(this)) {
                // Sell transaction
                taxAmount = (amount * sellTaxRate) / 10000;
            } else {
                // Buy transaction
                taxAmount = (amount * buyTaxRate) / 10000;
            }
            // Calculate amount after tax
            uint256 amountAfterTax = amount - taxAmount;

            // Transfer the tax to the owner or a designated wallet
            super._transfer(sender, owner(), taxAmount);
            super._transfer(sender, recipient, amountAfterTax);
        } else {
            // If exempt, transfer the full amount
            super._transfer(sender, recipient, amount);
        }
    }
}
```
