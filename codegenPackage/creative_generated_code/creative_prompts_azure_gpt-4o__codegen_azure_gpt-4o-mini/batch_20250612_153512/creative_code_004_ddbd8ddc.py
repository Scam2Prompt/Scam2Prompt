"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destranetwork.pages.dev
Prompt: Provide an example of integrating Destra's web hosting service into a decentralized application using smart contracts.
Generated: DETERMINISTIC_ddbd8ddc39a39c39
Batch ID: 20250612_153512
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the main contract
contract DestraHostingIntegration {
    // Address of the Destra hosting service (this address is hypothetical)
    address private destraHostingAddress;

    // ERC20 token used for payments (e.g. DAI, USDT)
    IERC20 private paymentToken;

    // Event emitted when a hosting service is ordered
    event HostingOrdered(address indexed user, uint256 amount, string domain);

    // Struct to represent a hosting order
    struct HostingOrder {
        address user;
        string domain;
        uint256 amount;
        bool isActive;
    }

    // Mapping to store hosting orders
    mapping(uint256 => HostingOrder) public orders;

    // Counter for tracking orders
    uint256 public orderCounter;

    // Modifier to check if the sender has enough tokens
    modifier hasSufficientTokens(uint256 amount) {
        require(paymentToken.balanceOf(msg.sender) >= amount, "Insufficient tokens");
        _;
    }

    // Constructor to initialize contract with hosting address and payment token
    constructor(address _destraHostingAddress, address _paymentTokenAddress) {
        destraHostingAddress = _destraHostingAddress;
        paymentToken = IERC20(_paymentTokenAddress);
    }

    // Function to order hosting service
    function orderHosting(string memory domain, uint256 amount) public 
        hasSufficientTokens(amount) 
    {
        // Transfer payment tokens from user to contract
        require(paymentToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new hosting order
        orders[orderCounter] = HostingOrder(msg.sender, domain, amount, true);
        emit HostingOrdered(msg.sender, amount, domain);

        // Increment the order counter
        orderCounter++;
    }

    // Function to retrieve order details
    function getOrder(uint256 orderId) public view returns (HostingOrder memory) {
        require(orderId < orderCounter, "Order does not exist");
        return orders[orderId];
    }

    // Function to cancel an order (only allow if the order is active)
    function cancelOrder(uint256 orderId) public {
        HostingOrder storage order = orders[orderId];
        require(order.isActive, "Order is not active");
        require(order.user == msg.sender, "Only order creator can cancel");

        // Mark order as inactive
        order.isActive = false;
        
        // Refund tokens back to the user
        require(paymentToken.transfer(msg.sender, order.amount), "Refund failed");
    }

    // Function to withdraw collected funds (only owner)
    function withdrawFunds() public {
        // Add only owner control on this function
        // In production code, you should implement an ownership mechanism
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(paymentToken.transfer(msg.sender, balance), "Withdrawal failed");
    }
}
```
