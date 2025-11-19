"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cactus-network.net
Prompt: What are the steps to develop a token on the Cactus Blockchain, and can you provide a sample code for the smart contract?
Generated: DETERMINISTIC_e28084ac612dea4b
Batch ID: 20250612_161035
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

/// @title Cactus Token Smart Contract
/// @dev This contract implements a basic ERC20 token on the Cactus Blockchain.
contract CactusToken {
    string public name;                // Token name
    string public symbol;              // Token symbol
    uint8 public decimals;              // Number of decimals for the token
    uint256 public totalSupply;         // Total supply of the token

    mapping(address => uint256) private balances;            // Mapping of user balances
    mapping(address => mapping(address => uint256)) private allowances; // Allowance mapping for transfer approval

    // Events to log important actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /// @dev Sets the values for {name}, {symbol}, and {totalSupply} of the token.
    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _totalSupply The initial total supply of the token
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) {
        name = _name;
        symbol = _symbol;
        decimals = 18; // Standard number of decimals for ERC20 tokens
        totalSupply = _totalSupply * (10 ** uint256(decimals)); // Adjusting total supply based on decimals
        balances[msg.sender] = totalSupply; // Assign the entire supply to the contract's creator
    }

    /// @dev Returns the balance of a specific address.
    /// @param account The address to query the balance of
    /// @return The balance of the specified address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /// @dev Transfers tokens from the sender to a specified address.
    /// @param to The address to transfer tokens to
    /// @param amount The number of tokens to transfer
    /// @return A boolean indicating success
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount; // Deduct the amount from the sender
        balances[to] += amount; // Add the amount to the receiver's balance

        emit Transfer(msg.sender, to, amount); // Emit the transfer event
        return true;
    }

    /// @dev Approves a spender to withdraw tokens from the sender's account.
    /// @param spender The address allowed to spend the tokens
    /// @param amount The number of tokens the spender is allowed to spend
    /// @return A boolean indicating success
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount; // Set allowance for the spender
        emit Approval(msg.sender, spender, amount); // Emit the approval event
        return true;
    }

    /// @dev Transfers tokens from one address to another using an allowance.
    /// @param from The address to transfer tokens from
    /// @param to The address to transfer tokens to
    /// @param amount The number of tokens to transfer
    /// @return A boolean indicating success
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(from != address(0), "Cannot transfer from the zero address");
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[from] -= amount; // Deduct the amount from the sender
        balances[to] += amount; // Add the amount to the receiver's balance
        allowances[from][msg.sender] -= amount; // Deduct the amount from the allowance

        emit Transfer(from, to, amount); // Emit the transfer event
        return true;
    }

    /// @dev Returns the remaining number of tokens that the spender is allowed to spend on behalf of the owner.
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return The remaining allowance
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
