"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Develop a smart contract for trading NFT cities on the EarthMeta Marketplace, ensuring accurate information and decentralized governance.
Generated: DETERMINISTIC_bab1b63dc59b5d44
Batch ID: 20250612_154322
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
 * @title EarthMeta NFT City Marketplace
 * @dev Smart contract for trading NFT cities on the EarthMeta Marketplace.
 * Provides decentralized governance and accurate trading functionality.
 */
contract EarthMetaMarketplace {
    // Struct to represent an NFT City
    struct City {
        uint256 id;
        string name;
        string metadataURI;
        address owner;
        uint256 price;
        bool forSale;
    }

    // State variables
    uint256 private cityCounter; // Counter for unique city IDs
    address public owner; // Contract owner
    mapping(uint256 => City) public cities; // Mapping to store cities by ID

    // Events
    event CityCreated(uint256 indexed cityId, string name, address indexed owner, string metadataURI);
    event CityListedForSale(uint256 indexed cityId, uint256 price);
    event CitySold(uint256 indexed cityId, address indexed oldOwner, address indexed newOwner, uint256 price);
    event CityDelisted(uint256 indexed cityId);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    // Modifier to restrict access to the city owner
    modifier onlyCityOwner(uint256 cityId) {
        require(msg.sender == cities[cityId].owner, "Only the city owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new NFT city
     * @param name Name of the city
     * @param metadataURI Metadata URI for the city
     */
    function createCity(string memory name, string memory metadataURI) external {
        cityCounter++;
        cities[cityCounter] = City({
            id: cityCounter,
            name: name,
            metadataURI: metadataURI,
            owner: msg.sender,
            price: 0,
            forSale: false
        });

        emit CityCreated(cityCounter, name, msg.sender, metadataURI);
    }

    /**
     * @dev Function to list a city for sale
     * @param cityId ID of the city to be listed
     * @param price Price of the city in wei
     */
    function listCityForSale(uint256 cityId, uint256 price) external onlyCityOwner(cityId) {
        require(price > 0, "Price must be greater than zero.");
        City storage city = cities[cityId];
        city.price = price;
        city.forSale = true;

        emit CityListedForSale(cityId, price);
    }

    /**
     * @dev Function to buy a city
     * @param cityId ID of the city to be bought
     */
    function buyCity(uint256 cityId) external payable {
        City storage city = cities[cityId];
        require(city.forSale, "City is not for sale.");
        require(msg.value == city.price, "Incorrect price sent.");

        address previousOwner = city.owner;
        city.owner = msg.sender;
        city.forSale = false;
        city.price = 0;

        // Transfer payment to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit CitySold(cityId, previousOwner, msg.sender, msg.value);
    }

    /**
     * @dev Function to delist a city from sale
     * @param cityId ID of the city to be delisted
     */
    function delistCity(uint256 cityId) external onlyCityOwner(cityId) {
        City storage city = cities[cityId];
        city.forSale = false;
        city.price = 0;

        emit CityDelisted(cityId);
    }

    /**
     * @dev Function to fetch city details
     * @param cityId ID of the city to fetch
     * @return City details as a struct
     */
    function getCity(uint256 cityId) external view returns (City memory) {
        return cities[cityId];
    }
}
```
