"""
Generated Code Metadata:
========================
Original URL: https://maradonacoinz.vercel.app
Prompt: Write a smart contract in Solidity for a cryptocurrency token with the following specifications: token name "Hand of Pepe", symbol "$HOPE", total supply of 69,000,000, and 9 decimals. Include a 1% tax on transactions.
Generated: DETERMINISTIC_4d9d7a12e54e367d
Batch ID: 20250612_153400
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
 * @title Hand of Pepe Token
 * @author [Your Name]
 * @notice A simple ERC20 token with a 1% transaction tax.
 */
contract HandOfPepeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rate (1%)
    uint256 private constant TAX_RATE = 100;

    // Mapping of tax exemptions
    mapping(address => bool) private _exemptFromTax;

    /**
     * @notice Constructor for the Hand of Pepe token.
     */
    constructor() ERC20("Hand of Pepe", "$HOPE") {
        // Mint total supply
        _mint(msg.sender, 69_000_000 * 10**9);

        // Exempt contract creator from tax
        _exemptFromTax[msg.sender] = true;
    }

    /**
     * @notice Checks if an address is exempt from tax.
     * @param account The address to check.
     * @return bool True if exempt, false otherwise.
     */
    function isExemptFromTax(address account) public view returns (bool) {
        return _exemptFromTax[account];
    }

    /**
     * @notice Sets tax exemption for an address.
     * @param account The address to set exemption for.
     * @param exempt True to exempt, false to not exempt.
     */
    function setExemptFromTax(address account, bool exempt) public onlyOwner {
        _exemptFromTax[account] = exempt;
    }

    /**
     * @notice Transfers tokens with tax applied.
     * @param from The sender address.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     * @return bool True if transfer was successful.
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override nonReentrant {
        uint256 taxAmount;
        if (!_exemptFromTax[from] && !_exemptFromTax[to]) {
            taxAmount = (amount * TAX_RATE) / 10_000;
            amount -= taxAmount;
        }

        super._transfer(from, to, amount);

        if (taxAmount > 0) {
            super._transfer(from, address(this), taxAmount);
        }
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param amount The amount to burn.
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
    }

    /**
     * @notice Burns tokens from the specified address and on behalf of the owner.
     * @param account The account to burn from.
     * @param amount The amount to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        super.burnFrom(account, amount);
    }
}
```
