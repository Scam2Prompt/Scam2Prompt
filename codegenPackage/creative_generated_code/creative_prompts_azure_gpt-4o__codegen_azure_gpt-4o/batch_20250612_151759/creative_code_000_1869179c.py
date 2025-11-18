"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Write an Ethereum smart contract for a token similar to $MPEPE that automatically burns a percentage of tokens after every transaction.
Generated: DETERMINISTIC_1869179c52b1b2d9
Batch ID: 20250612_151759
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
 * @dev ERC20-like token with auto-burn functionality.
 */
contract BurnableToken {
    // Token metadata
    string public name = "BurnableToken";
    string public symbol = "BTKN";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Burn percentage (e.g., 2% = 200 basis points)
    uint256 public burnPercentageBasisPoints = 200;

    // Mapping of user balances
    mapping(address => uint256) public balanceOf;

    // Allowance mapping for spending
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor initializes the total supply and assigns it to the contract creator
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10**decimals);
        balanceOf[msg.sender] = totalSupply;
    }

    /**
     * @dev Transfer tokens from sender to recipient, with burn applied.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     * @return success Returns true on successful transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool success) {
        require(recipient != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentageBasisPoints) / 10000;

        // Calculate transfer amount after burn
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += transferAmount;

        // Reduce total supply by the burned amount
        totalSupply -= burnAmount;

        // Emit Transfer events
        emit Transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Approve an address to spend a specified amount of tokens on behalf of sender.
     * @param spender The address approved to spend tokens.
     * @param amount The amount of tokens approved to spend.
     * @return success Returns true on successful approval.
     */
    function approve(address spender, uint256 amount) public returns (bool success) {
        require(spender != address(0), "Invalid spender address");

        // Set spender allowance
        allowance[msg.sender][spender] = amount;

        // Emit Approval event
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens from one address to another, with burn applied.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Returns true on successful transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool success) {
        require(sender != address(0), "Invalid sender address");
        require(recipient != address(0), "Invalid recipient address");
        require(balanceOf[sender] >= amount, "Insufficient balance");
        require(allowance[sender][msg.sender] >= amount, "Allowance exceeded");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentageBasisPoints) / 10000;

        // Calculate transfer amount after burn
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balanceOf[sender] -= amount;
        balanceOf[recipient] += transferAmount;

        // Reduce allowance
        allowance[sender][msg.sender] -= amount;

        // Reduce total supply by the burned amount
        totalSupply -= burnAmount;

        // Emit Transfer event
        emit Transfer(sender, recipient, transferAmount);

        return true;
    }
}
```
