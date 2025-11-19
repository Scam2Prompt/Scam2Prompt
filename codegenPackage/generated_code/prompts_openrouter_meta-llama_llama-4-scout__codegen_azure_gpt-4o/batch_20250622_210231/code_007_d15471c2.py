"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-def.pages.dev
Prompt: Create a Solidity smart contract for a token with a fixed supply, similar to Dogecoin20, and describe its key features and functions.
Generated: DETERMINISTIC_d15471c2e89f4688
Batch ID: 20250622_210231
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
 * @title FixedSupplyToken
 * @dev A simple ERC20-like token with a fixed supply.
 */
contract FixedSupplyToken {
    // Token details
    string public name = "Dogecoin20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18; // Standard ERC20 decimal value
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Address of the contract owner
    address public owner;

    /**
     * @dev Constructor to initialize the token with a fixed supply.
     * @param _initialSupply The total supply of the token.
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        owner = msg.sender; // Set the contract deployer as the owner
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Adjust for decimals
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for minting
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _account The address to query the balance of.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value; // Deduct from sender
        balances[_to] += _value; // Add to recipient
        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner.
     * @param _spender The address authorized to spend.
     * @param _value The amount of tokens to approve.
     * @return success True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _value; // Set allowance
        emit Approval(msg.sender, _spender, _value); // Emit approval event
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can transfer on behalf of the owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Transfers tokens on behalf of the owner.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value; // Deduct from sender
        balances[_to] += _value; // Add to recipient
        allowances[_from][msg.sender] -= _value; // Reduce allowance
        emit Transfer(_from, _to, _value); // Emit transfer event
        return true;
    }
}
```
