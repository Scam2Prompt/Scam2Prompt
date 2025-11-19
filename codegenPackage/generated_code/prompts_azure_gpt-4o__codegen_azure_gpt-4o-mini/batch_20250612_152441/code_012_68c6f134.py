"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: Develop a smart contract for a subscription-based NFT model for freelancers, including features like automatic payments and access control, inspired by DeeLance's gig framework.
Generated: DETERMINISTIC_68c6f1346cfddd77
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title SubscriptionBasedNFT
// @dev A smart contract for a subscription-based NFT model for freelancers
contract SubscriptionBasedNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    // Struct to hold subscription details
    struct Subscription {
        uint256 price; // Subscription price in wei
        uint256 duration; // Duration of the subscription in seconds
        uint256 startTime; // Start time of the subscription
        bool isActive; // Subscription status
    }

    // Mapping from token ID to subscription details
    mapping(uint256 => Subscription) public subscriptions;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a subscription is created
    event SubscriptionCreated(uint256 indexed tokenId, uint256 price, uint256 duration);

    // Event emitted when a subscription is renewed
    event SubscriptionRenewed(uint256 indexed tokenId, uint256 newStartTime);

    // Event emitted when a subscription is canceled
    event SubscriptionCanceled(uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("FreelancerNFT", "FNFT") {}

    // @dev Create a new subscription NFT
    // @param price The price of the subscription in wei
    // @param duration The duration of the subscription in seconds
    function createSubscription(uint256 price, uint256 duration) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        subscriptions[tokenId] = Subscription({
            price: price,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        _tokenIdCounter.increment();

        emit SubscriptionCreated(tokenId, price, duration);
    }

    // @dev Renew an existing subscription
    // @param tokenId The ID of the subscription NFT
    function renewSubscription(uint256 tokenId) external payable {
        require(_exists(tokenId), "Subscription does not exist");
        require(msg.value == subscriptions[tokenId].price, "Incorrect payment amount");
        require(subscriptions[tokenId].isActive, "Subscription is not active");

        // Update the start time to the current time
        subscriptions[tokenId].startTime = block.timestamp;

        emit SubscriptionRenewed(tokenId, subscriptions[tokenId].startTime);
    }

    // @dev Cancel an existing subscription
    // @param tokenId The ID of the subscription NFT
    function cancelSubscription(uint256 tokenId) external {
        require(_exists(tokenId), "Subscription does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can cancel the subscription");

        subscriptions[tokenId].isActive = false;

        emit SubscriptionCanceled(tokenId);
    }

    // @dev Check if a subscription is active
    // @param tokenId The ID of the subscription NFT
    // @return isActive True if the subscription is active, false otherwise
    function isSubscriptionActive(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Subscription does not exist");
        return subscriptions[tokenId].isActive && (block.timestamp < subscriptions[tokenId].startTime + subscriptions[tokenId].duration);
    }

    // @dev Withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // @dev Fallback function to accept Ether
    receive() external payable {}
}
```
