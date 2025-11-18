"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiro.pages.dev
Prompt: Write a smart contract in Solidity for an Ethereum-based token similar to $neiro, including functionality for rewarding participants in the project.
Generated: DETERMINISTIC_c57811e2ea7d846a
Batch ID: 20250612_151811
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
 * @title NeiroToken
 * @dev An ERC-20-like token contract with reward functionality for participants.
 */
contract NeiroToken {
    // State variables
    string public name = "NeiroToken";
    string public symbol = "NEIRO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Used to track rewarded participants
    mapping(address => uint256) public rewards;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Reward(address indexed participant, uint256 value);

    // Constructor to initialize the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Transfer function to move tokens between accounts
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Invalid recipient address"); // Prevent sending to zero address
        require(_value <= balanceOf[msg.sender], "Insufficient balance"); // Ensure sender has enough tokens

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Approve a spender to use tokens on behalf of the owner
    function approve(address _spender, uint256 _value) external returns (bool success) {
        require(_spender != address(0), "Invalid spender address"); // Prevent approving zero address

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Transfer tokens on behalf of an owner
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Invalid recipient address"); // Prevent sending to zero address
        require(_value <= balanceOf[_from], "Insufficient balance"); // Ensure sender has enough tokens
        require(_value <= allowance[_from][msg.sender], "Transfer exceeds allowance"); // Ensure amount is within allowance

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    // Reward participants with additional tokens
    function reward(address _participant, uint256 _value) external returns (bool success) {
        require(_participant != address(0), "Invalid participant address"); // Prevent rewarding zero address
        require(_value > 0, "Reward value must be greater than zero");

        // Mint new tokens for reward
        totalSupply += _value;
        balanceOf[_participant] += _value;
        rewards[_participant] += _value; // Track rewards for participant

        emit Reward(_participant, _value);
        emit Transfer(address(0), _participant, _value);
        return true;
    }
}
```
