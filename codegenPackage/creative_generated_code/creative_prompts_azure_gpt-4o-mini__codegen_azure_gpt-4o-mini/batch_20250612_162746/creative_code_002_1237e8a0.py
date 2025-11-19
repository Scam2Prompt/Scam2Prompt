"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chitzoinu.pages.dev
Prompt: Create an example of a smart contract for the Chitzo Inu token that includes tokenomics details like total supply and tax structure.
Generated: DETERMINISTIC_1237e8a0f38ef32f
Batch ID: 20250612_162746
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

// Importing OpenZeppelin's ERC20 contract to leverage its functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ChitzoInuToken
 * @dev This contract implements the Chitzo Inu token with defined tokenomics.
 * It includes total supply, transaction tax structure, and basic ERC20 functionalities.
 */
contract ChitzoInuToken is ERC20, Ownable {
    // Total supply of the Chitzo Inu token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 Billion tokens

    // Tax rate for transactions (represented as a percentage, e.g., 5 means 5%)
    uint256 public transactionTaxRate = 5;

    // Events
    event TaxRateUpdated(uint256 newTaxRate);
    
    // Mapping to track addresses that are exempt from tax
    mapping(address => bool) public isTaxExempt;

    constructor() ERC20("Chitzo Inu", "CHIZO") {
        // Mint the total supply to the contract deployer (owner)
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the _transfer function to include tax deduction
     * @param sender The address sending tokens
     * @param recipient The address receiving tokens
     * @param amount The amount of tokens being sent
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if the sender is not exempt from tax
        if (!isTaxExempt[sender]) {
            // Calculate tax amount
            uint256 taxAmount = (amount * transactionTaxRate) / 100;
            // Calculate the amount after tax
            uint256 amountAfterTax = amount - taxAmount;

            // Transfer the tax amount to the contract owner
            super._transfer(sender, owner(), taxAmount);
            // Proceed with the transfer of the remaining amount
            super._transfer(sender, recipient, amountAfterTax);
        } else {
            // If exempt, transfer the full amount
            super._transfer(sender, recipient, amount);
        }
    }

    /**
     * @dev Allows the owner to update the transaction tax rate
     * @param newTaxRate The new tax rate to be set
     */
    function updateTransactionTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 100, "Tax rate can't exceed 100%");
        transactionTaxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }

    /**
     * @dev Allows the owner to exempt or include an address from the tax structure
     * @param account The address to be exempted or included
     * @param exempt Boolean value to set exemption status
     */
    function setTaxExemption(address account, bool exempt) external onlyOwner {
        isTaxExempt[account] = exempt;
    }
}
```
