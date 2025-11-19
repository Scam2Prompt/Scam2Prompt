"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions and transparency using blockchain technology. Include features for listing products, browsing listings, and recording transactions.
Generated: DETERMINISTIC_b518b38e54c45a54
Batch ID: 20250612_151232
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
 * @title Decentralized Marketplace
 * @dev A smart contract for a decentralized marketplace with secure transactions
 */
contract DecentralizedMarketplace {
    // Struct to represent a product listing
    struct Product {
        uint256 id;
        address seller;
        string name;
        string description;
        uint256 price;
        uint256 quantity;
        bool isActive;
    }

    // Struct to represent a transaction
    struct Transaction {
        uint256 id;
        uint256 productId;
        address buyer;
        address seller;
        uint256 quantity;
        uint256 amount;
        uint256 timestamp;
    }

    // State variables
    uint256 private productCounter;
    uint256 private transactionCounter;
    mapping(uint256 => Product) private products;
    mapping(uint256 => Transaction) private transactions;
    mapping(address => uint256[]) private sellerProducts;
    mapping(address => uint256[]) private buyerTransactions;

    // Events
    event ProductListed(
        uint256 indexed id,
        address indexed seller,
        string name,
        uint256 price,
        uint256 quantity
    );
    event ProductUpdated(
        uint256 indexed id,
        address indexed seller,
        string name,
        uint256 price,
        uint256 quantity
    );
    event ProductPurchased(
        uint256 indexed transactionId,
        uint256 indexed productId,
        address indexed buyer,
        address seller,
        uint256 quantity,
        uint256 amount
    );
    event ProductRemoved(uint256 indexed id, address indexed seller);

    // Modifiers
    modifier onlySeller(uint256 _productId) {
        require(
            products[_productId].seller == msg.sender,
            "Only the seller can perform this action"
        );
        _;
    }

    modifier productExists(uint256 _productId) {
        require(products[_productId].id != 0, "Product does not exist");
        _;
    }

    modifier isActive(uint256 _productId) {
        require(products[_productId].isActive, "Product is not active");
        _;
    }

    /**
     * @dev List a new product for sale
     * @param _name Name of the product
     * @param _description Description of the product
     * @param _price Price per unit in wei
     * @param _quantity Available quantity
     */
    function listProduct(
        string memory _name,
        string memory _description,
        uint256 _price,
        uint256 _quantity
    ) external {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");

        productCounter++;
        products[productCounter] = Product(
            productCounter,
            msg.sender,
            _name,
            _description,
            _price,
            _quantity,
            true
        );

        sellerProducts[msg.sender].push(productCounter);

        emit ProductListed(productCounter, msg.sender, _name, _price, _quantity);
    }

    /**
     * @dev Update product details
     * @param _productId ID of the product to update
     * @param _name New name
     * @param _description New description
     * @param _price New price
     * @param _quantity New quantity
     */
    function updateProduct(
        uint256 _productId,
        string memory _name,
        string memory _description,
        uint256 _price,
        uint256 _quantity
    ) external productExists(_productId) onlySeller(_productId) isActive(_productId) {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(_price > 0, "Price must be greater than zero");
        require(_quantity > 0, "Quantity must be greater than zero");

        products[_productId].name = _name;
        products[_productId].description = _description;
        products[_productId].price = _price;
        products[_productId].quantity = _quantity;

        emit ProductUpdated(
            _productId,
            msg.sender,
            _name,
            _price,
            _quantity
        );
    }

    /**
     * @dev Remove a product listing
     * @param _productId ID of the product to remove
     */
    function removeProduct(uint256 _productId)
        external
        productExists(_productId)
        onlySeller(_productId)
        isActive(_productId)
    {
        products[_productId].isActive = false;
        emit ProductRemoved(_productId, msg.sender);
    }

    /**
     * @dev Purchase a product
     * @param _productId ID of the product to purchase
     * @param _quantity Quantity to purchase
     */
    function purchaseProduct(uint256 _productId, uint256 _quantity)
        external
        payable
        productExists(_productId)
        isActive(_productId)
    {
        Product storage product = products[_productId];
        require(_quantity > 0, "Quantity must be greater than zero");
        require(_quantity <= product.quantity, "Insufficient quantity available");
        require(msg.value == product.price * _quantity, "Incorrect payment amount");

        // Update product quantity
        product.quantity -= _quantity;
        if (product.quantity == 0) {
            product.isActive = false;
        }

        // Record transaction
        transactionCounter++;
        transactions[transactionCounter] = Transaction(
            transactionCounter,
            _productId,
            msg.sender,
            product.seller,
            _quantity,
            msg.value,
            block.timestamp
        );

        // Update buyer's transaction history
        buyerTransactions[msg.sender].push(transactionCounter);

        // Transfer funds to seller
        payable(product.seller).transfer(msg.value);

        emit ProductPurchased(
            transactionCounter,
            _productId,
            msg.sender,
            product.seller,
            _quantity,
            msg.value
        );
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
            product.quantity,
            product.isActive
        );
    }

    /**
     * @dev Get transaction details
     * @param _transactionId ID of the transaction
     * @return Transaction details
     */
    function getTransaction(uint256 _transactionId)
        external
        view
        returns (
            uint256,
            uint256,
            address,
            address,
            uint256,
            uint256,
            uint256
        )
    {
        require(_transactionId <= transactionCounter, "Transaction does not exist");
        Transaction memory transaction = transactions[_transactionId];
        return (
            transaction.id,
            transaction.productId,
            transaction.buyer,
            transaction.seller,
            transaction.quantity,
            transaction.amount,
            transaction.timestamp
        );
    }

    /**
     * @dev Get all product IDs listed by a seller
     * @param _seller Address of the seller
     * @return Array of product IDs
     */
    function getSellerProducts(address _seller)
        external
        view
        returns (uint256[] memory)
    {
        return sellerProducts[_seller];
    }

    /**
     * @dev Get all transaction IDs for a buyer
     * @param _buyer Address of the buyer
     * @return Array of transaction IDs
     */
    function getBuyerTransactions(address _buyer)
        external
        view
        returns (uint256[] memory)
    {
        return buyerTransactions[_buyer];
    }

    /**
     * @dev Get total number of products listed
     * @return Total product count
     */
    function getTotalProducts() external view returns (uint256) {
        return productCounter;
    }

    /**
     * @dev Get total number of transactions
     * @return Total transaction count
     */
    function getTotalTransactions() external view returns (uint256) {
        return transactionCounter;
    }
}
```
