"""
Generated Code Metadata:
========================
Original URL: https://metamask-two.vercel.app
Prompt: "Develop a function in Solidity to calculate the total supply of NFTs in a collection given the number of editions per NFT."
Generated: DETERMINISTIC_098f3f5664cd22d0
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title NFTSupplyCalculator
 * @author [Your Name]
 * @notice A utility contract for calculating the total supply of NFTs in a collection.
 */
contract NFTSupplyCalculator {

    /**
     * @dev Calculates the total supply of NFTs in a collection given the number of editions per NFT.
     * @param editionsPerNFT The number of editions per NFT.
     * @param numNFTs The number of NFTs in the collection.
     * @return The total supply of NFTs in the collection.
     */
    function calculateTotalSupply(uint256[] memory editionsPerNFT, uint256 numNFTs) public pure returns (uint256) {
        // Check if the input arrays have the correct length
        require(editionsPerNFT.length == numNFTs, "Editions per NFT array length must match the number of NFTs");

        // Initialize total supply to 0
        uint256 totalSupply = 0;

        // Iterate over each NFT in the collection
        for (uint256 i = 0; i < numNFTs; i++) {
            // Add the editions of the current NFT to the total supply
            totalSupply += editionsPerNFT[i];
        }

        // Return the total supply
        return totalSupply;
    }

    /**
     * @dev Calculates the total supply of NFTs in a collection given the number of editions per NFT (using a single edition per NFT value).
     * @param editionsPerNFT The number of editions per NFT.
     * @param numNFTs The number of NFTs in the collection.
     * @return The total supply of NFTs in the collection.
     */
    function calculateTotalSupply(uint256 editionsPerNFT, uint256 numNFTs) public pure returns (uint256) {
        // Calculate and return the total supply
        return editionsPerNFT * numNFTs;
    }
}
```
