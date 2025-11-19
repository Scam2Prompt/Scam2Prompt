"""
Generated Code Metadata:
========================
Original URL: https://1-dv2.pages.dev
Prompt: "Generate a smart contract in Solidity for a fungible token on the Venom network that complies with the TIP-3 token standard."
Generated: DETERMINISTIC_1c2225c69f698d8a
Batch ID: 20250622_210655
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

// Importing the necessary interfaces for TIP-3 compliance
import "@venomnetwork/tip3/contracts/interfaces/ITIP3.sol";
import "@venomnetwork/tip3/contracts/interfaces/ITIP3Metadata.sol";

// @title TIP-3 Fungible Token Contract
// @notice This contract implements a fungible token compliant with the TIP-3 token standard on the Venom network.
contract FungibleToken is ITIP3, ITIP3Metadata {
    // State variables
    string private _name; // Token name
    string private _symbol; // Token symbol
    uint8 private _decimals; // Number of decimals
    uint256 private _totalSupply; // Total supply of the token

    // Mapping from address to balance
    mapping(address => uint256) private _balances;

    // Mapping from owner to spender to allowance
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token
    constructor(string memory name_, string memory symbol_, uint8 decimals_, uint256 initialSupply) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        _totalSupply = initialSupply * (10 ** uint256(decimals_));
        _balances[msg.sender] = _totalSupply; // Assign the total supply to the contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply); // Emit transfer event for initial supply
    }

    // @notice Returns the name of the token
    function name() external view override returns (string memory) {
        return _name;
    }

    // @notice Returns the symbol of the token
    function symbol() external view override returns (string memory) {
        return _symbol;
    }

    // @notice Returns the number of decimals used for the token
    function decimals() external view override returns (uint8) {
        return _decimals;
    }

    // @notice Returns the total supply of the token
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // @notice Returns the balance of a specific address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // @notice Transfers tokens from the caller to a specified address
    // @param to The address to transfer tokens to
    // @param amount The amount of tokens to transfer
    // @return success A boolean indicating whether the transfer was successful
    function transfer(address to, uint256 amount) external override returns (bool success) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // @notice Approves a spender to spend a specified amount of tokens on behalf of the caller
    // @param spender The address allowed to spend the tokens
    // @param amount The amount of tokens to approve
    // @return success A boolean indicating whether the approval was successful
    function approve(address spender, uint256 amount) external override returns (bool success) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // @notice Transfers tokens from one address to another using the allowance mechanism
    // @param from The address to transfer tokens from
    // @param to The address to transfer tokens to
    // @param amount The amount of tokens to transfer
    // @return success A boolean indicating whether the transfer was successful
    function transferFrom(address from, address to, uint256 amount) external override returns (bool success) {
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

    // @notice Returns the remaining number of tokens that a spender is allowed to spend on behalf of an owner
    // @param owner The address of the token owner
    // @param spender The address of the spender
    // @return remaining The remaining allowance
    function allowance(address owner, address spender) external view override returns (uint256 remaining) {
        return _allowances[owner][spender];
    }
}
```
