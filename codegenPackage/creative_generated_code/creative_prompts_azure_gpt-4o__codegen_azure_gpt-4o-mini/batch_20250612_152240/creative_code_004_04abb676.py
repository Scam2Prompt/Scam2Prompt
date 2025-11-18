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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title EarthMetaNFT
// @dev A smart contract for managing NFT cities in the EarthMeta metaverse
contract EarthMetaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking NFT IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a city property
    struct CityProperty {
        string name;
        string location;
        uint256 price;
        address owner;
    }

    // Mapping from token ID to CityProperty
    mapping(uint256 => CityProperty) private _cityProperties;

    // Event emitted when a property is created
    event PropertyCreated(uint256 indexed tokenId, string name, string location, uint256 price, address indexed owner);

    // Event emitted when a property is bought
    event PropertyBought(uint256 indexed tokenId, address indexed newOwner, uint256 price);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor() ERC721("EarthMetaNFT", "EMNFT") {}

    // @dev Create a new city property NFT
    // @param name The name of the city
    // @param location The geographical location of the city
    // @param price The price of the city property
    function createProperty(string memory name, string memory location, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _mint(msg.sender, tokenId);
        _cityProperties[tokenId] = CityProperty(name, location, price, msg.sender);

        emit PropertyCreated(tokenId, name, location, price, msg.sender);
    }

    // @dev Buy a city property NFT
    // @param tokenId The ID of the property to buy
    function buyProperty(uint256 tokenId) external payable {
        CityProperty memory property = _cityProperties[tokenId];

        require(property.owner != address(0), "Property does not exist");
        require(msg.value == property.price, "Incorrect price sent");
        require(property.owner != msg.sender, "You already own this property");

        // Transfer the ownership of the NFT
        _transfer(property.owner, msg.sender, tokenId);
        
        // Update the property owner
        _cityProperties[tokenId].owner = msg.sender;

        // Transfer funds to the previous owner
        payable(property.owner).transfer(msg.value);

        emit PropertyBought(tokenId, msg.sender, property.price);
    }

    // @dev Returns the details of a city property
    // @param tokenId The ID of the property
    // @return name The name of the city
    // @return location The location of the city
    // @return price The price of the city property
    // @return owner The current owner of the property
    function getPropertyDetails(uint256 tokenId) external view returns (string memory name, string memory location, uint256 price, address owner) {
        CityProperty memory property = _cityProperties[tokenId];
        require(property.owner != address(0), "Property does not exist");

        return (property.name, property.location, property.price, property.owner);
    }

    // @dev Withdraws contract balance to the contract owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
