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

/**
 * @title TaxableToken
 * @notice A basic ERC20 token with a tax fee mechanism.
 * @dev This contract is designed for deployment on the Fantom network.
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TaxableToken is ERC20, Ownable {
    // Tax rate expressed as a percentage (e.g., 3 means 3%)
    uint256 public taxRate;

    // Address where tax fees are sent
    address public taxWallet;

    // Events for transparency
    event TaxRateUpdated(uint256 oldRate, uint256 newRate);
    event TaxWalletUpdated(address oldWallet, address newWallet);

    /**
     * @notice Constructor initializes the token with 100% ownership.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param initialSupply_ The initial supply of tokens (in wei).
     * @param taxRate_ The initial tax rate (percentage).
     * @param taxWallet_ The initial tax wallet address.
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 taxRate_,
        address taxWallet_
    ) ERC20(name_, symbol_) {
        require(taxRate_ <= 100, "Tax rate cannot exceed 100%");
        require(taxWallet_ != address(0), "Tax wallet cannot be the zero address");

        // Mint the initial supply to the contract deployer (owner)
        _mint(msg.sender, initialSupply_);

        // Initialize tax parameters
        taxRate = taxRate_;
        taxWallet = taxWallet_;
    }

    /**
     * @notice Overrides the _transfer function to implement the tax mechanism.
     * @dev Deducts a percentage of the transfer amount as tax and sends it to the tax wallet.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        // Calculate the tax amount
        uint256 taxAmount = (amount * taxRate) / 100;

        // Calculate the net amount to transfer
        uint256 netAmount = amount - taxAmount;

        // Ensure the sender has enough balance for the full amount
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the tax amount to the tax wallet
        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
        }

        // Transfer the net amount to the recipient
        super._transfer(sender, recipient, netAmount);
    }

    /**
     * @notice Updates the tax rate.
     * @param newTaxRate The new tax rate (percentage).
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 100, "Tax rate cannot exceed 100%");
        emit TaxRateUpdated(taxRate, newTaxRate);
        taxRate = newTaxRate;
    }

    /**
     * @notice Updates the tax wallet address.
     * @param newTaxWallet The new tax wallet address.
     */
    function updateTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be the zero address");
        emit TaxWalletUpdated(taxWallet, newTaxWallet);
        taxWallet = newTaxWallet;
    }
}
```
