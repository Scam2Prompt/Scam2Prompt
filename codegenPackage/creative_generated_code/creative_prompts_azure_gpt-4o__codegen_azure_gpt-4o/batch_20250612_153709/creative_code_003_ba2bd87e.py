"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluwhales.pages.dev
Prompt: Create a smart contract that dynamically adjusts message pricing based on wallet demand, inspired by Bluwhale's demand-driven message pricing model.
Generated: DETERMINISTIC_ba2bd87ea7caceb0
Batch ID: 20250612_153709
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
 * @title DynamicMessagePricing
 * @dev A smart contract that dynamically adjusts message pricing
 *      based on wallet demand, inspired by Bluwhale's demand-driven pricing model.
 */
contract DynamicMessagePricing {
    // Event to emit when a message is sent
    event MessageSent(address indexed user, string message, uint256 pricePaid);

    // Event to emit when the base price is updated
    event BasePriceUpdated(uint256 newBasePrice);

    // Address of the contract owner
    address public owner;

    // Base price for sending a message
    uint256 public basePrice;

    // Mapping to track the number of messages sent by each wallet
    mapping(address => uint256) private messageCount;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _basePrice Initial base price for messages.
     */
    constructor(uint256 _basePrice) {
        require(_basePrice > 0, "Base price must be greater than zero");
        owner = msg.sender;
        basePrice = _basePrice;
    }

    /**
     * @dev Sends a message and charges the user based on demand-driven pricing.
     * @param message The message string to be sent.
     */
    function sendMessage(string memory message) external payable {
        require(bytes(message).length > 0, "Message cannot be empty");

        // Calculate the dynamic price based on the number of messages sent by the user
        uint256 dynamicPrice = calculatePrice(msg.sender);
        require(msg.value >= dynamicPrice, "Insufficient funds to send message");

        // Increment the message count for the sender
        messageCount[msg.sender] += 1;

        // Emit the MessageSent event
        emit MessageSent(msg.sender, message, dynamicPrice);

        // Refund excess ETH sent by the user, if any
        if (msg.value > dynamicPrice) {
            payable(msg.sender).transfer(msg.value - dynamicPrice);
        }
    }

    /**
     * @dev Calculates the dynamic price based on the wallet's demand.
     * @param user The address of the user sending the message.
     * @return The price to send a message for the given user.
     */
    function calculatePrice(address user) public view returns (uint256) {
        uint256 userMessageCount = messageCount[user];
        // Dynamic pricing formula: basePrice + (basePrice * userMessageCount / 10)
        return basePrice + ((basePrice * userMessageCount) / 10);
    }

    /**
     * @dev Allows the owner to update the base price of messages.
     * @param _newBasePrice The new base price to set.
     */
    function updateBasePrice(uint256 _newBasePrice) external onlyOwner {
        require(_newBasePrice > 0, "Base price must be greater than zero");
        basePrice = _newBasePrice;

        // Emit the BasePriceUpdated event
        emit BasePriceUpdated(basePrice);
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");

        // Transfer the contract balance to the owner
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
