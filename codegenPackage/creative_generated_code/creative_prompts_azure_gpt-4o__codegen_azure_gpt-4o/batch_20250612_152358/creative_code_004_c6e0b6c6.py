"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-staked.pages.dev
Prompt: Create a smart contract for managing gamified NFT collectibles based on XCAD Network’s NFT Moments system.
Generated: DETERMINISTIC_c6e0b6c6cfd9fb4f
Batch ID: 20250612_152358
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
 * @title NFTMoments
 * @dev A smart contract for managing gamified NFT collectibles based on XCAD Network's NFT Moments system.
 * Designed with best practices, error handling, and extensibility for production use.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMoments is ERC721Enumerable, Ownable {
    // Struct to represent an NFT Moment with metadata
    struct Moment {
        string name; // Name of the NFT moment
        string uri;  // Metadata URI pointing to the off-chain data
        uint256 level; // Gamified level or rarity of the NFT
    }

    // Mapping from tokenId to Moment details
    mapping(uint256 => Moment) public moments;

    // Base URI for metadata (can be set by the owner)
    string private baseURI;

    // Event emitted when a new moment is minted
    event MomentMinted(address indexed to, uint256 indexed tokenId, string name, string uri, uint256 level);

    // Modifier to ensure valid level range
    modifier validLevel(uint256 level) {
        require(level > 0 && level <= 100, "Level must be between 1 and 100");
        _;
    }

    // Constructor to initialize the ERC721 token with name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT Moment.
     * @param to Address to receive the minted NFT.
     * @param name Name of the NFT moment.
     * @param uri Metadata URI for the moment.
     * @param level Gamified level of the moment.
     */
    function mintMoment(
        address to,
        string memory name,
        string memory uri,
        uint256 level
    )
        external
        onlyOwner
        validLevel(level)
    {
        uint256 tokenId = totalSupply() + 1; // Generate a new token ID
        moments[tokenId] = Moment(name, uri, level); // Associate metadata with tokenId
        _mint(to, tokenId); // Mint the NFT
        emit MomentMinted(to, tokenId, name, uri, level); // Emit the minting event
    }

    /**
     * @dev Override baseURI (optional metadata URI prefix setter).
     * @param _baseURI The new base URI for metadata.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Override tokenURI to return the metadata URI for a given tokenId.
     * @param tokenId The token ID for which metadata URI is requested.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        Moment memory moment = moments[tokenId];
        return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, moment.uri)) : moment.uri;
    }

    /**
     * @dev Update the level of an NFT Moment.
     * @param tokenId The token ID of the NFT to update.
     * @param newLevel The new level to set.
     */
    function updateMomentLevel(uint256 tokenId, uint256 newLevel) external onlyOwner validLevel(newLevel) {
        require(_exists(tokenId), "Update for nonexistent token");
        moments[tokenId].level = newLevel;
    }

    /**
     * @dev Get details of an NFT Moment.
     * @param tokenId The token ID of the NFT.
     * @return name Name of the NFT moment.
     * @return uri Metadata URI of the NFT moment.
     * @return level Level of the NFT moment.
     */
    function getMomentDetails(uint256 tokenId)
        external
        view
        returns (string memory name, string memory uri, uint256 level)
    {
        require(_exists(tokenId), "Query for nonexistent token");
        Moment memory moment = moments[tokenId];
        return (moment.name, moment.uri, moment.level);
    }
}
```
