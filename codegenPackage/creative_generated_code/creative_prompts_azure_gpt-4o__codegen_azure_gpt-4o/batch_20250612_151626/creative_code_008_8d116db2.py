"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftnovamarket.com
Prompt: Generate a Solidity contract for managing NFT transactions on Nftnovamarket's platform, including buying, selling, and transferring ownership.
Generated: DETERMINISTIC_8d116db23b789470
Batch ID: 20250612_151626
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

/**
 * @title NFTNovaMarket
 * @dev A contract for managing NFT transactions on the NftnovaMarket platform.
 * Allows buying, selling, and transferring ownership of ERC721-compliant NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTNovaMarket is ReentrancyGuard {
    // Struct to represent a listing
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from NFT contract address and token ID to its listing
    mapping(address => mapping(uint256 => Listing)) public listings;

    // Event emitted when an NFT is listed for sale
    event Listed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is bought
    event Bought(address indexed nftContract, uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Event emitted when a listing is canceled
    event Canceled(address indexed nftContract, uint256 indexed tokenId, address indexed seller);

    /**
     * @dev Lists an NFT for sale on the platform.
     * @param nftContract Address of the NFT contract (ERC721-compliant).
     * @param tokenId Token ID of the NFT.
     * @param price Sale price of the NFT (in wei).
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "Sender must be the owner of the NFT");
        require(nft.isApprovedForAll(msg.sender, address(this)) || nft.getApproved(tokenId) == address(this), "Contract must be approved to transfer this NFT");

        listings[nftContract][tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit Listed(nftContract, tokenId, msg.sender, price);
    }

    /**
     * @dev Cancels a sale listing for an NFT.
     * @param nftContract Address of the NFT contract (ERC721-compliant).
     * @param tokenId Token ID of the NFT.
     */
    function cancelListing(address nftContract, uint256 tokenId) external {
        Listing storage listing = listings[nftContract][tokenId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Caller is not the seller");

        listing.isActive = false;

        emit Canceled(nftContract, tokenId, msg.sender);
    }

    /**
     * @dev Buys an NFT listed for sale.
     * @param nftContract Address of the NFT contract (ERC721-compliant).
     * @param tokenId Token ID of the NFT.
     */
    function buyNFT(address nftContract, uint256 tokenId) external payable nonReentrant {
        Listing storage listing = listings[nftContract][tokenId];
        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer the payment to the seller
        (bool success, ) = listing.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Transfer NFT ownership to buyer
        IERC721 nft = IERC721(nftContract);
        nft.safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Mark listing as inactive
        listing.isActive = false;

        emit Bought(nftContract, tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Transfers ownership of an NFT to another address (manual transfer not involving a listing).
     * @param nftContract Address of the NFT contract (ERC721-compliant).
     * @param tokenId Token ID of the NFT.
     * @param to Address to transfer the NFT to.
     */
    function transferNFT(address nftContract, uint256 tokenId, address to) external {
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "Sender must be the owner of the NFT");
        require(to != address(0), "Invalid recipient address");

        nft.safeTransferFrom(msg.sender, to, tokenId);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not support direct ETH transfers");
    }
}
```
