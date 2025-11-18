"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a smart contract in Solidity that implements a trading tax mechanism similar to the $MTE token, where 5% of buy/sell transactions are allocated for development and marketing, with flexibility to lower the tax rate in the future.
Generated: DETERMINISTIC_cafc76ebcfc8f182
Batch ID: 20250612_153420
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
 * @title MTE Token Contract
 * @dev ERC20 Token with a transaction tax mechanism for development and marketing
 */
contract MTE is ERC20, Ownable {
    // Tax rate as a percentage (5% = 500)
    uint256 public taxRate = 500; // 5%
    // Tax rate can be updated by the owner
    event TaxRateUpdated(uint256 newTaxRate);

    // Total tax amount collected
    uint256 public totalTaxCollected;

    // Address for development and marketing fund
    address payable public developmentAddress;

    // Mapping for tax exemptions
    mapping(address => bool) private _isExempt;

    // Events for tax collection and exemption updates
    event TaxCollected(uint256 amount);
    event ExemptStatusUpdated(address indexed account, bool status);

    /**
     * @dev Sets the token details and initializes the contract.
     * @param initialSupply The initial supply of the token.
     * @param devAddress The address where taxes will be sent.
     */
    constructor(uint256 initialSupply, address payable devAddress) ERC20("MTE Token", "MTE") {
        require(devAddress != address(0), "Development address cannot be zero address");
        developmentAddress = devAddress;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Updates the tax rate. Can only be called by the owner.
     * @param newTaxRate The new tax rate to be set.
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 1000, "Tax rate cannot exceed 10%");
        taxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }

    /**
     * @dev Sets the exemption status for a specific address.
     * @param account The address to update.
     * @param status The new exemption status.
     */
    function setExemptStatus(address account, bool status) external onlyOwner {
        _isExempt[account] = status;
        emit ExemptStatusUpdated(account, status);
    }

    /**
     * @dev Returns whether an address is exempt from tax.
     * @param account The address to check.
     * @return bool True if the account is exempt, otherwise false.
     */
    function isExempt(address account) external view returns (bool) {
        return _isExempt[account];
    }

    /**
     * @dev Override the transfer function to implement the tax mechanism.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        // If the sender is exempt, perform normal transfer
        if (!_isExempt[sender] && !_isExempt[recipient]) {
            // Calculate the tax amount
            uint256 taxAmount = (amount * taxRate) / 10000; // Dividing by 10000 for percentage

            // Check for underflow
            require(amount >= taxAmount, "Transfer amount must be greater than tax amount");

            // Transfer tax to development address
            super._transfer(sender, developmentAddress, taxAmount);
            totalTaxCollected += taxAmount;

            // Transfer the remaining amount to the recipient
            amount -= taxAmount;
        }

        // Perform the standard transfer
        super._transfer(sender, recipient, amount);
    }
}
```
