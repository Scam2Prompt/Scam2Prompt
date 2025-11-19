"""
Generated Code Metadata:
========================
Original URL: https://shiba-swap.tilda.ws
Prompt: Propose a new feature for ShibaSwap's NFT marketplace, enabling users to create and trade unique digital assets, and provide a high-level implementation plan.
Generated: DETERMINISTIC_b5aa994093955ac3
Batch ID: 20250622_212248
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
 * @title ShibaSwap NFT Marketplace
 * @dev This contract enables users to create and trade unique digital assets (NFTs).
 *      It follows the ERC721 standard for NFTs and includes marketplace functionality.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ShibaSwapNFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Struct to represent an NFT listing
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to listing details
    mapping(uint256 => Listing) public listings;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address owner);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 tokenId, address seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 tokenId, address buyer, uint256 price);

    /**
     * @dev Constructor to initialize the NFT contract.
     */
    constructor() ERC721("ShibaSwapNFT", "SHIBNFT") {}

    /**
     * @dev Function to mint a new NFT.
     * @param tokenURI The metadata URI for the NFT.
     */
    function mintNFT(string memory tokenURI) external {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT to the caller
        _mint(msg.sender, newTokenId);

        // Set the token URI (metadata)
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(newTokenId, msg.sender);
    }

    /**
     * @dev Function to list an NFT for sale.
     * @param tokenId The ID of the token to list.
     * @param price The sale price of the NFT.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(price > 0, "Price must be greater than zero");

        // Approve the marketplace to transfer the NFT
        approve(address(this), tokenId);

        // Create the listing
        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Function to purchase an NFT.
     * @param tokenId The ID of the token to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "This NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        // Transfer payment to the seller
        payable(listing.seller).transfer(listing.price);

        // Transfer the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Function to cancel an NFT listing.
     * @param tokenId The ID of the token to cancel the listing for.
     */
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You are not the seller of this NFT");
        require(listing.isActive, "This listing is already inactive");

        // Mark the listing as inactive
        listings[tokenId].isActive = false;
    }
}
```
