"""
Generated Code Metadata:
========================
Original URL: https://firstledger-xaman-caches.pages.dev
Prompt: Explain how to implement a whale filter for a token on First Ledger to ensure no single wallet holds more than 5% of the supply.
Generated: DETERMINISTIC_7a8fa815d5fc306e
Batch ID: 20250612_162629
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

/**
 * @title WhaleFilterToken
 * @dev ERC20 token with a whale filter to ensure no wallet holds more than 5% of the total supply.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WhaleFilterToken is ERC20, Ownable {
    // Maximum percentage of total supply a single wallet can hold (5%)
    uint256 public constant MAX_HOLDING_PERCENTAGE = 5;

    // Total supply of the token
    uint256 private immutable _totalSupply;

    /**
     * @dev Constructor to initialize the token with a name, symbol, and total supply.
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _totalSupply = initialSupply;
        _mint(msg.sender, initialSupply); // Mint the initial supply to the contract owner
    }

    /**
     * @dev Override the _transfer function to enforce the whale filter.
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens being transferred
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the maximum allowed holding for a single wallet
        uint256 maxHolding = (_totalSupply * MAX_HOLDING_PERCENTAGE) / 100;

        // Ensure the recipient's balance after the transfer does not exceed the maximum allowed holding
        require(balanceOf(recipient) + amount <= maxHolding, "WhaleFilter: Transfer exceeds maximum wallet holding limit");

        // Perform the transfer
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Returns the total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
