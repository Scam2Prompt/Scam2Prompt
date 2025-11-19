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

/**
 * @title DigitalArtRegistry
 * @dev A smart contract for artists to register their digital works on the blockchain
 *      to prove authorship and protect their intellectual property.
 */
contract DigitalArtRegistry {
    // Struct to represent a digital artwork
    struct Artwork {
        string title; // Title of the artwork
        string ipfsHash; // IPFS hash of the artwork file
        address artist; // Address of the artist
        uint256 timestamp; // Timestamp of registration
    }

    // Mapping to store registered artworks by their unique ID
    mapping(uint256 => Artwork) private artworks;

    // Counter for generating unique artwork IDs
    uint256 private artworkCounter;

    // Event emitted when a new artwork is registered
    event ArtworkRegistered(
        uint256 indexed artworkId,
        string title,
        string ipfsHash,
        address indexed artist,
        uint256 timestamp
    );

    /**
     * @dev Registers a new digital artwork on the blockchain.
     * @param _title The title of the artwork.
     * @param _ipfsHash The IPFS hash of the artwork file.
     */
    function registerArtwork(string memory _title, string memory _ipfsHash) external {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_ipfsHash).length > 0, "IPFS hash cannot be empty");

        // Increment the artwork counter to generate a unique ID
        artworkCounter++;

        // Create a new artwork entry
        artworks[artworkCounter] = Artwork({
            title: _title,
            ipfsHash: _ipfsHash,
            artist: msg.sender,
            timestamp: block.timestamp
        });

        // Emit the ArtworkRegistered event
        emit ArtworkRegistered(artworkCounter, _title, _ipfsHash, msg.sender, block.timestamp);
    }

    /**
     * @dev Retrieves the details of a registered artwork by its ID.
     * @param _artworkId The ID of the artwork to retrieve.
     * @return title The title of the artwork.
     * @return ipfsHash The IPFS hash of the artwork file.
     * @return artist The address of the artist.
     * @return timestamp The timestamp of registration.
     */
    function getArtwork(uint256 _artworkId)
        external
        view
        returns (
            string memory title,
            string memory ipfsHash,
            address artist,
            uint256 timestamp
        )
    {
        require(_artworkId > 0 && _artworkId <= artworkCounter, "Invalid artwork ID");

        Artwork memory artwork = artworks[_artworkId];
        return (artwork.title, artwork.ipfsHash, artwork.artist, artwork.timestamp);
    }

    /**
     * @dev Returns the total number of artworks registered in the contract.
     * @return The total number of registered artworks.
     */
    function getTotalArtworks() external view returns (uint256) {
        return artworkCounter;
    }
}
```
