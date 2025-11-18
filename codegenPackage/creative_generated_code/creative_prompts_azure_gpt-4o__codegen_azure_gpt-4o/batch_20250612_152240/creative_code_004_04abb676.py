"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Write a Solidity smart contract for managing NFT cities in the EarthMeta metaverse, including features for buying, selling, and trading virtual properties.
Generated: DETERMINISTIC_04abb676f2d87df3
Batch ID: 20250612_152240
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

/**
 * @title EarthMeta NFT Cities Contract
 * @dev This contract allows for managing NFT cities in the EarthMeta metaverse, including buying, selling, and trading virtual properties.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EarthMetaNFTCities is ERC721, Ownable {
    // Struct to represent an NFT property
    struct CityProperty {
        uint256 id; // Unique identifier for the property
        string name; // Name of the property
        uint256 price; // Price of the property in wei
        bool forSale; // Boolean indicating if the property is for sale
    }

    // Mapping from token ID to CityProperty details
    mapping(uint256 => CityProperty) public properties;

    // Counter to generate unique token IDs
    uint256 private nextTokenId;

    // Events
    event PropertyCreated(uint256 indexed tokenId, string name, uint256 price);
    event PropertyListedForSale(uint256 indexed tokenId, uint256 price);
    event PropertySold(uint256 indexed tokenId, address indexed buyer, uint256 price);
    event PropertyRemovedFromSale(uint256 indexed tokenId);

    constructor() ERC721("EarthMetaNFTCities", "EMC") {
        nextTokenId = 1; // Start token IDs from 1
    }

    /**
     * @dev Create a new NFT property.
     * @param _name Name of the property.
     * @param _price Initial price of the property in wei.
     */
    function createProperty(string memory _name, uint256 _price) external onlyOwner {
        require(bytes(_name).length > 0, "Property name cannot be empty");
        require(_price > 0, "Property price must be greater than zero");

        uint256 tokenId = nextTokenId;
        nextTokenId++;

        properties[tokenId] = CityProperty({
            id: tokenId,
            name: _name,
            price: _price,
            forSale: false
        });

        _mint(msg.sender, tokenId); // Mint the NFT to the owner

        emit PropertyCreated(tokenId, _name, _price);
    }

    /**
     * @dev List a property for sale.
     * @param _tokenId Token ID of the property to be listed.
     * @param _price Sale price in wei.
     */
    function listPropertyForSale(uint256 _tokenId, uint256 _price) external {
        require(ownerOf(_tokenId) == msg.sender, "Only the owner can list the property for sale");
        require(_price > 0, "Sale price must be greater than zero");

        CityProperty storage property = properties[_tokenId];
        property.forSale = true;
        property.price = _price;

        emit PropertyListedForSale(_tokenId, _price);
    }

    /**
     * @dev Remove a property from sale.
     * @param _tokenId Token ID of the property to be removed.
     */
    function removePropertyFromSale(uint256 _tokenId) external {
        require(ownerOf(_tokenId) == msg.sender, "Only the owner can remove the property from sale");

        CityProperty storage property = properties[_tokenId];
        property.forSale = false;

        emit PropertyRemovedFromSale(_tokenId);
    }

    /**
     * @dev Buy a property listed for sale.
     * @param _tokenId Token ID of the property to buy.
     */
    function buyProperty(uint256 _tokenId) external payable {
        CityProperty storage property = properties[_tokenId];
        require(property.forSale, "Property is not listed for sale");
        require(msg.value >= property.price, "Insufficient payment");

        address seller = ownerOf(_tokenId);

        // Transfer ownership of the property
        _transfer(seller, msg.sender, _tokenId);

        // Update property sale status
        property.forSale = false;

        // Pay the seller
        payable(seller).transfer(property.price);

        emit PropertySold(_tokenId, msg.sender, property.price);

        // Refund excess payment (if any)
        if (msg.value > property.price) {
            payable(msg.sender).transfer(msg.value - property.price);
        }
    }

    /**
     * @dev Get details of a property.
     * @param _tokenId Token ID of the property.
     * @return Property details (id, name, price, forSale).
     */
    function getPropertyDetails(uint256 _tokenId) external view returns (uint256, string memory, uint256, bool) {
        CityProperty memory property = properties[_tokenId];
        return (property.id, property.name, property.price, property.forSale);
    }
}
```
