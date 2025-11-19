"""
Generated Code Metadata:
========================
Original URL: https://register-doublezero.com
Prompt: Generate an example of a smart contract that leverages the high bandwidth and low latency offered by DoubleZero's infrastructure.
Generated: DETERMINISTIC_fcd0c6a8fb20926f
Batch ID: 20250612_162701
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
 * @title HighFrequencyTradingContract
 * @dev A smart contract demonstrating high-frequency operations leveraging DoubleZero's infrastructure
 * @notice This contract includes features for rapid order placement and cancellation with minimal latency
 */
contract HighFrequencyTradingContract {
    // Struct to represent an order
    struct Order {
        address trader;
        uint256 amount;
        uint256 price;
        bool isBuy;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping to store orders by their IDs
    mapping(uint256 => Order) public orders;
    
    // Counter for order IDs
    uint256 public orderIdCounter;
    
    // Event emitted when a new order is placed
    event OrderPlaced(
        uint256 indexed orderId,
        address indexed trader,
        uint256 amount,
        uint256 price,
        bool isBuy,
        uint256 timestamp
    );
    
    // Event emitted when an order is canceled
    event OrderCanceled(uint256 indexed orderId, uint256 timestamp);
    
    // Event emitted when an order is executed
    event OrderExecuted(
        uint256 indexed orderId,
        address indexed buyer,
        address indexed seller,
        uint256 amount,
        uint256 price,
        uint256 timestamp
    );

    /**
     * @dev Place a new order
     * @param amount The amount of tokens to trade
     * @param price The price per token
     * @param isBuy Whether this is a buy order
     */
    function placeOrder(uint256 amount, uint256 price, bool isBuy) external {
        require(amount > 0, "Amount must be positive");
        require(price > 0, "Price must be positive");
        
        uint256 orderId = orderIdCounter++;
        orders[orderId] = Order({
            trader: msg.sender,
            amount: amount,
            price: price,
            isBuy: isBuy,
            timestamp: block.timestamp,
            isActive: true
        });
        
        emit OrderPlaced(orderId, msg.sender, amount, price, isBuy, block.timestamp);
        
        // Try to match orders immediately
        _matchOrders(orderId);
    }

    /**
     * @dev Cancel an existing order
     * @param orderId The ID of the order to cancel
     */
    function cancelOrder(uint256 orderId) external {
        Order storage order = orders[orderId];
        require(order.isActive, "Order is not active");
        require(order.trader == msg.sender, "Only order owner can cancel");
        
        order.isActive = false;
        emit OrderCanceled(orderId, block.timestamp);
    }

    /**
     * @dev Internal function to match orders
     * @param newOrderId The ID of the newly placed order
     */
    function _matchOrders(uint256 newOrderId) internal {
        Order storage newOrder = orders[newOrderId];
        if (!newOrder.isActive) return;
        
        // Iterate through orders to find matches
        for (uint256 i = 0; i < orderIdCounter; i++) {
            Order storage existingOrder = orders[i];
            
            // Skip if order doesn't exist, isn't active, or is the same order
            if (existingOrder.trader == address(0) || !existingOrder.isActive || i == newOrderId) {
                continue;
            }
            
            // Check for matching conditions (opposite sides, same price)
            if (existingOrder.isBuy != newOrder.isBuy && existingOrder.price == newOrder.price) {
                uint256 matchedAmount = newOrder.amount < existingOrder.amount 
                    ? newOrder.amount 
                    : existingOrder.amount;
                
                // Execute the trade
                if (matchedAmount > 0) {
                    // Update order amounts
                    newOrder.amount -= matchedAmount;
                    existingOrder.amount -= matchedAmount;
                    
                    // Deactivate orders if fully filled
                    if (newOrder.amount == 0) newOrder.isActive = false;
                    if (existingOrder.amount == 0) existingOrder.isActive = false;
                    
                    // Determine buyer and seller
                    address buyer = newOrder.isBuy ? newOrder.trader : existingOrder.trader;
                    address seller = newOrder.isBuy ? existingOrder.trader : newOrder.trader;
                    
                    emit OrderExecuted(
                        newOrderId,
                        buyer,
                        seller,
                        matchedAmount,
                        newOrder.price,
                        block.timestamp
                    );
                    
                    // If new order is fully filled, break the loop
                    if (!newOrder.isActive) break;
                }
            }
        }
    }

    /**
     * @dev Get order details
     * @param orderId The ID of the order to query
     * @return Order details
     */
    function getOrder(uint256 orderId) external view returns (
        address trader,
        uint256 amount,
        uint256 price,
        bool isBuy,
        uint256 timestamp,
        bool isActive
    ) {
        Order storage order = orders[orderId];
        require(order.trader != address(0), "Order does not exist");
        
        return (
            order.trader,
            order.amount,
            order.price,
            order.isBuy,
            order.timestamp,
            order.isActive
        );
    }
}
```
