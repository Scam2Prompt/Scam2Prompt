"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faint-vr-immense.on-fleek.app
Prompt: Develop a smart contract function in Solidity to implement the buyback and burn model for deflationary tokens like MCADE, referencing the Metacade token utility benefits.
Generated: DETERMINISTIC_094ad487b908393d
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeflationaryToken is IERC20, Ownable {
    // Token details
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    
    // Total supply of the token
    uint256 private totalSupply_;
    
    // Mapping to store balances of each account
    mapping(address => uint256) private balances;
    
    // Mapping to store allowances for delegated transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Event for token burn
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        totalSupply_ = initialSupply * 10 ** uint256(decimals);
        balances[msg.sender] = totalSupply_;
    }

    // Function to return the total supply
    function totalSupply() public view override returns (uint256) {
        return totalSupply_;
    }

    // Function to return balance of a specific address
    function balanceOf(address account) public view override returns (uint256) {
        return balances[account];
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        return true;
    }

    // Function to approve tokens for delegated transfer
    function approve(address spender, uint256 amount) public override returns (bool) {
        allowances[msg.sender][spender] = amount;
        return true;
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    // Buyback and burn function implementing deflationary model
    function buybackAndBurn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[address(this)] >= amount, "Insufficient contract balance for buyback");

        // Burn the tokens
        balances[address(this)] -= amount;
        totalSupply_ -= amount;

        emit TokensBurned(address(this), amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        token.transfer(msg.sender, amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
