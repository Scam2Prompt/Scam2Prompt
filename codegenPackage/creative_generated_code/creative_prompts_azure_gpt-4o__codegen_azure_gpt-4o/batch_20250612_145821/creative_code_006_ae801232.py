"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.now.sh
Prompt: Create a smart contract example for selling NFTs on PolyMarket 1.0 using the Polygon blockchain.
Generated: DETERMINISTIC_ae80123295642da0
Batch ID: 20250612_145821
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
 * @title NFTMarketplace
 * @dev A simple smart contract for selling NFTs on the Polygon blockchain.
 *      This contract uses ERC721 standard for NFTs.
 */
 
// Importing required interfaces and contracts from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is Ownable {
    // Struct to represent a listing for an NFT
    struct NFTListing {
        address seller;         // Address of the seller
        uint256 price;          // Price of the NFT (in wei)
        address nftContract;    // Address of the ERC721 contract
        uint256 tokenId;        // Token ID of the NFT
    }

    // Mapping to store active NFT listings
    mapping(uint256 => NFTListing) public listings;
    uint256 public listingCounter;

    // Events
    event NFTListed(
        uint256 indexed listingId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );
    event NFTPurchased(
        uint256 indexed listingId,
        address indexed buyer,
        address indexed nftContract,
        uint256 tokenId
    );

    /**
     * @dev List an NFT for sale.
     * @param nftContract Address of the ERC721 contract.
     * @param tokenId Token ID of the NFT to list.
     * @param price Price of the NFT in wei.
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(
            IERC721(nftContract).ownerOf(tokenId) == msg.sender,
            "Caller is not the owner of the NFT"
        );
        require(
            IERC721(nftContract).getApproved(tokenId) == address(this),
            "Contract is not approved to transfer the NFT"
        );

        // Increment the listing counter
        listingCounter++;

        // Create a new listing
        listings[listingCounter] = NFTListing({
            seller: msg.sender,
            price: price,
            nftContract: nftContract,
            tokenId: tokenId
        });

        emit NFTListed(listingCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Purchase an NFT.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 listingId) external payable {
        NFTListing memory listing = listings[listingId];
        require(listing.price > 0, "Listing does not exist");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer the NFT to the buyer
        IERC721(listing.nftContract).safeTransferFrom(
            listing.seller,
            msg.sender,
            listing.tokenId
        );

        // Delete the listing
        delete listings[listingId];

        emit NFTPurchased(listingId, msg.sender, listing.nftContract, listing.tokenId);
    }

    /**
     * @dev Allows the owner to withdraw funds in case there are any leftover balances.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental deposits.
     */
    fallback() external payable {
        revert("Direct deposits are not allowed");
    }

    receive() external payable {
        revert("Direct deposits are not allowed");
    }
}
```
