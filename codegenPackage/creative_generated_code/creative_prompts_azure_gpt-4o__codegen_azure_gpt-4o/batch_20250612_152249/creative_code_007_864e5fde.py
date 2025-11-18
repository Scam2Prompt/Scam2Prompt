"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibfgwbgr6vbhqeigt3olfaq2u4wzpjjilofgrjivnxebpy3giqh6u.ipfs.dweb.link
Prompt: Design a system in Solidity for Blum that allows users to trade ordinals and NFTs directly from their Web3 wallets.
Generated: DETERMINISTIC_864e5fde69a3ab50
Batch ID: 20250612_152249
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
 * @title OrdinalNFTTrading
 * @dev A smart contract for trading ordinals and NFTs directly between Web3 wallets.
 */
contract OrdinalNFTTrading {

    // Event emitted when an asset is listed for sale
    event AssetListed(
        address indexed seller,
        address indexed assetContract,
        uint256 indexed assetId,
        uint256 price
    );

    // Event emitted when an asset is purchased
    event AssetSold(
        address indexed buyer,
        address indexed seller,
        address indexed assetContract,
        uint256 assetId,
        uint256 price
    );

    // Structure to hold asset listing details
    struct Listing {
        address seller;       // Address of the seller
        uint256 price;        // Price of the asset in wei
        bool isActive;        // Whether the listing is active or not
    }

    // Mapping from asset contract + asset ID to listing details
    mapping(address => mapping(uint256 => Listing)) public listings;

    /**
     * @dev List an NFT or ordinal for sale.
     * @param assetContract Address of the NFT/ordinal contract.
     * @param assetId ID of the NFT/ordinal in the contract.
     * @param price Selling price in wei.
     */
    function listAsset(address assetContract, uint256 assetId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Check asset ownership
        require(IERC721(assetContract).ownerOf(assetId) == msg.sender, "Caller must own the asset");

        // Approve the contract to transfer the NFT on behalf of the seller
        require(IERC721(assetContract).getApproved(assetId) == address(this), "Asset must be approved for transfer");

        // Create the listing
        listings[assetContract][assetId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit AssetListed(msg.sender, assetContract, assetId, price);
    }

    /**
     * @dev Purchase an NFT or ordinal from a listing.
     * @param assetContract Address of the NFT/ordinal contract.
     * @param assetId ID of the NFT/ordinal in the contract.
     */
    function purchaseAsset(address assetContract, uint256 assetId) external payable {
        Listing storage listing = listings[assetContract][assetId];

        require(listing.isActive, "Asset is not listed for sale");
        require(msg.value == listing.price, "Incorrect payment amount");

        address seller = listing.seller;

        // Transfer the payment to the seller
        (bool paymentSent, ) = seller.call{value: msg.value}("");
        require(paymentSent, "Failed to transfer payment to seller");

        // Transfer the NFT to the buyer
        IERC721(assetContract).safeTransferFrom(seller, msg.sender, assetId);

        // Mark the listing as inactive
        listing.isActive = false;

        emit AssetSold(msg.sender, seller, assetContract, assetId, listing.price);
    }

    /**
     * @dev Cancel an active listing.
     * @param assetContract Address of the NFT/ordinal contract.
     * @param assetId ID of the NFT/ordinal in the contract.
     */
    function cancelListing(address assetContract, uint256 assetId) external {
        Listing storage listing = listings[assetContract][assetId];

        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");

        // Mark the listing as inactive
        listing.isActive = false;

        emit AssetListed(msg.sender, assetContract, assetId, 0); // Emitting a canceled event by setting price to 0
    }

    /**
     * @dev Fallback function to allow contract to receive ETH.
     */
    receive() external payable {}
}

/**
 * @dev Interface for ERC721 standard as required by the contract.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function getApproved(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
}
```
