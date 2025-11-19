"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates secure transactions on a decentralized marketplace like Pushd, utilizing Ethereum blockchain technology.
Generated: DETERMINISTIC_687dba9d89ca95e5
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract DecentralizedMarketplace is ReentrancyGuard {
    using Address for address payable;

    struct Listing {
        address seller;
        address tokenAddress; // Address of ERC20 token (address(0) for ETH)
        uint256 price;
        uint256 amount;
        bool isActive;
    }

    mapping(uint256 => Listing) public listings;
    uint256 public listingCount;
    uint256 public feePercentage; // Platform fee percentage (e.g., 100 = 1%)
    address public feeRecipient;

    event ItemListed(
        uint256 indexed listingId,
        address indexed seller,
        address tokenAddress,
        uint256 price,
        uint256 amount
    );
    event ItemPurchased(
        uint256 indexed listingId,
        address indexed buyer,
        address indexed seller,
        address tokenAddress,
        uint256 price,
        uint256 amount
    );
    event ListingCancelled(uint256 indexed listingId);
    event FeeUpdated(uint256 newFeePercentage);
    event FeeRecipientUpdated(address newFeeRecipient);

    constructor(uint256 _feePercentage, address _feeRecipient) {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        feePercentage = _feePercentage;
        feeRecipient = _feeRecipient;
    }

    function listItem(
        address _tokenAddress,
        uint256 _price,
        uint256 _amount
    ) external {
        require(_price > 0, "Price must be greater than 0");
        require(_amount > 0, "Amount must be greater than 0");

        if (_tokenAddress != address(0)) {
            IERC20 token = IERC20(_tokenAddress);
            require(
                token.allowance(msg.sender, address(this)) >= _amount,
                "Insufficient token allowance"
            );
            require(
                token.transferFrom(msg.sender, address(this), _amount),
                "Token transfer failed"
            );
        } else {
            require(msg.value == _amount, "Incorrect ETH amount");
        }

        listingCount++;
        listings[listingCount] = Listing(
            msg.sender,
            _tokenAddress,
            _price,
            _amount,
            true
        );

        emit ItemListed(listingCount, msg.sender, _tokenAddress, _price, _amount);
    }

    function purchaseItem(uint256 _listingId) external payable nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller != msg.sender, "Cannot purchase your own listing");

        uint256 totalPrice = listing.price * listing.amount;
        uint256 feeAmount = (totalPrice * feePercentage) / 10000;
        uint256 sellerAmount = totalPrice - feeAmount;

        if (listing.tokenAddress == address(0)) {
            require(msg.value == totalPrice, "Incorrect ETH amount");
            payable(listing.seller).sendValue(sellerAmount);
            payable(feeRecipient).sendValue(feeAmount);
        } else {
            IERC20 token = IERC20(listing.tokenAddress);
            require(
                token.allowance(msg.sender, address(this)) >= totalPrice,
                "Insufficient token allowance"
            );
            require(
                token.transferFrom(msg.sender, listing.seller, sellerAmount),
                "Token transfer to seller failed"
            );
            require(
                token.transferFrom(msg.sender, feeRecipient, feeAmount),
                "Token transfer to fee recipient failed"
            );
        }

        if (listing.tokenAddress == address(0)) {
            payable(msg.sender).sendValue(listing.amount);
        } else {
            IERC20(listing.tokenAddress).transfer(msg.sender, listing.amount);
        }

        listing.isActive = false;

        emit ItemPurchased(
            _listingId,
            msg.sender,
            listing.seller,
            listing.tokenAddress,
            listing.price,
            listing.amount
        );
    }

    function cancelListing(uint256 _listingId) external nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Only seller can cancel");

        if (listing.tokenAddress == address(0)) {
            payable(msg.sender).sendValue(listing.amount);
        } else {
            IERC20(listing.tokenAddress).transfer(msg.sender, listing.amount);
        }

        listing.isActive = false;

        emit ListingCancelled(_listingId);
    }

    function updateFeePercentage(uint256 _newFeePercentage) external {
        require(msg.sender == feeRecipient, "Only fee recipient can update fee");
        require(_newFeePercentage <= 1000, "Fee cannot exceed 10%");
        feePercentage = _newFeePercentage;
        emit FeeUpdated(_newFeePercentage);
    }

    function updateFeeRecipient(address _newFeeRecipient) external {
        require(msg.sender == feeRecipient, "Only fee recipient can update recipient");
        require(_newFeeRecipient != address(0), "Invalid fee recipient");
        feeRecipient = _newFeeRecipient;
        emit FeeRecipientUpdated(_newFeeRecipient);
    }
}
```
