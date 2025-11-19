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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title EarthMetaCities
 * @dev A smart contract for creating and managing NFT cities on the EarthMeta platform.
 * Supports buying, selling, and trading of digital city assets.
 */
contract EarthMetaCities is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store city metadata
    struct City {
        string name;
        uint256 latitude;
        uint256 longitude;
        uint256 price;
        bool forSale;
    }

    // Mapping from token ID to City
    mapping(uint256 => City) private _cities;

    // Mapping from owner address to their owned token IDs
    mapping(address => uint256[]) private _ownedCities;

    // Event emitted when a city is created
    event CityCreated(uint256 indexed tokenId, string name, uint256 latitude, uint256 longitude, uint256 price);

    // Event emitted when a city is bought
    event CityBought(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Event emitted when a city is listed for sale
    event CityListedForSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when a city is unlisted from sale
    event CityUnlistedFromSale(uint256 indexed tokenId);

    /**
     * @dev Constructor function
     */
    constructor() ERC721("EarthMetaCities", "EMC") {}

    /**
     * @dev Creates a new city NFT
     * @param name The name of the city
     * @param latitude The latitude coordinate of the city
     * @param longitude The longitude coordinate of the city
     * @param price The initial price of the city
     */
    function createCity(
        string memory name,
        uint256 latitude,
        uint256 longitude,
        uint256 price
    ) external onlyOwner {
        require(bytes(name).length > 0, "City name cannot be empty");
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(msg.sender, tokenId);
        
        _cities[tokenId] = City({
            name: name,
            latitude: latitude,
            longitude: longitude,
            price: price,
            forSale: false
        });

        _ownedCities[msg.sender].push(tokenId);

        emit CityCreated(tokenId, name, latitude, longitude, price);
    }

    /**
     * @dev Lists a city for sale
     * @param tokenId The ID of the city to list
     * @param price The sale price
     */
    function listCityForSale(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "City does not exist");
        require(ownerOf(tokenId) == msg.sender, "You don't own this city");
        require(price > 0, "Price must be greater than zero");

        _cities[tokenId].price = price;
        _cities[tokenId].forSale = true;

        emit CityListedForSale(tokenId, price);
    }

    /**
     * @dev Unlists a city from sale
     * @param tokenId The ID of the city to unlist
     */
    function unlistCityFromSale(uint256 tokenId) external {
        require(_exists(tokenId), "City does not exist");
        require(ownerOf(tokenId) == msg.sender, "You don't own this city");

        _cities[tokenId].forSale = false;

        emit CityUnlistedFromSale(tokenId);
    }

    /**
     * @dev Buys a city that is listed for sale
     * @param tokenId The ID of the city to buy
     */
    function buyCity(uint256 tokenId) external payable nonReentrant {
        require(_exists(tokenId), "City does not exist");
        require(_cities[tokenId].forSale, "City is not for sale");
        require(msg.value >= _cities[tokenId].price, "Insufficient funds");
        require(ownerOf(tokenId) != msg.sender, "You already own this city");

        address seller = ownerOf(tokenId);
        uint256 price = _cities[tokenId].price;

        // Transfer ownership
        _transfer(seller, msg.sender, tokenId);

        // Update ownership tracking
        _removeCityFromOwner(seller, tokenId);
        _ownedCities[msg.sender].push(tokenId);

        // Transfer funds
        payable(seller).transfer(price);

        // If buyer sent more than price, refund the difference
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }

        // Update city status
        _cities[tokenId].forSale = false;

        emit CityBought(tokenId, msg.sender, price);
    }

    /**
     * @dev Gets city details by token ID
     * @param tokenId The ID of the city
     * @return City details
     */
    function getCity(uint256 tokenId) external view returns (
        string memory name,
        uint256 latitude,
        uint256 longitude,
        uint256 price,
        bool forSale,
        address owner
    ) {
        require(_exists(tokenId), "City does not exist");
        City memory city = _cities[tokenId];
        return (
            city.name,
            city.latitude,
            city.longitude,
            city.price,
            city.forSale,
            ownerOf(tokenId)
        );
    }

    /**
     * @dev Gets all cities owned by an address
     * @param owner The address to query
     * @return Array of token IDs
     */
    function getCitiesByOwner(address owner) external view returns (uint256[] memory) {
        return _ownedCities[owner];
    }

    /**
     * @dev Internal function to remove a city from an owner's list
     * @param owner The owner's address
     * @param tokenId The ID of the city to remove
     */
    function _removeCityFromOwner(address owner, uint256 tokenId) private {
        uint256[] storage cities = _ownedCities[owner];
        for (uint256 i = 0; i < cities.length; i++) {
            if (cities[i] == tokenId) {
                cities[i] = cities[cities.length - 1];
                cities.pop();
                break;
            }
        }
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
