"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoniclabs.pages.dev
Prompt: Write a Solidity smart contract optimized for deployment on Sonic, the fastest EVM Layer-1 blockchain, leveraging its sub-second confirmation times and low transaction costs.
Generated: DETERMINISTIC_226337f1b32b5126
Batch ID: 20250612_153832
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

/// @title SonicToken - A simple ERC20 token for the Sonic blockchain
/// @notice This contract implements a basic ERC20 token with minting and burning capabilities
/// @dev The contract is designed to be optimized for deployment on the Sonic blockchain
contract SonicToken {
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Mapping from address to balances
    mapping(address => uint256) private _balances;
    // Mapping from owner to approved spenders
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;
    // Token name
    string public name;
    // Token symbol
    string public symbol;
    // Decimals for token representation
    uint8 public decimals;

    /// @notice Constructor to initialize the token with name, symbol, and decimals
    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _decimals The number of decimals for token representation
    constructor(string memory _name, string memory _symbol, uint8 _decimals) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
    }

    /// @notice Returns the total supply of the token
    /// @return The total supply as a uint256
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /// @notice Returns the balance of a specific account
    /// @param account The address of the account to query
    /// @return The balance of the account as a uint256
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /// @notice Transfers tokens from the caller's account to a recipient
    /// @param to The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean value indicating success
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /// @notice Approves a spender to transfer tokens on behalf of the caller
    /// @param spender The address of the spender
    /// @param amount The amount of tokens to approve
    /// @return A boolean value indicating success
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /// @notice Transfers tokens from a specified account to a recipient
    /// @param from The address of the sender
    /// @param to The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean value indicating success
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(from != address(0), "Transfer from the zero address is not allowed");
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(_balances[from] >= amount, "Insufficient balance");
        require(_allowances[from][msg.sender] >= amount, "Allowance exceeded");

        _balances[from] -= amount;
        _balances[to] += amount;
        _allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /// @notice Returns the remaining amount of tokens that a spender is allowed to spend on behalf of an owner
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return The remaining allowance as a uint256
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /// @notice Mints new tokens and assigns them to a specified account
    /// @param to The address of the account to mint tokens for
    /// @param amount The amount of tokens to mint
    /// @return A boolean value indicating success
    function mint(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Mint to the zero address is not allowed");

        _totalSupply += amount;
        _balances[to] += amount;

        emit Mint(to, amount);
        return true;
    }

    /// @notice Burns a specific amount of tokens from the caller's account
    /// @param amount The amount of tokens to burn
    /// @return A boolean value indicating success
    function burn(uint256 amount) public returns (bool) {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Burn(msg.sender, amount);
        return true;
    }
}
```
