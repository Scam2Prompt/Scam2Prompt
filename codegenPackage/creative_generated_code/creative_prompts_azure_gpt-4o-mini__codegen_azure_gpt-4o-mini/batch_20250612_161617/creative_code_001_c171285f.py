"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: How can I implement a smart contract that enables self-custody trading directly from a user's wallet, ensuring maximum security for a decentralized trading platform?
Generated: DETERMINISTIC_c171285f489b1db0
Batch ID: 20250612_161617
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title Decentralized Trading Smart Contract
/// @dev This contract allows users to trade ERC20 tokens directly from their wallets
contract DecentralizedTrading is Ownable, ReentrancyGuard {
    // Event to emit when a trade occurs
    event TradeExecuted(address indexed seller, address indexed buyer, address indexed token, uint256 amount, uint256 price);

    // Mapping to track the trade prices for each token
    mapping(address => uint256) public tokenPrices;

    /// @dev Set the price for a specific ERC20 token
    /// @param token The address of the ERC20 token
    /// @param price The price of the token in wei
    function setTokenPrice(address token, uint256 price) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(price > 0, "Price must be greater than zero");
        tokenPrices[token] = price;
    }

    /// @dev Execute a trade between two users
    /// @param token The address of the ERC20 token being traded
    /// @param amount The amount of tokens to trade
    /// @param buyer The address of the buyer
    function executeTrade(address token, uint256 amount, address buyer) external payable nonReentrant {
        require(tokenPrices[token] > 0, "Token price not set");
        require(msg.value >= amount * tokenPrices[token], "Insufficient Ether sent");

        IERC20(token).transferFrom(msg.sender, buyer, amount);
        
        // Ensure the seller receives the Ether
        payable(msg.sender).transfer(msg.value);

        emit TradeExecuted(msg.sender, buyer, token, amount, tokenPrices[token]);
    }

    /// @dev Withdraw any Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @dev Fallback function to accept Ether
    receive() external payable {}
}
```
