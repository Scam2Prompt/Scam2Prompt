"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telos-4ji.pages.dev
Prompt: Write a smart contract in Solidity optimized for deployment on Telos EVM, leveraging its hyper-speed transaction capabilities and low gas fees. Include comments explaining how Telos EVM's unique features improve performance.
Generated: DETERMINISTIC_217bbd19cc02cac4
Batch ID: 20250612_152018
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

/// @title SampleToken - A simple ERC20 token contract optimized for Telos EVM
/// @notice This contract implements an ERC20 token with features optimized for Telos EVM
/// @dev Telos EVM allows for faster transactions and lower gas fees, enhancing the user experience
contract SampleToken {
    // Mapping from token holder addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping from token holder addresses to their allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Metadata variables for the token
    string public name = "SampleToken";
    string public symbol = "STK";
    uint8 public decimals = 18;

    // Events for logging token transfers and approval actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /// @notice Constructor to initialize the total supply and assign it to the contract deployer
    /// @param initialSupply The initial supply of tokens to be created
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply; // Assign all initial tokens to the contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /// @notice Returns the total supply of the token
    /// @return The total supply of the token
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /// @notice Returns the balance of a specific address
    /// @param account The address of the token holder
    /// @return The balance of the specified address
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /// @notice Transfers tokens from the caller to a specified address
    /// @param recipient The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance for transfer");
        
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /// @notice Approves a spender to transfer a specified amount of tokens on behalf of the caller
    /// @param spender The address allowed to spend the tokens
    /// @param amount The amount of tokens to allow
    /// @return A boolean indicating success
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /// @notice Returns the allowance a spender has to transfer tokens on behalf of an owner
    /// @param owner The address of the token owner
    /// @param spender The address allowed to spend the tokens
    /// @return The remaining allowance for the spender
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /// @notice Transfers tokens from one address to another using the allowance mechanism
    /// @param sender The address from which to transfer tokens
    /// @param recipient The address to which to transfer tokens
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance for transfer");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
