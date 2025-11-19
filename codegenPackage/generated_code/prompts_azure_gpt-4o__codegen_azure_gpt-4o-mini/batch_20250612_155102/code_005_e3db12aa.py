"""
Generated Code Metadata:
========================
Original URL: https://flareevm-network.com
Prompt: Develop a scalable smart contract on Flare's EVM-based blockchain that utilizes its low-carbon consensus algorithm.
Generated: DETERMINISTIC_e3db12aae15aa57f
Batch ID: 20250612_155102
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

/// @title Scalable Smart Contract for Flare's EVM-based Blockchain
/// @author Your Name
/// @notice This contract demonstrates a simple token system utilizing Flare's low-carbon consensus algorithm
/// @dev This contract is designed to be scalable and follows best practices for security and efficiency

contract ScalableToken {
    // State variables
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimals for the token
    uint256 public totalSupply; // Total supply of the token

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Mapping from owner to approved spender
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /// @notice Constructor to initialize the token
    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _decimals The number of decimals for the token
    /// @param _initialSupply The initial supply of the token
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign the total supply to the contract deployer
    }

    /// @notice Get the balance of a specific address
    /// @param account The address to query the balance of
    /// @return The balance of the specified address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /// @notice Transfer tokens to a specified address
    /// @param to The address to transfer tokens to
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /// @notice Approve a spender to spend tokens on behalf of the owner
    /// @param spender The address allowed to spend the tokens
    /// @param amount The amount of tokens to approve
    /// @return A boolean indicating success
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /// @notice Transfer tokens from one address to another using allowance
    /// @param from The address to transfer tokens from
    /// @param to The address to transfer tokens to
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(from != address(0), "Transfer from the zero address is not allowed");
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /// @notice Get the allowance of a spender for a specific owner
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return The remaining number of tokens that the spender is allowed to spend
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
