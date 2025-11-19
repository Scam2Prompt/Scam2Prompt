"""
Generated Code Metadata:
========================
Original URL: https://ethereum.kim
Prompt: Write a smart contract in Solidity that mimics the functionality of creating buy, sell, and trade offers for Ethereum-based assets, including ETH, ERC-20, and ERC-721 tokens, as described on ethereum.kim.
Generated: DETERMINISTIC_0e719a4c3d42bc52
Batch ID: 20250612_151811
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

// Importing necessary interfaces for ERC20 and ERC721
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing buy, sell, and trade offers
contract AssetMarketplace is Ownable {
    // Struct to represent an offer
    struct Offer {
        address seller;
        address assetAddress;
        uint256 assetId; // For ERC721, 0 for ERC20
        uint256 price;
        bool isActive;
        OfferType offerType;
    }

    // Enum to differentiate between asset types
    enum OfferType { ERC20, ERC721 }

    // Mapping to store offers by their ID
    mapping(uint256 => Offer) public offers;
    uint256 public offerCount;

    // Events for logging actions
    event OfferCreated(uint256 offerId, address indexed seller, address indexed assetAddress, uint256 price, OfferType offerType);
    event OfferCancelled(uint256 offerId);
    event OfferExecuted(uint256 offerId, address indexed buyer);

    // Function to create a new offer
    function createOffer(address _assetAddress, uint256 _assetId, uint256 _price, OfferType _offerType) external {
        require(_price > 0, "Price must be greater than zero");

        // Increment offer count to create a unique offer ID
        offerCount++;
        offers[offerCount] = Offer(msg.sender, _assetAddress, _assetId, _price, true, _offerType);

        emit OfferCreated(offerCount, msg.sender, _assetAddress, _price, _offerType);
    }

    // Function to cancel an existing offer
    function cancelOffer(uint256 _offerId) external {
        Offer storage offer = offers[_offerId];
        require(offer.isActive, "Offer is not active");
        require(offer.seller == msg.sender, "Only the seller can cancel the offer");

        offer.isActive = false;

        emit OfferCancelled(_offerId);
    }

    // Function to execute an offer
    function executeOffer(uint256 _offerId) external payable {
        Offer storage offer = offers[_offerId];
        require(offer.isActive, "Offer is not active");
        require(msg.value == offer.price, "Incorrect payment amount");

        // Transfer ETH or tokens based on the offer type
        if (offer.offerType == OfferType.ERC20) {
            IERC20(offer.assetAddress).transferFrom(offer.seller, msg.sender, offer.assetId);
        } else if (offer.offerType == OfferType.ERC721) {
            IERC721(offer.assetAddress).transferFrom(offer.seller, msg.sender, offer.assetId);
        }

        // Transfer payment to the seller
        payable(offer.seller).transfer(msg.value);

        // Mark the offer as inactive
        offer.isActive = false;

        emit OfferExecuted(_offerId, msg.sender);
    }

    // Function to withdraw any accidentally sent ETH to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
