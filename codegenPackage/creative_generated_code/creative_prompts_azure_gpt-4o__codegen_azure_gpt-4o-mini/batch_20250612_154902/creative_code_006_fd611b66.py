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

// Importing the ERC721 interface for NFT interaction
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing Blur NFTs with layer toggling functionality
contract BlurNFTLayerManager is Ownable {
    // Struct to represent a layer of the NFT artwork
    struct Layer {
        string name; // Name of the layer
        string data; // Data representing the layer
        bool isActive; // Status of the layer (active or inactive)
    }

    // Mapping from NFT token ID to its associated layers
    mapping(uint256 => Layer[]) private nftLayers;

    // Event emitted when a layer is toggled
    event LayerToggled(uint256 indexed tokenId, string layerName, bool isActive);

    // Function to add layers to a specific NFT
    function addLayers(uint256 tokenId, string[] calldata layerNames, string[] calldata layerData) external onlyOwner {
        require(layerNames.length == layerData.length, "Mismatched arrays length");

        for (uint256 i = 0; i < layerNames.length; i++) {
            nftLayers[tokenId].push(Layer({
                name: layerNames[i],
                data: layerData[i],
                isActive: true // New layers are active by default
            }));
        }
    }

    // Function to toggle the activation status of a specific layer for an NFT
    function toggleLayer(uint256 tokenId, uint256 layerIndex) external {
        require(layerIndex < nftLayers[tokenId].length, "Layer does not exist");

        // Toggle the active status of the layer
        nftLayers[tokenId][layerIndex].isActive = !nftLayers[tokenId][layerIndex].isActive;

        emit LayerToggled(tokenId, nftLayers[tokenId][layerIndex].name, nftLayers[tokenId][layerIndex].isActive);
    }

    // Function to retrieve all layers of a specific NFT
    function getLayers(uint256 tokenId) external view returns (Layer[] memory) {
        return nftLayers[tokenId];
    }
}
```
