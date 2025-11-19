"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpunksxyz.pages.dev
Prompt: Develop a smart contract in Solidity for trading TPUNKS NFTs on the Tron blockchain, ensuring it handles transactions securely.
Generated: DETERMINISTIC_22ddc9448dbb5704
Batch ID: 20250612_161035
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TPUNKS Trading Smart Contract
 * @dev This contract facilitates secure trading of TPUNKS NFTs on the Tron blockchain.
 */
contract TPUNKSMarketplace {
    using SafeMath for uint256;

    // Struct to hold NFT listing information
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from tokenId to Listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when an NFT is listed
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // ERC721 token contract interface
    IERC721 public tpunkToken;

    /**
     * @dev Sets the TPUNKS token contract address
     * @param _tpunkTokenAddress address of the TPUNKS ERC721 token contract
     */
    constructor(address _tpunkTokenAddress) {
        tpunkToken = IERC721(_tpunkTokenAddress);
    }

    /**
     * @dev Lists an NFT for sale
     * @param tokenId The ID of the NFT to be listed
     * @param price The sale price of the NFT
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(tpunkToken.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Create a new listing
        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        // Emit the listing event
        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Cancels a listed NFT
     * @param tokenId The ID of the NFT to cancel
     */
    function cancelListing(uint256 tokenId) external {
        Listing storage listing = listings[tokenId];
        
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");
        require(listing.isActive, "Listing is not active");

        // Mark the listing as inactive
        listing.isActive = false;
    }

    /**
     * @dev Buys a listed NFT
     * @param tokenId The ID of the NFT to buy
     */
    function buyNFT(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];
        
        require(listing.isActive, "NFT is not for sale");
        require(msg.value == listing.price, "Incorrect price sent");

        // Transfer ownership of the NFT
        tpunkToken.safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Transfer funds to the seller
        payable(listing.seller).transfer(msg.value);

        // Mark the listing as inactive
        listing.isActive = false;

        // Emit the sale event
        emit NFTSold(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Retrieves the listing details for a specific NFT
     * @param tokenId The ID of the NFT to retrieve listing information for
     * @return Listing details including seller and price
     */
    function getListing(uint256 tokenId) external view returns (Listing memory) {
        return listings[tokenId];
    }
}
```
