"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-token.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary token similar to $GFOX, incorporating a burn mechanism that reduces the circulating supply with each transaction.
Generated: DETERMINISTIC_09d526b60ca4e148
Batch ID: 20250612_151024
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
 * @title DeflationaryToken
 * @dev A simple ERC20 token with a burn mechanism that reduces the total supply with each transaction.
 */
contract DeflationaryToken {
    string public name; // Token name
    string public symbol; // Token symbol
    uint8 public decimals; // Number of decimal places
    uint256 public totalSupply; // Total token supply

    mapping(address => uint256) private balances; // Mapping of balances for each address
    mapping(address => mapping(address => uint256)) private allowed; // Mapping for allowances

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token with a name, symbol, and total supply.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _totalSupply The total supply of tokens created.
     * @param _decimals The number of decimals for the token.
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply, uint8 _decimals) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply * (10 ** uint256(_decimals)); // Adjust for decimals
        decimals = _decimals;
        balances[msg.sender] = totalSupply; // Assign total supply to the contract creator
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param _owner The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens from the caller's account to another account, with a burn mechanism.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address"); // Ensure recipient is not zero address
        require(balances[msg.sender] >= _value, "Insufficient balance"); // Ensure sender has enough balance

        uint256 burnAmount = _value / 100; // Calculate 1% burn
        uint256 sendAmount = _value - burnAmount; // Amount to send after burn

        // Update balances
        balances[msg.sender] -= _value; 
        balances[_to] += sendAmount; 
        totalSupply -= burnAmount; // Reduce total supply

        emit Transfer(msg.sender, _to, sendAmount); // Emit transfer event
        emit Transfer(msg.sender, address(0), burnAmount); // Emit burn event

        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param _spender The address of the spender.
     * @param _value The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Invalid address"); // Ensure spender is not zero address
        allowed[msg.sender][_spender] = _value; // Set allowance

        emit Approval(msg.sender, _spender, _value); // Emit approval event
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism, with a burn.
     * @param _from The address of the sender.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address"); // Ensure recipient is not zero address
        require(balances[_from] >= _value, "Insufficient balance"); // Ensure sender has enough balance
        require(allowed[_from][msg.sender] >= _value, "Allowance exceeded"); // Ensure allowance is sufficient

        uint256 burnAmount = _value / 100; // Calculate 1% burn
        uint256 sendAmount = _value - burnAmount; // Amount to send after burn

        // Update balances
        balances[_from] -= _value; 
        balances[_to] += sendAmount; 
        totalSupply -= burnAmount; // Reduce total supply
        allowed[_from][msg.sender] -= _value; // Decrease allowance

        emit Transfer(_from, _to, sendAmount); // Emit transfer event
        emit Transfer(_from, address(0), burnAmount); // Emit burn event

        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend on behalf of an owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowed[_owner][_spender];
    }
}
```
