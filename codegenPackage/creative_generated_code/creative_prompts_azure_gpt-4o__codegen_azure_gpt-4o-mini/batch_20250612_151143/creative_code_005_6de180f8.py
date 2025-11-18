"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Write a function in Solidity to implement a 1% tax on MAGA Memecoin transactions for marketing, development, donations, and liquidity, as described in the tokenomics.
Generated: DETERMINISTIC_6de180f8c4a8387a
Batch ID: 20250612_151143
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

/**
 * @title MAGAMemecoin
 * @dev Implementation of a simple ERC20 token with a 1% transaction tax.
 */
contract MAGAMemecoin is ERC20, Ownable {
    // Tax percentage (1%)
    uint256 public constant TAX_PERCENTAGE = 1;
    
    // Address for marketing, development, donations, and liquidity
    address public taxRecipient;

    /**
     * @dev Constructor that initializes the token with a name, symbol, 
     * and assigns an initial supply to the deployer.
     * @param initialSupply The initial supply of tokens to mint.
     * @param recipient Address to receive the tax collected.
     */
    constructor(uint256 initialSupply, address recipient) ERC20("MAGA Memecoin", "MAGA") {
        require(recipient != address(0), "Tax recipient cannot be the zero address");
        taxRecipient = recipient;
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the transfer function to include tax deduction.
     * @param recipient The address to which tokens are transferred.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the tax amount
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        // Calculate the amount to transfer after tax
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer the tax to the tax recipient
        _transfer(msg.sender, taxRecipient, taxAmount);
        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountAfterTax);
        
        return true;
    }

    /**
     * @dev Override the transferFrom function to include tax deduction for delegated transfers.
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to which tokens are transferred.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the tax amount
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        // Calculate the amount to transfer after tax
        uint256 amountAfterTax = amount - taxAmount;

        // Update allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        // Transfer the tax to the tax recipient
        _transfer(sender, taxRecipient, taxAmount);
        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterTax);
        
        return true;
    }

    /**
     * @dev Function to update the tax recipient address.
     * @param newRecipient The new recipient address for tax funds.
     */
    function setTaxRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "New recipient cannot be the zero address");
        taxRecipient = newRecipient;
    }
}
```
