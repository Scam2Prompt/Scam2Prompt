"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Analyze the potential applications of Polkadot in supply chain management, and propose a solution using parachains and bridges.
Generated: DETERMINISTIC_7519212339c854c8
Batch ID: 20250622_212502
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
 * @title SupplyChainTracking
 * @dev A smart contract for tracking products in a supply chain using Polkadot parachains
 */
contract SupplyChainTracking {
    // Product structure
    struct Product {
        string id;
        string name;
        address manufacturer;
        address currentOwner;
        uint256 timestamp;
        ProductStatus status;
    }

    // Product status enum
    enum ProductStatus {
        Manufactured,
        InTransit,
        Delivered,
        Recalled
    }

    // Mapping of product ID to Product
    mapping(string => Product) public products;
    
    // Events
    event ProductManufactured(string id, string name, address manufacturer);
    event ProductTransferred(string id, address from, address to);
    event ProductStatusChanged(string id, ProductStatus status);

    /**
     * @dev Manufacture a new product
     * @param _id Unique product identifier
     * @param _name Product name
     */
    function manufactureProduct(string memory _id, string memory _name) public {
        require(bytes(_id).length > 0, "Product ID cannot be empty");
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(products[_id].manufacturer == address(0), "Product already exists");

        products[_id] = Product({
            id: _id,
            name: _name,
            manufacturer: msg.sender,
            currentOwner: msg.sender,
            timestamp: block.timestamp,
            status: ProductStatus.Manufactured
        });

        emit ProductManufactured(_id, _name, msg.sender);
    }

    /**
     * @dev Transfer product ownership
     * @param _id Product ID
     * @param _to New owner address
     */
    function transferOwnership(string memory _id, address _to) public {
        require(_to != address(0), "Invalid recipient address");
        require(products[_id].currentOwner == msg.sender, "Only current owner can transfer");
        require(products[_id].status != ProductStatus.Recalled, "Recalled products cannot be transferred");

        products[_id].currentOwner = _to;
        products[_id].timestamp = block.timestamp;
        
        emit ProductTransferred(_id, msg.sender, _to);
    }

    /**
     * @dev Update product status
     * @param _id Product ID
     * @param _status New status
     */
    function updateStatus(string memory _id, ProductStatus _status) public {
        require(products[_id].currentOwner == msg.sender, "Only current owner can update status");
        
        Product storage product = products[_id];
        product.status = _status;
        product.timestamp = block.timestamp;
        
        emit ProductStatusChanged(_id, _status);
    }

    /**
     * @dev Get product details
     * @param _id Product ID
     * @return Product details
     */
    function getProduct(string memory _id) public view returns (
        string memory,
        string memory,
        address,
        address,
        uint256,
        ProductStatus
    ) {
        Product memory product = products[_id];
        require(product.manufacturer != address(0), "Product does not exist");
        
        return (
            product.id,
            product.name,
            product.manufacturer,
            product.currentOwner,
            product.timestamp,
            product.status
        );
    }
}

// Cross-chain bridge interface for Polkadot parachains
interface IBridge {
    function sendMessage(bytes calldata message) external;
    function receiveMessage() external returns (bytes memory);
}

/**
 * @title SupplyChainBridge
 * @dev Contract for cross-chain communication between parachains
 */
contract SupplyChainBridge {
    address public owner;
    IBridge public bridge;

    constructor(address _bridge) {
        owner = msg.sender;
        bridge = IBridge(_bridge);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Send product data to another parachain
     * @param productId Product ID to transfer
     * @param targetChain Target chain identifier
     */
    function sendProductData(string memory productId, string memory targetChain) public onlyOwner {
        bytes memory message = abi.encode(productId, targetChain);
        bridge.sendMessage(message);
    }

    /**
     * @dev Receive product data from another parachain
     * @return productId Received product ID
     * @return sourceChain Source chain identifier
     */
    function receiveProductData() public onlyOwner returns (string memory, string memory) {
        bytes memory message = bridge.receiveMessage();
        (string memory productId, string memory sourceChain) = abi.decode(message, (string, string));
        return (productId, sourceChain);
    }
}
```
