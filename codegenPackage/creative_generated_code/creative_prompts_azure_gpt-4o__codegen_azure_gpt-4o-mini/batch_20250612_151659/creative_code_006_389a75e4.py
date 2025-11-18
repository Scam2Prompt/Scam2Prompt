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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DynamicNFT is a contract for creating dynamic NFT pricing based on attributes
contract DynamicNFT is ERC721Enumerable, Ownable {
    // Struct to hold NFT attributes
    struct NFTAttributes {
        string rarity; // Rarity of the NFT
        string nftType; // Type of the NFT
    }

    // Mapping from token ID to its attributes
    mapping(uint256 => NFTAttributes) private _attributes;

    // Base price for NFTs
    uint256 private constant BASE_PRICE = 0.1 ether;

    // Mapping of rarity multipliers
    mapping(string => uint256) private _rarityMultipliers;

    // Event emitted when NFT price is calculated
    event PriceCalculated(uint256 tokenId, uint256 price);

    // Constructor to initialize the ERC721 token and rarity multipliers
    constructor() ERC721("DynamicNFT", "DNFT") {
        // Set rarity multipliers
        _rarityMultipliers["common"] = 1;
        _rarityMultipliers["rare"] = 2;
        _rarityMultipliers["epic"] = 3;
        _rarityMultipliers["legendary"] = 4;
    }

    // Function to mint a new NFT with specified attributes
    function mintNFT(address to, uint256 tokenId, string memory rarity, string memory nftType) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        _attributes[tokenId] = NFTAttributes(rarity, nftType);
        _mint(to, tokenId);
    }

    // Function to calculate the price of an NFT based on its attributes
    function calculatePrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");

        // Get attributes for the specified token ID
        NFTAttributes memory attributes = _attributes[tokenId];

        // Calculate price based on rarity
        uint256 multiplier = _rarityMultipliers[attributes.rarity];
        require(multiplier > 0, "Rarity not recognized");

        // Calculate final price
        uint256 price = BASE_PRICE * multiplier;

        emit PriceCalculated(tokenId, price);
        return price;
    }

    // Function to retrieve attributes of a specific NFT
    function getAttributes(uint256 tokenId) external view returns (NFTAttributes memory) {
        require(_exists(tokenId), "Token does not exist");
        return _attributes[tokenId];
    }
}
```
