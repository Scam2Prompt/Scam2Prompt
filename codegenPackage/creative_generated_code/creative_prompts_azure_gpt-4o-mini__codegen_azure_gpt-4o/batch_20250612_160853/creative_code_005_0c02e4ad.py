"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Describe how to build a decentralized application (dApp) on Berachain using its modular EVM-compatible features.
Generated: DETERMINISTIC_0c02e4adde49c211
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title SimpleToken
 * @dev A decentralized application (dApp) example on Berachain using its EVM-compatible features.
 * This contract creates a basic ERC-20 token.
 */
contract SimpleToken {
    // State variables to store token details
    string public name = "BerachainToken";
    string public symbol = "BCHT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Mapping for allowances (for token transfer delegation)
    mapping(address => mapping(address => uint256)) public allowances;

    // Events for logging transactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token with a fixed supply.
     * @param _initialSupply Total supply of the token to be minted at deployment.
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than 0");
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Function to transfer tokens.
     * @param _to Recipient address.
     * @param _value Number of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the owner.
     * @param _spender Address authorized to spend the tokens.
     * @param _value Number of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of an owner.
     * @param _from Address of the owner.
     * @param _to Recipient address.
     * @param _value Number of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
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
     * @dev Function to check the balance of a given address.
     * @param _owner Address to query.
     * @return The balance of the queried address.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Function to check the allowance of a spender for a given owner.
     * @param _owner Address of the token owner.
     * @param _spender Address of the authorized spender.
     * @return The remaining allowance for the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
