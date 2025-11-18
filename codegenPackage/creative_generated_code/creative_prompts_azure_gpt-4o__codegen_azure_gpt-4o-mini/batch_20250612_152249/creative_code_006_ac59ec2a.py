"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Develop a smart contract in Solidity to facilitate decentralized commodity trading (e.g., Gold, Silver, Coffee) on the CVEX platform using USDC as collateral.
Generated: DETERMINISTIC_ac59ec2adfb81bc0
Batch ID: 20250612_152249
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

/**
 * @title CommodityTrading
 * @dev A smart contract for decentralized commodity trading using USDC as collateral.
 */
contract CommodityTrading is Ownable {
    // Define an event for trade creation
    event TradeCreated(
        uint256 indexed tradeId,
        address indexed seller,
        address indexed buyer,
        string commodity,
        uint256 amount,
        uint256 price,
        uint256 collateral
    );

    event TradeExecuted(uint256 indexed tradeId);
    event TradeCancelled(uint256 indexed tradeId);

    struct Trade {
        uint256 id;                   // Unique identifier for the trade
        address seller;               // Seller's address
        address buyer;                // Buyer's address
        string commodity;             // Type of commodity
        uint256 amount;               // Amount of commodity being traded
        uint256 price;                // Price per unit of commodity in USDC
        uint256 collateral;           // Amount of USDC collateral
        bool executed;                // Status of the trade
        bool cancelled;               // Cancellation status
    }

    IERC20 public usdc;                 // USDC token interface
    Trade[] public trades;              // Array to store trades
    uint256 public nextTradeId;        // Counter for next trade ID

    /**
     * @dev Constructor to set the USDC token address.
     * @param _usdcAddress Address of the USDC token contract.
     */
    constructor(address _usdcAddress) {
        usdc = IERC20(_usdcAddress);
        nextTradeId = 1; // Start trade IDs from 1
    }

    /**
     * @dev Create a new trade.
     * @param _commodity Commodity type (e.g., "Gold").
     * @param _amount Amount of commodity.
     * @param _price Price per unit in USDC.
     * @param _collateral Amount of USDC collateral.
     */
    function createTrade(
        string memory _commodity,
        uint256 _amount,
        uint256 _price,
        uint256 _collateral
    ) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");
        require(_collateral > 0, "Collateral must be greater than zero");

        // Transfer collateral from seller to contract
        usdc.transferFrom(msg.sender, address(this), _collateral);

        // Create a new trade
        trades.push(Trade({
            id: nextTradeId,
            seller: msg.sender,
            buyer: address(0),
            commodity: _commodity,
            amount: _amount,
            price: _price,
            collateral: _collateral,
            executed: false,
            cancelled: false
        }));

        emit TradeCreated(nextTradeId, msg.sender, address(0), _commodity, _amount, _price, _collateral);
        nextTradeId++;
    }

    /**
     * @dev Execute the trade.
     * @param _tradeId ID of the trade to execute.
     */
    function executeTrade(uint256 _tradeId) external {
        // Retrieve the trade
        Trade storage trade = trades[_tradeId - 1];

        require(trade.id == _tradeId, "Trade does not exist");
        require(!trade.executed, "Trade already executed");
        require(!trade.cancelled, "Trade has been cancelled");
        require(msg.sender != trade.seller, "Seller cannot execute their own trade");

        // Transfer USDC from buyer to seller
        uint256 totalPrice = trade.amount * trade.price;
        usdc.transferFrom(msg.sender, trade.seller, totalPrice);

        // Transfer collateral back to buyer
        usdc.transfer(msg.sender, trade.collateral);

        // Mark trade as executed
        trade.buyer = msg.sender;
        trade.executed = true;

        emit TradeExecuted(_tradeId);
    }

    /**
     * @dev Cancel an existing trade.
     * @param _tradeId ID of the trade to cancel.
     */
    function cancelTrade(uint256 _tradeId) external {
        // Retrieve the trade
        Trade storage trade = trades[_tradeId - 1];

        require(trade.id == _tradeId, "Trade does not exist");
        require(msg.sender == trade.seller, "Only seller can cancel the trade");
        require(!trade.executed, "Cannot cancel an executed trade");
        require(!trade.cancelled, "Trade has already been cancelled");

        // Mark trade as cancelled
        trade.cancelled = true;

        // Refund collateral to seller
        usdc.transfer(msg.sender, trade.collateral);

        emit TradeCancelled(_tradeId);
    }

    /**
     * @dev Retrieve trade details.
     * @param _tradeId ID of the trade to retrieve.
     * @return Trade object.
     */
    function getTrade(uint256 _tradeId) external view returns (Trade memory) {
        require(_tradeId > 0 && _tradeId < nextTradeId, "Trade does not exist");
        return trades[_tradeId - 1];
    }
}
```
