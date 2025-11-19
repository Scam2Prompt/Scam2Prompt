"""
Generated Code Metadata:
========================
Original URL: https://skillchain.io
Prompt: Generate a smart contract code for a Skillchain-like platform that allows artists to protect their digital works and prove authorship using blockchain technology.
Generated: DETERMINISTIC_dcd575a79a773b51
Batch ID: 20250622_210706
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DigitalArtRegistry
 * @dev A smart contract for registering and managing digital artworks on the blockchain.
 * This contract allows artists to mint NFTs representing their digital works, proving authorship and ownership.
 */
contract DigitalArtRegistry is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold artwork details
    struct Artwork {
        string title;
        string artist;
        string uri; // URI pointing to the digital artwork
        uint256 timestamp; // Timestamp of creation
    }

    // Mapping from token ID to artwork details
    mapping(uint256 => Artwork) private _artworks;

    // Event emitted when a new artwork is registered
    event ArtworkRegistered(uint256 indexed tokenId, string title, string artist, string uri);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT.
     */
    constructor() ERC721("DigitalArt", "DART") {}

    /**
     * @dev Function to register a new artwork.
     * @param title The title of the artwork.
     * @param artist The name of the artist.
     * @param uri The URI pointing to the digital artwork.
     */
    function registerArtwork(string memory title, string memory artist, string memory uri) external onlyOwner {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(artist).length > 0, "Artist cannot be empty");
        require(bytes(uri).length > 0, "URI cannot be empty");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the owner
        _mint(msg.sender, tokenId);

        // Store artwork details
        _artworks[tokenId] = Artwork({
            title: title,
            artist: artist,
            uri: uri,
            timestamp: block.timestamp
        });

        // Emit the artwork registration event
        emit ArtworkRegistered(tokenId, title, artist, uri);
    }

    /**
     * @dev Function to retrieve artwork details by token ID.
     * @param tokenId The ID of the token to retrieve.
     * @return title The title of the artwork.
     * @return artist The name of the artist.
     * @return uri The URI pointing to the digital artwork.
     * @return timestamp The timestamp of creation.
     */
    function getArtwork(uint256 tokenId) external view returns (string memory title, string memory artist, string memory uri, uint256 timestamp) {
        require(_exists(tokenId), "Artwork does not exist");

        Artwork memory artwork = _artworks[tokenId];
        return (artwork.title, artwork.artist, artwork.uri, artwork.timestamp);
    }

    /**
     * @dev Function to check if an artwork exists.
     * @param tokenId The ID of the token to check.
     * @return bool indicating whether the artwork exists.
     */
    function artworkExists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}
```
