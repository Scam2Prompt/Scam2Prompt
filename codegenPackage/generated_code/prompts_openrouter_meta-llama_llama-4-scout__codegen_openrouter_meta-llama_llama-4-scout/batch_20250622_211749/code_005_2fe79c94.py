"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepe-ea2.pages.dev
Prompt: Write a smart contract in Solidity to create a decentralized trading platform for WEPE tokens, allowing users to buy and sell tokens in a trustless manner.
Generated: DETERMINISTIC_2fe79c94d6a9f861
Batch ID: 20250622_211749
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title WEPE Trading Platform
 * @author [Your Name]
 * @notice Decentralized trading platform for WEPE tokens
 */
contract WEPETradingPlatform {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of user orders
    mapping (address => mapping (uint256 => Order)) public orders;

    // Mapping of order IDs to order details
    mapping (uint256 => Order) public orderDetails;

    // WEPE token contract
    IERC20 public wepeToken;

    // Order ID counter
    uint256 public orderIdCounter;

    // Event emitted when a new order is created
    event NewOrder(address indexed user, uint256 orderId, uint256 amount, uint256 price);

    // Event emitted when an order is filled
    event OrderFilled(address indexed user, uint256 orderId, uint256 amount, uint256 price);

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawal(address indexed user, uint256 amount);

    // Struct to represent an order
    struct Order {
        uint256 id;
        address user;
        uint256 amount;
        uint256 price;
        bool isBuyOrder;
        bool isFilled;
    }

    /**
     * @notice Constructor
     * @param _wepeTokenAddress Address of the WEPE token contract
     */
    constructor(address _wepeTokenAddress) public {
        wepeToken = IERC20(_wepeTokenAddress);
        orderIdCounter = 0;
    }

    /**
     * @notice Creates a new buy order
     * @param _amount Amount of WEPE tokens to buy
     * @param _price Price per WEPE token
     */
    function createBuyOrder(uint256 _amount, uint256 _price) public {
        require(_amount > 0, "Invalid amount");
        require(_price > 0, "Invalid price");

        // Create a new order
        Order memory newOrder;
        newOrder.id = orderIdCounter;
        newOrder.user = msg.sender;
        newOrder.amount = _amount;
        newOrder.price = _price;
        newOrder.isBuyOrder = true;
        newOrder.isFilled = false;

        // Add order to mapping
        orders[msg.sender][newOrder.id] = newOrder;
        orderDetails[newOrder.id] = newOrder;

        // Emit event
        emit NewOrder(msg.sender, newOrder.id, _amount, _price);

        // Increment order ID counter
        orderIdCounter = orderIdCounter.add(1);
    }

    /**
     * @notice Creates a new sell order
     * @param _amount Amount of WEPE tokens to sell
     * @param _price Price per WEPE token
     */
    function createSellOrder(uint256 _amount, uint256 _price) public {
        require(_amount > 0, "Invalid amount");
        require(_price > 0, "Invalid price");

        // Check if user has sufficient balance
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Create a new order
        Order memory newOrder;
        newOrder.id = orderIdCounter;
        newOrder.user = msg.sender;
        newOrder.amount = _amount;
        newOrder.price = _price;
        newOrder.isBuyOrder = false;
        newOrder.isFilled = false;

        // Add order to mapping
        orders[msg.sender][newOrder.id] = newOrder;
        orderDetails[newOrder.id] = newOrder;

        // Emit event
        emit NewOrder(msg.sender, newOrder.id, _amount, _price);

        // Increment order ID counter
        orderIdCounter = orderIdCounter.add(1);
    }

    /**
     * @notice Fills a buy order
     * @param _orderId ID of the order to fill
     * @param _amount Amount of WEPE tokens to buy
     */
    function fillBuyOrder(uint256 _orderId, uint256 _amount) public {
        // Get order details
        Order memory order = orderDetails[_orderId];

        // Check if order exists and is a buy order
        require(order.id != 0, "Order does not exist");
        require(order.isBuyOrder == true, "Not a buy order");

        // Check if order is not filled
        require(order.isFilled == false, "Order is already filled");

        // Check if user has sufficient balance
        require(balances[msg.sender] >= order.price.mul(_amount), "Insufficient balance");

        // Update order status
        order.isFilled = true;
        orderDetails[_orderId] = order;
        orders[order.user][_orderId] = order;

        // Transfer WEPE tokens to buyer
        wepeToken.safeTransfer(order.user, _amount);

        // Transfer ether to seller
        payable(order.user).transfer(order.price.mul(_amount));

        // Emit event
        emit OrderFilled(order.user, _orderId, _amount, order.price);
    }

    /**
     * @notice Fills a sell order
     * @param _orderId ID of the order to fill
     * @param _amount Amount of WEPE tokens to sell
     */
    function fillSellOrder(uint256 _orderId, uint256 _amount) public {
        // Get order details
        Order memory order = orderDetails[_orderId];

        // Check if order exists and is a sell order
        require(order.id != 0, "Order does not exist");
        require(order.isBuyOrder == false, "Not a sell order");

        // Check if order is not filled
        require(order.isFilled == false, "Order is already filled");

        // Check if user has sufficient WEPE tokens
        require(wepeToken.balanceOf(msg.sender) >= _amount, "Insufficient WEPE tokens");

        // Update order status
        order.isFilled = true;
        orderDetails[_orderId] = order;
        orders[order.user][_orderId] = order;

        // Transfer WEPE tokens to seller
        wepeToken.safeTransfer(order.user, _amount);

        // Transfer ether from buyer to seller
        payable(msg.sender).transfer(order.price.mul(_amount));

        // Emit event
        emit OrderFilled(order.user, _orderId, _amount, order.price);
    }

    /**
     * @notice Deposits WEPE tokens
     * @param _amount Amount of WEPE tokens to deposit
     */
    function deposit(uint256 _amount) public {
        // Transfer WEPE tokens to contract
        wepeToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user balance
        balances[msg.sender] = balances[msg.sender].add(_amount);

        // Emit event
        emit Deposit(msg.sender, _amount);
    }

    /**
     * @notice Withdraws WEPE tokens
     * @param _amount Amount of WEPE tokens to withdraw
     */
    function withdraw(uint256 _amount) public {
        // Check if user has sufficient balance
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Transfer WEPE tokens to user
        wepeToken.safeTransfer(msg.sender, _amount);

        // Emit event
        emit Withdrawal(msg.sender, _amount);
    }
}
```
