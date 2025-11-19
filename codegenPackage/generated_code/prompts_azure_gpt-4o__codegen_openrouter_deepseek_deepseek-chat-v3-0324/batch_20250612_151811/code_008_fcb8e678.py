"""
Generated Code Metadata:
========================
Original URL: https://ethereum.kim
Prompt: Write a Solidity contract that supports listing and querying active buy and sell offers for ERC-20 tokens, similar to the functionality described on ethereum.kim.
Generated: DETERMINISTIC_fcb8e678a6bcd42b
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenExchange is Ownable, ReentrancyGuard {
    struct Offer {
        address maker;
        address token;
        uint256 amount;
        uint256 price; // price per token in wei
        bool isBuy;
        bool isActive;
    }

    uint256 public offerIdCounter;
    mapping(uint256 => Offer) public offers;
    mapping(address => uint256[]) public userOffers;

    event OfferCreated(
        uint256 indexed offerId,
        address indexed maker,
        address indexed token,
        uint256 amount,
        uint256 price,
        bool isBuy
    );
    event OfferCancelled(uint256 indexed offerId);
    event OfferFilled(
        uint256 indexed offerId,
        address indexed taker,
        uint256 amountFilled
    );

    modifier onlyOfferMaker(uint256 offerId) {
        require(
            offers[offerId].maker == msg.sender,
            "Only offer maker can perform this action"
        );
        _;
    }

    modifier activeOffer(uint256 offerId) {
        require(offers[offerId].isActive, "Offer is not active");
        _;
    }

    function createOffer(
        address token,
        uint256 amount,
        uint256 price,
        bool isBuy
    ) external payable nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        require(price > 0, "Price must be greater than 0");

        if (isBuy) {
            require(
                msg.value == amount * price,
                "ETH sent must equal amount * price"
            );
        } else {
            IERC20 tokenContract = IERC20(token);
            require(
                tokenContract.allowance(msg.sender, address(this)) >= amount,
                "Insufficient token allowance"
            );
            tokenContract.transferFrom(msg.sender, address(this), amount);
        }

        uint256 offerId = ++offerIdCounter;
        offers[offerId] = Offer({
            maker: msg.sender,
            token: token,
            amount: amount,
            price: price,
            isBuy: isBuy,
            isActive: true
        });

        userOffers[msg.sender].push(offerId);

        emit OfferCreated(offerId, msg.sender, token, amount, price, isBuy);
    }

    function cancelOffer(uint256 offerId)
        external
        onlyOfferMaker(offerId)
        activeOffer(offerId)
        nonReentrant
    {
        Offer storage offer = offers[offerId];
        offer.isActive = false;

        if (offer.isBuy) {
            payable(msg.sender).transfer(offer.amount * offer.price);
        } else {
            IERC20(offer.token).transfer(msg.sender, offer.amount);
        }

        emit OfferCancelled(offerId);
    }

    function fillOffer(uint256 offerId, uint256 amount)
        external
        payable
        activeOffer(offerId)
        nonReentrant
    {
        Offer storage offer = offers[offerId];
        require(amount > 0, "Amount must be greater than 0");
        require(amount <= offer.amount, "Amount exceeds offer amount");

        if (offer.isBuy) {
            // Selling tokens to the buyer
            IERC20 tokenContract = IERC20(offer.token);
            require(
                tokenContract.allowance(msg.sender, address(this)) >= amount,
                "Insufficient token allowance"
            );
            tokenContract.transferFrom(msg.sender, offer.maker, amount);
            payable(msg.sender).transfer(amount * offer.price);
        } else {
            // Buying tokens from the seller
            require(
                msg.value == amount * offer.price,
                "ETH sent must equal amount * price"
            );
            IERC20(offer.token).transfer(msg.sender, amount);
            payable(offer.maker).transfer(msg.value);
        }

        offer.amount -= amount;
        if (offer.amount == 0) {
            offer.isActive = false;
        }

        emit OfferFilled(offerId, msg.sender, amount);
    }

    function getUserOffers(address user) external view returns (uint256[] memory) {
        return userOffers[user];
    }

    function getActiveOffers(
        address token,
        bool isBuy,
        uint256 skip,
        uint256 limit
    ) external view returns (uint256[] memory) {
        uint256[] memory result = new uint256[](limit);
        uint256 count = 0;

        for (uint256 i = 1; i <= offerIdCounter && count < limit; i++) {
            if (
                offers[i].isActive &&
                offers[i].token == token &&
                offers[i].isBuy == isBuy
            ) {
                if (skip > 0) {
                    skip--;
                } else {
                    result[count] = i;
                    count++;
                }
            }
        }

        // Resize array to actual count
        uint256[] memory trimmedResult = new uint256[](count);
        for (uint256 j = 0; j < count; j++) {
            trimmedResult[j] = result[j];
        }

        return trimmedResult;
    }

    function getOfferDetails(uint256 offerId)
        external
        view
        returns (
            address maker,
            address token,
            uint256 amount,
            uint256 price,
            bool isBuy,
            bool isActive
        )
    {
        Offer storage offer = offers[offerId];
        return (
            offer.maker,
            offer.token,
            offer.amount,
            offer.price,
            offer.isBuy,
            offer.isActive
        );
    }
}
```
