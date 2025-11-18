"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-iio.pages.dev
Prompt: Using Solidity, design a smart contract that prevents inflation by enforcing a fixed token supply, similar to DOGE20's approach.
Generated: DETERMINISTIC_1d2e19b93d0498a9
Batch ID: 20250612_153526
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
 * @title FixedSupplyToken
 * @dev A simple ERC-20-like token with a fixed supply to prevent inflation.
 */
contract FixedSupplyToken {
    // Token metadata
    string public name = "FixedSupplyToken";
    string public symbol = "FST";
    uint8 public decimals = 18;

    // Fixed token supply
    uint256 public totalSupply;

    // Mapping of addresses to their token balances
    mapping(address => uint256) private balances;

    // Mapping to handle allowances for spending tokens on behalf of others
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for transfer and approval actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the fixed token supply and assign it to the deployer
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply; // Assign entire supply to contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's address to another address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Allows a spender to withdraw a specific amount of tokens from the caller's account.
     * @param spender The address authorized to spend tokens.
     * @param amount The amount of tokens the spender is allowed to spend.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can spend on behalf of the owner.
     * @param owner The address that owns the tokens.
     * @param spender The address authorized to spend the tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        // Update balances and allowances
        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }
}
```
