"""
Generated Code Metadata:
========================
Original URL: https://starsarena.trade
Prompt: Provide an example of a smart contract that could be used for monetization in a SocialFi application like the one described on starsarena.trade.
Generated: DETERMINISTIC_5e2feb1f5efb1c98
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SocialFi Monetization Contract
 * @dev Implements monetization features for a SocialFi platform including:
 * - Content monetization
 * - Tipping
 * - Subscription model
 * - Revenue sharing
 */
contract SocialFiMonetization is Ownable, ReentrancyGuard {
    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercentage = 5;
    
    // Supported payment token (can be native token or ERC20)
    IERC20 public paymentToken;
    
    // User balances
    mapping(address => uint256) public userBalances;
    
    // Content creators and their content
    struct Content {
        uint256 price;
        address creator;
        bool isActive;
    }
    
    mapping(uint256 => Content) public contents;
    uint256 public contentCount;
    
    // Subscriptions
    struct Subscription {
        uint256 pricePerMonth;
        uint256 lastPaymentDate;
    }
    
    mapping(address => Subscription) public creatorSubscriptions;
    mapping(address => mapping(address => uint256)) public subscriberExpiry;
    
    // Events
    event ContentCreated(uint256 indexed contentId, address indexed creator, uint256 price);
    event ContentPurchased(uint256 indexed contentId, address indexed buyer, uint256 price);
    event TipSent(address indexed from, address indexed to, uint256 amount);
    event SubscriptionCreated(address indexed creator, uint256 pricePerMonth);
    event Subscribed(address indexed subscriber, address indexed creator, uint256 expiryDate);
    event Withdrawn(address indexed user, uint256 amount);
    event PlatformFeeUpdated(uint256 newFee);
    
    constructor(address _paymentToken) {
        paymentToken = IERC20(_paymentToken);
    }
    
    /**
     * @dev Create a new paid content
     * @param price Price to access this content
     */
    function createContent(uint256 price) external {
        contentCount++;
        contents[contentCount] = Content({
            price: price,
            creator: msg.sender,
            isActive: true
        });
        
        emit ContentCreated(contentCount, msg.sender, price);
    }
    
    /**
     * @dev Purchase access to content
     * @param contentId ID of the content to purchase
     */
    function purchaseContent(uint256 contentId) external nonReentrant {
        require(contents[contentId].isActive, "Content not available");
        require(contents[contentId].creator != msg.sender, "Cannot purchase your own content");
        
        uint256 price = contents[contentId].price;
        uint256 platformFee = (price * platformFeePercentage) / 100;
        uint256 creatorAmount = price - platformFee;
        
        // Transfer payment
        require(
            paymentToken.transferFrom(msg.sender, address(this), price),
            "Payment failed"
        );
        
        // Distribute funds
        userBalances[contents[contentId].creator] += creatorAmount;
        userBalances[owner()] += platformFee;
        
        emit ContentPurchased(contentId, msg.sender, price);
    }
    
    /**
     * @dev Send a tip to a creator
     * @param creator Address of the creator to tip
     * @param amount Amount to tip
     */
    function sendTip(address creator, uint256 amount) external nonReentrant {
        require(creator != address(0), "Invalid creator address");
        require(creator != msg.sender, "Cannot tip yourself");
        require(amount > 0, "Amount must be positive");
        
        uint256 platformFee = (amount * platformFeePercentage) / 100;
        uint256 creatorAmount = amount - platformFee;
        
        // Transfer payment
        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Payment failed"
        );
        
        // Distribute funds
        userBalances[creator] += creatorAmount;
        userBalances[owner()] += platformFee;
        
        emit TipSent(msg.sender, creator, amount);
    }
    
    /**
     * @dev Create a subscription plan
     * @param pricePerMonth Price per month in payment tokens
     */
    function createSubscriptionPlan(uint256 pricePerMonth) external {
        require(pricePerMonth > 0, "Price must be positive");
        
        creatorSubscriptions[msg.sender] = Subscription({
            pricePerMonth: pricePerMonth,
            lastPaymentDate: 0
        });
        
        emit SubscriptionCreated(msg.sender, pricePerMonth);
    }
    
    /**
     * @dev Subscribe to a creator
     * @param creator Address of the creator to subscribe to
     * @param months Number of months to subscribe for
     */
    function subscribe(address creator, uint256 months) external nonReentrant {
        require(creatorSubscriptions[creator].pricePerMonth > 0, "Creator has no subscription plan");
        require(months > 0, "Must subscribe for at least 1 month");
        
        uint256 totalAmount = creatorSubscriptions[creator].pricePerMonth * months;
        uint256 platformFee = (totalAmount * platformFeePercentage) / 100;
        uint256 creatorAmount = totalAmount - platformFee;
        
        // Transfer payment
        require(
            paymentToken.transferFrom(msg.sender, address(this), totalAmount),
            "Payment failed"
        );
        
        // Update subscription
        uint256 currentExpiry = subscriberExpiry[msg.sender][creator];
        uint256 newExpiry = currentExpiry > block.timestamp ? 
            currentExpiry + (months * 30 days) : 
            block.timestamp + (months * 30 days);
            
        subscriberExpiry[msg.sender][creator] = newExpiry;
        
        // Distribute funds
        userBalances[creator] += creatorAmount;
        userBalances[owner()] += platformFee;
        
        emit Subscribed(msg.sender, creator, newExpiry);
    }
    
    /**
     * @dev Withdraw accumulated balance
     */
    function withdraw() external nonReentrant {
        uint256 amount = userBalances[msg.sender];
        require(amount > 0, "No balance to withdraw");
        
        userBalances[msg.sender] = 0;
        
        require(
            paymentToken.transfer(msg.sender, amount),
            "Withdrawal failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Update platform fee percentage (owner only)
     * @param newFee New fee percentage (1 = 1%)
     */
    function setPlatformFeePercentage(uint256 newFee) external onlyOwner {
        require(newFee <= 20, "Fee cannot exceed 20%");
        platformFeePercentage = newFee;
        emit PlatformFeeUpdated(newFee);
    }
    
    /**
     * @dev Check if a user is subscribed to a creator
     * @param subscriber Subscriber address
     * @param creator Creator address
     * @return bool True if subscription is active
     */
    function isSubscribed(address subscriber, address creator) external view returns (bool) {
        return subscriberExpiry[subscriber][creator] > block.timestamp;
    }
}
```
