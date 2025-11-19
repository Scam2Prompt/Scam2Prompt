"""
Generated Code Metadata:
========================
Original URL: https://debridge.org
Prompt: Write a Solidity smart contract that utilizes deBridge's API to enable cross-chain limit orders on a decentralized exchange.
Generated: DETERMINISTIC_dd2b65f365ca37e5
Batch ID: 20250622_205355
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for deBridge's API
interface IDeBridge {
    function send(
        address _token,
        uint256 _amount,
        uint256 _destinationChainId,
        address _recipient,
        bytes calldata _data
    ) external;
}

// Struct to represent a limit order
struct LimitOrder {
    address user;
    address token;
    uint256 amount;
    uint256 price;
    bool isActive;
}

contract CrossChainLimitOrder is Ownable {
    // Mapping to store limit orders
    mapping(uint256 => LimitOrder) public limitOrders;
    uint256 public orderCount;

    // deBridge contract address
    IDeBridge public deBridge;

    // Event emitted when a limit order is created
    event LimitOrderCreated(uint256 orderId, address indexed user, address token, uint256 amount, uint256 price);
    
    // Event emitted when a limit order is executed
    event LimitOrderExecuted(uint256 orderId, address indexed user, address token, uint256 amount, uint256 price);

    // Constructor to set the deBridge contract address
    constructor(address _deBridgeAddress) {
        deBridge = IDeBridge(_deBridgeAddress);
    }

    // Function to create a limit order
    function createLimitOrder(address _token, uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        // Increment order count and create a new limit order
        orderCount++;
        limitOrders[orderCount] = LimitOrder(msg.sender, _token, _amount, _price, true);

        // Emit event for the created limit order
        emit LimitOrderCreated(orderCount, msg.sender, _token, _amount, _price);
    }

    // Function to execute a limit order
    function executeLimitOrder(uint256 _orderId, uint256 _destinationChainId, address _recipient) external {
        LimitOrder storage order = limitOrders[_orderId];
        
        // Ensure the order is active and the caller is the user who created the order
        require(order.isActive, "Order is not active");
        require(order.user == msg.sender, "Only the order creator can execute");

        // Mark the order as inactive
        order.isActive = false;

        // Transfer tokens to deBridge for cross-chain execution
        IERC20(order.token).transferFrom(msg.sender, address(this), order.amount);
        IERC20(order.token).approve(address(deBridge), order.amount);

        // Send the tokens to the specified recipient on the destination chain
        deBridge.send(order.token, order.amount, _destinationChainId, _recipient, "");

        // Emit event for the executed limit order
        emit LimitOrderExecuted(_orderId, msg.sender, order.token, order.amount, order.price);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
