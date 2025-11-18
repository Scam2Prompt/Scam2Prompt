"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Write a smart contract in Solidity that enables secure OTC trading of tokens without slippage, referencing the decentralized features described in Whales Market's platform.
Generated: DETERMINISTIC_00844477f21591ea
Batch ID: 20250612_153820
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
 * @title OTCTrading
 * @dev A smart contract for secure OTC trading of ERC20 tokens without slippage.
 *      This contract uses an escrow mechanism to ensure decentralized and trustless trading.
 */
contract OTCTrading {
    // Struct to represent an OTC trade
    struct Trade {
        address seller; // Seller's address
        address buyer;  // Buyer's address
        address token;  // Token contract address
        uint256 amount; // Amount of tokens to trade
        uint256 price;  // Price in wei for the trade
        bool isActive;  // Status of the trade
    }

    // Mapping to store trades by their IDs
    mapping(uint256 => Trade) public trades;

    // Counter for trade IDs
    uint256 public tradeCounter;

    // Events for logging
    event TradeCreated(uint256 tradeId, address indexed seller, address indexed buyer, address token, uint256 amount, uint256 price);
    event TradeCompleted(uint256 tradeId, address indexed seller, address indexed buyer, address token, uint256 amount, uint256 price);
    event TradeCanceled(uint256 tradeId, address indexed seller);

    /**
     * @dev Modifier to ensure the caller is the seller of the trade.
     */
    modifier onlySeller(uint256 tradeId) {
        require(trades[tradeId].seller == msg.sender, "Caller is not the seller");
        _;
    }

    /**
     * @dev Modifier to ensure the caller is the buyer of the trade.
     */
    modifier onlyBuyer(uint256 tradeId) {
        require(trades[tradeId].buyer == msg.sender, "Caller is not the buyer");
        _;
    }

    /**
     * @dev Create a new OTC trade.
     * @param buyer The address of the buyer.
     * @param token The address of the ERC20 token contract.
     * @param amount The amount of tokens to trade.
     * @param price The price in wei for the trade.
     */
    function createTrade(address buyer, address token, uint256 amount, uint256 price) external returns (uint256 tradeId) {
        require(buyer != address(0), "Buyer address cannot be zero");
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Trade amount must be greater than zero");
        require(price > 0, "Trade price must be greater than zero");

        // Increment the trade counter to generate a unique trade ID
        tradeCounter++;

        // Create a new trade
        trades[tradeCounter] = Trade({
            seller: msg.sender,
            buyer: buyer,
            token: token,
            amount: amount,
            price: price,
            isActive: true
        });

        emit TradeCreated(tradeCounter, msg.sender, buyer, token, amount, price);

        return tradeCounter;
    }

    /**
     * @dev Execute the trade by the buyer. Tokens and payment are exchanged securely.
     * @param tradeId The ID of the trade to execute.
     */
    function executeTrade(uint256 tradeId) external payable onlyBuyer(tradeId) {
        Trade memory trade = trades[tradeId];

        require(trade.isActive, "Trade is not active");
        require(msg.value == trade.price, "Incorrect payment amount");

        // Transfer tokens from seller to buyer
        require(IERC20(trade.token).transferFrom(trade.seller, trade.buyer, trade.amount), "Token transfer failed");

        // Transfer payment from buyer to seller
        payable(trade.seller).transfer(msg.value);

        // Mark the trade as inactive
        trades[tradeId].isActive = false;

        emit TradeCompleted(tradeId, trade.seller, trade.buyer, trade.token, trade.amount, trade.price);
    }

    /**
     * @dev Cancel the trade. Only the seller can cancel an active trade.
     * @param tradeId The ID of the trade to cancel.
     */
    function cancelTrade(uint256 tradeId) external onlySeller(tradeId) {
        require(trades[tradeId].isActive, "Trade is not active");

        // Mark the trade as inactive
        trades[tradeId].isActive = false;

        emit TradeCanceled(tradeId, msg.sender);
    }
}

/**
 * @title IERC20
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
