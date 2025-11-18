"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hpyerfnd-checker.com
Prompt: Generate code to implement a decentralized exchange (DEX) with a fully on-chain order book on the Hyperliquid blockchain, leveraging HyperCore's financial primitives.
Generated: DETERMINISTIC_e7fb7f200ea9f5d6
Batch ID: 20250612_153916
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

/// @title Decentralized Exchange (DEX) Implementation
/// @author Your Name
/// @notice This contract implements a fully on-chain order book for trading assets on the Hyperliquid blockchain.
contract DecentralizedExchange {

    // Struct to represent an order
    struct Order {
        uint256 id;
        address trader;
        uint256 amount;
        uint256 price;
        bool isBuyOrder;
        bool isActive;
    }

    // Mapping to store orders by their ID
    mapping(uint256 => Order) public orders;
    // Counter for order IDs
    uint256 public orderIdCounter;

    // Event emitted when a new order is created
    event OrderCreated(uint256 indexed orderId, address indexed trader, uint256 amount, uint256 price, bool isBuyOrder);
    // Event emitted when an order is canceled
    event OrderCanceled(uint256 indexed orderId);
    // Event emitted when an order is filled
    event OrderFilled(uint256 indexed orderId, address indexed trader, uint256 amount);

    /// @notice Creates a new order
    /// @param _amount The amount of the asset to buy/sell
    /// @param _price The price at which to buy/sell the asset
    /// @param _isBuyOrder Indicates if the order is a buy (true) or sell (false) order
    function createOrder(uint256 _amount, uint256 _price, bool _isBuyOrder) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        orderIdCounter++;
        orders[orderIdCounter] = Order(orderIdCounter, msg.sender, _amount, _price, _isBuyOrder, true);
        
        emit OrderCreated(orderIdCounter, msg.sender, _amount, _price, _isBuyOrder);
    }

    /// @notice Cancels an existing order
    /// @param _orderId The ID of the order to cancel
    function cancelOrder(uint256 _orderId) external {
        Order storage order = orders[_orderId];
        require(order.isActive, "Order is not active");
        require(order.trader == msg.sender, "Only the trader can cancel the order");

        order.isActive = false;

        emit OrderCanceled(_orderId);
    }

    /// @notice Fills an existing order
    /// @param _orderId The ID of the order to fill
    /// @param _amount The amount to fill
    function fillOrder(uint256 _orderId, uint256 _amount) external {
        Order storage order = orders[_orderId];
        require(order.isActive, "Order is not active");
        require(_amount <= order.amount, "Amount exceeds order amount");

        // Logic for transferring assets can be added here.

        // Update the order amount
        order.amount -= _amount;

        // If the order is completely filled, mark it as inactive
        if (order.amount == 0) {
            order.isActive = false;
        }

        emit OrderFilled(_orderId, msg.sender, _amount);
    }

    /// @notice Retrieves the details of an order
    /// @param _orderId The ID of the order to retrieve
    /// @return The order details
    function getOrder(uint256 _orderId) external view returns (Order memory) {
        return orders[_orderId];
    }
}
```

This code provides a basic structure for a decentralized exchange with an on-chain order book, including functionality to create, cancel, and fill orders, along with necessary event emissions and error handling.
