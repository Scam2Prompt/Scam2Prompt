"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Write a Solidity contract to manage token burning (10% of payouts) as part of Everyworld's ecosystem economic equilibrium.
Generated: DETERMINISTIC_e7b79923ca064291
Batch ID: 20250612_152439
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
 * @title EveryworldToken
 * @dev A token contract with burn functionality that burns 10% of payouts
 *      as part of the ecosystem's economic equilibrium.
 */
contract EveryworldToken {
    // State variables
    string public name = "EveryworldToken";
    string public symbol = "EWT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Modifier to check for sufficient balance
    modifier hasSufficientBalance(address account, uint256 amount) {
        require(balances[account] >= amount, "Insufficient balance.");
        _;
    }

    // Constructor to initialize the total supply and assign all tokens to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
    }

    /**
     * @dev Transfer tokens from sender to recipient, automatically burns 10% of the payout.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     * @return success A boolean indicating the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) external hasSufficientBalance(msg.sender, amount) returns (bool success) {
        require(recipient != address(0), "Cannot transfer to the zero address.");

        // Calculate burn amount (10%)
        uint256 burnAmount = (amount * 10) / 100;

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += (amount - burnAmount);

        // Reduce total supply by the burn amount
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(msg.sender, recipient, amount - burnAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approve an address to spend a specified amount of tokens on behalf of the caller.
     * @param spender Address authorized to spend the tokens.
     * @param amount Amount of tokens authorized for spending.
     * @return success A boolean indicating the operation succeeded.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Cannot approve the zero address.");

        // Update allowance
        allowances[msg.sender][spender] = amount;

        // Emit event
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens on behalf of an account (requires prior approval).
     * @param sender Address to transfer tokens from.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     * @return success A boolean indicating the operation succeeded.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external hasSufficientBalance(sender, amount) returns (bool success) {
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance.");

        // Calculate burn amount (10%)
        uint256 burnAmount = (amount * 10) / 100;

        // Update balances and allowance
        balances[sender] -= amount;
        balances[recipient] += (amount - burnAmount);
        allowances[sender][msg.sender] -= amount;

        // Reduce total supply by the burn amount
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(sender, recipient, amount - burnAmount);
        emit Burn(sender, burnAmount);

        return true;
    }

    /**
     * @dev Get the balance of an address.
     * @param account Address to query the balance of.
     * @return balance The balance of the queried address.
     */
    function balanceOf(address account) external view returns (uint256 balance) {
        return balances[account];
    }

    /**
     * @dev Get the allowance for a spender on behalf of an owner.
     * @param owner Address owning the tokens.
     * @param spender Address authorized to spend the tokens.
     * @return remaining The remaining tokens that the spender is authorized to spend.
     */
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return allowances[owner][spender];
    }
}
```
