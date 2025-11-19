"""
Generated Code Metadata:
========================
Original URL: https://rayonnanft.com
Prompt: Design a smart contract using Solidity that enables the creation, buying, and selling of NFTs on the Rayonna NFT platform, incorporating features like royalty payments to creators.
Generated: DETERMINISTIC_1907fd4eb9479449
Batch ID: 20250622_212015
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
 * @title RayonnaNFTPlatform
 * @dev A smart contract for creating, buying, and selling NFTs with royalty payments to creators.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract RayonnaNFTPlatform is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Struct to store NFT details
    struct NFT {
        address creator;
        uint256 royaltyPercentage; // Royalty percentage (e.g., 5 for 5%)
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) private _nftDetails;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 tokenId, address creator, uint256 royaltyPercentage, string tokenURI);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 tokenId, address buyer, uint256 salePrice);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("RayonnaNFT", "RAYNFT") {}

    /**
     * @dev Function to create a new NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @param royaltyPercentage Percentage of royalties for the creator (0-100).
     */
    function createNFT(string memory tokenURI, uint256 royaltyPercentage) external {
        require(royaltyPercentage <= 100, "Royalty percentage cannot exceed 100");

        // Increment the token ID counter
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT to the creator
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Store NFT details
        _nftDetails[newTokenId] = NFT({
            creator: msg.sender,
            royaltyPercentage: royaltyPercentage
        });

        emit NFTCreated(newTokenId, msg.sender, royaltyPercentage, tokenURI);
    }

    /**
     * @dev Function to buy an NFT.
     * @param tokenId ID of the NFT to buy.
     */
    function buyNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");

        address seller = ownerOf(tokenId);
        require(seller != msg.sender, "Cannot buy your own NFT");

        // Calculate royalty payment
        NFT memory nft = _nftDetails[tokenId];
        uint256 royaltyAmount = (msg.value * nft.royaltyPercentage) / 100;

        // Transfer royalty to the creator
        payable(nft.creator).transfer(royaltyAmount);

        // Transfer remaining amount to the seller
        payable(seller).transfer(msg.value - royaltyAmount);

        // Transfer ownership of the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        emit NFTSold(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Function to get NFT details.
     * @param tokenId ID of the NFT.
     * @return creator Address of the creator.
     * @return royaltyPercentage Royalty percentage for the creator.
     */
    function getNFTDetails(uint256 tokenId) external view returns (address creator, uint256 royaltyPercentage) {
        require(_exists(tokenId), "NFT does not exist");

        NFT memory nft = _nftDetails[tokenId];
        return (nft.creator, nft.royaltyPercentage);
    }
}
```
