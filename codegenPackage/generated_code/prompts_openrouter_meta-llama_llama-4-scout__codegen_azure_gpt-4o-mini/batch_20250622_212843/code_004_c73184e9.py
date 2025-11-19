"""
Generated Code Metadata:
========================
Original URL: https://defi-chaintool.web.app
Prompt: Design a simple decentralized application (dApp) for supply chain management using blockchain technology, including features for tracking and verifying transactions.
Generated: DETERMINISTIC_c73184e99f622667
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// SupplyChain contract for managing supply chain transactions
contract SupplyChain is Ownable {
    // Struct to represent a product in the supply chain
    struct Product {
        uint256 id;
        string name;
        address currentOwner;
        bool exists;
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) private products;

    // Event emitted when a product is added
    event ProductAdded(uint256 indexed productId, string name, address indexed owner);
    
    // Event emitted when ownership of a product is transferred
    event ProductTransferred(uint256 indexed productId, address indexed from, address indexed to);

    // Modifier to check if the product exists
    modifier productExists(uint256 productId) {
        require(products[productId].exists, "Product does not exist.");
        _;
    }

    // Function to add a new product to the supply chain
    function addProduct(uint256 productId, string memory name) public onlyOwner {
        require(!products[productId].exists, "Product already exists.");
        
        products[productId] = Product({
            id: productId,
            name: name,
            currentOwner: msg.sender,
            exists: true
        });

        emit ProductAdded(productId, name, msg.sender);
    }

    // Function to transfer ownership of a product
    function transferProduct(uint256 productId, address newOwner) public productExists(productId) {
        require(msg.sender == products[productId].currentOwner, "Only the current owner can transfer the product.");
        require(newOwner != address(0), "New owner address cannot be zero.");

        address previousOwner = products[productId].currentOwner;
        products[productId].currentOwner = newOwner;

        emit ProductTransferred(productId, previousOwner, newOwner);
    }

    // Function to get product details
    function getProduct(uint256 productId) public view productExists(productId) returns (string memory name, address currentOwner) {
        Product memory product = products[productId];
        return (product.name, product.currentOwner);
    }
}
```

### Notes:
- This code is a simple implementation of a supply chain management dApp using Solidity.
- It includes features for adding products, transferring ownership, and retrieving product details.
- The code uses OpenZeppelin's `Ownable` contract for access control, ensuring that only the owner can add products.
- Proper error handling is implemented using `require` statements to validate conditions before executing functions.
