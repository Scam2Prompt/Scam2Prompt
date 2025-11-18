"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remixide.ist
Prompt: Write a Solidity smart contract using Remix IDE that includes a function for transferring tokens between two addresses.
Generated: DETERMINISTIC_13eef52c857a72dc
Batch ID: 20250612_153710
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
 * @title ERC20Token
 * @dev A simple ERC20 token contract that allows token transfers between addresses.
 */
contract ERC20Token {
    // State variables
    string public name = "ExampleToken";
    string public symbol = "EXT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances of each address
    mapping(address => uint256) private balances;

    // Mapping for allowances (approval mechanism)
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the total supply and assign it to the deployer.
     * @param _initialSupply Initial number of tokens to mint.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10**uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param _owner Address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Function to transfer tokens to a specified address.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        // Emit the Transfer event
        emit Transfer(msg.sender, _to, _value);

        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param _spender Address to grant spending rights to.
     * @param _value Amount of tokens to approve.
     * @return Success status of the approval.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;

        // Emit the Approval event
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of an owner, using an allowance.
     * @param _from Address holding the tokens.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Perform the transfer
        balances[_from] -= _value;
        balances[_to] += _value;

        // Deduct the allowance
        allowances[_from][msg.sender] -= _value;

        // Emit the Transfer event
        emit Transfer(_from, _to, _value);

        return true;
    }

    /**
     * @dev Function to check the remaining allowance for a spender.
     * @param _owner Address of the token holder.
     * @param _spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
