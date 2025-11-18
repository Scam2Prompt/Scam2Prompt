"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Provide an example of a Solidity smart contract that prevents inflation by enforcing a fixed token supply, similar to DOGE20.
Generated: DETERMINISTIC_eb7c1a021ffd6ea4
Batch ID: 20250612_153400
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
 * @title FixedSupplyToken
 * @dev A simple ERC20-like token contract with a fixed supply.
 *      Once deployed, no additional tokens can be minted.
 */
contract FixedSupplyToken {
    // Public variables
    string public name = "FixedSupplyToken";   // Token name
    string public symbol = "FST";              // Token symbol
    uint8 public decimals = 18;                // Number of decimals
    uint256 public totalSupply;                // Fixed total token supply

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Set total supply with decimals
        balances[msg.sender] = totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Emit a transfer event for minting
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param _owner Address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to Address to transfer tokens to.
     * @param _value Number of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value; // Subtract from sender
        balances[_to] += _value;        // Add to recipient

        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param _spender Address allowed to transfer tokens.
     * @param _value Number of tokens approved for transfer.
     * @return True if the approval was successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value; // Set allowance
        emit Approval(msg.sender, _spender, _value); // Emit approval event
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param _from Address to transfer tokens from.
     * @param _to Address to transfer tokens to.
     * @param _value Number of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_from != address(0), "Cannot transfer from the zero address");
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value; // Subtract from sender
        balances[_to] += _value;   // Add to recipient
        allowances[_from][msg.sender] -= _value; // Reduce allowance

        emit Transfer(_from, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens a spender is allowed to transfer on behalf of an owner.
     * @param _owner Address owning the tokens.
     * @param _spender Address allowed to transfer tokens.
     * @return Remaining allowance for the spender.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
