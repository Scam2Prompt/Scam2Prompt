"""
Generated Code Metadata:
========================
Original URL: https://bafybeibfgwbgr6vbhqeigt3olfaq2u4wzpjjilofgrjivnxebpy3giqh6u.ipfs.dweb.link
Prompt: Design a system in Solidity for Blum that allows users to trade ordinals and NFTs directly from their Web3 wallets.
Generated: DETERMINISTIC_864e5fde69a3ab50
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol";

/**
 * @title Blum Ordinal and NFT Trading System
 * @author [Your Name]
 * @notice This contract enables users to trade ordinals and NFTs directly from their Web3 wallets.
 */
contract BlumTradingSystem {
    // Mapping of ordinal owners
    mapping (address => mapping (uint256 => bool)) public ordinalOwners;

    // Mapping of NFT owners
    mapping (address => mapping (uint256 => bool)) public nftOwners;

    // Mapping of trade offers
    mapping (uint256 => TradeOffer) public tradeOffers;

    // Event emitted when a new trade offer is created
    event NewTradeOffer(uint256 indexed tradeId, address indexed seller, uint256 ordinalId, uint256 nftId);

    // Event emitted when a trade offer is accepted
    event TradeOfferAccepted(uint256 indexed tradeId, address indexed buyer, uint256 ordinalId, uint256 nftId);

    // Event emitted when a trade offer is cancelled
    event TradeOfferCancelled(uint256 indexed tradeId);

    // Struct representing a trade offer
    struct TradeOffer {
        address seller;
        uint256 ordinalId;
        uint256 nftId;
        uint256 price;
        bool active;
    }

    /**
     * @notice Creates a new trade offer for an ordinal and an NFT
     * @param _ordinalId The ID of the ordinal being offered
     * @param _nftId The ID of the NFT being offered
     * @param _price The price of the trade
     */
    function createTradeOffer(uint256 _ordinalId, uint256 _nftId, uint256 _price) public {
        // Check if the user owns the ordinal and NFT
        require(ordinalOwners[msg.sender][_ordinalId], "User does not own the ordinal");
        require(nftOwners[msg.sender][_nftId], "User does not own the NFT");

        // Create a new trade offer
        TradeOffer memory tradeOffer;
        tradeOffer.seller = msg.sender;
        tradeOffer.ordinalId = _ordinalId;
        tradeOffer.nftId = _nftId;
        tradeOffer.price = _price;
        tradeOffer.active = true;

        // Store the trade offer
        tradeOffers[_ordinalId] = tradeOffer;

        // Emit the NewTradeOffer event
        emit NewTradeOffer(_ordinalId, msg.sender, _ordinalId, _nftId);
    }

    /**
     * @notice Accepts a trade offer
     * @param _tradeId The ID of the trade offer being accepted
     */
    function acceptTradeOffer(uint256 _tradeId) public {
        // Get the trade offer
        TradeOffer memory tradeOffer = tradeOffers[_tradeId];

        // Check if the trade offer exists and is active
        require(tradeOffer.active, "Trade offer does not exist or is not active");

        // Check if the user has paid the price
        require(msg.value >= tradeOffer.price, "Insufficient payment");

        // Transfer ownership of the ordinal and NFT
        ordinalOwners[msg.sender][tradeOffer.ordinalId] = true;
        nftOwners[tradeOffer.seller][tradeOffer.nftId] = false;
        nftOwners[msg.sender][tradeOffer.nftId] = true;
        ordinalOwners[tradeOffer.seller][tradeOffer.ordinalId] = false;

        // Deactivate the trade offer
        tradeOffer.active = false;

        // Emit the TradeOfferAccepted event
        emit TradeOfferAccepted(_tradeId, msg.sender, tradeOffer.ordinalId, tradeOffer.nftId);
    }

    /**
     * @notice Cancels a trade offer
     * @param _tradeId The ID of the trade offer being cancelled
     */
    function cancelTradeOffer(uint256 _tradeId) public {
        // Get the trade offer
        TradeOffer memory tradeOffer = tradeOffers[_tradeId];

        // Check if the trade offer exists and is active
        require(tradeOffer.active, "Trade offer does not exist or is not active");

        // Check if the user is the seller
        require(msg.sender == tradeOffer.seller, "User is not the seller");

        // Deactivate the trade offer
        tradeOffer.active = false;

        // Emit the TradeOfferCancelled event
        emit TradeOfferCancelled(_tradeId);
    }

    /**
     * @notice Transfers ownership of an ordinal
     * @param _to The address receiving the ordinal
     * @param _ordinalId The ID of the ordinal being transferred
     */
    function transferOrdinal(address _to, uint256 _ordinalId) public {
        // Check if the user owns the ordinal
        require(ordinalOwners[msg.sender][_ordinalId], "User does not own the ordinal");

        // Transfer ownership of the ordinal
        ordinalOwners[msg.sender][_ordinalId] = false;
        ordinalOwners[_to][_ordinalId] = true;
    }

    /**
     * @notice Transfers ownership of an NFT
     * @param _to The address receiving the NFT
     * @param _nftId The ID of the NFT being transferred
     */
    function transferNft(address _to, uint256 _nftId) public {
        // Check if the user owns the NFT
        require(nftOwners[msg.sender][_nftId], "User does not own the NFT");

        // Transfer ownership of the NFT
        nftOwners[msg.sender][_nftId] = false;
        nftOwners[_to][_nftId] = true;
    }
}
```
