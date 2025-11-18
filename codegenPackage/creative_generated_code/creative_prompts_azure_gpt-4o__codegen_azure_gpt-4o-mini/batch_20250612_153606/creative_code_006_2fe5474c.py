"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Develop a Solidity contract for a decentralized NFT marketplace similar to the one in the Catgirl ecosystem, including features for buying and selling CATGIRL¢-based NFTs.
Generated: DETERMINISTIC_2fe5474c3898dfe8
Batch ID: 20250612_153606
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTMarketplace contract to facilitate the buying and selling of NFTs
contract NFTMarketplace is Ownable, ERC721Holder {
    // Struct representing an NFT listing
    struct Listing {
        address seller;
        uint256 price; // Price in CATGIRL¢
    }

    // Mapping of token ID to its listing details
    mapping(uint256 => Listing) public listings;
    // ERC20 token used for payments (CATGIRL¢)
    IERC20 public catgirlToken;

    // Event emitted when a new NFT is listed
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    // Event emitted when an NFT is sold
    event NFTSold(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);
    // Event emitted when an NFT is unlisted
    event NFTUnlisted(address indexed seller, uint256 indexed tokenId);

    // Constructor to initialize the contract with the CATGIRL¢ token address
    constructor(address _catgirlToken) {
        catgirlToken = IERC20(_catgirlToken);
    }

    // Function to list an NFT for sale
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You must own the NFT to list it");

        // Transfer NFT to the marketplace contract
        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);

        // Create listing
        listings[tokenId] = Listing(msg.sender, price);

        emit NFTListed(msg.sender, tokenId, price);
    }

    // Function to buy a listed NFT
    function buyNFT(address nftContract, uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT is not listed for sale");
        require(catgirlToken.balanceOf(msg.sender) >= listing.price, "Insufficient CATGIRL¢ balance");
        
        // Transfer the payment to the seller
        catgirlToken.transferFrom(msg.sender, listing.seller, listing.price);
        
        // Transfer the NFT to the buyer
        IERC721(nftContract).safeTransferFrom(address(this), msg.sender, tokenId);
        
        // Delete the listing
        delete listings[tokenId];

        emit NFTSold(msg.sender, listing.seller, tokenId, listing.price);
    }

    // Function to unlist an NFT
    function unlistNFT(address nftContract, uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You are not the seller of this NFT");

        // Transfer NFT back to the seller
        IERC721(nftContract).safeTransferFrom(address(this), msg.sender, tokenId);
        
        // Delete the listing
        delete listings[tokenId];

        emit NFTUnlisted(msg.sender, tokenId);
    }

    // Function to get the listing details for an NFT
    function getListing(uint256 tokenId) external view returns (address, uint256) {
        Listing memory listing = listings[tokenId];
        return (listing.seller, listing.price);
    }
}
```
