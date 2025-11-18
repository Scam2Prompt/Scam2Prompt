"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale with a cap of 1000 ETH, where 0.1 ETH equals 99,500 tokens, similar to the DOG token presale described on the webpage. Include functionality for wallet connection and deposit tracking.
Generated: DETERMINISTIC_b8cf658382912790
Batch ID: 20250612_153420
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

contract TokenPresale is Ownable {
    // Constants
    uint256 public constant TOKEN_RATE = 99500; // Tokens per 0.1 ETH
    uint256 public constant CAP = 1000 ether; // Presale cap in ETH
    uint256 public totalRaised; // Total amount raised in ETH
    IERC20 public token; // Token being sold
    mapping(address => uint256) public deposits; // Track deposits by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Withdrawal(address indexed owner, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to buy tokens
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= CAP, "Presale cap reached");

        // Calculate tokens to mint
        uint256 tokensToMint = (msg.value * TOKEN_RATE) / 0.1 ether;
        deposits[msg.sender] += msg.value; // Track individual deposits
        totalRaised += msg.value; // Update total raised

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokensToMint), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToMint);
    }

    // Function to withdraw funds by the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
        emit Withdrawal(owner(), balance);
    }

    // Function to check the presale status
    function getPresaleStatus() external view returns (uint256, uint256) {
        return (totalRaised, CAP);
    }
}
```
