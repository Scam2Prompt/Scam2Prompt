"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a Solidity contract for managing NFT cities in the EarthMeta metaverse, allowing users to buy, sell, and trade virtual properties while incorporating a 2% transaction tax as described on the site.
Generated: DETERMINISTIC_9695f432dfd2b4c9
Batch ID: 20250612_152658
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

// @title EarthMeta NFT City Management Contract
// @dev This contract allows users to buy, sell, and trade virtual properties as NFTs with a transaction tax.
contract EarthMetaCities is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent a City
    struct City {
        string name;
        uint256 price;
        address owner;
    }

    // Variables
    Counters.Counter private _cityIdCounter; // Counter for city IDs
    mapping(uint256 => City) private _cities; // Mapping of city IDs to City struct
    uint256 public transactionTaxPercent = 2; // Transaction tax percentage
    uint256 public totalCities; // Total number of cities created

    // Events
    event CityCreated(uint256 indexed cityId, string name, uint256 price, address indexed owner);
    event CityTransferred(uint256 indexed cityId, address indexed from, address indexed to, uint256 salePrice);
    
    // Constructor to initialize the NFT contract with a name and symbol
    constructor() ERC721("EarthMetaCity", "EMC") {}

    // @dev Create a new city NFT
    // @param name The name of the city
    // @param price The initial price of the city
    function createCity(string memory name, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 cityId = _cityIdCounter.current();
        _cityIdCounter.increment();
        totalCities++;

        _safeMint(msg.sender, cityId);
        _cities[cityId] = City(name, price, msg.sender);

        emit CityCreated(cityId, name, price, msg.sender);
    }

    // @dev Buy a city NFT
    // @param cityId The ID of the city to purchase
    function buyCity(uint256 cityId) external payable {
        require(_exists(cityId), "City does not exist");
        City storage city = _cities[cityId];
        require(msg.value >= city.price, "Insufficient funds sent");

        uint256 taxAmount = (msg.value * transactionTaxPercent) / 100;
        uint256 sellerAmount = msg.value - taxAmount;

        // Transfer tax to the contract owner
        payable(owner()).transfer(taxAmount);
        // Transfer remaining amount to the seller
        payable(city.owner).transfer(sellerAmount);

        // Transfer the city ownership
        _transfer(city.owner, msg.sender, cityId);
        city.owner = msg.sender;

        emit CityTransferred(cityId, city.owner, msg.sender, city.price);
    }

    // @dev Get city details by ID
    // @param cityId The ID of the city to retrieve
    // @return name The name of the city
    // @return price The price of the city
    // @return owner The current owner of the city
    function getCity(uint256 cityId) external view returns (string memory name, uint256 price, address owner) {
        require(_exists(cityId), "City does not exist");
        City storage city = _cities[cityId];
        return (city.name, city.price, city.owner);
    }
    
    // @dev Update the price of a city NFT
    // @param cityId The ID of the city to update
    // @param newPrice The new price for the city
    function updateCityPrice(uint256 cityId, uint256 newPrice) external {
        require(_exists(cityId), "City does not exist");
        City storage city = _cities[cityId];
        require(msg.sender == city.owner, "Only the owner can update the price");
        require(newPrice > 0, "Price must be greater than zero");

        city.price = newPrice;
    }
    
    // @dev Function to withdraw leftover balance from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
