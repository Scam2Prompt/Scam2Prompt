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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SubscriptionNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Subscription {
        uint256 tokenId;
        address subscriber;
        uint256 startTime;
        uint256 endTime;
        uint256 price;
        bool isActive;
        address paymentToken; // Address of ERC20 token used for payment (zero address for ETH)
    }

    struct Freelancer {
        address wallet;
        string name;
        bool isActive;
    }

    mapping(uint256 => Subscription) public subscriptions;
    mapping(address => Freelancer) public freelancers;
    mapping(address => mapping(uint256 => bool)) public hasAccess;

    uint256 public subscriptionDuration = 30 days;
    uint256 public platformFeePercentage = 5; // 5% platform fee
    address public platformWallet;

    event SubscriptionCreated(
        uint256 indexed tokenId,
        address indexed subscriber,
        uint256 startTime,
        uint256 endTime,
        uint256 price,
        address paymentToken
    );
    event SubscriptionRenewed(uint256 indexed tokenId, uint256 newEndTime);
    event SubscriptionCancelled(uint256 indexed tokenId);
    event FreelancerRegistered(address indexed freelancer, string name);
    event FreelancerDeactivated(address indexed freelancer);
    event PaymentTokenUpdated(address indexed freelancer, address paymentToken);

    constructor(
        string memory _name,
        string memory _symbol,
        address _platformWallet
    ) ERC721(_name, _symbol) {
        require(_platformWallet != address(0), "Invalid platform wallet");
        platformWallet = _platformWallet;
    }

    modifier onlyFreelancer() {
        require(freelancers[msg.sender].isActive, "Not an active freelancer");
        _;
    }

    modifier onlySubscriber(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the subscriber");
        _;
    }

    function registerFreelancer(string memory name) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(!freelancers[msg.sender].isActive, "Already registered");

        freelancers[msg.sender] = Freelancer({
            wallet: msg.sender,
            name: name,
            isActive: true
        });

        emit FreelancerRegistered(msg.sender, name);
    }

    function deactivateFreelancer(address freelancer) external onlyOwner {
        require(freelancers[freelancer].isActive, "Freelancer not active");
        freelancers[freelancer].isActive = false;
        emit FreelancerDeactivated(freelancer);
    }

    function createSubscription(
        address freelancer,
        uint256 price,
        address paymentToken
    ) external payable nonReentrant {
        require(freelancers[freelancer].isActive, "Freelancer not active");
        require(price > 0, "Price must be greater than 0");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + subscriptionDuration;

        if (paymentToken == address(0)) {
            require(msg.value == price, "Incorrect ETH amount");
            uint256 platformFee = (price * platformFeePercentage) / 100;
            payable(platformWallet).transfer(platformFee);
            payable(freelancer).transfer(price - platformFee);
        } else {
            IERC20 token = IERC20(paymentToken);
            require(
                token.transferFrom(msg.sender, address(this), price),
                "Payment failed"
            );
            uint256 platformFee = (price * platformFeePercentage) / 100;
            token.transfer(platformWallet, platformFee);
            token.transfer(freelancer, price - platformFee);
        }

        _safeMint(msg.sender, tokenId);

        subscriptions[tokenId] = Subscription({
            tokenId: tokenId,
            subscriber: msg.sender,
            startTime: startTime,
            endTime: endTime,
            price: price,
            isActive: true,
            paymentToken: paymentToken
        });

        hasAccess[msg.sender][tokenId] = true;

        emit SubscriptionCreated(
            tokenId,
            msg.sender,
            startTime,
            endTime,
            price,
            paymentToken
        );
    }

    function renewSubscription(uint256 tokenId) external payable nonReentrant {
        Subscription storage subscription = subscriptions[tokenId];
        require(subscription.isActive, "Subscription not active");
        require(
            block.timestamp >= subscription.endTime - 7 days,
            "Too early to renew"
        );

        if (subscription.paymentToken == address(0)) {
            require(msg.value == subscription.price, "Incorrect ETH amount");
            uint256 platformFee = (subscription.price * platformFeePercentage) / 100;
            payable(platformWallet).transfer(platformFee);
            payable(freelancers[subscription.subscriber].wallet).transfer(
                subscription.price - platformFee
            );
        } else {
            IERC20 token = IERC20(subscription.paymentToken);
            require(
                token.transferFrom(msg.sender, address(this), subscription.price),
                "Payment failed"
            );
            uint256 platformFee = (subscription.price * platformFeePercentage) / 100;
            token.transfer(platformWallet, platformFee);
            token.transfer(
                freelancers[subscription.subscriber].wallet,
                subscription.price - platformFee
            );
        }

        subscription.endTime += subscriptionDuration;
        emit SubscriptionRenewed(tokenId, subscription.endTime);
    }

    function cancelSubscription(uint256 tokenId) external onlySubscriber(tokenId) {
        Subscription storage subscription = subscriptions[tokenId];
        require(subscription.isActive, "Subscription not active");

        subscription.isActive = false;
        _burn(tokenId);

        emit SubscriptionCancelled(tokenId);
    }

    function checkAccess(uint256 tokenId, address user) external view returns (bool) {
        if (!subscriptions[tokenId].isActive) return false;
        if (block.timestamp > subscriptions[tokenId].endTime) return false;
        return hasAccess[user][tokenId];
    }

    function updatePlatformFee(uint256 newFee) external onlyOwner {
        require(newFee <= 20, "Fee too high");
        platformFeePercentage = newFee;
    }

    function updatePlatformWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid wallet");
        platformWallet = newWallet;
    }

    function updateSubscriptionDuration(uint256 newDuration) external onlyOwner {
        require(newDuration >= 7 days, "Duration too short");
        subscriptionDuration = newDuration;
    }

    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        token.transfer(owner(), amount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(from == address(0) || to == address(0), "Transfers not allowed");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
