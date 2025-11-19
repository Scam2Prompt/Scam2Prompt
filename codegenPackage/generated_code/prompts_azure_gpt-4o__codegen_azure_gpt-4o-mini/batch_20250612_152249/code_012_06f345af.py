"""
Generated Code Metadata:
========================
Original URL: https://xcad-chain.pages.dev
Prompt: Write a Solidity contract to mint gamified NFT collectibles based on iconic YouTube moments, following XCAD Network's NFT Moments concept.
Generated: DETERMINISTIC_06f345affe63ef67
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting gamified NFT collectibles based on iconic YouTube moments
contract YouTubeMomentsNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a YouTube moment
    struct YouTubeMoment {
        string title; // Title of the moment
        string videoUrl; // URL of the YouTube video
        string description; // Description of the moment
        string imageUrl; // URL of the image representing the moment
    }

    // Mapping from token ID to YouTube moment
    mapping(uint256 => YouTubeMoment) private _moments;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, string title, address owner);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("YouTube Moments NFT", "YT-MOMENT") {}

    // Function to mint a new NFT collectible
    // Only the contract owner can mint new NFTs
    function mintNFT(
        string memory title,
        string memory videoUrl,
        string memory description,
        string memory imageUrl
    ) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Create a new YouTube moment
        YouTubeMoment memory newMoment = YouTubeMoment({
            title: title,
            videoUrl: videoUrl,
            description: description,
            imageUrl: imageUrl
        });

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store the moment details
        _moments[tokenId] = newMoment;

        // Emit the NFTMinted event
        emit NFTMinted(tokenId, title, msg.sender);
    }

    // Function to retrieve details of a specific YouTube moment by token ID
    function getMomentDetails(uint256 tokenId) external view returns (YouTubeMoment memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Return the moment details
        return _moments[tokenId];
    }

    // Function to get the total number of minted NFTs
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
