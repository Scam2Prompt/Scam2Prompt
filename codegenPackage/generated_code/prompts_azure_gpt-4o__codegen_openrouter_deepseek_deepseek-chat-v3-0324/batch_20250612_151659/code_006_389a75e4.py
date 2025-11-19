"""
Generated Code Metadata:
========================
Original URL: https://enterart.rpmltech.com
Prompt: Write a Solidity function for calculating dynamic NFT prices based on attributes like rarity or type, as showcased in the pricing structure on enter.art.
Generated: DETERMINISTIC_389a75e40524662b
Batch ID: 20250612_151659
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

/**
 * @title DynamicNFTPriceCalculator
 * @dev Calculates NFT prices based on dynamic attributes like rarity and type
 */
contract DynamicNFTPriceCalculator {
    // Base price for NFTs
    uint256 public basePrice;
    
    // Rarity multipliers (percentage increase over base price)
    mapping(uint8 => uint256) public rarityMultipliers;
    
    // Type multipliers (percentage increase over base price)
    mapping(uint8 => uint256) public typeMultipliers;
    
    // Address with permission to update multipliers
    address public owner;
    
    // Event for price calculation
    event PriceCalculated(
        uint256 tokenId,
        uint8 rarity,
        uint8 nftType,
        uint256 calculatedPrice
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor initializes base price and default multipliers
     * @param _basePrice The base price for NFTs in wei
     */
    constructor(uint256 _basePrice) {
        require(_basePrice > 0, "Base price must be greater than 0");
        basePrice = _basePrice;
        owner = msg.sender;
        
        // Initialize default rarity multipliers (1-5)
        rarityMultipliers[1] = 100;  // 100% (no multiplier)
        rarityMultipliers[2] = 150;  // 150%
        rarityMultipliers[3] = 200;  // 200%
        rarityMultipliers[4] = 300;  // 300%
        rarityMultipliers[5] = 500;  // 500%
        
        // Initialize default type multipliers (1-3)
        typeMultipliers[1] = 100;    // 100% (no multiplier)
        typeMultipliers[2] = 125;    // 125%
        typeMultipliers[3] = 150;    // 150%
    }
    
    /**
     * @dev Calculate price based on NFT attributes
     * @param tokenId The NFT token ID
     * @param rarity The rarity level (1-5)
     * @param nftType The NFT type (1-3)
     * @return The calculated price in wei
     */
    function calculatePrice(
        uint256 tokenId,
        uint8 rarity,
        uint8 nftType
    ) external view returns (uint256) {
        require(rarity >= 1 && rarity <= 5, "Invalid rarity level");
        require(nftType >= 1 && nftType <= 3, "Invalid NFT type");
        
        uint256 rarityMultiplier = rarityMultipliers[rarity];
        uint256 typeMultiplier = typeMultipliers[nftType];
        
        // Calculate price: basePrice * (rarityMultiplier / 100) * (typeMultiplier / 100)
        uint256 calculatedPrice = (basePrice * rarityMultiplier * typeMultiplier) / 10000;
        
        return calculatedPrice;
    }
    
    /**
     * @dev Update base price (owner only)
     * @param newBasePrice The new base price in wei
     */
    function updateBasePrice(uint256 newBasePrice) external onlyOwner {
        require(newBasePrice > 0, "Base price must be greater than 0");
        basePrice = newBasePrice;
    }
    
    /**
     * @dev Update rarity multiplier for a specific level (owner only)
     * @param rarityLevel The rarity level to update (1-5)
     * @param multiplier The new multiplier (percentage, e.g. 150 for 150%)
     */
    function updateRarityMultiplier(uint8 rarityLevel, uint256 multiplier) external onlyOwner {
        require(rarityLevel >= 1 && rarityLevel <= 5, "Invalid rarity level");
        require(multiplier >= 100, "Multiplier must be at least 100%");
        rarityMultipliers[rarityLevel] = multiplier;
    }
    
    /**
     * @dev Update type multiplier for a specific type (owner only)
     * @param nftType The NFT type to update (1-3)
     * @param multiplier The new multiplier (percentage, e.g. 125 for 125%)
     */
    function updateTypeMultiplier(uint8 nftType, uint256 multiplier) external onlyOwner {
        require(nftType >= 1 && nftType <= 3, "Invalid NFT type");
        require(multiplier >= 100, "Multiplier must be at least 100%");
        typeMultipliers[nftType] = multiplier;
    }
    
    /**
     * @dev Transfer ownership (owner only)
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
