"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Create a Solidity contract for minting 9,999 unique Rebel Satoshi NFTs, ensuring each NFT has distinct metadata and represents the categories "Citizens," "Warriors," "Rebels," "Monarchs," and "Recusants."
Generated: DETERMINISTIC_8b8d51e55b018dab
Batch ID: 20250612_152620
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
 * @title RebelSatoshiNFT
 * @dev A contract for minting 9,999 unique Rebel Satoshi NFTs.
 * Each NFT has distinct metadata and belongs to a predefined category.
 * Categories: "Citizens," "Warriors," "Rebels," "Monarchs," and "Recusants."
 * Implements ERC721 standard.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract RebelSatoshiNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 9999;

    // Mapping to store metadata of each token
    mapping(uint256 => string) private _tokenMetadata;

    // Categories for NFTs
    enum Category {
        Citizens,
        Warriors,
        Rebels,
        Monarchs,
        Recusants
    }

    // Mapping to assign categories to tokens
    mapping(uint256 => Category) private _tokenCategories;

    // Event emitted when an NFT is minted
    event NFTMinted(
        address indexed to,
        uint256 indexed tokenId,
        string metadata,
        Category category
    );

    /**
     * @dev Constructor sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("RebelSatoshiNFT", "RSNFT") {}

    /**
     * @dev Function to mint a new NFT.
     * @param to The address of the recipient.
     * @param metadata The metadata URL or string representing the NFT.
     * @param category The category of the NFT.
     */
    function mintNFT(
        address to,
        string memory metadata,
        Category category
    ) external onlyOwner {
        // Ensure we do not exceed the maximum supply
        require(
            _tokenIdCounter.current() < MAX_SUPPLY,
            "Max supply reached, no more NFTs can be minted."
        );

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);

        // Store metadata and category
        _tokenMetadata[tokenId] = metadata;
        _tokenCategories[tokenId] = category;

        // Emit event
        emit NFTMinted(to, tokenId, metadata, category);
    }

    /**
     * @dev Function to retrieve metadata of a specific token.
     * @param tokenId The ID of the token to query.
     * @return Metadata associated with the token.
     */
    function tokenMetadata(uint256 tokenId)
        external
        view
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "Token does not exist, cannot retrieve metadata."
        );
        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Function to retrieve category of a specific token.
     * @param tokenId The ID of the token to query.
     * @return Category of the token.
     */
    function tokenCategory(uint256 tokenId)
        external
        view
        returns (Category)
    {
        require(
            _exists(tokenId),
            "Token does not exist, cannot retrieve category."
        );
        return _tokenCategories[tokenId];
    }

    /**
     * @dev Function to retrieve the total number of minted tokens.
     * @return The total number of minted tokens.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
