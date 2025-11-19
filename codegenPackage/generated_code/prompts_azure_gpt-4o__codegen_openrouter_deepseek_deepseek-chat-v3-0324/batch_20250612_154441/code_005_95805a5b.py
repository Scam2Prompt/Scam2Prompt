"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract that categorizes NFT holders into groups (e.g., Human, Robot, Demon, etc.) based on metadata, as described in the Clone Force™ pledge system.
Generated: DETERMINISTIC_95805a5b1c06872c
Batch ID: 20250612_154441
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CloneForceCategorizer
 * @dev Smart contract that categorizes NFT holders into groups based on metadata
 */
contract CloneForceCategorizer is Ownable {
    // Enum representing different categories
    enum Category {
        HUMAN,
        ROBOT,
        DEMON,
        UNCATEGORIZED
    }

    // Struct to hold NFT metadata information
    struct NFTMetadata {
        string traitType;
        string value;
    }

    // Mapping from NFT contract address to token ID to category
    mapping(address => mapping(uint256 => Category)) public nftCategories;

    // Mapping from NFT contract address to metadata trait type used for categorization
    mapping(address => string) public categorizationTrait;

    // Events
    event CategoryAssigned(address indexed nftContract, uint256 indexed tokenId, Category category);
    event CategorizationTraitSet(address indexed nftContract, string traitType);

    /**
     * @dev Set the trait type to use for categorization for a specific NFT contract
     * @param nftContract Address of the NFT contract
     * @param traitType The trait type to use for categorization
     */
    function setCategorizationTrait(address nftContract, string memory traitType) external onlyOwner {
        categorizationTrait[nftContract] = traitType;
        emit CategorizationTraitSet(nftContract, traitType);
    }

    /**
     * @dev Categorize an NFT based on its metadata
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT token
     * @param metadata Array of metadata traits for the NFT
     */
    function categorizeNFT(
        address nftContract,
        uint256 tokenId,
        NFTMetadata[] memory metadata
    ) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        require(metadata.length > 0, "No metadata provided");

        string memory traitType = categorizationTrait[nftContract];
        require(bytes(traitType).length > 0, "Categorization trait not set for this contract");

        Category category = Category.UNCATEGORIZED;

        for (uint256 i = 0; i < metadata.length; i++) {
            if (keccak256(bytes(metadata[i].traitType)) == keccak256(bytes(traitType))) {
                string memory value = metadata[i].value;
                
                if (keccak256(bytes(value)) == keccak256(bytes("Human"))) {
                    category = Category.HUMAN;
                } else if (keccak256(bytes(value)) == keccak256(bytes("Robot"))) {
                    category = Category.ROBOT;
                } else if (keccak256(bytes(value)) == keccak256(bytes("Demon"))) {
                    category = Category.DEMON;
                }
                break;
            }
        }

        nftCategories[nftContract][tokenId] = category;
        emit CategoryAssigned(nftContract, tokenId, category);
    }

    /**
     * @dev Get the category of a specific NFT
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT token
     * @return The category of the NFT
     */
    function getCategory(address nftContract, uint256 tokenId) external view returns (Category) {
        return nftCategories[nftContract][tokenId];
    }

    /**
     * @dev Batch categorize multiple NFTs
     * @param nftContract Address of the NFT contract
     * @param tokenIds Array of token IDs
     * @param metadataArray Array of metadata arrays for each token
     */
    function batchCategorizeNFTs(
        address nftContract,
        uint256[] memory tokenIds,
        NFTMetadata[][] memory metadataArray
    ) external {
        require(tokenIds.length == metadataArray.length, "Arrays length mismatch");

        for (uint256 i = 0; i < tokenIds.length; i++) {
            categorizeNFT(nftContract, tokenIds[i], metadataArray[i]);
        }
    }
}
```
