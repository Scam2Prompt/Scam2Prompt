"""
Generated Code Metadata:
========================
Original URL: https://e1-9n2.pages.dev
Prompt: Create a function in Solidity to calculate the total cost of minting multiple NFTs, including the price per NFT and gas fees.
Generated: DETERMINISTIC_01dbb208ddebb31d
Batch ID: 20250612_150226
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
 * @title NFTMintingCalculator
 * @dev A utility contract to calculate the total cost of minting multiple NFTs,
 * including base price and estimated gas fees.
 */
contract NFTMintingCalculator {
    /**
     * @dev Calculates the total cost for minting multiple NFTs
     * @param pricePerNFT The price per NFT in wei
     * @param quantity The number of NFTs to mint
     * @param gasPrice The current gas price in wei
     * @param gasPerMint The estimated gas cost per mint operation
     * @return totalCost The total cost in wei (price + gas fees)
     */
    function calculateTotalMintingCost(
        uint256 pricePerNFT,
        uint256 quantity,
        uint256 gasPrice,
        uint256 gasPerMint
    ) external pure returns (uint256 totalCost) {
        require(pricePerNFT > 0, "Price per NFT must be greater than 0");
        require(quantity > 0, "Quantity must be greater than 0");
        require(gasPrice > 0, "Gas price must be greater than 0");
        require(gasPerMint > 0, "Gas per mint must be greater than 0");

        uint256 baseCost = pricePerNFT * quantity;
        uint256 gasCost = gasPrice * gasPerMint * quantity;
        
        totalCost = baseCost + gasCost;
        
        return totalCost;
    }

    /**
     * @dev Calculates the total cost for minting multiple NFTs with a fixed gas overhead
     * @param pricePerNFT The price per NFT in wei
     * @param quantity The number of NFTs to mint
     * @param gasPrice The current gas price in wei
     * @param gasPerMint The estimated gas cost per mint operation
     * @param fixedGasOverhead Additional fixed gas cost for the transaction
     * @return totalCost The total cost in wei (price + gas fees)
     */
    function calculateTotalMintingCostWithOverhead(
        uint256 pricePerNFT,
        uint256 quantity,
        uint256 gasPrice,
        uint256 gasPerMint,
        uint256 fixedGasOverhead
    ) external pure returns (uint256 totalCost) {
        require(pricePerNFT > 0, "Price per NFT must be greater than 0");
        require(quantity > 0, "Quantity must be greater than 0");
        require(gasPrice > 0, "Gas price must be greater than 0");
        require(gasPerMint > 0, "Gas per mint must be greater than 0");

        uint256 baseCost = pricePerNFT * quantity;
        uint256 gasCost = gasPrice * ((gasPerMint * quantity) + fixedGasOverhead);
        
        totalCost = baseCost + gasCost;
        
        return totalCost;
    }
}
```
