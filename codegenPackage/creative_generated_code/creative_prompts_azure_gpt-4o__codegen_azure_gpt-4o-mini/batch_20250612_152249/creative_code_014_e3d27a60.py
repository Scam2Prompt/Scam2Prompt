"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Write a Solidity smart contract for a decentralized logistics platform similar to SaitaLogistics, enabling crypto payments for shipping services.
Generated: DETERMINISTIC_e3d27a60b44d8b52
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

// This contract represents a decentralized logistics platform for shipping services
contract LogisticsPlatform is Ownable {
    // Struct to represent a shipping order
    struct ShippingOrder {
        uint256 id;
        address shipper; // Address of the shipper
        address receiver; // Address of the receiver
        uint256 amount; // Payment amount in tokens
        bool isPaid; // Payment status
        bool isShipped; // Shipping status
    }

    // Mapping to store shipping orders
    mapping(uint256 => ShippingOrder) public orders;
    uint256 public orderCount; // Counter for the number of orders

    // ERC20 token for payments
    IERC20 public paymentToken;

    // Event emitted when a new shipping order is created
    event ShippingOrderCreated(uint256 indexed orderId, address indexed shipper, address indexed receiver, uint256 amount);

    // Event emitted when a shipping order is paid
    event ShippingOrderPaid(uint256 indexed orderId, address indexed shipper);

    // Event emitted when a shipping order is shipped
    event ShippingOrderShipped(uint256 indexed orderId, address indexed shipper);

    // Constructor to initialize the payment token
    constructor(IERC20 _paymentToken) {
        paymentToken = _paymentToken;
    }

    // Function to create a new shipping order
    function createShippingOrder(address _receiver, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        orderCount++;
        orders[orderCount] = ShippingOrder(orderCount, msg.sender, _receiver, _amount, false, false);
        
        emit ShippingOrderCreated(orderCount, msg.sender, _receiver, _amount);
    }

    // Function for the shipper to pay for the shipping service
    function payForShipping(uint256 _orderId) external {
        ShippingOrder storage order = orders[_orderId];
        
        require(order.id != 0, "Order does not exist");
        require(order.shipper == msg.sender, "Only the shipper can pay for this order");
        require(!order.isPaid, "Order already paid");
        require(order.amount > 0, "Amount must be greater than zero");

        // Transfer the payment from the shipper to the contract
        bool success = paymentToken.transferFrom(msg.sender, address(this), order.amount);
        require(success, "Payment failed");
        
        order.isPaid = true;

        emit ShippingOrderPaid(_orderId, msg.sender);
    }

    // Function to mark the order as shipped by the shipper
    function markAsShipped(uint256 _orderId) external {
        ShippingOrder storage order = orders[_orderId];

        require(order.id != 0, "Order does not exist");
        require(order.shipper == msg.sender, "Only the shipper can mark this order as shipped");
        require(order.isPaid, "Order must be paid before shipping");

        order.isShipped = true;

        emit ShippingOrderShipped(_orderId, msg.sender);
    }

    // Function to withdraw funds from the contract by the owner
    function withdrawFunds(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(paymentToken.balanceOf(address(this)) >= _amount, "Insufficient funds");

        // Transfer tokens to the specified address
        bool success = paymentToken.transfer(_to, _amount);
        require(success, "Withdrawal failed");
    }
}
```
