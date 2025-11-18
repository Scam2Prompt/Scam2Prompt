"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-token.pages.dev
Prompt: Write a Solidity contract to tokenize freelancer work as NFTs, including functionality for verifying ownership and enabling royalties, similar to the DeeLance NFT marketplace.
Generated: DETERMINISTIC_d114ad4cca683b44
Batch ID: 20250612_152422
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

/**
 * @title FreelancerWorkNFT
 * @dev ERC721 token for tokenizing freelancer work with royalty functionality
 */
contract FreelancerWorkNFT is ERC721Enumerable, Ownable, ERC721Royalty {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _creators;

    // Event to emit when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed creator, string tokenURI, uint96 royaltyPercentage);

    /**
     * @dev Constructor to initialize the NFT contract
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT
     * @param recipient Address to receive the NFT
     * @param tokenURI URI for the token metadata
     * @param royaltyPercentage Percentage of the sale price to be paid to the creator
     */
    function mintNFT(address recipient, string memory tokenURI, uint96 royaltyPercentage) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(royaltyPercentage <= 10000, "Royalty percentage must be less than or equal to 100%");

        // Increment token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(recipient, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _creators[tokenId] = msg.sender;

        // Set royalty for the NFT
        _setTokenRoyalty(tokenId, recipient, royaltyPercentage);

        emit NFTCreated(tokenId, recipient, tokenURI, royaltyPercentage);
    }

    /**
     * @dev Function to verify ownership of a token
     * @param tokenId ID of the token to check ownership
     * @return address of the token owner
     */
    function verifyOwnership(uint256 tokenId) external view returns (address) {
        return ownerOf(tokenId);
    }

    /**
     * @dev Function to get the creator of a specific token
     * @param tokenId ID of the token to check the creator
     * @return address of the creator
     */
    function getCreator(uint256 tokenId) external view returns (address) {
        return _creators[tokenId];
    }

    /**
     * @dev Override supportsInterface to enable ERC721 and ERC2981 (Royalties)
     * @param interfaceId The interface identifier
     * @return bool indicating whether the contract supports the interface
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Royalty) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
