"""
Generated Code Metadata:
========================
Original URL: https://presales-earthmetasite.web.app
Prompt: "Generate a smart contract code snippet in Solidity for a simple NFT marketplace on a blockchain platform like Ethereum or Polygon, inspired by EarthMeta's virtual real estate trading."
Generated: DETERMINISTIC_48203178070c2c42
Batch ID: 20250622_210236
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
 * @title NFTMarketplace
 * @dev A simple NFT marketplace for buying and selling virtual real estate NFTs.
 */
contract NFTMarketplace {
    // Struct to represent a listed NFT
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from NFT contract address and token ID to Listing
    mapping(address => mapping(uint256 => Listing)) public listings;

    // Event emitted when an NFT is listed for sale
    event NFTListed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed nftContract, uint256 indexed tokenId, address indexed buyer, uint256 price);

    /**
     * @dev List an NFT for sale.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     * @param price Sale price in wei.
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the marketplace contract for escrow
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create a new listing
        listings[nftContract][tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(nftContract, tokenId, msg.sender, price);
    }

    /**
     * @dev Purchase an NFT.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     */
    function purchaseNFT(address nftContract, uint256 tokenId) external payable {
        Listing memory listing = listings[nftContract][tokenId];

        require(listing.isActive, "NFT is not listed for sale");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Mark the listing as inactive
        listings[nftContract][tokenId].isActive = false;

        // Transfer payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer the NFT to the buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTPurchased(nftContract, tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Cancel an NFT listing.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     */
    function cancelListing(address nftContract, uint256 tokenId) external {
        Listing memory listing = listings[nftContract][tokenId];

        require(listing.isActive, "NFT is not listed for sale");
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");

        // Mark the listing as inactive
        listings[nftContract][tokenId].isActive = false;

        // Transfer the NFT back to the seller
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);
    }
}

// Interface for ERC721 standard
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
