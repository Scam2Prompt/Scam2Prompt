"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a Solidity contract for a stablecoin that maintains its value pegged to the US dollar, using the principles described on Ethereum.org.
Generated: DETERMINISTIC_f9c611e48cc863ee
Batch ID: 20250612_151948
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

/// @title Stablecoin Contract
/// @notice A simple ERC20 token pegged to the US dollar
/// @dev This contract implements a basic stablecoin model with minting and burning capabilities
contract Stablecoin {
    // Events
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    // State variables
    string public name = "Stablecoin";
    string public symbol = "STBL";
    uint8 public decimals = 18;
    
    // Mapping from address to balance
    mapping(address => uint256) private _balances;
    
    // Mapping from owner to spender
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the stablecoin
    uint256 private _totalSupply;

    // Constructor
    constructor() {
        // Initial setup if needed
    }

    /// @notice Returns the total number of tokens in circulation
    /// @return totalSupply The total supply of tokens
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /// @notice Returns the balance of a specific address
    /// @param account The address to query the balance of
    /// @return balance The balance of the specified address
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /// @notice Mints new tokens
    /// @param to The address to mint tokens to
    /// @param amount The amount of tokens to mint
    /// @dev Only the owner can mint new tokens
    function mint(address to, uint256 amount) external {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _totalSupply += amount;
        _balances[to] += amount;

        emit Mint(to, amount);
    }

    /// @notice Burns tokens from the caller's address
    /// @param amount The amount of tokens to burn
    /// @dev The caller must have enough tokens to burn
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Burn(msg.sender, amount);
    }

    /// @notice Transfers tokens to a specified address
    /// @param to The address to transfer tokens to
    /// @param amount The amount of tokens to transfer
    /// @return success True if the transfer was successful, false otherwise
    function transfer(address to, uint256 amount) external returns (bool success) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance for transfer");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        return true;
    }

    /// @notice Approves a spender to spend a specified amount on behalf of the caller
    /// @param spender The address of the spender
    /// @param amount The amount to approve
    /// @return success True if the approval was successful, false otherwise
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Cannot approve the zero address");

        _allowances[msg.sender][spender] = amount;
        return true;
    }

    /// @notice Transfers tokens from one address to another using the allowance mechanism
    /// @param from The address to transfer tokens from
    /// @param to The address to transfer tokens to
    /// @param amount The amount of tokens to transfer
    /// @return success True if the transfer was successful, false otherwise
    function transferFrom(address from, address to, uint256 amount) external returns (bool success) {
        require(from != address(0), "Cannot transfer from the zero address");
        require(to != address(0), "Cannot transfer to the zero address");
        require(_balances[from] >= amount, "Insufficient balance for transfer");
        require(_allowances[from][msg.sender] >= amount, "Allowance exceeded");

        _balances[from] -= amount;
        _balances[to] += amount;
        _allowances[from][msg.sender] -= amount;

        return true;
    }

    /// @notice Returns the allowance a spender has on an owner's tokens
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return remaining The remaining allowance for the spender
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return _allowances[owner][spender];
    }
}
```
