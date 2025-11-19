"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that enables decentralized leveraged trading for crypto, forex, and commodities, similar to the functionality described on the gTrade platform. Ensure the contract supports self-custody and permissionless access.
Generated: DETERMINISTIC_29d66fba11217f22
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the price feed (e.g., Chainlink)
interface IPriceFeed {
    function getLatestPrice() external view returns (int);
}

// Leveraged Trading Smart Contract
contract LeveragedTrading is Ownable {
    using SafeMath for uint256;

    // Struct to hold trade information
    struct Trade {
        address trader;
        uint256 amount;
        uint256 leverage;
        uint256 entryPrice;
        bool isOpen;
    }

    // Mapping to store trades by trader address
    mapping(address => Trade) public trades;

    // Price feed for the asset being traded
    IPriceFeed public priceFeed;

    // Event emitted when a trade is opened
    event TradeOpened(address indexed trader, uint256 amount, uint256 leverage, uint256 entryPrice);
    
    // Event emitted when a trade is closed
    event TradeClosed(address indexed trader, uint256 profitOrLoss);

    // Constructor to set the price feed address
    constructor(address _priceFeed) {
        priceFeed = IPriceFeed(_priceFeed);
    }

    // Function to open a leveraged trade
    function openTrade(uint256 amount, uint256 leverage) external {
        require(amount > 0, "Amount must be greater than 0");
        require(leverage > 1 && leverage <= 100, "Leverage must be between 2 and 100");

        // Get the current price of the asset
        int price = priceFeed.getLatestPrice();
        require(price > 0, "Invalid price");

        // Create a new trade
        trades[msg.sender] = Trade({
            trader: msg.sender,
            amount: amount,
            leverage: leverage,
            entryPrice: uint256(price),
            isOpen: true
        });

        emit TradeOpened(msg.sender, amount, leverage, uint256(price));
    }

    // Function to close a trade
    function closeTrade() external {
        Trade storage trade = trades[msg.sender];
        require(trade.isOpen, "No open trade found");

        // Get the current price of the asset
        int price = priceFeed.getLatestPrice();
        require(price > 0, "Invalid price");

        // Calculate profit or loss
        uint256 exitPrice = uint256(price);
        uint256 profitOrLoss = (exitPrice.sub(trade.entryPrice)).mul(trade.amount).mul(trade.leverage).div(trade.entryPrice);

        // Mark the trade as closed
        trade.isOpen = false;

        emit TradeClosed(msg.sender, profitOrLoss);
    }

    // Function to get the current trade details
    function getTradeDetails() external view returns (Trade memory) {
        return trades[msg.sender];
    }

    // Function to withdraw funds (if applicable)
    function withdrawFunds(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
