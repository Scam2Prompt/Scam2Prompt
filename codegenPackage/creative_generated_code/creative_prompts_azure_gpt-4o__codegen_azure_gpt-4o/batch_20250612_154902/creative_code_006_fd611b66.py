"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Write a Solidity smart contract that allows users to interact with Blur NFTs by toggling between different layers or levels of abstraction in the artwork.
Generated: DETERMINISTIC_fd611b661cc467d9
Batch ID: 20250612_154902
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
 * @title BlurNFTLayerManager
 * @dev This contract allows users to interact with Blur NFTs by toggling different layers of artwork abstraction.
 */
contract BlurNFTLayerManager {
    // Struct representing the metadata of a Blur NFT
    struct BlurNFT {
        uint256 tokenId;
        address owner;
        string baseLayerURI;
        string[] abstractionLayersURIs;
        uint256 activeLayerIndex;
    }

    // Mapping from token ID to BlurNFT metadata
    mapping(uint256 => BlurNFT) private blurNFTs;

    // Event emitted when a layer is toggled for a specific NFT
    event LayerToggled(uint256 indexed tokenId, uint256 newActiveLayerIndex);

    // Modifier to check if the caller is the owner of the NFT
    modifier onlyOwner(uint256 tokenId) {
        require(msg.sender == blurNFTs[tokenId].owner, "Caller is not the owner of the NFT");
        _;
    }

    /**
     * @dev Function to register a new Blur NFT with its layers.
     * @param tokenId The unique identifier of the NFT.
     * @param owner The address of the NFT owner.
     * @param baseLayerURI The URI of the base layer artwork.
     * @param abstractionLayersURIs An array of URIs for different abstraction layers.
     */
    function registerBlurNFT(
        uint256 tokenId,
        address owner,
        string memory baseLayerURI,
        string[] memory abstractionLayersURIs
    ) external {
        require(blurNFTs[tokenId].owner == address(0), "NFT with this token ID already exists");

        blurNFTs[tokenId] = BlurNFT({
            tokenId: tokenId,
            owner: owner,
            baseLayerURI: baseLayerURI,
            abstractionLayersURIs: abstractionLayersURIs,
            activeLayerIndex: 0 // Default to base layer
        });
    }

    /**
     * @dev Function to toggle the active layer of a specific Blur NFT.
     * @param tokenId The unique identifier of the NFT.
     * @param layerIndex The index of the layer to activate.
     */
    function toggleLayer(uint256 tokenId, uint256 layerIndex) external onlyOwner(tokenId) {
        BlurNFT storage nft = blurNFTs[tokenId];

        require(layerIndex < nft.abstractionLayersURIs.length, "Invalid layer index");

        nft.activeLayerIndex = layerIndex;

        emit LayerToggled(tokenId, layerIndex);
    }

    /**
     * @dev Function to get the active layer URI of a Blur NFT.
     * @param tokenId The unique identifier of the NFT.
     * @return The URI of the active layer.
     */
    function getActiveLayerURI(uint256 tokenId) external view returns (string memory) {
        BlurNFT storage nft = blurNFTs[tokenId];

        // Return the active layer URI based on the index
        if (nft.activeLayerIndex == 0) {
            return nft.baseLayerURI;
        } else {
            return nft.abstractionLayersURIs[nft.activeLayerIndex];
        }
    }

    /**
     * @dev Function to get all abstraction layer URIs of a Blur NFT.
     * @param tokenId The unique identifier of the NFT.
     * @return An array of URIs for all abstraction layers.
     */
    function getAllLayerURIs(uint256 tokenId) external view returns (string[] memory) {
        return blurNFTs[tokenId].abstractionLayersURIs;
    }
}
```
