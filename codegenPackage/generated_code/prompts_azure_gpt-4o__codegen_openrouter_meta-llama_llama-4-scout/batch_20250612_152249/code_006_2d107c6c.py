"""
Generated Code Metadata:
========================
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Create a Solidity function to implement a token burn mechanism for BTCETF, reducing the supply by 5% each time a Bitcoin ETF milestone is reached.
Generated: DETERMINISTIC_2d107c6c715743a7
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";

/**
 * @title BTCETF Token Contract
 * @author [Your Name]
 * @notice This contract implements a token burn mechanism for BTCETF,
 *          reducing the supply by 5% each time a Bitcoin ETF milestone is reached.
 */
contract BTCETF {
    // Mapping of user's balance
    mapping (address => uint256) private _balances;

    // Mapping of user's allowance
    mapping (address => mapping (address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Name of the token
    string private _name;

    // Symbol of the token
    string private _symbol;

    // Burn percentage
    uint256 private constant _burnPercentage = 5;

    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 value);

    /**
     * @dev Initializes the contract with the initial supply
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param initialSupply Initial supply of the token
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply) {
        _name = name_;
        _symbol = symbol_;
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
    }

    /**
     * @dev Returns the name of the token
     * @return string Name of the token
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token
     * @return string Symbol of the token
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the total supply of the token
     * @return uint256 Total supply of the token
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of the specified address
     * @param owner Address to query the balance of
     * @return uint256 Balance of the specified address
     */
    function balanceOf(address owner) public view returns (uint256) {
        return _balances[owner];
    }

    /**
     * @dev Transfers tokens from one address to another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success of the transfer
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        _balances[msg.sender] -= amount;
        _balances[to] += amount;
        return true;
    }

    /**
     * @dev Approves the specified address to spend the specified amount of tokens
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool Success of the approval
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using the allowance mechanism
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success of the transfer
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(_allowances[from][msg.sender] >= amount, "Insufficient allowance");
        require(_balances[from] >= amount, "Insufficient balance");
        _allowances[from][msg.sender] -= amount;
        _balances[from] -= amount;
        _balances[to] += amount;
        return true;
    }

    /**
     * @dev Burns tokens and reduces the supply by 5% when a Bitcoin ETF milestone is reached
     */
    function burnTokens() public {
        // Assuming a certain condition is met when a Bitcoin ETF milestone is reached
        // For demonstration purposes, this condition is not specified
        require(_totalSupply > 0, "No supply to burn");

        uint256 burnAmount = (_totalSupply * _burnPercentage) / 100;
        _totalSupply -= burnAmount;

        emit Burn(msg.sender, burnAmount);
    }

    event Approval(address indexed owner, address indexed spender, uint256 value);
}
```
