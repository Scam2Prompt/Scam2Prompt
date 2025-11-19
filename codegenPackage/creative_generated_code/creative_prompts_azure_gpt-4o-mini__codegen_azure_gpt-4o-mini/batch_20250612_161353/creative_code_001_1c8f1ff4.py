"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market.pages.dev
Prompt: How can I implement a feature that allows users to cancel orders and claim seller collateral in a decentralized marketplace like Whales Market?
Generated: DETERMINISTIC_1c8f1ff4887a826a
Batch ID: 20250612_161353
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

contract WhalesMarket {
    enum OrderStatus { Open, Canceled, Completed }

    struct Order {
        address seller;
        address buyer;
        uint256 price;
        OrderStatus status;
        uint256 collateral;
    }

    // Mapping to store orders by ID
    mapping(uint256 => Order) public orders;
    // Counter for order IDs
    uint256 public orderCount;

    // Event declarations for logging
    event OrderCreated(uint256 orderId, address seller, uint256 price, uint256 collateral);
    event OrderCanceled(uint256 orderId);
    event CollateralClaimed(uint256 orderId, address seller, uint256 amount);

    // Modifier to check if the caller is the seller
    modifier onlySeller(uint256 _orderId) {
        require(msg.sender == orders[_orderId].seller, "Only seller can perform this action");
        _;
    }

    // Function to create a new order
    function createOrder(uint256 _price, uint256 _collateral) external {
        require(_price > 0, "Price must be greater than zero");
        require(_collateral > 0, "Collateral must be greater than zero");
        
        // Create the order
        orderCount++;
        orders[orderCount] = Order(msg.sender, address(0), _price, OrderStatus.Open, _collateral);
        
        // Emit the order creation event
        emit OrderCreated(orderCount, msg.sender, _price, _collateral);
    }

    // Function to cancel an order by the seller
    function cancelOrder(uint256 _orderId) external onlySeller(_orderId) {
        Order storage order = orders[_orderId];
        require(order.status == OrderStatus.Open, "Order must be open to cancel");

        // Update the order status
        order.status = OrderStatus.Canceled;

        // Emit the order cancellation event
        emit OrderCanceled(_orderId);
    }

    // Function to claim collateral back
    function claimCollateral(uint256 _orderId) external onlySeller(_orderId) {
        Order storage order = orders[_orderId];
        require(order.status == OrderStatus.Canceled, "Order must be canceled to claim collateral");

        uint256 collateralAmount = order.collateral;
        order.collateral = 0; // Prevent re-entrancy
        order.status = OrderStatus.Completed; // Mark as completed after collateral claim

        // Transfer collateral back to the seller
        payable(msg.sender).transfer(collateralAmount);

        // Emit the collateral claimed event
        emit CollateralClaimed(_orderId, msg.sender, collateralAmount);
    }

    // Fallback function to accept ether
    receive() external payable {}
}
```
