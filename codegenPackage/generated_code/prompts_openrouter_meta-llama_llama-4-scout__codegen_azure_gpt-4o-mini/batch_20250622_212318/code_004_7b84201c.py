"""
Generated Code Metadata:
========================
Original URL: https://safemoon.network
Prompt: Design a smart contract for implementing anti-whale measures in a cryptocurrency project like SafeMoon.
Generated: DETERMINISTIC_7b84201c74aeb037
Batch ID: 20250622_212318
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
 * @title AntiWhaleToken
 * @dev ERC20 Token with anti-whale measures to limit large transactions
 */
contract AntiWhaleToken is ERC20, Ownable {
    // Maximum transaction amount (in tokens)
    uint256 public maxTransactionAmount;
    
    // Mapping to track addresses that are exempt from the anti-whale measures
    mapping(address => bool) private _isExcludedFromAntiWhale;

    // Event emitted when the max transaction amount is updated
    event MaxTransactionAmountUpdated(uint256 newMaxTransactionAmount);

    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens.
     * @param _maxTransactionAmount The maximum transaction amount allowed.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _maxTransactionAmount) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        maxTransactionAmount = _maxTransactionAmount * (10 ** decimals());
    }

    /**
     * @dev Function to update the maximum transaction amount.
     * @param newMaxTransactionAmount The new maximum transaction amount.
     */
    function updateMaxTransactionAmount(uint256 newMaxTransactionAmount) external onlyOwner {
        maxTransactionAmount = newMaxTransactionAmount * (10 ** decimals());
        emit MaxTransactionAmountUpdated(maxTransactionAmount);
    }

    /**
     * @dev Function to exclude an address from anti-whale measures.
     * @param account The address to exclude.
     */
    function excludeFromAntiWhale(address account) external onlyOwner {
        _isExcludedFromAntiWhale[account] = true;
    }

    /**
     * @dev Function to include an address back into anti-whale measures.
     * @param account The address to include.
     */
    function includeInAntiWhale(address account) external onlyOwner {
        _isExcludedFromAntiWhale[account] = false;
    }

    /**
     * @dev Override the _transfer function to implement anti-whale measures.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if the sender is excluded from anti-whale measures
        if (!_isExcludedFromAntiWhale[sender] && !_isExcludedFromAntiWhale[recipient]) {
            require(amount <= maxTransactionAmount, "Transfer amount exceeds the maxTransactionAmount.");
        }

        // Call the parent _transfer function to execute the transfer
        super._transfer(sender, recipient, amount);
    }
}
```
