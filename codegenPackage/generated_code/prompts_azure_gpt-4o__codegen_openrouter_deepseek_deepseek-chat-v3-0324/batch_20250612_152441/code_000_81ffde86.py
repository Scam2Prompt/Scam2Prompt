"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Write a smart contract in Solidity for a blockchain-based coffee trading ecosystem that directly connects farmers and consumers, inspired by the Crypto N' Kafe model.
Generated: DETERMINISTIC_81ffde86e41d31f7
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CoffeeTrade is Ownable, ReentrancyGuard {
    // Struct to represent a coffee product
    struct CoffeeProduct {
        uint256 id;
        address farmer;
        string name;
        string origin;
        uint256 price; // Price per unit in wei
        uint256 quantity; // Quantity available in grams
        uint256 roastDate;
        bool isActive;
    }

    // Struct to represent an order
    struct Order {
        uint256 id;
        uint256 productId;
        address consumer;
        uint256 quantity;
        uint256 totalPrice;
        uint256 orderDate;
        OrderStatus status;
    }

    // Enum for order status
    enum OrderStatus {
        Pending,
        Shipped,
        Delivered,
        Cancelled
    }

    // Mapping from product ID to CoffeeProduct
    mapping(uint256 => CoffeeProduct) public products;

    // Mapping from order ID to Order
    mapping(uint256 => Order) public orders;

    // Counter for product IDs
    uint256 public productCounter;

    // Counter for order IDs
    uint256 public orderCounter;

    // Accepted payment token (can be ETH or ERC20)
    address public paymentToken;

    // Events
    event ProductAdded(
        uint256 indexed id,
        address indexed farmer,
        string name,
        string origin,
        uint256 price,
        uint256 quantity
    );
    event ProductUpdated(uint256 indexed id, uint256 price, uint256 quantity);
    event ProductDeactivated(uint256 indexed id);
    event OrderPlaced(
        uint256 indexed orderId,
        uint256 indexed productId,
        address indexed consumer,
        uint256 quantity,
        uint256 totalPrice
    );
    event OrderStatusUpdated(uint256 indexed orderId, OrderStatus status);
    event PaymentWithdrawn(address indexed farmer, uint256 amount);

    constructor(address _paymentToken) {
        paymentToken = _paymentToken;
        productCounter = 1;
        orderCounter = 1;
    }

    /**
     * @dev Add a new coffee product to the marketplace
     * @param _name Name of the coffee product
     * @param _origin Origin country/region of the coffee
     * @param _price Price per gram in wei
     * @param _quantity Available quantity in grams
     */
    function addProduct(
        string memory _name,
        string memory _origin,
        uint256 _price,
        uint256 _quantity
    ) external {
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_origin).length > 0, "Origin cannot be empty");

        uint256 productId = productCounter;
        products[productId] = CoffeeProduct({
            id: productId,
            farmer: msg.sender,
            name: _name,
            origin: _origin,
            price: _price,
            quantity: _quantity,
            roastDate: block.timestamp,
            isActive: true
        });

        productCounter++;
        emit ProductAdded(productId, msg.sender, _name, _origin, _price, _quantity);
    }

    /**
     * @dev Update product details (only by the farmer who created it)
     * @param _productId ID of the product to update
     * @param _price New price per gram in wei
     * @param _quantity New available quantity in grams
     */
    function updateProduct(
        uint256 _productId,
        uint256 _price,
        uint256 _quantity
    ) external {
        require(products[_productId].farmer == msg.sender, "Only the farmer can update the product");
        require(products[_productId].isActive, "Product is not active");
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");

        products[_productId].price = _price;
        products[_productId].quantity = _quantity;

        emit ProductUpdated(_productId, _price, _quantity);
    }

    /**
     * @dev Deactivate a product (only by the farmer who created it)
     * @param _productId ID of the product to deactivate
     */
    function deactivateProduct(uint256 _productId) external {
        require(products[_productId].farmer == msg.sender, "Only the farmer can deactivate the product");
        require(products[_productId].isActive, "Product is already inactive");

        products[_productId].isActive = false;
        emit ProductDeactivated(_productId);
    }

    /**
     * @dev Place an order for a coffee product
     * @param _productId ID of the product to order
     * @param _quantity Quantity to order in grams
     */
    function placeOrder(uint256 _productId, uint256 _quantity) external payable nonReentrant {
        CoffeeProduct storage product = products[_productId];
        require(product.isActive, "Product is not available");
        require(_quantity > 0, "Quantity must be greater than zero");
        require(_quantity <= product.quantity, "Not enough quantity available");

        uint256 totalPrice = product.price * _quantity;
        
        if (paymentToken == address(0)) {
            // Pay with ETH
            require(msg.value >= totalPrice, "Insufficient ETH sent");
            if (msg.value > totalPrice) {
                payable(msg.sender).transfer(msg.value - totalPrice);
            }
        } else {
            // Pay with ERC20 token
            require(IERC20(paymentToken).transferFrom(msg.sender, address(this), totalPrice), "Token transfer failed");
        }

        // Update product quantity
        product.quantity -= _quantity;

        // Create order
        uint256 orderId = orderCounter;
        orders[orderId] = Order({
            id: orderId,
            productId: _productId,
            consumer: msg.sender,
            quantity: _quantity,
            totalPrice: totalPrice,
            orderDate: block.timestamp,
            status: OrderStatus.Pending
        });

        orderCounter++;
        emit OrderPlaced(orderId, _productId, msg.sender, _quantity, totalPrice);
    }

    /**
     * @dev Update order status (only by the farmer)
     * @param _orderId ID of the order to update
     * @param _status New status of the order
     */
    function updateOrderStatus(uint256 _orderId, OrderStatus _status) external {
        Order storage order = orders[_orderId];
        CoffeeProduct storage product = products[order.productId];
        
        require(product.farmer == msg.sender, "Only the farmer can update order status");
        require(order.status != OrderStatus.Cancelled, "Order is already cancelled");
        require(order.status != OrderStatus.Delivered, "Order is already delivered");

        // Validate status transitions
        if (order.status == OrderStatus.Pending) {
            require(_status == OrderStatus.Shipped || _status == OrderStatus.Cancelled, "Invalid status transition");
        } else if (order.status == OrderStatus.Shipped) {
            require(_status == OrderStatus.Delivered, "Invalid status transition");
        }

        order.status = _status;
        emit OrderStatusUpdated(_orderId, _status);
    }

    /**
     * @dev Withdraw earnings for a farmer
     */
    function withdrawEarnings() external nonReentrant {
        uint256 balance;
        
        if (paymentToken == address(0)) {
            balance = address(this).balance;
        } else {
            balance = IERC20(paymentToken).balanceOf(address(this));
        }

        require(balance > 0, "No funds available to withdraw");

        if (paymentToken == address(0)) {
            payable(msg.sender).transfer(balance);
        } else {
            require(IERC20(paymentToken).transfer(msg.sender, balance), "Token transfer failed");
        }

        emit PaymentWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Emergency function to cancel an order (only by owner)
     * @param _orderId ID of the order to cancel
     */
    function emergencyCancelOrder(uint256 _orderId) external onlyOwner {
        Order storage order = orders[_orderId];
        require(order.status != OrderStatus.Delivered, "Order is already delivered");

        // Refund the consumer
        if (paymentToken == address(0)) {
            payable(order.consumer).transfer(order.totalPrice);
        } else {
            require(IERC20(paymentToken).transfer(order.consumer, order.totalPrice), "Token transfer failed");
        }

        // Restore product quantity
        products[order.productId].quantity += order.quantity;

        order.status = OrderStatus.Cancelled;
        emit OrderStatusUpdated(_orderId, OrderStatus.Cancelled);
    }
}
```
