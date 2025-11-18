"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate a Solidity contract for a decentralized marketplace where users can trade tokenized assets, as described in Ethereum.org's NFT use cases.
Generated: DETERMINISTIC_431891bd4637341d
Batch ID: 20250612_151948
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
 * @title Decentralized Marketplace for Tokenized Assets
 * @dev This contract implements a marketplace where users can list, buy, and sell NFTs (ERC721 tokens).
 */
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedMarketplace is Ownable, ReentrancyGuard {
    // Structure to store information about listed items
    struct Listing {
        address seller;
        address tokenAddress;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping of item IDs to listings
    mapping(uint256 => Listing) public listings;
    // Counter for unique listing IDs
    uint256 public listingCounter;

    // Event for when a new listing is created
    event ItemListed(
        uint256 listingId,
        address indexed seller,
        address indexed tokenAddress,
        uint256 indexed tokenId,
        uint256 price
    );

    // Event for when an item is purchased
    event ItemPurchased(
        uint256 listingId,
        address indexed buyer,
        address indexed seller,
        uint256 price
    );

    // Event for when a listing is cancelled
    event ListingCancelled(uint256 listingId, address indexed seller);

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param tokenAddress Address of the ERC721 contract.
     * @param tokenId ID of the token to list.
     * @param price Price at which the token is listed (in wei).
     */
    function listItem(
        address tokenAddress,
        uint256 tokenId,
        uint256 price
    ) external nonReentrant {
        require(price > 0, "Price must be greater than zero");
        IERC721 tokenContract = IERC721(tokenAddress);
        require(
            tokenContract.ownerOf(tokenId) == msg.sender,
            "Caller must own the token"
        );
        require(
            tokenContract.getApproved(tokenId) == address(this) ||
                tokenContract.isApprovedForAll(msg.sender, address(this)),
            "Marketplace must be approved to transfer the token"
        );

        listingCounter++;
        listings[listingCounter] = Listing({
            seller: msg.sender,
            tokenAddress: tokenAddress,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit ItemListed(listingCounter, msg.sender, tokenAddress, tokenId, price);
    }

    /**
     * @dev Purchase an NFT from the marketplace.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseItem(uint256 listingId) external payable nonReentrant {
        Listing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(
            msg.value == listing.price,
            "Incorrect payment amount"
        );

        // Transfer funds to the seller
        (bool sent, ) = listing.seller.call{value: msg.value}("");
        require(sent, "Failed to send funds to seller");

        // Transfer the token to the buyer
        IERC721 tokenContract = IERC721(listing.tokenAddress);
        tokenContract.safeTransferFrom(
            listing.seller,
            msg.sender,
            listing.tokenId
        );

        // Mark the listing as inactive
        listing.isActive = false;

        emit ItemPurchased(
            listingId,
            msg.sender,
            listing.seller,
            listing.price
        );
    }

    /**
     * @dev Cancel a listing that is currently active.
     * @param listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external nonReentrant {
        Listing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(
            listing.seller == msg.sender,
            "Caller is not the seller"
        );

        // Mark the listing as inactive
        listing.isActive = false;

        emit ListingCancelled(listingId, msg.sender);
    }

    /**
     * @dev Withdraw the balance in case the contract receives ETH accidentally.
     * Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool sent, ) = owner().call{value: balance}("");
        require(sent, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    fallback() external payable {
        revert("Fallback function called incorrectly");
    }
}
```
