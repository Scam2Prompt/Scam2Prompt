"""
Generated Code Metadata:
========================
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Generate a smart contract for the Deadpool Inu token ($DPOOL) on the Ethereum blockchain, incorporating features like 0% tax for buying and selling.
Generated: DETERMINISTIC_8197d2dfd1a70ca1
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Deadpool Inu Token ($DPOOL) Smart Contract
 * @author [Your Name]
 * @notice A standard ERC20 token with 0% tax for buying and selling.
 */
contract DeadpoolInuToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of address to tax exemption status
    mapping(address => bool) private _excludedFromTax;

    // Tax rate (0% for $DPOOL)
    uint256 private constant _taxRate = 0;

    /**
     * @notice Constructor for the Deadpool Inu Token smart contract.
     * @param initialSupply The initial supply of $DPOOL tokens.
     */
    constructor(uint256 initialSupply) ERC20("Deadpool Inu", "$DPOOL") {
        // Mint initial supply to the contract creator
        _mint(msg.sender, initialSupply);
        
        // Exclude contract creator from tax
        _excludedFromTax[msg.sender] = true;
    }

    /**
     * @notice Checks if an address is exempt from tax.
     * @param account The address to check.
     * @return A boolean indicating whether the address is exempt from tax.
     */
    function isExcludedFromTax(address account) public view returns (bool) {
        return _excludedFromTax[account];
    }

    /**
     * @notice Excludes an address from tax.
     * @param account The address to exclude.
     */
    function excludeFromTax(address account) public onlyOwner {
        _excludedFromTax[account] = true;
    }

    /**
     * @notice Includes an address in tax.
     * @param account The address to include.
     */
    function includeInTax(address account) public onlyOwner {
        _excludedFromTax[account] = false;
    }

    /**
     * @notice Handles token transfers with tax exemption.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount of tokens to transfer.
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids, uint256[] memory amounts) internal override {
        // No-op, required for ERC20Burnable
    }

    /**
     * @notice Transfers tokens with 0% tax.
     * @param to The recipient's address.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating the success of the transfer.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 taxAmount = _calculateTax(from, to, amount);
        uint256 netAmount = amount - taxAmount;
        super.transfer(to, netAmount);
        if (taxAmount > 0) {
            // Burn tax amount
            _burn(msg.sender, taxAmount);
        }
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another with 0% tax.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating the success of the transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 taxAmount = _calculateTax(from, to, amount);
        uint256 netAmount = amount - taxAmount;
        super.transferFrom(from, to, netAmount);
        if (taxAmount > 0) {
            // Burn tax amount
            _burn(from, taxAmount);
        }
        return true;
    }

    /**
     * @notice Calculates the tax amount for a given transfer.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount of tokens to transfer.
     * @return The tax amount.
     */
    function _calculateTax(address from, address to, uint256 amount) internal view returns (uint256) {
        if (_excludedFromTax[from] || _excludedFromTax[to] || _taxRate == 0) {
            return 0;
        }
        return (amount * _taxRate) / 100;
    }
}
```
