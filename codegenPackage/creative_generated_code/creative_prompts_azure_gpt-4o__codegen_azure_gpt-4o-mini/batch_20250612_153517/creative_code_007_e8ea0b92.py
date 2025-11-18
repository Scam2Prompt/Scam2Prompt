"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openweb-3ua.pages.dev
Prompt: Create a smart contract that integrates with the Opepen protocol to facilitate decentralized voting on submitted artworks for the Permanent Collection.
Generated: DETERMINISTIC_e8ea0b921e5b6aca
Batch ID: 20250612_153517
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

/// @title Permanent Collection Voting Smart Contract
/// @dev This contract facilitates decentralized voting on submitted artworks for the Permanent Collection.
contract PermanentCollectionVoting is Ownable {
    // Structure to represent an Artwork
    struct Artwork {
        address artist;
        string metadataURI; // URI for the artwork metadata
        uint256 voteCount; // Number of votes the artwork has received
        bool exists; // Check if the artwork exists
    }

    // Mapping to store artworks by their unique ID
    mapping(uint256 => Artwork) public artworks;
    uint256 public artworkCount; // Counter for total artworks submitted

    // Mapping to track votes by address to prevent double voting
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    // Event emitted when a new artwork is submitted
    event ArtworkSubmitted(uint256 indexed artworkId, address indexed artist, string metadataURI);

    // Event emitted when a vote is cast
    event VoteCasted(uint256 indexed artworkId, address indexed voter);

    /// @dev Submit a new artwork for voting
    /// @param _metadataURI The URI of the artwork metadata
    function submitArtwork(string calldata _metadataURI) external {
        artworkCount++;
        artworks[artworkCount] = Artwork({
            artist: msg.sender,
            metadataURI: _metadataURI,
            voteCount: 0,
            exists: true
        });

        emit ArtworkSubmitted(artworkCount, msg.sender, _metadataURI);
    }

    /// @dev Vote for an artwork
    /// @param _artworkId The ID of the artwork to vote for
    function vote(uint256 _artworkId) external {
        require(artworks[_artworkId].exists, "Artwork does not exist");
        require(!hasVoted[msg.sender][_artworkId], "You have already voted for this artwork");

        // Cast the vote
        artworks[_artworkId].voteCount++;
        hasVoted[msg.sender][_artworkId] = true;

        emit VoteCasted(_artworkId, msg.sender);
    }

    /// @dev Get the details of an artwork
    /// @param _artworkId The ID of the artwork to retrieve
    /// @return artist The address of the artist
    /// @return metadataURI The URI of the artwork metadata
    /// @return voteCount The total votes received for the artwork
    function getArtwork(uint256 _artworkId) external view returns (address artist, string memory metadataURI, uint256 voteCount) {
        require(artworks[_artworkId].exists, "Artwork does not exist");

        Artwork memory artwork = artworks[_artworkId];
        return (artwork.artist, artwork.metadataURI, artwork.voteCount);
    }

    /// @dev Get total number of artworks submitted
    /// @return Total count of submitted artworks
    function totalArtworks() external view returns (uint256) {
        return artworkCount;
    }
}
```
