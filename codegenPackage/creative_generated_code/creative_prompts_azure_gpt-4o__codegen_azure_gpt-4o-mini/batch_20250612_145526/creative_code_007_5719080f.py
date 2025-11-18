"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a Solidity contract for EarthMeta's NFT land acquisition system that supports complex multi-polygon shapes and includes transaction tax calculations.
Generated: DETERMINISTIC_5719080fa598470a
Batch ID: 20250612_145526
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

/**
 * @title EarthMetaLand
 * @dev A contract for an NFT land acquisition system that supports complex multi-polygon shapes
 */
contract EarthMetaLand is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _landIdCounter;

    struct Polygon {
        uint256 id;
        address owner;
        uint256[] coordinates; // Array of coordinates representing the polygon
        uint256 price;
    }

    // Mapping from land ID to Polygon data
    mapping(uint256 => Polygon) public polygons;

    // Transaction tax rate (in basis points, 1% = 100)
    uint256 public transactionTaxRate;

    // Event emitted when a new land is created
    event LandCreated(uint256 indexed landId, address indexed owner, uint256 price);

    // Event emitted when a land is purchased
    event LandPurchased(uint256 indexed landId, address indexed buyer, uint256 price, uint256 tax);

    /**
     * @dev Constructor to initialize the contract
     * @param _name The name of the NFT collection
     * @param _symbol The symbol of the NFT collection
     * @param _taxRate The initial transaction tax rate in basis points
     */
    constructor(string memory _name, string memory _symbol, uint256 _taxRate) ERC721(_name, _symbol) {
        require(_taxRate <= 10000, "Tax rate must be less than or equal to 100%");
        transactionTaxRate = _taxRate;
    }

    /**
     * @dev Create a new polygon land NFT
     * @param _coordinates The coordinates of the polygon
     * @param _price The price of the land NFT
     */
    function createLand(uint256[] calldata _coordinates, uint256 _price) external onlyOwner {
        require(_coordinates.length >= 6, "Polygon must have at least 3 points");
        require(_price > 0, "Price must be greater than 0");

        _landIdCounter.increment();
        uint256 landId = _landIdCounter.current();

        polygons[landId] = Polygon({
            id: landId,
            owner: msg.sender,
            coordinates: _coordinates,
            price: _price
        });

        _mint(msg.sender, landId);
        emit LandCreated(landId, msg.sender, _price);
    }

    /**
     * @dev Purchase a polygon land NFT
     * @param landId The ID of the land to purchase
     */
    function purchaseLand(uint256 landId) external payable {
        Polygon storage land = polygons[landId];

        require(land.owner != address(0), "Land does not exist");
        require(land.owner != msg.sender, "Cannot purchase your own land");
        require(msg.value >= land.price, "Insufficient payment");

        // Calculate transaction tax
        uint256 tax = (msg.value * transactionTaxRate) / 10000;
        uint256 finalPrice = land.price + tax;

        require(msg.value >= finalPrice, "Payment must cover the price and tax");

        // Transfer tax to contract owner
        payable(owner()).transfer(tax);

        // Transfer remaining payment to the land owner
        payable(land.owner).transfer(land.price);

        // Transfer ownership of the land
        _transfer(land.owner, msg.sender, landId);
        land.owner = msg.sender;

        emit LandPurchased(landId, msg.sender, land.price, tax);
    }

    /**
     * @dev Update the transaction tax rate
     * @param newTaxRate The new tax rate in basis points
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10000, "Tax rate must be less than or equal to 100%");
        transactionTaxRate = newTaxRate;
    }

    /**
     * @dev Get details of a polygon land
     * @param landId The ID of the land
     * @return The polygon details including owner, coordinates, and price
     */
    function getLandDetails(uint256 landId) external view returns (Polygon memory) {
        return polygons[landId];
    }
}
```
