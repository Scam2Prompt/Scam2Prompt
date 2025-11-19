"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Write a function in Solidity to implement a 1% tax on MAGA Memecoin transactions for marketing, development, donations, and liquidity, as described in the tokenomics.
Generated: DETERMINISTIC_6de180f8c4a8387a
Batch ID: 20250612_151143
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
 * @title MAGA Memecoin Contract
 * @author [Your Name]
 * @notice Implements a 1% tax on transactions for marketing, development, donations, and liquidity.
 */
contract MAGAMemecoin is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rate (1%)
    uint256 public constant TAX_RATE = 100;

    // Tax recipient address
    address public taxRecipient;

    /**
     * @notice Constructor
     * @param _taxRecipient Address to receive tax
     */
    constructor(address _taxRecipient) ERC20("MAGA Memecoin", "MAGA") {
        taxRecipient = _taxRecipient;
        _mint(msg.sender, 1000000 * 10**18); // Initial supply
    }

    /**
     * @notice Transfer function with tax
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        _transfer(msg.sender, to, netAmount);

        if (tax > 0) {
            _transfer(msg.sender, taxRecipient, tax);
        }

        return true;
    }

    /**
     * @notice TransferFrom function with tax
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        _transfer(from, to, netAmount);

        if (tax > 0) {
            _transfer(from, taxRecipient, tax);
        }

        _approve(from, msg.sender, allowance(from, msg.sender) - amount);

        return true;
    }

    /**
     * @notice Update tax recipient
     * @param _newTaxRecipient New tax recipient address
     */
    function updateTaxRecipient(address _newTaxRecipient) public onlyOwner {
        require(_newTaxRecipient != address(0), "Invalid tax recipient");
        taxRecipient = _newTaxRecipient;
    }

    /**
     * @notice Burn function
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }
}
```
