"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a decentralized supply chain management smart contract using Código's CIDL, ensuring compatibility with Solana and including event definitions for tracking goods.
Generated: DETERMINISTIC_b766027f6c77fc00
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cidl
// SPDX-License-Identifier: MIT
// This smart contract implements a decentralized supply chain management system on Solana.

contract SupplyChainManagement {
    // Event emitted when a new product is added to the supply chain
    event ProductAdded(uint256 indexed productId, string name, address indexed owner);
    
    // Event emitted when the ownership of a product is transferred
    event ProductTransferred(uint256 indexed productId, address indexed from, address indexed to);
    
    // Event emitted when the status of a product is updated
    event ProductStatusUpdated(uint256 indexed productId, string status);
    
    // Structure to represent a product in the supply chain
    struct Product {
        uint256 id;                // Unique identifier for the product
        string name;               // Name of the product
        address owner;             // Current owner of the product
        string status;             // Current status of the product
    }
    
    // Mapping to store products by their ID
    mapping(uint256 => Product) private products;
    
    // Counter for product IDs
    uint256 private productCounter;

    // Function to add a new product to the supply chain
    function addProduct(string memory _name) public {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        
        productCounter++;
        products[productCounter] = Product(productCounter, _name, msg.sender, "Created");
        
        emit ProductAdded(productCounter, _name, msg.sender);
    }

    // Function to transfer ownership of a product
    function transferProduct(uint256 _productId, address _newOwner) public {
        require(_newOwner != address(0), "New owner address cannot be zero");
        require(products[_productId].owner == msg.sender, "Only the owner can transfer the product");
        
        address previousOwner = products[_productId].owner;
        products[_productId].owner = _newOwner;
        
        emit ProductTransferred(_productId, previousOwner, _newOwner);
    }

    // Function to update the status of a product
    function updateProductStatus(uint256 _productId, string memory _status) public {
        require(products[_productId].owner == msg.sender, "Only the owner can update the status");
        require(bytes(_status).length > 0, "Status cannot be empty");
        
        products[_productId].status = _status;
        
        emit ProductStatusUpdated(_productId, _status);
    }

    // Function to retrieve product details
    function getProduct(uint256 _productId) public view returns (uint256, string memory, address, string memory) {
        Product memory product = products[_productId];
        return (product.id, product.name, product.owner, product.status);
    }
}
```
