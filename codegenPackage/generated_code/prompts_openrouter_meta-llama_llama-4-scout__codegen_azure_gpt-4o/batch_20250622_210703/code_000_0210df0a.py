"""
Generated Code Metadata:
========================
Original URL: https://mollars-in.web.app
Prompt: Write a smart contract for a decentralized token on the Ethereum blockchain, similar to the Mollars token, including a function for token distribution and rewards.
Generated: DETERMINISTIC_0210df0a106346aa
Batch ID: 20250622_210703
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
 * @title MollarsToken
 * @dev A decentralized ERC20 token with distribution and rewards functionality.
 */
contract MollarsToken {
    // Token details
    string public name = "MollarsToken";
    string public symbol = "MOLL";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) public balanceOf;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event RewardDistributed(address indexed to, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token and set the total supply.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from the caller to a recipient.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the caller.
     * @param _spender The address authorized to spend.
     * @param _value The amount of tokens to approve.
     * @return success True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from The address to transfer from.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Distribute rewards to a specific address.
     * @param _to The recipient address.
     * @param _value The amount of tokens to distribute as rewards.
     * @return success True if the distribution is successful.
     */
    function distributeReward(address _to, uint256 _value) public onlyOwner returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[owner] >= _value, "Insufficient balance in owner account");

        balanceOf[owner] -= _value;
        balanceOf[_to] += _value;

        emit RewardDistributed(_to, _value);
        return true;
    }
}
```
