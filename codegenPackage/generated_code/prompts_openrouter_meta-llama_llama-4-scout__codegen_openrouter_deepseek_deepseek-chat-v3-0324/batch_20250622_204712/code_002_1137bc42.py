"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: "Design a simple smart contract in Solidity for a decentralized marketplace like Pushd, focusing on secure and transparent transactions."
Generated: DETERMINISTIC_1137bc427a4a492f
Batch ID: 20250622_204712
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
 * @title Decentralized Marketplace Contract
 * @dev Implements a simple marketplace with secure transactions and escrow functionality
 */
contract DecentralizedMarketplace {
    // Struct to represent a product listing
    struct Product {
        uint256 id;
        address seller;
        string name;
        string description;
        uint256 price;
        bool isListed;
    }

    // Struct to represent an order
    struct Order {
        uint256 productId;
        address buyer;
        uint256 amountPaid;
        bool isCompleted;
        bool isDisputed;
    }

    // State variables
    uint256 public productCount;
    uint256 public orderCount;
    address public owner;

    // Mappings
    mapping(uint256 => Product) public products;
    mapping(uint256 => Order) public orders;
    mapping(address => uint256) public balances;

    // Events
    event ProductListed(
        uint256 id,
        address indexed seller,
        string name,
        uint256 price
    );
    event ProductUpdated(uint256 id);
    event ProductDelisted(uint256 id);
    event OrderCreated(
        uint256 orderId,
        uint256 productId,
        address indexed buyer,
        uint256 amount
    );
    event OrderCompleted(uint256 orderId);
    event OrderDisputed(uint256 orderId);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier productExists(uint256 _productId) {
        require(_productId <= productCount && _productId > 0, "Product does not exist");
        _;
    }

    modifier orderExists(uint256 _orderId) {
        require(_orderId <= orderCount && _orderId > 0, "Order does not exist");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev List a new product for sale
     * @param _name Name of the product
     * @param _description Description of the product
     * @param _price Price of the product in wei
     */
    function listProduct(
        string memory _name,
        string memory _description,
        uint256 _price
    ) external {
        require(_price > 0, "Price must be greater than zero");
        productCount++;
        products[productCount] = Product(
            productCount,
            msg.sender,
            _name,
            _description,
            _price,
            true
        );
        emit ProductListed(productCount, msg.sender, _name, _price);
    }

    /**
     * @dev Update product details
     * @param _productId ID of the product to update
     * @param _name New name
     * @param _description New description
     * @param _price New price
     */
    function updateProduct(
        uint256 _productId,
        string memory _name,
        string memory _description,
        uint256 _price
    ) external productExists(_productId) {
        Product storage product = products[_productId];
        require(msg.sender == product.seller, "Only seller can update product");
        require(product.isListed, "Product is not listed");
        require(_price > 0, "Price must be greater than zero");

        product.name = _name;
        product.description = _description;
        product.price = _price;
        emit ProductUpdated(_productId);
    }

    /**
     * @dev Delist a product
     * @param _productId ID of the product to delist
     */
    function delistProduct(uint256 _productId) external productExists(_productId) {
        Product storage product = products[_productId];
        require(msg.sender == product.seller, "Only seller can delist product");
        require(product.isListed, "Product is already delisted");

        product.isListed = false;
        emit ProductDelisted(_productId);
    }

    /**
     * @dev Purchase a product
     * @param _productId ID of the product to purchase
     */
    function purchaseProduct(uint256 _productId) external payable productExists(_productId) {
        Product storage product = products[_productId];
        require(product.isListed, "Product is not available");
        require(msg.sender != product.seller, "Seller cannot buy own product");
        require(msg.value == product.price, "Incorrect payment amount");

        orderCount++;
        orders[orderCount] = Order(
            _productId,
            msg.sender,
            msg.value,
            false,
            false
        );
        emit OrderCreated(orderCount, _productId, msg.sender, msg.value);
    }

    /**
     * @dev Complete an order and release funds to seller
     * @param _orderId ID of the order to complete
     */
    function completeOrder(uint256 _orderId) external orderExists(_orderId) {
        Order storage order = orders[_orderId];
        Product storage product = products[order.productId];
        
        require(!order.isCompleted, "Order already completed");
        require(!order.isDisputed, "Order is under dispute");
        require(msg.sender == order.buyer, "Only buyer can complete order");

        order.isCompleted = true;
        balances[product.seller] += order.amountPaid;
        emit OrderCompleted(_orderId);
    }

    /**
     * @dev Mark an order as disputed
     * @param _orderId ID of the order to dispute
     */
    function disputeOrder(uint256 _orderId) external orderExists(_orderId) {
        Order storage order = orders[_orderId];
        Product storage product = products[order.productId];
        
        require(!order.isCompleted, "Order already completed");
        require(!order.isDisputed, "Order already disputed");
        require(
            msg.sender == order.buyer || msg.sender == product.seller,
            "Only buyer or seller can dispute order"
        );

        order.isDisputed = true;
        emit OrderDisputed(_orderId);
    }

    /**
     * @dev Resolve a disputed order (owner only)
     * @param _orderId ID of the order to resolve
     * @param _refundBuyer Whether to refund the buyer (true) or pay the seller (false)
     */
    function resolveDispute(uint256 _orderId, bool _refundBuyer)
        external
        onlyOwner
        orderExists(_orderId)
    {
        Order storage order = orders[_orderId];
        require(order.isDisputed, "Order is not disputed");
        require(!order.isCompleted, "Order already completed");

        order.isCompleted = true;
        if (_refundBuyer) {
            balances[order.buyer] += order.amountPaid;
        } else {
            Product storage product = products[order.productId];
            balances[product.seller] += order.amountPaid;
        }
        emit OrderCompleted(_orderId);
    }

    /**
     * @dev Withdraw funds from contract
     */
    function withdrawFunds() external {
        uint256 balance = balances[msg.sender];
        require(balance > 0, "No funds available");

        balances[msg.sender] = 0;
        payable(msg.sender).transfer(balance);
        emit FundsWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Get product details
     * @param _productId ID of the product
     * @return Product details
     */
    function getProduct(uint256 _productId)
        external
        view
        productExists(_productId)
        returns (
            uint256,
            address,
            string memory,
            string memory,
            uint256,
            bool
        )
    {
        Product memory product = products[_productId];
        return (
            product.id,
            product.seller,
            product.name,
            product.description,
            product.price,
            product.isListed
        );
    }

    /**
     * @dev Get order details
     * @param _orderId ID of the order
     * @return Order details
     */
    function getOrder(uint256 _orderId)
        external
        view
        orderExists(_orderId)
        returns (
            uint256,
            address,
            uint256,
            bool,
            bool
        )
    {
        Order memory order = orders[_orderId];
        return (
            order.productId,
            order.buyer,
            order.amountPaid,
            order.isCompleted,
            order.isDisputed
        );
    }
}
```
