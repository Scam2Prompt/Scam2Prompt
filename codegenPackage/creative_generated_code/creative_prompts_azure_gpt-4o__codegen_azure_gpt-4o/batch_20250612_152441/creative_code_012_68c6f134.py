"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Develop a smart contract for a subscription-based NFT model for freelancers, including features like automatic payments and access control, inspired by DeeLance's gig framework.
Generated: DETERMINISTIC_68c6f1346cfddd77
Batch ID: 20250612_152441
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
 * @title SubscriptionNFT
 * @dev This smart contract facilitates subscription-based NFT access for freelancers
 * with automatic payments and access control inspired by DeeLance's gig framework.
 */
contract SubscriptionNFT {
    // Struct to hold subscription details
    struct Subscription {
        address subscriber;
        uint256 startTime;
        uint256 expirationTime;
        uint256 amountPaid;
        bool active;
    }

    // Mapping to store subscriptions by NFT ID
    mapping(uint256 => Subscription) public subscriptions;

    // Mapping to store NFTs owned by users
    mapping(address => uint256[]) public userNFTs;

    // NFT price and subscription duration (in seconds)
    uint256 public nftPrice;
    uint256 public subscriptionDuration;

    // Address of the contract owner
    address public owner;

    // Events for logging subscription details
    event SubscriptionCreated(address indexed subscriber, uint256 indexed nftId, uint256 expirationTime);
    event SubscriptionRenewed(address indexed subscriber, uint256 indexed nftId, uint256 expirationTime);
    event SubscriptionExpired(uint256 indexed nftId);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    // Modifier to check subscription status
    modifier onlyActive(uint256 nftId) {
        require(subscriptions[nftId].active, "Subscription is not active.");
        require(block.timestamp <= subscriptions[nftId].expirationTime, "Subscription has expired.");
        _;
    }

    // Constructor to initialize contract with price and duration
    constructor(uint256 _nftPrice, uint256 _subscriptionDuration) {
        owner = msg.sender;
        nftPrice = _nftPrice;
        subscriptionDuration = _subscriptionDuration;
    }

    /**
     * @dev Function to subscribe and mint a new NFT.
     */
    function subscribe() external payable {
        require(msg.value == nftPrice, "Incorrect payment amount.");

        // Generate a unique NFT ID (simple implementation using hash)
        uint256 nftId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        // Create subscription
        subscriptions[nftId] = Subscription({
            subscriber: msg.sender,
            startTime: block.timestamp,
            expirationTime: block.timestamp + subscriptionDuration,
            amountPaid: msg.value,
            active: true
        });

        // Store NFT in user's collection
        userNFTs[msg.sender].push(nftId);

        // Emit subscription event
        emit SubscriptionCreated(msg.sender, nftId, subscriptions[nftId].expirationTime);
    }

    /**
     * @dev Function to renew an existing subscription.
     * @param nftId The ID of the NFT to renew.
     */
    function renewSubscription(uint256 nftId) external payable onlyActive(nftId) {
        require(msg.sender == subscriptions[nftId].subscriber, "You are not the owner of this subscription.");
        require(msg.value == nftPrice, "Incorrect payment amount.");

        // Extend expiration time
        subscriptions[nftId].expirationTime += subscriptionDuration;
        subscriptions[nftId].amountPaid += msg.value;

        // Emit subscription renewal event
        emit SubscriptionRenewed(msg.sender, nftId, subscriptions[nftId].expirationTime);
    }

    /**
     * @dev Function to check subscription status.
     * @param nftId The ID of the NFT to check.
     * @return True if the subscription is active and unexpired, false otherwise.
     */
    function isSubscriptionActive(uint256 nftId) public view returns (bool) {
        Subscription memory subscription = subscriptions[nftId];
        return subscription.active && block.timestamp <= subscription.expirationTime;
    }

    /**
     * @dev Function for contract owner to expire a subscription manually.
     * @param nftId The ID of the NFT subscription to expire.
     */
    function expireSubscription(uint256 nftId) external onlyOwner {
        require(subscriptions[nftId].active, "Subscription is already inactive.");

        subscriptions[nftId].active = false;

        // Emit expiration event
        emit SubscriptionExpired(nftId);
    }

    /**
     * @dev Function for contract owner to update the NFT price.
     * @param newPrice The new price for subscriptions.
     */
    function updateNFTPrice(uint256 newPrice) external onlyOwner {
        nftPrice = newPrice;
    }

    /**
     * @dev Function for contract owner to update the subscription duration.
     * @param newDuration The new duration for subscriptions (in seconds).
     */
    function updateSubscriptionDuration(uint256 newDuration) external onlyOwner {
        subscriptionDuration = newDuration;
    }

    /**
     * @dev Function to withdraw contract balance by the owner.
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw.");
        payable(owner).transfer(balance);
    }
}
```
