"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummyh.pages.dev
Prompt: Explain how to create your own version of the $Gummy token using the principles discussed in Gummynomics101.
Generated: DETERMINISTIC_4bdcb87bc73a78ff
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
 * @title Gummy Token Contract
 * @dev Implementation of a custom ERC20 token named $Gummy.
 * This contract demonstrates principles of token economics.
 */
contract GummyToken {
    // State variables
    string public name = "$Gummy"; // Token name
    string public symbol = "GUMMY"; // Token symbol
    uint8 public decimals = 18; // Token decimal places
    uint256 public totalSupply; // Total supply of tokens

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;
    
    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) private allowances;
    
    // Events for logging key contract activities
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to set the initial supply of tokens to the contract owner.
     * @param initialSupply The initial token supply (in base units).
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero.");
        
        // Assign the initial supply to the contract's creator
        totalSupply = initialSupply * (10**decimals); // Adjust for decimal places
        balances[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply); // Mint event
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account The address of the account to query.
     * @return The account's balance.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param recipient The address to transfer tokens to.
     * @param amount The number of tokens to transfer (in base units).
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        
        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Approves a spender to transfer a specified number of tokens on behalf of the owner.
     * @param spender The address authorized to spend tokens.
     * @param amount The maximum number of tokens the spender can transfer (in base units).
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address.");
        
        // Set the allowance
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    /**
     * @dev Transfers tokens from a sender to a recipient using an allowance.
     * @param sender The address of the token owner.
     * @param recipient The address to transfer tokens to.
     * @param amount The number of tokens to transfer (in base units).
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "Cannot transfer from the zero address.");
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(balances[sender] >= amount, "Insufficient balance.");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded.");
        
        // Adjust balances and allowances
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Returns the allowance for a spender on behalf of an owner.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
