"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Provide an example of how to implement a smart contract for trading virtual real estate in the EarthMeta metaverse.
Generated: DETERMINISTIC_6f5df73148bd9d8c
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the OpenZeppelin contracts for access control and safe math
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the ERC721 token standard (for virtual real estate tokens)
interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Smart contract for trading virtual real estate in the EarthMeta metaverse
contract VirtualRealEstateTrading is Ownable {
    using SafeMath for uint256;

    // Event emitted when a property is listed for sale
    event PropertyListed(uint256 indexed tokenId, address indexed owner, uint256 price);
    
    // Event emitted when a property is sold
    event PropertySold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Structure to hold property details
    struct Property {
        uint256 tokenId;
        address owner;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to property details
    mapping(uint256 => Property) public properties;

    // Address of the ERC721 contract representing the virtual real estate
    IERC721 public erc721Token;

    // Constructor to set the ERC721 token address
    constructor(address _erc721Token) {
        erc721Token = IERC721(_erc721Token);
    }

    // Function to list a property for sale
    function listProperty(uint256 tokenId, uint256 price) external {
        // Check that the caller is the owner of the property
        require(erc721Token.ownerOf(tokenId) == msg.sender, "You do not own this property.");

        // Check for a valid price
        require(price > 0, "Price must be greater than zero.");

        // Update the property details
        properties[tokenId] = Property({
            tokenId: tokenId,
            owner: msg.sender,
            price: price,
            isListed: true
        });

        // Emit the property listed event
        emit PropertyListed(tokenId, msg.sender, price);
    }

    // Function to purchase a listed property
    function purchaseProperty(uint256 tokenId) external payable {
        Property storage property = properties[tokenId];

        // Check if the property is listed
        require(property.isListed, "Property is not listed for sale.");

        // Check that the correct amount of Ether was sent
        require(msg.value == property.price, "Incorrect Ether value sent.");

        // Transfer ownership of the property
        property.isListed = false;
        property.owner = msg.sender;

        // Transfer the property token to the buyer
        erc721Token.safeTransferFrom(property.owner, msg.sender, tokenId);

        // Emit the property sold event
        emit PropertySold(tokenId, msg.sender, msg.value);

        // Transfer the sale amount to the previous owner
        payable(property.owner).transfer(msg.value);
    }

    // Function to unlist a property if it is not sold
    function unlistProperty(uint256 tokenId) external {
        Property storage property = properties[tokenId];

        // Check that the caller is the owner of the property
        require(property.owner == msg.sender, "You do not own this property.");
        
        // Check if the property is listed
        require(property.isListed, "Property is not currently listed.");

        // Unlist the property
        property.isListed = false;
    }

    // Function to retrieve property details by tokenId
    function getProperty(uint256 tokenId) external view returns (Property memory) {
        return properties[tokenId];
    }
}
```
