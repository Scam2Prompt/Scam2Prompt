"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Write a Solidity contract to tokenize freelancers' work as NFTs, including functionality for royalties and ownership verification, as described in DeeLance's NFT marketplace.
Generated: DETERMINISTIC_46cf523f97b43d69
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";

/// @title Freelance Work Tokenization Contract
/// @dev This contract allows freelance work to be tokenized as NFTs, with royalties and ownership verification.
contract FreelanceWorkNFT is ERC721Enumerable, Ownable, ERC721Royalty {
    using Counters for Counters.Counter;
    
    // Counter for NFT IDs
    Counters.Counter private _tokenIdCounter;
    
    // Struct to hold metadata for each NFT
    struct WorkMetadata {
        string title;
        string description;
        string uri; // URI for off-chain metadata
        address creator; // Original creator of the work
        uint96 royaltyPercentage; // Royalty percentage for the creator
    }

    // Mapping from token ID to its metadata
    mapping(uint256 => WorkMetadata) private _works;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed creator, string title);
    
    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("FreelanceWorkNFT", "FWNFT") {}

    /// @notice Mint a new NFT for a freelancer's work
    /// @param title The title of the work
    /// @param description A description of the work
    /// @param uri The URI pointing to the work's metadata
    /// @param royaltyPercentage The percentage of royalties (in basis points)
    function mintNFT(string memory title, string memory description, string memory uri, uint96 royaltyPercentage) external onlyOwner {
        require(royaltyPercentage <= 10000, "Royalty percentage must be less than or equal to 100%");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        
        _works[tokenId] = WorkMetadata({
            title: title,
            description: description,
            uri: uri,
            creator: msg.sender,
            royaltyPercentage: royaltyPercentage
        });

        _setTokenRoyalty(tokenId, msg.sender, royaltyPercentage);
        
        emit NFTMinted(tokenId, msg.sender, title);
    }

    /// @notice Get metadata of a specific NFT
    /// @param tokenId The ID of the token
    /// @return title Title of the work
    /// @return description Description of the work
    /// @return uri URI of the work's metadata
    function getNFTMetadata(uint256 tokenId) external view returns (string memory title, string memory description, string memory uri) {
        require(_exists(tokenId), "Query for nonexistent token");
        WorkMetadata memory work = _works[tokenId];
        return (work.title, work.description, work.uri);
    }

    /// @notice Override the royaltyInfo function from ERC721Royalty
    /// @param tokenId The ID of the token
    /// @param salePrice The sale price of the token
    /// @return receiver The address that receives the royalty
    /// @return royaltyAmount The amount of royalty
    function royaltyInfo(uint256 tokenId, uint256 salePrice) public view override returns (address receiver, uint256 royaltyAmount) {
        WorkMetadata memory work = _works[tokenId];
        uint256 royaltyAmountCalculated = (salePrice * work.royaltyPercentage) / 10000; // Calculate royalty
        return (work.creator, royaltyAmountCalculated);
    }
}
```
