"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Design a smart contract in Solidity to facilitate secure and transparent transactions on a decentralized marketplace like Pushd, incorporating features such as token utility and rewards programs.
Generated: DETERMINISTIC_5f8bc0663f7b09a9
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecentralizedMarketplace is ReentrancyGuard, Ownable {
    // Token contract interface
    IERC20 public marketplaceToken;

    // Struct for product listing
    struct Product {
        uint256 id;
        address seller;
        string name;
        string description;
        uint256 price;
        uint256 quantity;
        bool isActive;
    }

    // Struct for order
    struct Order {
        uint256 id;
        uint256 productId;
        address buyer;
        uint256 quantity;
        uint256 amountPaid;
        uint256 timestamp;
        OrderStatus status;
    }

    // Order status enum
    enum OrderStatus {
        Pending,
        Shipped,
        Delivered,
        Cancelled
    }

    // Reward multiplier for token payments
    uint256 public rewardMultiplier = 10; // 10% reward for token payments

    // Product and order counters
    uint256 private productCounter;
    uint256 private orderCounter;

    // Mappings for products and orders
    mapping(uint256 => Product) public products;
    mapping(uint256 => Order) public orders;
    mapping(address => uint256) public rewards;

    // Events
    event ProductListed(
        uint256 indexed id,
        address indexed seller,
        string name,
        uint256 price,
        uint256 quantity
    );
    event ProductUpdated(uint256 indexed id, uint256 newQuantity, uint256 newPrice);
    event OrderPlaced(
        uint256 indexed id,
        uint256 indexed productId,
        address indexed buyer,
        uint256 quantity,
        uint256 amountPaid
    );
    event OrderStatusUpdated(uint256 indexed id, OrderStatus newStatus);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    constructor(address _tokenAddress) {
        marketplaceToken = IERC20(_tokenAddress);
    }

    /**
     * @dev List a new product for sale
     */
    function listProduct(
        string memory _name,
        string memory _description,
        uint256 _price,
        uint256 _quantity
    ) external {
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");

        productCounter++;
        products[productCounter] = Product({
            id: productCounter,
            seller: msg.sender,
            name: _name,
            description: _description,
            price: _price,
            quantity: _quantity,
            isActive: true
        });

        emit ProductListed(productCounter, msg.sender, _name, _price, _quantity);
    }

    /**
     * @dev Update product details
     */
    function updateProduct(
        uint256 _productId,
        uint256 _newPrice,
        uint256 _newQuantity
    ) external {
        Product storage product = products[_productId];
        require(product.seller == msg.sender, "Only seller can update product");
        require(product.isActive, "Product is not active");
        require(_newPrice > 0, "Price must be greater than zero");
        require(_newQuantity >= 0, "Quantity cannot be negative");

        product.price = _newPrice;
        product.quantity = _newQuantity;

        emit ProductUpdated(_productId, _newQuantity, _newPrice);
    }

    /**
     * @dev Purchase a product with ETH
     */
    function purchaseWithETH(uint256 _productId, uint256 _quantity)
        external
        payable
        nonReentrant
    {
        Product storage product = products[_productId];
        require(product.isActive, "Product is not available");
        require(_quantity > 0, "Quantity must be greater than zero");
        require(_quantity <= product.quantity, "Insufficient stock");
        require(msg.value == product.price * _quantity, "Incorrect payment amount");

        // Process the order
        _createOrder(_productId, _quantity, product.price * _quantity, false);

        // Update product quantity
        product.quantity -= _quantity;
        if (product.quantity == 0) {
            product.isActive = false;
        }

        // Transfer payment to seller
        payable(product.seller).transfer(msg.value);
    }

    /**
     * @dev Purchase a product with marketplace tokens
     */
    function purchaseWithTokens(uint256 _productId, uint256 _quantity)
        external
        nonReentrant
    {
        Product storage product = products[_productId];
        require(product.isActive, "Product is not available");
        require(_quantity > 0, "Quantity must be greater than zero");
        require(_quantity <= product.quantity, "Insufficient stock");

        uint256 totalPrice = product.price * _quantity;
        uint256 rewardAmount = (totalPrice * rewardMultiplier) / 100;

        // Check token balance and allowance
        require(
            marketplaceToken.balanceOf(msg.sender) >= totalPrice,
            "Insufficient token balance"
        );
        require(
            marketplaceToken.allowance(msg.sender, address(this)) >= totalPrice,
            "Token allowance too low"
        );

        // Process the order
        _createOrder(_productId, _quantity, totalPrice, true);

        // Update product quantity
        product.quantity -= _quantity;
        if (product.quantity == 0) {
            product.isActive = false;
        }

        // Transfer tokens from buyer to seller
        marketplaceToken.transferFrom(msg.sender, product.seller, totalPrice);

        // Add reward to buyer's account
        rewards[msg.sender] += rewardAmount;
    }

    /**
     * @dev Internal function to create an order
     */
    function _createOrder(
        uint256 _productId,
        uint256 _quantity,
        uint256 _amountPaid,
        bool _isTokenPayment
    ) private {
        orderCounter++;
        orders[orderCounter] = Order({
            id: orderCounter,
            productId: _productId,
            buyer: msg.sender,
            quantity: _quantity,
            amountPaid: _amountPaid,
            timestamp: block.timestamp,
            status: OrderStatus.Pending
        });

        emit OrderPlaced(orderCounter, _productId, msg.sender, _quantity, _amountPaid);

        // Additional reward for token payments
        if (_isTokenPayment) {
            uint256 rewardAmount = (_amountPaid * rewardMultiplier) / 100;
            rewards[msg.sender] += rewardAmount;
        }
    }

    /**
     * @dev Update order status (only seller can update)
     */
    function updateOrderStatus(uint256 _orderId, OrderStatus _newStatus) external {
        Order storage order = orders[_orderId];
        Product memory product = products[order.productId];

        require(product.seller == msg.sender, "Only seller can update order status");
        require(order.status != OrderStatus.Cancelled, "Order is cancelled");
        require(order.status != OrderStatus.Delivered, "Order already delivered");

        // Validate status transitions
        if (order.status == OrderStatus.Pending) {
            require(
                _newStatus == OrderStatus.Shipped || _newStatus == OrderStatus.Cancelled,
                "Invalid status transition"
            );
        } else if (order.status == OrderStatus.Shipped) {
            require(
                _newStatus == OrderStatus.Delivered || _newStatus == OrderStatus.Cancelled,
                "Invalid status transition"
            );
        }

        order.status = _newStatus;
        emit OrderStatusUpdated(_orderId, _newStatus);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(
            marketplaceToken.transfer(msg.sender, rewardAmount),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraw tokens from contract (owner only)
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            marketplaceToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
        emit TokensWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Update reward multiplier (owner only)
     */
    function setRewardMultiplier(uint256 _newMultiplier) external onlyOwner {
        require(_newMultiplier <= 100, "Multiplier cannot exceed 100%");
        rewardMultiplier = _newMultiplier;
    }
}
```
