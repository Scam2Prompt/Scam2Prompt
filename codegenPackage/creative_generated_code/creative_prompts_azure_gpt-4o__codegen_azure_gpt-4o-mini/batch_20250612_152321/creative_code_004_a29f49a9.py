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
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing unique digital artwork claims
contract DigitalArtClaim is ERC721Enumerable, Ownable {
    // Struct to represent an artwork
    struct Artwork {
        string name;
        string uri; // URI to the artwork metadata
        address creator;
        bool claimed;
    }

    // Mapping from token ID to Artwork struct
    mapping(uint256 => Artwork) public artworks;

    // Event emitted when an artwork is created
    event ArtworkCreated(uint256 indexed tokenId, string name, string uri, address indexed creator);

    // Event emitted when an artwork is claimed
    event ArtworkClaimed(uint256 indexed tokenId, address indexed claimant);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor() ERC721("DigitalArtClaim", "DAC") {}

    // Function to create a new artwork
    function createArtwork(string memory _name, string memory _uri) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Generate a new token ID
        artworks[tokenId] = Artwork(_name, _uri, msg.sender, false); // Store artwork data
        _mint(msg.sender, tokenId); // Mint the NFT to the creator

        emit ArtworkCreated(tokenId, _name, _uri, msg.sender); // Emit event
    }

    // Function to claim an artwork
    function claimArtwork(uint256 _tokenId) external {
        // Check if the token exists and has not been claimed
        require(_exists(_tokenId), "Artwork does not exist");
        require(!artworks[_tokenId].claimed, "Artwork already claimed");
        
        artworks[_tokenId].claimed = true; // Mark artwork as claimed
        transferFrom(ownerOf(_tokenId), msg.sender, _tokenId); // Transfer the artwork to the claimant

        emit ArtworkClaimed(_tokenId, msg.sender); // Emit event
    }

    // Function to view artwork details
    function getArtwork(uint256 _tokenId) external view returns (string memory name, string memory uri, address creator, bool claimed) {
        require(_exists(_tokenId), "Artwork does not exist");
        
        Artwork memory artwork = artworks[_tokenId]; // Retrieve artwork data
        return (artwork.name, artwork.uri, artwork.creator, artwork.claimed);
    }
}
```
