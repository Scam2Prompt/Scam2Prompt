"""
Generated Code Metadata:
========================
Original URL: https://smartordinalwallet.pages.dev
Prompt: Design a dapp on the Smartdappchain that allows users to buy/sell tokens and handle verification and validation processes.
Generated: DETERMINISTIC_1349f4538b6629c7
Batch ID: 20250622_205842
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenMarketplace is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public tokensSold;
    bool public paused;

    struct Order {
        address seller;
        uint256 amount;
        uint256 price;
        bool active;
    }

    mapping(uint256 => Order) public orders;
    uint256 public orderCount;

    event TokenPurchase(
        address indexed buyer,
        address indexed seller,
        uint256 amount,
        uint256 price
    );
    event OrderCreated(
        uint256 indexed orderId,
        address indexed seller,
        uint256 amount,
        uint256 price
    );
    event OrderCancelled(uint256 indexed orderId);
    event Paused(bool isPaused);
    event PriceUpdated(uint256 newPrice);

    constructor(address _token, uint256 _tokenPrice) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        tokenPrice = _tokenPrice;
    }

    modifier whenNotPaused() {
        require(!paused, "Contract is paused");
        _;
    }

    function buyTokens(uint256 _orderId, uint256 _amount) external payable nonReentrant whenNotPaused {
        Order storage order = orders[_orderId];
        require(order.active, "Order is not active");
        require(_amount <= order.amount, "Insufficient tokens in order");
        require(msg.value >= _amount * order.price, "Insufficient payment");

        uint256 totalPrice = _amount * order.price;
        uint256 excessPayment = msg.value - totalPrice;

        order.amount -= _amount;
        if (order.amount == 0) {
            order.active = false;
        }

        tokensSold += _amount;

        payable(order.seller).transfer(totalPrice);
        if (excessPayment > 0) {
            payable(msg.sender).transfer(excessPayment);
        }

        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokenPurchase(msg.sender, order.seller, _amount, order.price);
    }

    function createOrder(uint256 _amount, uint256 _price) external whenNotPaused {
        require(_amount > 0, "Amount must be greater than 0");
        require(_price > 0, "Price must be greater than 0");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= _amount, "Token allowance too low");

        orderCount++;
        orders[orderCount] = Order({
            seller: msg.sender,
            amount: _amount,
            price: _price,
            active: true
        });

        emit OrderCreated(orderCount, msg.sender, _amount, _price);
    }

    function cancelOrder(uint256 _orderId) external {
        Order storage order = orders[_orderId];
        require(order.seller == msg.sender, "Not the order owner");
        require(order.active, "Order is not active");

        order.active = false;

        emit OrderCancelled(_orderId);
    }

    function setPaused(bool _paused) external onlyOwner {
        paused = _paused;
        emit Paused(_paused);
    }

    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than 0");
        tokenPrice = _newPrice;
        emit PriceUpdated(_newPrice);
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(token.transfer(owner(), _amount), "Token transfer failed");
    }

    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
