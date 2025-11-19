"""
Generated Code Metadata:
========================
Original URL: https://snap-metis.pages.dev
Prompt: "Create a Metis-specific smart contract using Solidity, implementing a basic NFT marketplace with on-chain storage and Community Ecosystem Governance (CEG) integration."
Generated: DETERMINISTIC_15ecb153a023b971
Batch ID: 20250622_205623
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
 * @title Metis NFT Marketplace with Community Ecosystem Governance (CEG) Integration
 * @dev This contract implements a basic NFT marketplace with on-chain storage and CEG integration.
 */
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetisNFTMarketplace is Ownable {
    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping to store all listings
    mapping(uint256 => Listing) public listings;
    uint256 public listingCounter;

    // Community Ecosystem Governance (CEG) fee percentage (e.g., 2%)
    uint256 public cegFeePercentage = 2;

    // Address to receive CEG fees
    address public cegFeeRecipient;

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
        address indexed seller,
        uint256 price
    );
    event ListingCancelled(uint256 indexed listingId);

    /**
     * @dev Constructor to initialize the CEG fee recipient.
     * @param _cegFeeRecipient Address to receive CEG fees.
     */
    constructor(address _cegFeeRecipient) {
        require(_cegFeeRecipient != address(0), "Invalid CEG fee recipient address");
        cegFeeRecipient = _cegFeeRecipient;
    }

    /**
     * @dev Function to list an NFT for sale.
     * @param _nftContract Address of the NFT contract.
     * @param _tokenId Token ID of the NFT.
     * @param _price Sale price of the NFT.
     */
    function listNFT(
        address _nftContract,
        uint256 _tokenId,
        uint256 _price
    ) external {
        require(_price > 0, "Price must be greater than zero");
        require(IERC721(_nftContract).ownerOf(_tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(IERC721(_nftContract).isApprovedForAll(msg.sender, address(this)), "Marketplace is not approved");

        listingCounter++;
        listings[listingCounter] = Listing({
            seller: msg.sender,
            nftContract: _nftContract,
            tokenId: _tokenId,
            price: _price,
            isActive: true
        });

        emit NFTListed(listingCounter, msg.sender, _nftContract, _tokenId, _price);
    }

    /**
     * @dev Function to purchase an NFT.
     * @param _listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 _listingId) external payable {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Calculate CEG fee
        uint256 cegFee = (listing.price * cegFeePercentage) / 100;
        uint256 sellerAmount = listing.price - cegFee;

        // Transfer funds
        payable(listing.seller).transfer(sellerAmount);
        payable(cegFeeRecipient).transfer(cegFee);

        // Transfer NFT
        IERC721(listing.nftContract).safeTransferFrom(listing.seller, msg.sender, listing.tokenId);

        // Mark listing as inactive
        listing.isActive = false;

        emit NFTPurchased(_listingId, msg.sender, listing.seller, listing.price);
    }

    /**
     * @dev Function to cancel an NFT listing.
     * @param _listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 _listingId) external {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Caller is not the seller");

        listing.isActive = false;

        emit ListingCancelled(_listingId);
    }

    /**
     * @dev Function to update the CEG fee percentage.
     * @param _newFeePercentage New fee percentage (e.g., 2 for 2%).
     */
    function updateCegFeePercentage(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage <= 100, "Fee percentage cannot exceed 100");
        cegFeePercentage = _newFeePercentage;
    }

    /**
     * @dev Function to update the CEG fee recipient address.
     * @param _newRecipient New recipient address.
     */
    function updateCegFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid recipient address");
        cegFeeRecipient = _newRecipient;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
