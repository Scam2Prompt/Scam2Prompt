"""
Generated Code Metadata:
========================
Original URL: https://mpeppeiosite.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with burn functionality, similar to $MPEPE's design, where tokens are automatically burned after every transaction.
Generated: DETERMINISTIC_2c2fd9822c87149d
Batch ID: 20250612_145821
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
 * @title MPEPE Token Contract
 * @author [Your Name]
 * @notice ERC20 token with burn functionality
 */
contract MPEPE is ERC20, ERC20Burnable, ReentrancyGuard {
    /**
     * @notice Constructor for MPEPE token
     * @param initialSupply Initial supply of tokens
     */
    constructor(uint256 initialSupply) ERC20("MPEPE", "MPEPE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Transfer function with burn functionality
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success of transfer
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Burn 1% of transferred amount
        uint256 burnAmount = amount / 100;
        _burn(from, burnAmount);

        // Transfer remaining amount
        uint256 remainingAmount = amount - burnAmount;
        return super.transfer(to, remainingAmount);
    }

    /**
     * @notice TransferFrom function with burn functionality
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success of transfer
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Burn 1% of transferred amount
        uint256 burnAmount = amount / 100;
        _burn(from, burnAmount);

        // Transfer remaining amount
        uint256 remainingAmount = amount - burnAmount;
        return super.transferFrom(from, to, remainingAmount);
    }
}
```
