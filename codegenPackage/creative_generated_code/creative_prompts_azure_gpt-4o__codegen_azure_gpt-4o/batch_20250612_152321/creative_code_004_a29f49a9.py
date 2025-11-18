"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webnodepad.pages.dev
Prompt: Write a smart contract to manage the claiming process of unique digital artwork assets, inspired by the Dapp NodePad platform's functionality.
Generated: DETERMINISTIC_a29f49a989a16a5f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/// @title Digital Artwork Claiming Contract
/// @dev A smart contract to manage the claiming process for unique digital assets
contract ArtworkClaim {
    // Struct to store artwork details
    struct Artwork {
        uint256 id;
        string metadataURI; // URI for artwork metadata
        address creator; // Address of the artwork creator
        address claimedBy; // Address that claimed the artwork
        bool isClaimed; // Claim status
    }

    // Mapping to store artwork information by ID
    mapping(uint256 => Artwork) public artworks;

    // Count of total artworks created
    uint256 public totalArtworks;

    // Event emitted when a new artwork is created
    event ArtworkCreated(uint256 indexed artworkId, address indexed creator, string metadataURI);

    // Event emitted when an artwork is claimed
    event ArtworkClaimed(uint256 indexed artworkId, address indexed claimer);

    /// @notice Create a new artwork and register it in the contract
    /// @param _metadataURI URI pointing to the metadata of the artwork
    function createArtwork(string memory _metadataURI) external {
        require(bytes(_metadataURI).length > 0, "Metadata URI cannot be empty");

        uint256 newArtworkId = totalArtworks + 1;

        artworks[newArtworkId] = Artwork({
            id: newArtworkId,
            metadataURI: _metadataURI,
            creator: msg.sender,
            claimedBy: address(0),
            isClaimed: false
        });

        totalArtworks = newArtworkId;

        emit ArtworkCreated(newArtworkId, msg.sender, _metadataURI);
    }

    /// @notice Claim an artwork by providing its ID
    /// @param _artworkId ID of the artwork to claim
    function claimArtwork(uint256 _artworkId) external {
        require(_artworkId > 0 && _artworkId <= totalArtworks, "Invalid artwork ID");
        Artwork storage artwork = artworks[_artworkId];
        require(!artwork.isClaimed, "Artwork already claimed");

        artwork.claimedBy = msg.sender;
        artwork.isClaimed = true;

        emit ArtworkClaimed(_artworkId, msg.sender);
    }

    /// @notice Fetch details of an artwork by its ID
    /// @param _artworkId ID of the artwork to retrieve information
    /// @return Artwork details {id, metadataURI, creator, claimedBy, isClaimed}
    function getArtwork(uint256 _artworkId) external view returns (Artwork memory) {
        require(_artworkId > 0 && _artworkId <= totalArtworks, "Invalid artwork ID");
        return artworks[_artworkId];
    }
}
```
