"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meowworldsnft.pages.dev
Prompt: Create a code snippet for a smart contract that allows users to buy and sell Meow World NFTs on OpenSea.
Generated: DETERMINISTIC_e760e151b739f5bd
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/// @title Meow World NFT Marketplace
/// @notice A smart contract for buying and selling Meow World NFTs on OpenSea.
/// @dev Integrates with ERC721 standard for NFTs.

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MeowWorldMarketplace is Ownable, ReentrancyGuard {
    /// @notice Structure to define a listing.
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
    }

    /// @dev Address of the Meow World NFT contract.
    IERC721 public immutable meowWorldNFT;

    /// @dev Mapping of tokenId to active listings.
    mapping(uint256 => Listing) public listings;

    /// @dev Event emitted when a new listing is created.
    event Listed(uint256 indexed tokenId, address indexed seller, uint256 price);

    /// @dev Event emitted when a listing is cancelled.
    event Cancelled(uint256 indexed tokenId, address indexed seller);

    /// @dev Event emitted when a token is bought.
    event Purchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    /// @param nftContract The address of the Meow World NFT contract.
    constructor(address nftContract) {
        require(nftContract != address(0), "Invalid NFT contract address");
        meowWorldNFT = IERC721(nftContract);
    }

    /// @notice List an NFT for sale.
    /// @param tokenId The tokenId of the NFT to list.
    /// @param price The price to sell the NFT for.
    function listNFT(uint256 tokenId, uint256 price) external nonReentrant {
        require(price > 0, "Price must be greater than zero");
        require(
            meowWorldNFT.ownerOf(tokenId) == msg.sender,
            "You must own the NFT to list it"
        );

        // Approve the marketplace to transfer this token if not already approved.
        require(
            meowWorldNFT.getApproved(tokenId) == address(this),
            "Marketplace must be approved to transfer this NFT"
        );

        // Create the listing.
        listings[tokenId] = Listing(tokenId, msg.sender, price);

        emit Listed(tokenId, msg.sender, price);
    }

    /// @notice Cancel an active listing for an NFT.
    /// @param tokenId The tokenId of the NFT whose listing is to be cancelled.
    function cancelListing(uint256 tokenId) external nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You can only cancel your own listing");
        require(listing.tokenId == tokenId, "Listing does not exist");

        // Remove the listing.
        delete listings[tokenId];

        emit Cancelled(tokenId, msg.sender);
    }

    /// @notice Buy an NFT from an active listing.
    /// @param tokenId The tokenId of the NFT to buy.
    function buyNFT(uint256 tokenId) external payable nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds to buy NFT");

        // Transfer the NFT to the buyer.
        meowWorldNFT.safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Transfer the payment to the seller.
        (bool success, ) = listing.seller.call{value: listing.price}("");
        require(success, "Payment transfer failed");

        // Remove the listing.
        delete listings[tokenId];

        emit Purchased(tokenId, msg.sender, listing.price);
    }

    /// @notice Withdraw funds from the contract (owner-only function).
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Fallback function to accept ETH.
    receive() external payable {}

    /// @notice Prevent sending ETH directly to the contract.
    fallback() external payable {
        revert("Unsupported function call");
    }
}
```
