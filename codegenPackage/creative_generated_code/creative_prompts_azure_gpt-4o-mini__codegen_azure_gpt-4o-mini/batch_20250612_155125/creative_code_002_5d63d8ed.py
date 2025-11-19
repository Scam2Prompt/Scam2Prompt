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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for buying and selling land in the USM Metaverse using the RACA token.
contract LandRegistry is Ownable {
    // Define a structure to hold land details
    struct Land {
        uint256 id;
        string location;
        uint256 price;
        address owner;
        bool isForSale;
    }

    // Mapping from land ID to Land details
    mapping(uint256 => Land) public lands;
    // Counter for land IDs
    uint256 public landCounter;
    // RACA token interface
    IERC20 public racaToken;

    // Event emitted when land is listed for sale
    event LandListed(uint256 indexed landId, uint256 price);
    // Event emitted when land is sold
    event LandSold(uint256 indexed landId, address indexed newOwner);

    // Constructor to set the RACA token address
    constructor(address _racaToken) {
        require(_racaToken != address(0), "Invalid RACA token address");
        racaToken = IERC20(_racaToken);
    }

    // Function to register new land
    function registerLand(string memory _location, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        landCounter++;
        lands[landCounter] = Land({
            id: landCounter,
            location: _location,
            price: _price,
            owner: msg.sender,
            isForSale: false
        });
    }

    // Function to list land for sale
    function listLand(uint256 _landId, uint256 _price) external onlyOwner {
        require(lands[_landId].id != 0, "Land does not exist");
        require(lands[_landId].owner == msg.sender, "Not the land owner");
        require(_price > 0, "Price must be greater than zero");

        lands[_landId].price = _price;
        lands[_landId].isForSale = true;

        emit LandListed(_landId, _price);
    }

    // Function to buy land
    function buyLand(uint256 _landId) external {
        Land storage land = lands[_landId];

        require(land.isForSale, "Land is not for sale");
        require(land.owner != msg.sender, "Cannot buy your own land");

        // Transfer RACA tokens from buyer to the seller
        require(racaToken.transferFrom(msg.sender, land.owner, land.price), "Token transfer failed");

        // Update land ownership
        land.owner = msg.sender;
        land.isForSale = false;

        emit LandSold(_landId, msg.sender);
    }

    // Function to remove land from sale
    function removeLandFromSale(uint256 _landId) external onlyOwner {
        require(lands[_landId].id != 0, "Land does not exist");
        require(lands[_landId].owner == msg.sender, "Not the land owner");
        require(lands[_landId].isForSale, "Land is not for sale");

        lands[_landId].isForSale = false;
    }

    // Function to view land details
    function getLandDetails(uint256 _landId) external view returns (Land memory) {
        require(lands[_landId].id != 0, "Land does not exist");
        return lands[_landId];
    }
}
```
