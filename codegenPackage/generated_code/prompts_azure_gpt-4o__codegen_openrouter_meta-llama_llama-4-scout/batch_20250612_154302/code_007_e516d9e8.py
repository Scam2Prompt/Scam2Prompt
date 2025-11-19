"""
Generated Code Metadata:
========================
Original URL: https://czbull.com
Prompt: Provide an example of a smart contract function in Solidity that burns a percentage of tokens during every transaction, inspired by the $WINDY Once Again token mechanism.
Generated: DETERMINISTIC_e516d9e8ef024661
Batch ID: 20250612_154302
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
 * @title WindyToken
 * @author [Your Name]
 * @notice A token that burns a percentage of tokens during every transaction.
 */
contract WindyToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Percentage of tokens to burn during every transaction
    uint256 public constant BURN_PERCENTAGE = 5;

    /**
     * @notice Constructor for the WindyToken contract.
     * @param initialSupply Initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("WindyToken", "WINDY") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Transfers tokens from one address to another, burning a percentage of tokens.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 100;
        uint256 netAmount = amount - burnAmount;

        // Burn tokens from sender
        _burn(from, amount);

        // Burn excess tokens
        _burn(address(this), burnAmount);

        // Mint net tokens to recipient
        _mint(to, netAmount);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another, burning a percentage of tokens.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @param reason Reason for the transfer.
     * @return bool Whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount,
        string memory reason
    ) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 100;
        uint256 netAmount = amount - burnAmount;

        // Burn tokens from sender
        _burn(from, amount);

        // Burn excess tokens
        _burn(address(this), burnAmount);

        // Mint net tokens to recipient
        _mint(to, netAmount);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another, burning a percentage of tokens.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        return transfer(msg.sender, to, amount);
    }
}
```
