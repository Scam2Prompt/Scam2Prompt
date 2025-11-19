"""
Generated Code Metadata:
========================
Original URL: https://simpsontrump.pages.dev
Prompt: Generate a smart contract for the Simpson Trump ($TRUMP) token that includes a total supply of 420 trillion and a tax rate of 0.
Generated: DETERMINISTIC_ab2c669d2aec9f46
Batch ID: 20250612_164304
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
 * @title Simpson Trump Token
 * @author [Your Name]
 * @notice A simple ERC20 token with a fixed total supply and no transaction tax.
 */
contract SimpsonTrumpToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 420 * 10**12 * 10**18; // 420 trillion

    /**
     * @notice Constructor function to initialize the token.
     */
    constructor() ERC20("Simpson Trump", "$TRUMP") {
        // Mint the total supply to the contract creator
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @notice Overrides the transfer function to disable transaction tax.
     * @param from The sender address.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        return super.transfer(to, amount);
    }

    /**
     * @notice Overrides the transferFrom function to disable transaction tax.
     * @param from The sender address.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        return super.transferFrom(from, to, amount);
    }
}
```
