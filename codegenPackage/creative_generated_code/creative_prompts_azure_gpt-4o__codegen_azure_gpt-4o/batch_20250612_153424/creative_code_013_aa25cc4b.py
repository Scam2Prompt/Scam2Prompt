"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-eth.github.io
Prompt: Generate code in Solidity for creating a simple ERC-20 token and include instructions for verifying the contract on Etherscan.
Generated: DETERMINISTIC_aa25cc4b5b588302
Batch ID: 20250612_153424
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
 * @title SimpleERC20Token
 * @dev Implementation of a basic ERC-20 token contract.
 */
contract SimpleERC20Token {
    // Token details
    string public name = "SimpleToken";
    string public symbol = "STKN";
    uint8 public decimals = 18; // Standard decimal value for ERC-20 tokens
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging activity
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = initialSupply * (10 ** uint256(decimals)); // Adjusting for decimals
        balances[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Emit transfer event for minting tokens
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success Indicates whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Transfer to zero address is prohibited");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner.
     * @param spender The address allowed to spend tokens.
     * @param amount The maximum amount of tokens the spender can transfer.
     * @return success Indicates whether the approval was successful.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Approval to zero address is prohibited");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens a spender is allowed to transfer.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address from which tokens will be sent.
     * @param recipient The address that will receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Indicates whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
}

/*
 * Instructions for verifying the contract on Etherscan:
 * 1. Deploy the contract using your preferred Ethereum network (e.g., Mainnet, Goerli).
 * 2. Navigate to Etherscan and search for the deployed contract's address.
 * 3. On the contract page, click "Verify and Publish".
 * 4. Select "Solidity (Single file)" and choose the appropriate compiler version (e.g., 0.8.x).
 * 5. License type should be set to "MIT".
 * 6. Paste the contract code into the verification window and submit.
 * 7. Verify that the contract is successfully published by checking Etherscan.
 */
```
