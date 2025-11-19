"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Write a Solidity smart contract code for creating and managing NFT cities on the EarthMeta platform, including functions for buying, selling, and trading these digital assets.
Generated: DETERMINISTIC_64eb53a6b39ad21f
Batch ID: 20250622_211557
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title NFTCity - A smart contract for creating and managing NFT cities on the EarthMeta platform
contract NFTCity is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a city
    struct City {
        string name;
        string location;
        uint256 price;
        address owner;
    }

    // Mapping from token ID to City details
    mapping(uint256 => City) private cities;

    // Counter for token IDs
    Counters.Counter private _cityIdCounter;

    // Event emitted when a city is created
    event CityCreated(uint256 indexed cityId, string name, string location, uint256 price, address indexed owner);

    // Event emitted when a city is sold
    event CitySold(uint256 indexed cityId, address indexed previousOwner, address indexed newOwner, uint256 price);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("NFTCity", "CITY") {}

    // Function to create a new city NFT
    function createCity(string memory _name, string memory _location, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        uint256 cityId = _cityIdCounter.current();
        _cityIdCounter.increment();

        cities[cityId] = City({
            name: _name,
            location: _location,
            price: _price,
            owner: msg.sender
        });

        _mint(msg.sender, cityId);
        emit CityCreated(cityId, _name, _location, _price, msg.sender);
    }

    // Function to buy a city NFT
    function buyCity(uint256 _cityId) external payable {
        City storage city = cities[_cityId];
        require(city.owner != address(0), "City does not exist");
        require(msg.value >= city.price, "Insufficient funds sent");
        require(city.owner != msg.sender, "You already own this city");

        // Transfer ownership
        address previousOwner = city.owner;
        city.owner = msg.sender;

        // Transfer the NFT
        _transfer(previousOwner, msg.sender, _cityId);

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit CitySold(_cityId, previousOwner, msg.sender, city.price);
    }

    // Function to get city details
    function getCity(uint256 _cityId) external view returns (string memory, string memory, uint256, address) {
        City storage city = cities[_cityId];
        require(city.owner != address(0), "City does not exist");
        return (city.name, city.location, city.price, city.owner);
    }

    // Function to update the price of a city
    function updateCityPrice(uint256 _cityId, uint256 _newPrice) external {
        City storage city = cities[_cityId];
        require(city.owner == msg.sender, "Only the owner can update the price");
        require(_newPrice > 0, "Price must be greater than zero");

        city.price = _newPrice;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(msg.sender).transfer(balance);
    }
}
```
