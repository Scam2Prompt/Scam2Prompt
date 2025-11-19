"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 billion, similar to the $COW token on Cow On Base.
Generated: DETERMINISTIC_a3b676e3bf9ce10d
Batch ID: 20250612_163840
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
 * @title CowToken ($COW)
 * @dev ERC20-compatible token with a fixed total supply of 1 billion.
 * Implements basic features of a fungible token.
 */
contract CowToken {
    // Token metadata
    string public name = "CowToken";
    string public symbol = "COW";
    uint8 public decimals = 18;

    // Total token supply
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals));

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;

    // Mapping to track allowances for delegated transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for tracking token transfers and approval actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Contract deployer receives the entire token supply
    constructor() {
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the token balance of a given address.
     * @param account The address to query the balance for.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's account to another address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform token transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender The address allowed to spend the tokens.
     * @param amount The maximum amount that can be spent.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to zero address is not allowed");

        // Set the allowance
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using the allowance mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from zero address is not allowed");
        require(recipient != address(0), "Transfer to zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Deduct from sender's balance and allowance
        balances[sender] -= amount;
        allowances[sender][msg.sender] -= amount;

        // Add to recipient's balance
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining amount that a spender is allowed to transfer on behalf of an owner.
     * @param owner The address giving the allowance.
     * @param spender The address allowed to spend the tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
