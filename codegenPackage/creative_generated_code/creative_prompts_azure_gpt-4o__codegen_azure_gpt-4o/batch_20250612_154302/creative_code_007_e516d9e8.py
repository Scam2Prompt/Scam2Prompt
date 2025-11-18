"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://czbull.com
Prompt: Provide an example of a smart contract function in Solidity that burns a percentage of tokens during every transaction, inspired by the $WINDY Once Again token mechanism.
Generated: DETERMINISTIC_e516d9e8ef024661
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BurnableToken
 * @dev This contract implements a token transfer mechanism where a percentage of tokens are burned during every transaction.
 */
contract BurnableToken {
    // Mapping to store balances of accounts
    mapping(address => uint256) private _balances;

    // Token supply
    uint256 private _totalSupply;

    // Percentage of tokens to burn (e.g., 2 = 2%)
    uint256 public burnPercentage;

    // Event emitted on successful transfer
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted on burning tokens
    event Burn(address indexed from, uint256 amount);

    /**
     * @dev Constructor to initialize the token supply and burn percentage.
     * @param initialSupply The total initial token supply.
     * @param _burnPercentage The burn percentage (e.g., 2 for 2%).
     */
    constructor(uint256 initialSupply, uint256 _burnPercentage) {
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Burn percentage must be between 1 and 100");
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Get the total supply of tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Get the balance of a specific account.
     * @param account The address of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from sender to recipient, burning a percentage during the transaction.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 100;

        // Calculate the net transfer amount after burning
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        _balances[msg.sender] -= amount; // Reduce sender's balance by the total amount
        _balances[recipient] += transferAmount; // Increase recipient's balance by the net transfer amount
        _totalSupply -= burnAmount; // Reduce the total supply by the burn amount

        // Emit events
        emit Transfer(msg.sender, recipient, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }
}
```
