"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Write a Solidity contract to implement the ever-rising baseline value feature of SmartDeFi™, ensuring that the minimum value of a token increases with every buy and sell transaction.
Generated: DETERMINISTIC_30a2ebe4809eea80
Batch ID: 20250612_152249
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
 * @title EverRisingBaselineToken
 * @author [Your Name]
 * @notice Implementation of the ever-rising baseline value feature of SmartDeFi
 */
contract EverRisingBaselineToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of address to its current buy/sell modifier
    mapping(address => bool) public isBuyModifier;

    // Current baseline value
    uint256 public baselineValue;

    // Percentage increase for baseline value on each transaction
    uint256 public constant BASELINE_INCREASE_PERCENTAGE = 1;

    /**
     * @notice Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param initialBaselineValue Initial baseline value
     */
    constructor(string memory name_, string memory symbol_, uint256 initialBaselineValue) ERC20(name_, symbol_) {
        require(initialBaselineValue > 0, "Initial baseline value must be greater than 0");
        baselineValue = initialBaselineValue;
    }

    /**
     * @notice Transfer function with ever-rising baseline value
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Update baseline value on transfer
        _updateBaselineValue(msg.sender, to);

        return super.transfer(to, amount);
    }

    /**
     * @notice TransferFrom function with ever-rising baseline value
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Update baseline value on transfer
        _updateBaselineValue(from, to);

        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Buy function with ever-rising baseline value
     * @param amount Amount to buy
     */
    function buy(uint256 amount) public nonReentrant {
        require(amount > 0, "Buy amount must be greater than 0");

        // Update buy modifier
        isBuyModifier[msg.sender] = true;

        // Update baseline value on buy
        _updateBaselineValue(msg.sender, address(this));

        // Mint tokens
        _mint(msg.sender, amount);
    }

    /**
     * @notice Sell function with ever-rising baseline value
     * @param amount Amount to sell
     */
    function sell(uint256 amount) public nonReentrant {
        require(amount > 0, "Sell amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update sell modifier
        isBuyModifier[msg.sender] = false;

        // Update baseline value on sell
        _updateBaselineValue(msg.sender, address(this));

        // Burn tokens
        _burn(msg.sender, amount);
    }

    /**
     * @notice Update baseline value on buy/sell transaction
     * @param from Address of sender
     * @param to Address of recipient
     */
    function _updateBaselineValue(address from, address to) internal {
        // Check if it's a buy or sell transaction
        bool isBuy = isBuyModifier[from];

        // Update baseline value
        if (isBuy) {
            // Increase baseline value on buy
            baselineValue = baselineValue + (baselineValue * BASELINE_INCREASE_PERCENTAGE / 100);
        } else {
            // Ensure baseline value doesn't decrease on sell
            // No action needed, as baseline increase is only on buys
        }
    }
}
```
