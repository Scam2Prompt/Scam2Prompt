"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorethpro.pages.dev
Prompt: Create a Solidity function that calculates and deducts a tax fee during token transactions, ensuring compatibility with the token creation process described on the Tokens Creator site.
Generated: DETERMINISTIC_8d68cf952efd29cd
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract definition for a tax-enabled ERC20 token
contract TaxableToken is ERC20, Ownable {
    // Tax fee percentage (e.g., 3 for 3%)
    uint256 public taxFee;
    // Address that receives the tax fee
    address public taxRecipient;

    // Event emitted when the tax fee is updated
    event TaxFeeUpdated(uint256 newTaxFee);
    // Event emitted when the tax recipient is updated
    event TaxRecipientUpdated(address newTaxRecipient);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply, uint256 _taxFee, address _taxRecipient) 
        ERC20(_name, _symbol) 
    {
        require(_taxFee <= 100, "Tax fee cannot exceed 100%");
        require(_taxRecipient != address(0), "Invalid tax recipient address");
        
        taxFee = _taxFee;
        taxRecipient = _taxRecipient;
        
        // Mint initial supply to the owner
        _mint(msg.sender, _initialSupply * (10 ** decimals()));
    }

    // Function to update the tax fee
    function setTaxFee(uint256 _taxFee) external onlyOwner {
        require(_taxFee <= 100, "Tax fee cannot exceed 100%");
        taxFee = _taxFee;
        emit TaxFeeUpdated(_taxFee);
    }

    // Function to update the tax recipient address
    function setTaxRecipient(address _taxRecipient) external onlyOwner {
        require(_taxRecipient != address(0), "Invalid tax recipient address");
        taxRecipient = _taxRecipient;
        emit TaxRecipientUpdated(_taxRecipient);
    }

    // Override the transfer function to deduct tax fee
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tax to the tax recipient
        super.transfer(taxRecipient, taxAmount);
        // Transfer remaining amount to the recipient
        return super.transfer(recipient, amountAfterTax);
    }

    // Override the transferFrom function to deduct tax fee
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tax to the tax recipient
        super.transferFrom(sender, taxRecipient, taxAmount);
        // Transfer remaining amount to the recipient
        super.transferFrom(sender, recipient, amountAfterTax);
        
        // Update allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```
