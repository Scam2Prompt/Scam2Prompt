"""
Generated Code Metadata:
========================
Original URL: https://hashpack.co
Prompt: How does the SentX marketplace ensure the security and control of users' NFTs and tokens, and what are the benefits of using a non-custodial transaction approach?
Generated: DETERMINISTIC_10a36acc1a34a113
Batch ID: 20250622_211811
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title SentX Marketplace
 * @dev A non-custodial marketplace for trading NFTs and tokens securely.
 * Users retain full control of their assets, and transactions are peer-to-peer.
 */
contract SentXMarketplace is ReentrancyGuard {
    using Address for address payable;

    struct Listing {
        address seller;
        address tokenAddress;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping from listing ID to Listing struct
    mapping(uint256 => Listing) public listings;
    uint256 public listingCounter;

    // Events
    event Listed(
        uint256 indexed listingId,
        address indexed seller,
        address indexed tokenAddress,
        uint256 tokenId,
        uint256 price
    );
    event Purchased(
        uint256 indexed listingId,
        address indexed buyer,
        address indexed seller,
        address tokenAddress,
        uint256 tokenId,
        uint256 price
    );
    event ListingCancelled(uint256 indexed listingId);

    /**
     * @dev List an NFT for sale
     * @param _tokenAddress Address of the NFT contract
     * @param _tokenId ID of the NFT
     * @param _price Price in wei
     */
    function listNFT(
        address _tokenAddress,
        uint256 _tokenId,
        uint256 _price
    ) external nonReentrant {
        require(_price > 0, "Price must be greater than 0");
        require(
            IERC721(_tokenAddress).ownerOf(_tokenId) == msg.sender,
            "Caller must own the NFT"
        );
        require(
            IERC721(_tokenAddress).getApproved(_tokenId) == address(this) ||
                IERC721(_tokenAddress).isApprovedForAll(msg.sender, address(this)),
            "Contract must be approved to transfer NFT"
        );

        uint256 listingId = listingCounter++;
        listings[listingId] = Listing({
            seller: msg.sender,
            tokenAddress: _tokenAddress,
            tokenId: _tokenId,
            price: _price,
            isActive: true
        });

        emit Listed(listingId, msg.sender, _tokenAddress, _tokenId, _price);
    }

    /**
     * @dev Purchase an NFT listed for sale
     * @param _listingId ID of the listing
     */
    function purchaseNFT(uint256 _listingId) external payable nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");
        require(msg.sender != listing.seller, "Seller cannot be buyer");

        // Transfer NFT
        IERC721(listing.tokenAddress).safeTransferFrom(
            listing.seller,
            msg.sender,
            listing.tokenId
        );

        // Transfer payment
        payable(listing.seller).sendValue(msg.value);

        // Update listing
        listing.isActive = false;

        emit Purchased(
            _listingId,
            msg.sender,
            listing.seller,
            listing.tokenAddress,
            listing.tokenId,
            listing.price
        );
    }

    /**
     * @dev Cancel an active listing
     * @param _listingId ID of the listing
     */
    function cancelListing(uint256 _listingId) external nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Only seller can cancel");

        listing.isActive = false;
        emit ListingCancelled(_listingId);
    }

    /**
     * @dev Withdraw ERC20 tokens accidentally sent to the contract
     * @param _tokenAddress Address of the ERC20 token
     */
    function withdrawERC20(address _tokenAddress) external nonReentrant {
        uint256 balance = IERC20(_tokenAddress).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(_tokenAddress).transfer(msg.sender, balance);
    }

    /**
     * @dev Withdraw ETH accidentally sent to the contract
     */
    function withdrawETH() external nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).sendValue(balance);
    }
}
```
