"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Design a smart contract for a Hash AI token, where income from AI-enhanced mining rigs is shared with token holders, using Solidity or another suitable programming language.
Generated: DETERMINISTIC_c5b7d96437f653cb
Batch ID: 20250622_205919
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
 * @title HashAIToken
 * @dev A smart contract for distributing income from AI-enhanced mining rigs to token holders.
 */
contract HashAIToken {
    // Token details
    string public name = "Hash AI Token";
    string public symbol = "HAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of token holders
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) public allowance;

    // Income pool for distribution
    uint256 public incomePool;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event IncomeDistributed(uint256 amount, uint256 totalSupply);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
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
     * @dev Approve a spender to transfer tokens on behalf of the sender.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Address to transfer tokens from.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
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
     * @dev Add income to the pool for distribution.
     * @param _amount Amount of income to add.
     */
    function addIncome(uint256 _amount) public payable onlyOwner {
        require(msg.value == _amount, "Incorrect value sent");
        incomePool += _amount;
    }

    /**
     * @dev Distribute income from the pool to token holders proportionally.
     */
    function distributeIncome() public onlyOwner {
        require(incomePool > 0, "No income to distribute");
        require(totalSupply > 0, "No tokens in circulation");

        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i)); // Simulated holder address
            uint256 holderBalance = balanceOf[holder];
            uint256 share = (incomePool * holderBalance) / totalSupply;
            payable(holder).transfer(share);
        }

        emit IncomeDistributed(incomePool, totalSupply);
        incomePool = 0;
    }
}
```
