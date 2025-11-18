"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-beef-meme.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a deflationary token model similar to BEEF Coin, including token burning functionality to reduce supply over time.
Generated: DETERMINISTIC_5ecb5229cc094772
Batch ID: 20250612_151255
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

/// @title Deflationary Token Contract
/// @author Your Name
/// @notice This contract implements a deflationary token model with burning functionality
contract DeflationaryToken {
    // Declare state variables
    string public name;                  // Name of the token
    string public symbol;                // Symbol of the token
    uint8 public decimals;                // Number of decimals for the token
    uint256 private _totalSupply;        // Total supply of the token
    mapping(address => uint256) private _balances;  // Balances of each account
    mapping(address => mapping(address => uint256)) private _allowances; // Allowances for delegated transfers

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    /// @notice Constructor to initialize the token
    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _decimals The number of decimals for the token
    /// @param initialSupply The initial supply of the token
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        _totalSupply = initialSupply * (10 ** uint256(decimals)); // Adjust for decimals
        _balances[msg.sender] = _totalSupply; // Assign total supply to contract creator
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /// @notice Returns the total supply of the token
    /// @return Total supply of the token
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /// @notice Returns the balance of a given address
    /// @param account The address to query the balance of
    /// @return The balance of the specified address
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /// @notice Transfers tokens from the caller's account to a recipient
    /// @param recipient The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /// @notice Approves a spender to spend tokens on behalf of the caller
    /// @param spender The address of the spender
    /// @param amount The amount of tokens to approve
    /// @return A boolean indicating success
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /// @notice Transfers tokens from one address to another using allowances
    /// @param sender The address of the sender
    /// @param recipient The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /// @notice Allows users to burn their tokens, reducing total supply
    /// @param amount The amount of tokens to burn
    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Burn(msg.sender, amount);
    }

    /// @notice Returns the allowance of a spender for a given owner
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return The remaining number of tokens that spender is allowed to spend
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
