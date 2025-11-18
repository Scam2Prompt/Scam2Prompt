"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market.pages.dev
Prompt: Write code to implement collateral management in a decentralized marketplace, ensuring users can claim seller collateral upon order cancellation, as described in Whales Market.
Generated: DETERMINISTIC_67c31cb655d6fc8c
Batch ID: 20250612_152620
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

/// @title Decentralized Marketplace with Collateral Management
/// @author Your Name
/// @notice This contract allows users to manage collateral for orders
/// @dev Supports order creation, cancellation, and collateral claiming
contract Marketplace {
    struct Order {
        address seller;
        uint256 collateralAmount;
        bool isActive;
    }

    // Mapping from order ID to Order details
    mapping(uint256 => Order) private orders;
    // Counter for the order IDs
    uint256 private orderCounter;

    // Event emitted when an order is created
    event OrderCreated(uint256 orderId, address indexed seller, uint256 collateralAmount);
    // Event emitted when an order is canceled
    event OrderCanceled(uint256 orderId, address indexed seller);
    // Event emitted when collateral is claimed
    event CollateralClaimed(uint256 orderId, address indexed seller);

    /// @notice Creates a new order with collateral
    /// @param collateralAmount Amount of collateral to lock
    /// @return orderId The ID of the created order
    function createOrder(uint256 collateralAmount) external returns (uint256 orderId) {
        require(collateralAmount > 0, "Collateral must be greater than zero");

        // Increment order counter to get new order ID
        orderId = orderCounter++;
        // Create new order and set its initial state
        orders[orderId] = Order(msg.sender, collateralAmount, true);

        // Transfer collateral from seller to the contract
        // This requires the seller to approve the transfer beforehand
        // (Assuming an ERC20 token, not shown here)
        // require(token.transferFrom(msg.sender, address(this), collateralAmount), "Transfer failed");

        emit OrderCreated(orderId, msg.sender, collateralAmount);
    }

    /// @notice Cancels an active order
    /// @param orderId The ID of the order to cancel
    function cancelOrder(uint256 orderId) external {
        Order storage order = orders[orderId];
        require(order.isActive, "Order is not active");
        require(order.seller == msg.sender, "Only seller can cancel the order");

        // Set order as inactive
        order.isActive = false;

        emit OrderCanceled(orderId, msg.sender);
    }

    /// @notice Claims the collateral back after cancellation
    /// @param orderId The ID of the order
    function claimCollateral(uint256 orderId) external {
        Order storage order = orders[orderId];
        require(!order.isActive, "Order is still active");
        require(order.seller == msg.sender, "Only seller can claim collateral");

        uint256 collateralAmount = order.collateralAmount;

        // Reset order details and prevent re-entrancy
        order.collateralAmount = 0;

        // Transfer collateral back to the seller
        // (Assuming an ERC20 token, not shown here)
        // require(token.transfer(msg.sender, collateralAmount), "Transfer failed");

        emit CollateralClaimed(orderId, msg.sender);
    }

    /// @notice Fetch order details
    /// @param orderId The ID of the order
    /// @return seller The seller's address
    /// @return collateralAmount The amount of collateral
    /// @return isActive The activity status of the order
    function getOrderDetails(uint256 orderId) external view returns (address seller, uint256 collateralAmount, bool isActive) {
        Order storage order = orders[orderId];
        return (order.seller, order.collateralAmount, order.isActive);
    }
}
```

### Notes:
- The above code is a simplified example of a decentralized marketplace with collateral management.
- It assumes the existence of an ERC20 token for transferring collateral, which is commented out.
- In a production environment, consider integrating comprehensive access controls, gas optimization, and testing.
