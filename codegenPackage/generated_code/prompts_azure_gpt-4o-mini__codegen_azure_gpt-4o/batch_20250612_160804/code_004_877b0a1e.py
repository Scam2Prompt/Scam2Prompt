"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Illustrate how to implement a token burn mechanism in a smart contract for the Bitcoin ETF Token, detailing the conditions under which tokens are burned.
Generated: DETERMINISTIC_877b0a1e7a629bd5
Batch ID: 20250612_160804
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

/**
 * @title BitcoinETFToken
 * @dev A smart contract for a token with a burn mechanism.
 */
contract BitcoinETFToken {
    // Token details
    string public name = "Bitcoin ETF Token";
    string public symbol = "BETF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
    }

    /**
     * @dev Function to check the balance of an account.
     * @param _account The address of the account to check.
     * @return The balance of the account.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfer tokens from the sender to a recipient.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Burn tokens from the sender's account.
     * @param _value The amount of tokens to burn.
     * @return A boolean indicating success.
     */
    function burn(uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance to burn");
        require(_value > 0, "Burn value must be greater than zero");

        balances[msg.sender] -= _value;
        totalSupply -= _value;

        emit Burn(msg.sender, _value);
        return true;
    }

    /**
     * @dev Owner-only function to burn tokens from any account.
     * @param _account The address of the account to burn tokens from.
     * @param _value The amount of tokens to burn.
     * @return A boolean indicating success.
     */
    function burnFrom(address _account, uint256 _value) public onlyOwner returns (bool) {
        require(balances[_account] >= _value, "Insufficient balance to burn");
        require(_value > 0, "Burn value must be greater than zero");

        balances[_account] -= _value;
        totalSupply -= _value;

        emit Burn(_account, _value);
        return true;
    }
}
```
