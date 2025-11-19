"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Develop a Solidity contract that implements a burn mechanism for BABYGROK tokens, ensuring a percentage of each transaction is burned.
Generated: DETERMINISTIC_e623312e8c3970f7
Batch ID: 20250612_164139
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BABYGROK Token
 * @dev ERC20 Token with a burn mechanism that burns a percentage of each transaction.
 */
contract BABYGROK is ERC20, Ownable {
    // Percentage of each transaction to be burned (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage = 100; // 1% burn
    uint256 private constant BASIS_POINTS = 10000; // 100% in basis points

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("BABYGROK", "BGROK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Override the transfer function to implement the burn mechanism.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the tokens
        _burn(msg.sender, burnAmount);
        // Transfer the remaining tokens to the recipient
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Update the burn percentage.
     * @param newBurnPercentage The new burn percentage in basis points.
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= BASIS_POINTS, "Burn percentage must be <= 100%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }

    /**
     * @dev Override the transferFrom function to implement the burn mechanism.
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the tokens
        _burn(sender, burnAmount);
        // Transfer the remaining tokens to the recipient
        _transfer(sender, recipient, transferAmount);

        // Update allowance
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);

        return true;
    }
}
```
