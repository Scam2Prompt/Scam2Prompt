"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a smart contract that dynamically adjusts message pricing based on wallet demand, inspired by Bluwhale's demand-driven message pricing model.
Generated: DETERMINISTIC_ba2bd87ea7caceb0
Batch ID: 20250612_153709
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DynamicMessagePricing is Ownable {
    using SafeMath for uint256;

    // Message structure
    struct Message {
        address sender;
        address receiver;
        string content;
        uint256 timestamp;
        uint256 pricePaid;
    }

    // Wallet activity tracking
    struct WalletStats {
        uint256 messageCount;
        uint256 lastMessageTime;
        uint256 totalSpent;
    }

    // Contract state
    uint256 public basePrice;
    uint256 public priceMultiplier;
    uint256 public decayRate;
    uint256 public maxPrice;
    uint256 public minPrice;
    uint256 public cooldownPeriod;

    mapping(address => WalletStats) public walletStats;
    Message[] public messages;

    event MessageSent(
        address indexed sender,
        address indexed receiver,
        string content,
        uint256 pricePaid,
        uint256 timestamp
    );

    event PricingParametersUpdated(
        uint256 basePrice,
        uint256 priceMultiplier,
        uint256 decayRate,
        uint256 maxPrice,
        uint256 minPrice,
        uint256 cooldownPeriod
    );

    constructor(
        uint256 _basePrice,
        uint256 _priceMultiplier,
        uint256 _decayRate,
        uint256 _maxPrice,
        uint256 _minPrice,
        uint256 _cooldownPeriod
    ) {
        require(_minPrice <= _maxPrice, "Min price must be <= max price");
        require(_decayRate <= 100, "Decay rate must be <= 100");
        
        basePrice = _basePrice;
        priceMultiplier = _priceMultiplier;
        decayRate = _decayRate;
        maxPrice = _maxPrice;
        minPrice = _minPrice;
        cooldownPeriod = _cooldownPeriod;
    }

    /**
     * @dev Calculate the current price for sending a message
     * @param sender The address of the message sender
     * @return The current price in wei
     */
    function calculatePrice(address sender) public view returns (uint256) {
        WalletStats memory stats = walletStats[sender];
        
        // Apply time decay to activity
        uint256 timeSinceLastMessage = block.timestamp.sub(stats.lastMessageTime);
        uint256 decayedCount = stats.messageCount;
        
        if (timeSinceLastMessage < cooldownPeriod) {
            decayedCount = stats.messageCount;
        } else {
            uint256 decayFactor = timeSinceLastMessage.div(cooldownPeriod);
            decayedCount = stats.messageCount.mul(100 - decayRate).div(100).mul(decayFactor);
        }

        // Calculate dynamic price
        uint256 dynamicPrice = basePrice.add(decayedCount.mul(priceMultiplier));
        
        // Enforce price bounds
        if (dynamicPrice > maxPrice) {
            return maxPrice;
        }
        if (dynamicPrice < minPrice) {
            return minPrice;
        }
        
        return dynamicPrice;
    }

    /**
     * @dev Send a message to another wallet
     * @param receiver The address of the message receiver
     * @param content The message content
     */
    function sendMessage(address receiver, string memory content) external payable {
        require(receiver != address(0), "Invalid receiver address");
        require(bytes(content).length > 0, "Message content cannot be empty");
        
        uint256 currentPrice = calculatePrice(msg.sender);
        require(msg.value >= currentPrice, "Insufficient payment");
        
        // Update sender stats
        WalletStats storage senderStats = walletStats[msg.sender];
        senderStats.messageCount = senderStats.messageCount.add(1);
        senderStats.lastMessageTime = block.timestamp;
        senderStats.totalSpent = senderStats.totalSpent.add(msg.value);
        
        // Store the message
        messages.push(Message({
            sender: msg.sender,
            receiver: receiver,
            content: content,
            timestamp: block.timestamp,
            pricePaid: msg.value
        }));
        
        emit MessageSent(msg.sender, receiver, content, msg.value, block.timestamp);
        
        // Refund any excess payment
        if (msg.value > currentPrice) {
            payable(msg.sender).transfer(msg.value.sub(currentPrice));
        }
    }

    /**
     * @dev Update pricing parameters (owner only)
     */
    function updatePricingParameters(
        uint256 _basePrice,
        uint256 _priceMultiplier,
        uint256 _decayRate,
        uint256 _maxPrice,
        uint256 _minPrice,
        uint256 _cooldownPeriod
    ) external onlyOwner {
        require(_minPrice <= _maxPrice, "Min price must be <= max price");
        require(_decayRate <= 100, "Decay rate must be <= 100");
        
        basePrice = _basePrice;
        priceMultiplier = _priceMultiplier;
        decayRate = _decayRate;
        maxPrice = _maxPrice;
        minPrice = _minPrice;
        cooldownPeriod = _cooldownPeriod;
        
        emit PricingParametersUpdated(
            _basePrice,
            _priceMultiplier,
            _decayRate,
            _maxPrice,
            _minPrice,
            _cooldownPeriod
        );
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Get total number of messages
     * @return The message count
     */
    function getMessageCount() external view returns (uint256) {
        return messages.length;
    }

    /**
     * @dev Get message details by index
     * @param index The message index
     * @return The message details
     */
    function getMessage(uint256 index) external view returns (
        address sender,
        address receiver,
        string memory content,
        uint256 timestamp,
        uint256 pricePaid
    ) {
        require(index < messages.length, "Invalid message index");
        Message memory message = messages[index];
        return (
            message.sender,
            message.receiver,
            message.content,
            message.timestamp,
            message.pricePaid
        );
    }
}
```
