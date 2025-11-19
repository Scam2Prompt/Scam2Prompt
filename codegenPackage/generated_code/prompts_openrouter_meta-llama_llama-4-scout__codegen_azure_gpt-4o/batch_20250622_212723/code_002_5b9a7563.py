"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Develop a simple smart contract in Solidity to manage the token deployment and staking process for a cryptocurrency like $MIND.
Generated: DETERMINISTIC_5b9a756379809403
Batch ID: 20250622_212723
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
 * @title TokenStaking
 * @dev A simple smart contract for token deployment and staking.
 */
contract TokenStaking {
    // Token details
    string public name = "MindToken";
    string public symbol = "MIND";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and staked amounts
    mapping(address => uint256) public balances;
    mapping(address => uint256) public stakedBalances;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Address of the recipient.
     * @param _amount Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Stake tokens to the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance to stake");

        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance to unstake");

        stakedBalances[msg.sender] -= _amount;
        balances[msg.sender] += _amount;

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @dev Mint new tokens to the owner's balance.
     * @param _amount Amount of tokens to mint.
     */
    function mint(uint256 _amount) external onlyOwner {
        uint256 mintAmount = _amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[owner] += mintAmount;

        emit Transfer(address(0), owner, mintAmount);
    }

    /**
     * @dev Burn tokens from the owner's balance.
     * @param _amount Amount of tokens to burn.
     */
    function burn(uint256 _amount) external onlyOwner {
        uint256 burnAmount = _amount * (10 ** uint256(decimals));
        require(balances[owner] >= burnAmount, "Insufficient balance to burn");

        totalSupply -= burnAmount;
        balances[owner] -= burnAmount;

        emit Transfer(owner, address(0), burnAmount);
    }
}
```
