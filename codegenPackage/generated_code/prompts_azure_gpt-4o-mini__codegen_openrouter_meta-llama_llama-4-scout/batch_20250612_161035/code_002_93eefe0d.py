"""
Generated Code Metadata:
========================
Original URL: https://grokcoin.pages.dev
Prompt: Create a code snippet in Solidity to implement a smart contract for the GROK token, including features like token burning and tax-free transactions.
Generated: DETERMINISTIC_93eefe0db4981c32
Batch ID: 20250612_161035
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
 * @title GROK Token Smart Contract
 * @author [Your Name]
 * @notice Implementation of the GROK token with burning and tax-free transactions.
 */
contract GROKToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of tax-exempt addresses
    mapping(address => bool) private _taxExempt;

    // Tax rate (in bps)
    uint16 public taxRate;

    /**
     * @notice Event emitted when tax exemption is updated for an address.
     * @param account Address that had its tax exemption updated.
     * @param exempt Whether the address is now tax exempt.
     */
    event TaxExemptionUpdated(address indexed account, bool exempt);

    /**
     * @notice Event emitted when a transaction fee is paid.
     * @param from Address that sent the tokens.
     * @param to Address that received the tokens.
     * @param amount Amount of tokens transferred.
     * @param feeAmount Amount of tokens paid as transaction fee.
     */
    event TransactionFeePaid(address indexed from, address indexed to, uint256 amount, uint256 feeAmount);

    /**
     * @notice Constructor for the GROK token contract.
     * @param initialSupply Initial supply of tokens.
     * @param taxRateBps Initial tax rate in basis points.
     */
    constructor(uint256 initialSupply, uint16 taxRateBps) ERC20("GROK Token", "GROK") {
        _mint(msg.sender, initialSupply);
        taxRate = taxRateBps;
        _taxExempt[msg.sender] = true; // Deployer's address is tax exempt by default
    }

    /**
     * @notice Updates the tax exemption status for an address.
     * @param account Address to update tax exemption for.
     * @param exempt Whether the address should be tax exempt.
     */
    function updateTaxExemption(address account, bool exempt) public onlyOwner {
        _taxExempt[account] = exempt;
        emit TaxExemptionUpdated(account, exempt);
    }

    /**
     * @notice Checks if an address is tax exempt.
     * @param account Address to check.
     * @return Whether the address is tax exempt.
     */
    function isTaxExempt(address account) public view returns (bool) {
        return _taxExempt[account];
    }

    /**
     * @notice Transfers tokens with potential tax deduction.
     * @param from Address that sends the tokens.
     * @param to Address that receives the tokens.
     * @param amount Amount of tokens to transfer.
     * @return Amount of tokens transferred after potential tax deduction.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (uint256) {
        uint256 feeAmount;
        if (!isTaxExempt(from)) {
            feeAmount = (amount * taxRate) / 10_000;
            _burn(from, feeAmount);
            emit TransactionFeePaid(from, to, amount, feeAmount);
        }
        uint256 netAmount = amount - feeAmount;
        super.transferFrom(from, to, netAmount);
        return netAmount;
    }

    /**
     * @notice Transfers tokens with potential tax deduction.
     * @param to Address that receives the tokens.
     * @param amount Amount of tokens to transfer.
     * @return Amount of tokens transferred after potential tax deduction.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (uint256) {
        uint256 feeAmount;
        if (!isTaxExempt(msg.sender)) {
            feeAmount = (amount * taxRate) / 10_000;
            _burn(msg.sender, feeAmount);
            emit TransactionFeePaid(msg.sender, to, amount, feeAmount);
        }
        uint256 netAmount = amount - feeAmount;
        super.transfer(to, netAmount);
        return netAmount;
    }
}
```
