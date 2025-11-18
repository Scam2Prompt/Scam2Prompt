"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Write a Solidity function for calculating dynamic NFT prices based on attributes like rarity or type, as showcased in the pricing structure on enter.art.
Generated: DETERMINISTIC_389a75e40524662b
Batch ID: 20250612_151659
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
 * @title Dynamic Pricing for NFTs
 * @dev This contract calculates dynamic NFT prices based on attributes like rarity and type.
 */
contract DynamicNFTPricing {

    // Struct to define an NFT's attributes
    struct NFTAttributes {
        uint256 rarity; // Rarity level (e.g., 1 to 100)
        string nftType; // Type of NFT (e.g., "Art", "Collectible", "Music")
    }

    // Mapping to store base prices for different NFT types
    mapping(string => uint256) private basePrices;

    // Event to log calculated price for an NFT
    event PriceCalculated(uint256 price, uint256 rarity, string nftType);

    // Constructor to initialize base prices for known NFT types
    constructor() {
        basePrices["Art"] = 0.1 ether;
        basePrices["Collectible"] = 0.05 ether;
        basePrices["Music"] = 0.07 ether;
    }

    /**
     * @dev Function to calculate the price of an NFT based on its attributes.
     * @param attributes Struct containing NFT's rarity and type.
     * @return price The calculated price of the NFT.
     *
     * The price calculation logic:
     * - Base price is retrieved based on the NFT type.
     * - Dynamic price is calculated by multiplying base price with rarity modifier (rarity / 100).
     */
    function calculateNFTPrice(NFTAttributes memory attributes) public view returns (uint256 price) {
        // Check if the NFT type is valid
        require(basePrices[attributes.nftType] > 0, "Invalid NFT type");

        // Base price for the NFT type
        uint256 basePrice = basePrices[attributes.nftType];

        // Calculate dynamic price based on rarity
        // Rarity is divided by 100 to act as a multiplier (e.g., 50 rarity = 0.5 multiplier)
        price = basePrice * attributes.rarity / 100;

        // Emit price calculation event
        emit PriceCalculated(price, attributes.rarity, attributes.nftType);

        return price;
    }

    /**
     * @dev Function to update the base price for a given NFT type.
     * @param nftType Type of NFT.
     * @param newBasePrice New base price for the NFT type.
     *
     * Only the contract owner should be able to set new base prices.
     * For simplicity, this function does not include access control logic.
     */
    function updateBasePrice(string memory nftType, uint256 newBasePrice) public {
        require(newBasePrice > 0, "Base price must be greater than zero");
        basePrices[nftType] = newBasePrice;
    }
}
```
