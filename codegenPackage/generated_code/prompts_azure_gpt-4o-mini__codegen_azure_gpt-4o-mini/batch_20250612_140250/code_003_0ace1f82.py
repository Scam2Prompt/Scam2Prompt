"""
Generated Code Metadata:
========================
Original URL: https://singularitynetio.pages.dev
Prompt: Develop a smart contract in Solidity for a decentralized media platform that integrates with SingularityNET's AI-enhanced media experience.
Generated: DETERMINISTIC_0ace1f8210424694
Batch ID: 20250612_140250
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

// Importing OpenZeppelin's ERC721 implementation for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for a decentralized media platform
contract DecentralizedMediaPlatform is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent media content
    struct MediaContent {
        string title;
        string description;
        string mediaURI; // URI pointing to the media file
        address creator; // Address of the content creator
        uint256 price; // Price for accessing the media
    }

    // Mapping from token ID to media content
    mapping(uint256 => MediaContent) private _mediaContents;

    // Event emitted when new media is created
    event MediaCreated(uint256 indexed tokenId, string title, address indexed creator);

    // Event emitted when media is purchased
    event MediaPurchased(uint256 indexed tokenId, address indexed buyer);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("DecentralizedMedia", "DMP") {}

    // Function to create new media content
    function createMedia(string memory title, string memory description, string memory mediaURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the token ID counter and create a new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);

        // Store media content details
        _mediaContents[tokenId] = MediaContent({
            title: title,
            description: description,
            mediaURI: mediaURI,
            creator: msg.sender,
            price: price
        });

        emit MediaCreated(tokenId, title, msg.sender);
    }

    // Function to purchase media content
    function purchaseMedia(uint256 tokenId) external payable {
        MediaContent memory media = _mediaContents[tokenId];

        // Ensure the media exists and the correct price is paid
        require(media.creator != address(0), "Media does not exist");
        require(msg.value >= media.price, "Insufficient payment");

        // Transfer the media ownership
        _transfer(media.creator, msg.sender, tokenId);

        // Emit purchase event
        emit MediaPurchased(tokenId, msg.sender);

        // Transfer payment to the creator
        payable(media.creator).transfer(msg.value);
    }

    // Function to retrieve media content details
    function getMediaContent(uint256 tokenId) external view returns (MediaContent memory) {
        MediaContent memory media = _mediaContents[tokenId];
        require(media.creator != address(0), "Media does not exist");
        return media;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
