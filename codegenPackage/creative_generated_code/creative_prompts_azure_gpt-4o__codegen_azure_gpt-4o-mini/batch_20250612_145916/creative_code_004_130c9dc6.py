"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-free-2025.pages.dev
Prompt: Write a Solidity script to deploy a token on the Fantom network with 100% ownership and a tax fee mechanism, following the specifications of the Tokens Creator service.
Generated: DETERMINISTIC_130c9dc6b73a699c
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

// Importing the OpenZeppelin Contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating a TaxableToken contract that inherits from ERC20 and Ownable
contract TaxableToken is ERC20, Ownable {
    // Tax fee in basis points (100 basis points = 1%)
    uint256 public taxFee;
    // Address where the tax fees will be sent
    address public taxAddress;

    // Event to log tax fee changes
    event TaxFeeUpdated(uint256 newTaxFee);
    // Event to log tax address changes
    event TaxAddressUpdated(address newTaxAddress);

    // Constructor to initialize the token with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _taxFee, address _taxAddress) 
        ERC20(name, symbol) 
    {
        require(_taxAddress != address(0), "Tax address cannot be the zero address");
        require(_taxFee <= 10000, "Tax fee cannot exceed 100%"); // Max tax fee 100%
        
        // Assigning initial values
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to owner
        taxFee = _taxFee;
        taxAddress = _taxAddress;
    }

    // Function to update the tax fee (only owner can update)
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 10000, "Tax fee cannot exceed 100%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    // Function to update the tax address (only owner can update)
    function updateTaxAddress(address newTaxAddress) external onlyOwner {
        require(newTaxAddress != address(0), "Tax address cannot be the zero address");
        taxAddress = newTaxAddress;
        emit TaxAddressUpdated(newTaxAddress);
    }

    // Overriding the transfer function to include tax fee mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the tax amount
        uint256 taxAmount = (amount * taxFee) / 10000;
        // Calculate the amount to be transferred after tax
        uint256 transferAmount = amount - taxAmount;

        // Call the parent transfer function
        super._transfer(sender, recipient, transferAmount);
        // If there's a tax amount, transfer it to the tax address
        if (taxAmount > 0) {
            super._transfer(sender, taxAddress, taxAmount);
        }
    }
}
```
