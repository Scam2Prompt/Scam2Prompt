"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoniclabs.pages.dev
Prompt: Write a Solidity smart contract optimized for deployment on Sonic, the fastest EVM Layer-1 blockchain, leveraging its sub-second confirmation times and low transaction costs.
Generated: DETERMINISTIC_226337f1b32b5126
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title SonicToken
 * @dev A simple ERC20-like token optimized for deployment on Sonic (fast EVM Layer-1 blockchain)
 */
contract SonicToken {
    // Token metadata
    string public name = "SonicToken";
    string public symbol = "SONIC";
    uint8 public decimals = 18; // Standard for ERC20 tokens
    
    // Total token supply
    uint256 public totalSupply;

    // Balances mapping: Tracks the balance of each address
    mapping(address => uint256) private balances;

    // Allowances mapping: Tracks allowed transfers by other addresses
    mapping(address => mapping(address => uint256)) private allowances;

    // Events to log contract interactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor initializes the contract and mints the initial supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10 ** decimals); // Scale by decimals
        balances[msg.sender] = totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Log the minting
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param _owner The address to query the balance of.
     * @return uint256 The balance of the provided address.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer to.
     * @param _value The amount to be transferred.
     * @return bool Returns true if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid recipient");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value; // Deduct from sender
        balances[_to] += _value; // Add to recipient
        emit Transfer(msg.sender, _to, _value); // Log the transfer
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param _spender The address authorized to spend.
     * @param _value The maximum amount they are allowed to spend.
     * @return bool Returns true if the approval is successful.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Invalid spender");

        allowances[msg.sender][_spender] = _value; // Set the allowance
        emit Approval(msg.sender, _spender, _value); // Log the approval
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of another address.
     * @param _from The address to transfer from.
     * @param _to The address to transfer to.
     * @param _value The amount to be transferred.
     * @return bool Returns true if the transfer is successful.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_from != address(0), "Invalid sender");
        require(_to != address(0), "Invalid recipient");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value; // Deduct from sender
        balances[_to] += _value; // Add to recipient
        allowances[_from][msg.sender] -= _value; // Reduce allowance
        emit Transfer(_from, _to, _value); // Log the transfer
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens the spender is allowed to spend.
     * @param _owner The address that owns the tokens.
     * @param _spender The address authorized to spend the tokens.
     * @return uint256 The remaining amount the spender is allowed to spend.
     */
    function allowance(
        address _owner,
        address _spender
    ) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
