"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmostrader.pages.dev
Prompt: Provide an example of a smart contract for managing NFT trades securely, inspired by the Cosmos Home Trade platform's emphasis on blockchain security and encryption.
Generated: DETERMINISTIC_dd284ef0f363e733
Batch ID: 20250612_151003
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SecureNFTTrade
 * @dev This contract manages the trading of NFTs securely.
 */
contract SecureNFTTrade is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Structure to hold NFT offer details
    struct Offer {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to offer details
    mapping(uint256 => Offer) private _offers;

    // Event emitted when a new offer is created
    event OfferCreated(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an offer is accepted
    event OfferAccepted(uint256 indexed tokenId, address indexed buyer);

    // Event emitted when an offer is canceled
    event OfferCanceled(uint256 indexed tokenId);

    constructor() ERC721("SecureNFT", "SNFT") {}

    /**
     * @dev Mint a new NFT.
     * @param to The address of the recipient.
     */
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Create a trade offer for an NFT.
     * @param tokenId The ID of the NFT being offered.
     * @param price The sale price for the NFT.
     */
    function createOffer(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "NFT does not exist.");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can create an offer.");
        require(price > 0, "Price must be greater than zero.");

        _offers[tokenId] = Offer({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit OfferCreated(tokenId, msg.sender, price);
    }

    /**
     * @dev Accept an existing trade offer.
     * @param tokenId The ID of the NFT being purchased.
     */
    function acceptOffer(uint256 tokenId) external payable {
        Offer memory offer = _offers[tokenId];
        require(offer.isActive, "Offer is not active.");
        require(msg.value == offer.price, "Incorrect price sent.");

        // Transfer the NFT from the seller to the buyer
        _transfer(offer.seller, msg.sender, tokenId);

        // Mark the offer as inactive
        _offers[tokenId].isActive = false;

        // Transfer the funds to the seller
        payable(offer.seller).transfer(msg.value);

        emit OfferAccepted(tokenId, msg.sender);
    }

    /**
     * @dev Cancel an existing trade offer.
     * @param tokenId The ID of the NFT whose offer is being canceled.
     */
    function cancelOffer(uint256 tokenId) external {
        Offer memory offer = _offers[tokenId];
        require(offer.isActive, "Offer is not active.");
        require(offer.seller == msg.sender, "Only the seller can cancel the offer.");

        // Mark the offer as inactive
        _offers[tokenId].isActive = false;

        emit OfferCanceled(tokenId);
    }

    /**
     * @dev Retrieve offer details for a specific token ID.
     * @param tokenId The ID of the NFT.
     * @return The offer details.
     */
    function getOffer(uint256 tokenId) external view returns (Offer memory) {
        return _offers[tokenId];
    }
}
```
