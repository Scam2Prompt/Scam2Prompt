"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Design a simple smart contract for a token presale using Solidity that includes functionality similar to the BOI token sale.
Generated: DETERMINISTIC_0bca525deca85d7c
Batch ID: 20250622_205158
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenPresale
 * @dev A simple token presale contract
 */
contract TokenPresale is Ownable {
    // The token being sold
    IERC20 public token;

    // Address where funds are collected
    address payable public wallet;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Rate of tokens per ether
    uint256 public rate;

    // Presale start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Event for token purchase
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract
     * @param _token Address of the token being sold
     * @param _wallet Address where funds will be collected
     * @param _rate Rate of tokens per ether
     * @param _startTime Start time of the presale
     * @param _endTime End time of the presale
     */
    constructor(
        IERC20 _token,
        address payable _wallet,
        uint256 _rate,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        require(_startTime < _endTime, "Start time must be before end time");

        token = _token;
        wallet = _wallet;
        rate = _rate;
        startTime = _startTime;
        endTime = _endTime;
    }

    /**
     * @dev Fallback function to accept ether and purchase tokens
     */
    receive() external payable {
        buyTokens(msg.sender);
    }

    /**
     * @dev Function to buy tokens
     * @param beneficiary Address of the token purchaser
     */
    function buyTokens(address beneficiary) public payable {
        require(block.timestamp >= startTime, "Presale has not started yet");
        require(block.timestamp <= endTime, "Presale has ended");
        require(msg.value > 0, "Ether value must be greater than 0");

        uint256 tokens = msg.value * rate;
        tokensSold += tokens;

        // Transfer tokens to the purchaser
        require(token.balanceOf(address(this)) >= tokens, "Not enough tokens in the contract");
        token.transfer(beneficiary, tokens);

        // Forward funds to the wallet
        wallet.transfer(msg.value);

        emit TokensPurchased(beneficiary, msg.value, tokens);
    }

    /**
     * @dev Function to withdraw unsold tokens after the presale
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Presale has not ended yet");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Function to change the wallet address
     * @param newWallet New wallet address
     */
    function changeWallet(address payable newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet address cannot be zero");
        wallet = newWallet;
    }
}
```
