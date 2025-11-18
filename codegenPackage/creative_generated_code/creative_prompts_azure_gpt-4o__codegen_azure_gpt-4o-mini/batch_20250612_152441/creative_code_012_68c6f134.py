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

// Import OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for a subscription-based NFT model
contract SubscriptionNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a subscription
    struct Subscription {
        uint256 price; // Price of the subscription
        uint256 duration; // Duration of the subscription in seconds
        uint256 endTime; // End time of the subscription
        bool isActive; // Status of the subscription
    }

    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    mapping(uint256 => Subscription) private _subscriptions; // Mapping from token ID to subscription
    mapping(address => uint256) private _activeTokens; // Mapping from user to their active subscription token ID

    // Event emitted when a new subscription is created
    event SubscriptionCreated(uint256 indexed tokenId, uint256 price, uint256 duration);

    // Event emitted when a subscription is renewed
    event SubscriptionRenewed(uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("FreelancerNFT", "FNFT") {}

    // Function to create a new subscription NFT
    function createSubscription(uint256 price, uint256 duration) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Mint a new NFT for the subscription
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        // Create the subscription
        _subscriptions[tokenId] = Subscription(price, duration, 0, false);
        emit SubscriptionCreated(tokenId, price, duration);
    }

    // Function to purchase a subscription
    function purchaseSubscription(uint256 tokenId) external payable {
        Subscription storage subscription = _subscriptions[tokenId];

        require(subscription.price > 0, "Subscription does not exist");
        require(!subscription.isActive, "Subscription is already active");
        require(msg.value >= subscription.price, "Insufficient payment");

        // Activate the subscription
        subscription.endTime = block.timestamp + subscription.duration;
        subscription.isActive = true;
        _activeTokens[msg.sender] = tokenId;

        // Emit event for subscription renewal
        emit SubscriptionRenewed(tokenId);
    }

    // Function to check if a subscription is active for a user
    function isSubscriptionActive(address user) external view returns (bool) {
        uint256 tokenId = _activeTokens[user];
        Subscription storage subscription = _subscriptions[tokenId];

        return subscription.isActive && (block.timestamp < subscription.endTime);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to get subscription details
    function getSubscriptionDetails(uint256 tokenId) external view returns (Subscription memory) {
        return _subscriptions[tokenId];
    }
}
```
