"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smeth.pages.dev
Prompt: Write Solidity code for a custom NFT contract that stores both image data and attributes fully on-chain, inspired by the compression techniques used for CryptoPunks.
Generated: DETERMINISTIC_37ab4f9e7869737e
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
 * @title OnChainNFT
 * @dev Custom NFT contract that stores both image data and attributes fully on-chain.
 * Inspired by compression techniques used for CryptoPunks.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OnChainNFT is ERC721Enumerable, Ownable {
    // Struct to store NFT metadata
    struct NFTMetadata {
        string attributes; // Compressed attributes string
        bytes imageData;   // Compressed image data (e.g., base64 encoded or binary data)
    }

    // Mapping from token ID to metadata
    mapping(uint256 => NFTMetadata) private metadata;

    // Event emitted when metadata is set for a token
    event MetadataSet(uint256 indexed tokenId, string attributes, bytes imageData);

    // Constructor to initialize the NFT contract
    constructor() ERC721("OnChainNFT", "ONFT") {}

    /**
     * @notice Mint a new NFT and set its metadata.
     * @dev Metadata is stored fully on-chain.
     * @param to Address to mint the NFT to.
     * @param tokenId Token ID of the new NFT.
     * @param attributes Compressed attributes string.
     * @param imageData Compressed image data.
     */
    function mintNFT(
        address to,
        uint256 tokenId,
        string memory attributes,
        bytes memory imageData
    ) external onlyOwner {
        // Ensure token ID does not already exist
        require(!_exists(tokenId), "Token ID already exists");

        // Mint the NFT
        _mint(to, tokenId);

        // Set metadata
        metadata[tokenId] = NFTMetadata(attributes, imageData);

        // Emit event
        emit MetadataSet(tokenId, attributes, imageData);
    }

    /**
     * @notice Get the metadata for a given token ID.
     * @param tokenId Token ID of the NFT.
     * @return attributes The attributes string of the NFT.
     * @return imageData The image data of the NFT.
     */
    function getMetadata(uint256 tokenId)
        external
        view
        returns (string memory attributes, bytes memory imageData)
    {
        // Ensure token exists
        require(_exists(tokenId), "Token does not exist");

        NFTMetadata storage data = metadata[tokenId];
        return (data.attributes, data.imageData);
    }

    /**
     * @notice Update metadata for an existing NFT.
     * @dev Only the contract owner can update metadata.
     * @param tokenId Token ID of the NFT.
     * @param attributes New compressed attributes string.
     * @param imageData New compressed image data.
     */
    function updateMetadata(
        uint256 tokenId,
        string memory attributes,
        bytes memory imageData
    ) external onlyOwner {
        // Ensure token exists
        require(_exists(tokenId), "Token does not exist");

        // Update metadata
        metadata[tokenId] = NFTMetadata(attributes, imageData);

        // Emit event
        emit MetadataSet(tokenId, attributes, imageData);
    }

    /**
     * @notice Burn an NFT and delete its metadata.
     * @dev Only the contract owner can burn NFTs.
     * @param tokenId Token ID of the NFT to burn.
     */
    function burnNFT(uint256 tokenId) external onlyOwner {
        // Ensure token exists
        require(_exists(tokenId), "Token does not exist");

        // Delete metadata
        delete metadata[tokenId];

        // Burn the NFT
        _burn(tokenId);
    }
}
```
