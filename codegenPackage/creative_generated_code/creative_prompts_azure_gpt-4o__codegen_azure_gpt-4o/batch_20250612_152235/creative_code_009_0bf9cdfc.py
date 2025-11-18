"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20presale-claim.pages.dev
Prompt: Write a Solidity contract that prevents inflation by enforcing a fixed supply of 140,000,000,000 DOGE20 tokens, as described in the tokenomics.
Generated: DETERMINISTIC_0bf9cdfcf141b572
Batch ID: 20250612_152235
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
 * @dev This contract implements a fixed-supply ERC20-like token named DOGE20.
 */
contract DOGE20 {
    // Public variables of the token
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;

    // Fixed total supply of tokens (140,000,000,000 * 10^18 for decimal precision)
    uint256 public totalSupply = 140_000_000_000 * 10**uint256(decimals);

    // Mapping to store balances of addresses
    mapping(address => uint256) public balanceOf;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for logging transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor that initializes the token supply and assigns it to the deployer's address.
     */
    constructor() {
        // Assign the total supply to the deployer of the contract
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens from the sender to a specified address.
     * @param to The destination address.
     * @param value The amount of tokens to transfer.
     * @return success A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 value) public returns (bool success) {
        require(to != address(0), "Invalid address"); // Prevent transfers to the zero address
        require(balanceOf[msg.sender] >= value, "Insufficient balance"); // Check sender's balance

        // Perform the transfer
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;

        // Emit the transfer event
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param spender The address allowed to transfer tokens.
     * @param value The amount of tokens approved for transfer.
     * @return success A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 value) public returns (bool success) {
        require(spender != address(0), "Invalid address"); // Prevent approvals to the zero address

        // Update the allowance
        allowance[msg.sender][spender] = value;

        // Emit the approval event
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of an owner, given sufficient allowance.
     * @param from The address from which tokens are transferred.
     * @param to The destination address.
     * @param value The amount of tokens to transfer.
     * @return success A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 value
    ) public returns (bool success) {
        require(to != address(0), "Invalid address"); // Prevent transfers to the zero address
        require(balanceOf[from] >= value, "Insufficient balance"); // Check sender's balance
        require(allowance[from][msg.sender] >= value, "Allowance exceeded"); // Check allowance

        // Perform the transfer
        balanceOf[from] -= value;
        balanceOf[to] += value;

        // Update the allowance
        allowance[from][msg.sender] -= value;

        // Emit the transfer event
        emit Transfer(from, to, value);
        return true;
    }
}
```
