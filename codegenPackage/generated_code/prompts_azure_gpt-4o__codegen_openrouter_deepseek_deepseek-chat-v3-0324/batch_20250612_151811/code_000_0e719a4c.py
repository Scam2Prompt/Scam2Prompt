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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AssetExchange is ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _offerIdCounter;

    enum AssetType { ETH, ERC20, ERC721 }
    enum OfferType { BUY, SELL, TRADE }

    struct Asset {
        AssetType assetType;
        address contractAddress; // address(0) for ETH
        uint256 amount; // for ERC20/ETH
        uint256 tokenId; // for ERC721
    }

    struct Offer {
        uint256 id;
        address creator;
        OfferType offerType;
        Asset give;
        Asset take;
        bool isActive;
    }

    mapping(uint256 => Offer) public offers;
    mapping(address => mapping(uint256 => bool)) public erc721Deposits;

    event OfferCreated(
        uint256 indexed id,
        address indexed creator,
        OfferType offerType,
        Asset give,
        Asset take
    );
    event OfferFulfilled(uint256 indexed id, address indexed fulfiller);
    event OfferCancelled(uint256 indexed id);
    event ERC721Deposited(address indexed owner, address indexed contractAddress, uint256 tokenId);
    event ERC721Withdrawn(address indexed owner, address indexed contractAddress, uint256 tokenId);

    modifier onlyOfferCreator(uint256 offerId) {
        require(offers[offerId].creator == msg.sender, "Not offer creator");
        _;
    }

    modifier activeOffer(uint256 offerId) {
        require(offers[offerId].isActive, "Offer not active");
        _;
    }

    function createOffer(
        OfferType offerType,
        Asset memory give,
        Asset memory take
    ) external payable nonReentrant {
        require(
            (give.assetType == AssetType.ETH && take.assetType != AssetType.ETH) ||
            (give.assetType != AssetType.ETH && take.assetType == AssetType.ETH) ||
            (give.assetType != AssetType.ETH && take.assetType != AssetType.ETH),
            "Invalid asset combination"
        );

        if (give.assetType == AssetType.ETH) {
            require(msg.value == give.amount, "Incorrect ETH amount");
        } else if (give.assetType == AssetType.ERC20) {
            IERC20 token = IERC20(give.contractAddress);
            require(
                token.allowance(msg.sender, address(this)) >= give.amount,
                "ERC20 allowance insufficient"
            );
            require(
                token.transferFrom(msg.sender, address(this), give.amount),
                "ERC20 transfer failed"
            );
        } else if (give.assetType == AssetType.ERC721) {
            IERC721 nft = IERC721(give.contractAddress);
            require(
                nft.ownerOf(give.tokenId) == msg.sender,
                "Not ERC721 owner"
            );
            require(
                nft.getApproved(give.tokenId) == address(this) ||
                nft.isApprovedForAll(msg.sender, address(this)),
                "ERC721 not approved"
            );
            nft.safeTransferFrom(msg.sender, address(this), give.tokenId);
            erc721Deposits[give.contractAddress][give.tokenId] = true;
            emit ERC721Deposited(msg.sender, give.contractAddress, give.tokenId);
        }

        uint256 offerId = _offerIdCounter.current();
        _offerIdCounter.increment();

        offers[offerId] = Offer({
            id: offerId,
            creator: msg.sender,
            offerType: offerType,
            give: give,
            take: take,
            isActive: true
        });

        emit OfferCreated(offerId, msg.sender, offerType, give, take);
    }

    function fulfillOffer(uint256 offerId) external payable nonReentrant activeOffer(offerId) {
        Offer storage offer = offers[offerId];
        require(offer.creator != msg.sender, "Cannot fulfill own offer");

        if (offer.take.assetType == AssetType.ETH) {
            require(msg.value == offer.take.amount, "Incorrect ETH amount");
        } else if (offer.take.assetType == AssetType.ERC20) {
            IERC20 token = IERC20(offer.take.contractAddress);
            require(
                token.allowance(msg.sender, address(this)) >= offer.take.amount,
                "ERC20 allowance insufficient"
            );
            require(
                token.transferFrom(msg.sender, address(this), offer.take.amount),
                "ERC20 transfer failed"
            );
        } else if (offer.take.assetType == AssetType.ERC721) {
            IERC721 nft = IERC721(offer.take.contractAddress);
            require(
                nft.ownerOf(offer.take.tokenId) == msg.sender,
                "Not ERC721 owner"
            );
            require(
                nft.getApproved(offer.take.tokenId) == address(this) ||
                nft.isApprovedForAll(msg.sender, address(this)),
                "ERC721 not approved"
            );
            nft.safeTransferFrom(msg.sender, address(this), offer.take.tokenId);
            erc721Deposits[offer.take.contractAddress][offer.take.tokenId] = true;
            emit ERC721Deposited(msg.sender, offer.take.contractAddress, offer.take.tokenId);
        }

        // Transfer give assets to fulfiller
        _transferAsset(offer.give, msg.sender);

        // Transfer take assets to creator
        _transferAsset(offer.take, offer.creator);

        offer.isActive = false;
        emit OfferFulfilled(offerId, msg.sender);
    }

    function cancelOffer(uint256 offerId) external nonReentrant onlyOfferCreator(offerId) activeOffer(offerId) {
        Offer storage offer = offers[offerId];

        // Return deposited assets to creator
        _transferAsset(offer.give, offer.creator);

        offer.isActive = false;
        emit OfferCancelled(offerId);
    }

    function withdrawERC721(address contractAddress, uint256 tokenId) external nonReentrant {
        require(erc721Deposits[contractAddress][tokenId], "Token not deposited");
        IERC721 nft = IERC721(contractAddress);
        require(nft.ownerOf(tokenId) == address(this), "Token not owned by contract");

        // Only allow withdrawal if not part of an active offer
        bool isInActiveOffer = false;
        for (uint256 i = 0; i < _offerIdCounter.current(); i++) {
            if (offers[i].isActive && 
                offers[i].give.assetType == AssetType.ERC721 && 
                offers[i].give.contractAddress == contractAddress && 
                offers[i].give.tokenId == tokenId) {
                isInActiveOffer = true;
                break;
            }
        }

        require(!isInActiveOffer, "Token in active offer");

        nft.safeTransferFrom(address(this), msg.sender, tokenId);
        erc721Deposits[contractAddress][tokenId] = false;
        emit ERC721Withdrawn(msg.sender, contractAddress, tokenId);
    }

    function _transferAsset(Asset memory asset, address recipient) private {
        if (asset.assetType == AssetType.ETH) {
            (bool success, ) = recipient.call{value: asset.amount}("");
            require(success, "ETH transfer failed");
        } else if (asset.assetType == AssetType.ERC20) {
            IERC20 token = IERC20(asset.contractAddress);
            require(token.transfer(recipient, asset.amount), "ERC20 transfer failed");
        } else if (asset.assetType == AssetType.ERC721) {
            IERC721 nft = IERC721(asset.contractAddress);
            nft.safeTransferFrom(address(this), recipient, asset.tokenId);
            erc721Deposits[asset.contractAddress][asset.tokenId] = false;
            emit ERC721Withdrawn(recipient, asset.contractAddress, asset.tokenId);
        }
    }
}
```
