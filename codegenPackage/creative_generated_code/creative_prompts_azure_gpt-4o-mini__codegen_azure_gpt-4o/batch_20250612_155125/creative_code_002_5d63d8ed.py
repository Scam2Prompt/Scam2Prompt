"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Create a smart contract in Solidity that allows users to buy and sell land in the USM Metaverse using the RACA token.
Generated: DETERMINISTIC_5d63d8edd0d26184
Batch ID: 20250612_155125
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
 * @title USM Metaverse Land Marketplace
 * @dev This contract allows users to buy and sell land parcels in the USM Metaverse using the RACA token.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MetaverseLandMarketplace {
    // RACA token contract
    IERC20 public racaToken;

    // Struct representing a land parcel
    struct Land {
        uint256 id;
        address owner;
        uint256 price;
        bool isForSale;
    }

    // Mapping to store land parcels (id => Land)
    mapping(uint256 => Land) public lands;

    // Total number of land parcels
    uint256 public totalLands;

    // Events
    event LandListed(uint256 indexed id, address indexed owner, uint256 price);
    event LandDelisted(uint256 indexed id, address indexed owner);
    event LandSold(uint256 indexed id, address indexed seller, address indexed buyer, uint256 price);

    /**
     * @dev Constructor to initialize the RACA token address.
     * @param _racaTokenAddress Address of the RACA token contract.
     */
    constructor(address _racaTokenAddress) {
        require(_racaTokenAddress != address(0), "Invalid RACA token address");
        racaToken = IERC20(_racaTokenAddress);
    }

    /**
     * @dev Function to list a new land parcel for sale.
     * @param _price Price of the land parcel (in RACA tokens).
     */
    function listLandForSale(uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Create a new land parcel
        totalLands++;
        lands[totalLands] = Land({
            id: totalLands,
            owner: msg.sender,
            price: _price,
            isForSale: true
        });

        emit LandListed(totalLands, msg.sender, _price);
    }

    /**
     * @dev Function to delist a land parcel from sale.
     * @param _landId ID of the land parcel to delist.
     */
    function delistLand(uint256 _landId) external {
        Land storage land = lands[_landId];
        require(land.isForSale, "Land is not listed for sale");
        require(land.owner == msg.sender, "Only the owner can delist the land");

        land.isForSale = false;

        emit LandDelisted(_landId, msg.sender);
    }

    /**
     * @dev Function to buy a land parcel.
     * @param _landId ID of the land parcel to buy.
     */
    function buyLand(uint256 _landId) external {
        Land storage land = lands[_landId];
        require(land.isForSale, "Land is not listed for sale");
        require(land.owner != msg.sender, "Owner cannot buy their own land");

        // Transfer RACA tokens from the buyer to the seller
        require(
            racaToken.transferFrom(msg.sender, land.owner, land.price),
            "Token transfer failed"
        );

        // Transfer ownership of the land
        address previousOwner = land.owner;
        land.owner = msg.sender;
        land.isForSale = false;

        emit LandSold(_landId, previousOwner, msg.sender, land.price);
    }

    /**
     * @dev Function to view the details of a land parcel.
     * @param _landId ID of the land parcel to view.
     * @return Land details (id, owner, price, isForSale).
     */
    function viewLand(uint256 _landId) external view returns (Land memory) {
        return lands[_landId];
    }
}
```
