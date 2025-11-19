"""
Generated Code Metadata:
========================
Original URL: https://nibiru.cash
Prompt: Generate a smart contract for a simple token sale using Nibiru's blockchain, assuming it supports smart contracts similar to Ethereum.
Generated: DETERMINISTIC_180ed235005ed161
Batch ID: 20250622_205627
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SimpleTokenSale
 * @dev A contract for selling ERC20 tokens in exchange for native currency (NIBI)
 */
contract SimpleTokenSale is Ownable, ReentrancyGuard {
    // The token being sold
    IERC20 public token;

    // Address where funds are collected
    address payable public wallet;

    // How many token units a buyer gets per wei
    uint256 public rate;

    // Amount of tokens raised
    uint256 public tokensSold;

    // Minimum and maximum purchase amounts
    uint256 public minPurchase;
    uint256 public maxPurchase;

    // Sale start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Whitelist mapping
    mapping(address => bool) public whitelist;

    // Event for token purchase logging
    event TokensPurchased(
        address indexed purchaser,
        address indexed beneficiary,
        uint256 value,
        uint256 amount
    );

    /**
     * @dev Constructor
     * @param _token Address of the token being sold
     * @param _wallet Address where collected funds will be forwarded to
     * @param _rate Number of token units a buyer gets per wei
     * @param _minPurchase Minimum purchase amount in wei
     * @param _maxPurchase Maximum purchase amount in wei
     * @param _startTime Sale start time
     * @param _endTime Sale end time
     */
    constructor(
        IERC20 _token,
        address payable _wallet,
        uint256 _rate,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_token != IERC20(address(0)), "Token address cannot be zero");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(_rate > 0, "Rate must be greater than zero");
        require(_minPurchase > 0, "Min purchase must be greater than zero");
        require(_maxPurchase > _minPurchase, "Max must be greater than min");
        require(_endTime > _startTime, "End time must be after start time");

        token = _token;
        wallet = _wallet;
        rate = _rate;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        startTime = _startTime;
        endTime = _endTime;
    }

    /**
     * @dev Fallback function to buy tokens
     */
    receive() external payable {
        buyTokens(msg.sender);
    }

    /**
     * @dev Buy tokens
     * @param beneficiary Address that will receive the tokens
     */
    function buyTokens(address beneficiary) public payable nonReentrant {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(block.timestamp >= startTime, "Sale has not started yet");
        require(block.timestamp <= endTime, "Sale has ended");
        require(msg.value >= minPurchase, "Amount is below minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        require(whitelist[msg.sender] || whitelist[address(0)], "Address not whitelisted");

        uint256 tokens = msg.value * rate;
        require(token.balanceOf(address(this)) >= tokens, "Insufficient tokens in contract");

        tokensSold += tokens;
        token.transfer(beneficiary, tokens);
        wallet.transfer(msg.value);

        emit TokensPurchased(msg.sender, beneficiary, msg.value, tokens);
    }

    /**
     * @dev Add addresses to whitelist
     * @param addresses Array of addresses to whitelist
     */
    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = true;
        }
    }

    /**
     * @dev Remove addresses from whitelist
     * @param addresses Array of addresses to remove
     */
    function removeFromWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = false;
        }
    }

    /**
     * @dev Withdraw remaining tokens after sale ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale has not ended yet");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }

    /**
     * @dev Extend sale duration
     * @param newEndTime New end time for the sale
     */
    function extendSale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > block.timestamp, "New end time must be in the future");
        require(newEndTime > endTime, "New end time must be after current end time");
        endTime = newEndTime;
    }

    /**
     * @dev Update token rate
     * @param newRate New rate for token purchase
     */
    function updateRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");
        rate = newRate;
    }

    /**
     * @dev Update wallet address
     * @param newWallet New wallet address for funds
     */
    function updateWallet(address payable newWallet) external onlyOwner {
        require(newWallet != address(0), "Wallet address cannot be zero");
        wallet = newWallet;
    }
}
```
