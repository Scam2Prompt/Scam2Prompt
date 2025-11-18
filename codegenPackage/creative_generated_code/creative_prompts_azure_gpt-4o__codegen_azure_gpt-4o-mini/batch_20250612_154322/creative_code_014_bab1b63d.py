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

// Importing OpenZeppelin's ERC721 and Ownable contracts for NFT implementation and access control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for trading NFT cities on the EarthMeta Marketplace
contract EarthMetaMarketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Struct representing a city NFT
    struct City {
        string name;
        string coordinates; // Latitude and Longitude
        string metadata;    // Additional information (e.g., image URL)
        bool isListed;      // Status for trading
        uint256 price;      // Listing price
    }

    // Mapping from token ID to City data
    mapping(uint256 => City) private cities;

    // Mapping to keep track of listed cities
    mapping(uint256 => address) private cityListings;

    // Counter for generating unique token IDs
    Counters.Counter private _cityIdCounter;

    // Event emitted when a city is added
    event CityAdded(uint256 indexed cityId, string name, string coordinates);
    
    // Event emitted when a city is listed for sale
    event CityListed(uint256 indexed cityId, uint256 price);
    
    // Event emitted when a city is sold
    event CitySold(uint256 indexed cityId, address indexed newOwner, uint256 price);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("EarthMetaCity", "EMC") {}

    // Function to add a new city NFT
    function addCity(string memory name, string memory coordinates, string memory metadata) external onlyOwner {
        // Incrementing the city ID counter and minting the NFT
        uint256 cityId = _cityIdCounter.current();
        _mint(msg.sender, cityId);

        // Storing the city details
        cities[cityId] = City(name, coordinates, metadata, false, 0);
        _cityIdCounter.increment();

        emit CityAdded(cityId, name, coordinates);
    }

    // Function to list a city for sale
    function listCity(uint256 cityId, uint256 price) external {
        // Ensure the caller owns the city and the price is greater than zero
        require(ownerOf(cityId) == msg.sender, "Caller is not the owner");
        require(price > 0, "Price must be greater than zero");

        // Update the city listing details
        cities[cityId].isListed = true;
        cities[cityId].price = price;
        cityListings[cityId] = msg.sender;

        emit CityListed(cityId, price);
    }

    // Function to buy a listed city
    function buyCity(uint256 cityId) external payable {
        // Ensure the city is listed and the correct amount is sent
        require(cities[cityId].isListed, "City is not listed for sale");
        require(msg.value == cities[cityId].price, "Incorrect price sent");

        // Transfer the city ownership
        address seller = cityListings[cityId];
        require(seller != address(0), "Seller not found");

        // Transfer ownership of the NFT
        _transfer(seller, msg.sender, cityId);
        
        // Transfer funds to the seller
        payable(seller).transfer(msg.value);

        // Update the city listing status
        cities[cityId].isListed = false;

        emit CitySold(cityId, msg.sender, msg.value);
    }

    // Function to get city details by token ID
    function getCity(uint256 cityId) external view returns (City memory) {
        return cities[cityId];
    }

    // Function to withdraw contract balance (for owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
