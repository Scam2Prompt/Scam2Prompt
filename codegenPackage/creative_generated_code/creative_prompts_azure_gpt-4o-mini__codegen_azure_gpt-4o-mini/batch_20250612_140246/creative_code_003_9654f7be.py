"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-stores.web.app
Prompt: Provide an example of how to list products on a decentralized marketplace similar to Pushd, including smart contract interactions.
Generated: DETERMINISTIC_9654f7be7f7c1d23
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecentralizedMarketplace is Ownable {
    // Struct to hold product details
    struct Product {
        address seller;
        uint256 price;
        address nftContract;
        uint256 tokenId;
        bool isListed;
    }

    // Mapping from product ID to Product details
    mapping(uint256 => Product) public products;
    // Counter for product IDs
    uint256 public productIdCounter;

    // Event emitted when a product is listed
    event ProductListed(uint256 productId, address indexed seller, uint256 price, address indexed nftContract, uint256 tokenId);
    // Event emitted when a product is purchased
    event ProductPurchased(uint256 productId, address indexed buyer);

    // Function to list a product on the marketplace
    function listProduct(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You must own the NFT to list it");
        
        // Approve the marketplace to transfer the NFT
        IERC721(nftContract).approve(address(this), tokenId);

        // Create a new product
        productIdCounter++;
        products[productIdCounter] = Product({
            seller: msg.sender,
            price: price,
            nftContract: nftContract,
            tokenId: tokenId,
            isListed: true
        });

        emit ProductListed(productIdCounter, msg.sender, price, nftContract, tokenId);
    }

    // Function to purchase a product from the marketplace
    function purchaseProduct(uint256 productId) external payable {
        Product memory product = products[productId];
        
        require(product.isListed, "Product is not listed");
        require(msg.value >= product.price, "Insufficient funds sent");
        
        // Transfer the funds to the seller
        payable(product.seller).transfer(msg.value);
        
        // Transfer the NFT to the buyer
        IERC721(product.nftContract).safeTransferFrom(product.seller, msg.sender, product.tokenId);

        // Mark the product as no longer listed
        products[productId].isListed = false;

        emit ProductPurchased(productId, msg.sender);
    }

    // Function to get product details
    function getProduct(uint256 productId) external view returns (Product memory) {
        return products[productId];
    }

    // Function to withdraw funds from contract (in case of accidental ether sent)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
