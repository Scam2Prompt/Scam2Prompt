"""
Generated Code Metadata:
========================
Original URL: https://berachain.pumpevm.net
Prompt: "Create a simple blockchain-based token using BeraChain's technology and PumpEVM's smart contract functionality."
Generated: DETERMINISTIC_eacb076b6f667a23
Batch ID: 20250622_211811
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
 * @title SimpleToken
 * @dev A basic ERC-20-like token implementation using PumpEVM's smart contract functionality.
 *      This contract is designed to work on BeraChain's blockchain.
 */
contract SimpleToken {
    // Token metadata
    string public name = "SimpleToken";
    string public symbol = "STKN";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging important actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token with a fixed supply.
     * @param _initialSupply The initial supply of tokens to mint.
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _owner The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param _spender The address authorized to spend the tokens.
     * @param _value The amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend on behalf of the owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
