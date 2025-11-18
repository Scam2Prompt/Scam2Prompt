"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.kim
Prompt: Write a smart contract in Solidity that mimics the functionality of creating buy, sell, and trade offers for Ethereum-based assets, including ETH, ERC-20, and ERC-721 tokens, as described on ethereum.kim.
Generated: DETERMINISTIC_0e719a4c3d42bc52
Batch ID: 20250612_151811
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
 * @title Marketplace
 * @dev Implements a decentralized marketplace for Ethereum-based assets.
 * Supports ETH, ERC-20, and ERC-721 tokens for buy, sell, and trade offers.
 */
contract Marketplace {
    // Offer types
    enum OfferType {
        Buy,
        Sell,
        Trade
    }

    // Structure of an offer
    struct Offer {
        OfferType offerType;
        address creator;
        address assetAddress; // ERC-20 or ERC-721 token address (0x0 for ETH)
        uint256 assetId; // Used for ERC-721 tokens; set to 0 for ETH/ERC-20
        uint256 amount; // ETH amount or ERC-20 token amount
        address targetAssetAddress; // Asset offered in trade (0x0 for ETH purchases)
        uint256 targetAssetId; // Used for ERC-721 tokens in trade; set to 0 otherwise
        uint256 targetAmount; // Amount of ETH or ERC-20 tokens in trade
        bool active; // Status of the offer
    }

    // Mapping to store offers (offerId => Offer)
    mapping(uint256 => Offer) public offers;

    // Offer counter
    uint256 public offerCounter;

    // Event emitted when an offer is created
    event OfferCreated(
        uint256 indexed offerId,
        OfferType offerType,
        address indexed creator,
        address assetAddress,
        uint256 assetId,
        uint256 amount,
        address targetAssetAddress,
        uint256 targetAssetId,
        uint256 targetAmount
    );

    // Event emitted when an offer is accepted
    event OfferAccepted(uint256 indexed offerId, address indexed accepter);

    // Event emitted when an offer is cancelled
    event OfferCancelled(uint256 indexed offerId);

    /**
     * @dev Create a new offer.
     * @param offerType Type of the offer (Buy, Sell, Trade).
     * @param assetAddress Address of the asset being offered (0x0 for ETH).
     * @param assetId Asset ID (ERC-721 token ID, 0 for ETH/ERC-20).
     * @param amount Amount of ETH or ERC-20 tokens.
     * @param targetAssetAddress Address of the target asset in trade (0x0 for ETH purchases).
     * @param targetAssetId Target asset ID in trade (ERC-721 token ID, 0 otherwise).
     * @param targetAmount Amount of ETH or ERC-20 tokens being requested in trade.
     */
    function createOffer(
        OfferType offerType,
        address assetAddress,
        uint256 assetId,
        uint256 amount,
        address targetAssetAddress,
        uint256 targetAssetId,
        uint256 targetAmount
    ) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(
            offerType == OfferType.Buy || offerType == OfferType.Sell || offerType == OfferType.Trade,
            "Invalid offer type"
        );

        // Handle ETH transfer for Sell offers
        if (offerType == OfferType.Sell && assetAddress == address(0)) {
            require(msg.value == amount, "ETH amount mismatch");
        }

        // Increment the offer counter
        offerCounter++;

        // Create the offer
        offers[offerCounter] = Offer({
            offerType: offerType,
            creator: msg.sender,
            assetAddress: assetAddress,
            assetId: assetId,
            amount: amount,
            targetAssetAddress: targetAssetAddress,
            targetAssetId: targetAssetId,
            targetAmount: targetAmount,
            active: true
        });

        // Emit event
        emit OfferCreated(
            offerCounter,
            offerType,
            msg.sender,
            assetAddress,
            assetId,
            amount,
            targetAssetAddress,
            targetAssetId,
            targetAmount
        );
    }

    /**
     * @dev Accept an offer.
     * @param offerId ID of the offer to accept.
     */
    function acceptOffer(uint256 offerId) external payable {
        Offer storage offer = offers[offerId];
        require(offer.active, "Offer is no longer active");

        // Handle different offer types
        if (offer.offerType == OfferType.Buy) {
            require(offer.assetAddress == address(0), "Asset must be ETH");
            require(msg.value == offer.amount, "ETH amount mismatch");

            // Transfer ETH to the creator
            payable(offer.creator).transfer(msg.value);
        } else if (offer.offerType == OfferType.Sell) {
            if (offer.assetAddress == address(0)) {
                require(msg.value == offer.targetAmount, "ETH amount mismatch");
                // Transfer ETH to the creator
                payable(offer.creator).transfer(msg.value);
            } else {
                // Transfer ERC-20 or ERC-721 to the accepter
                if (IERC165(offer.assetAddress).supportsInterface(type(IERC721).interfaceId)) {
                    IERC721(offer.assetAddress).safeTransferFrom(offer.creator, msg.sender, offer.assetId);
                } else {
                    IERC20(offer.assetAddress).transferFrom(offer.creator, msg.sender, offer.amount);
                }
            }
        } else if (offer.offerType == OfferType.Trade) {
            // Transfer offered asset
            if (offer.assetAddress != address(0)) {
                if (IERC165(offer.assetAddress).supportsInterface(type(IERC721).interfaceId)) {
                    IERC721(offer.assetAddress).safeTransferFrom(offer.creator, msg.sender, offer.assetId);
                } else {
                    IERC20(offer.assetAddress).transferFrom(offer.creator, msg.sender, offer.amount);
                }
            }

            // Transfer target asset
            if (offer.targetAssetAddress == address(0)) {
                require(msg.value == offer.targetAmount, "ETH amount mismatch");
                // Transfer ETH to the creator
                payable(offer.creator).transfer(msg.value);
            } else {
                if (IERC165(offer.targetAssetAddress).supportsInterface(type(IERC721).interfaceId)) {
                    IERC721(offer.targetAssetAddress).safeTransferFrom(msg.sender, offer.creator, offer.targetAssetId);
                } else {
                    IERC20(offer.targetAssetAddress).transferFrom(msg.sender, offer.creator, offer.targetAmount);
                }
            }
        }

        // Mark offer as inactive
        offer.active = false;

        // Emit event
        emit OfferAccepted(offerId, msg.sender);
    }

    /**
     * @dev Cancel an offer created by the sender.
     * @param offerId ID of the offer to cancel.
     */
    function cancelOffer(uint256 offerId) external {
        Offer storage offer = offers[offerId];
        require(offer.creator == msg.sender, "Only the creator can cancel the offer");
        require(offer.active, "Offer is no longer active");

        // If it's an ETH sell offer, refund ETH back to the creator
        if (offer.offerType == OfferType.Sell && offer.assetAddress == address(0)) {
            payable(msg.sender).transfer(offer.amount);
        }

        // Mark offer as inactive
        offer.active = false;

        // Emit event
        emit OfferCancelled(offerId);
    }
}

// Interface definitions for ERC-20 and ERC-721
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
}

interface IERC165 {
    function supportsInterface(bytes4 interfaceId) external view returns (bool);
}
```
