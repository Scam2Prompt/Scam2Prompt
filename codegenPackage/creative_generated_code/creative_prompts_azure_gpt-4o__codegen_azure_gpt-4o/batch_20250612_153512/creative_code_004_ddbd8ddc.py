"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destranetwork.pages.dev
Prompt: Provide an example of integrating Destra's web hosting service into a decentralized application using smart contracts.
Generated: DETERMINISTIC_ddbd8ddc39a39c39
Batch ID: 20250612_153512
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
 * @title Destra Web Hosting Integration Contract
 * @dev This smart contract facilitates payments and integration with Destra's web hosting service
 * for decentralized applications (dApps). It allows users to subscribe to hosting services
 * using Ethereum and integrates with Destra's API via events.
 */
contract DestraHostingIntegration {
    // Address of the Destra service provider
    address payable public destraProvider;

    // Mapping to track subscriptions (userAddress => subscriptionExpiryTimestamp)
    mapping(address => uint256) public subscriptions;

    // Event to notify the Destra service of a new subscription
    event NewSubscription(address indexed user, uint256 expiryTimestamp);

    // Event to notify users of a successful subscription
    event SubscriptionSuccessful(address indexed user, uint256 expiryTimestamp);

    // Price per month for hosting services (in wei)
    uint256 public pricePerMonth;

    /**
     * @dev Sets the Destra provider address and hosting price.
     * @param _destraProvider Address of the Destra service provider.
     * @param _pricePerMonth Price per month for hosting services (in wei).
     */
    constructor(address payable _destraProvider, uint256 _pricePerMonth) {
        require(_destraProvider != address(0), "Invalid provider address.");
        require(_pricePerMonth > 0, "Price per month must be positive.");

        destraProvider = _destraProvider;
        pricePerMonth = _pricePerMonth;
    }

    /**
     * @dev Allows users to subscribe to Destra's hosting service by sending ETH.
     * @param months Number of months the user wants to subscribe for.
     */
    function subscribe(uint256 months) external payable {
        require(months > 0, "Subscription months must be greater than zero.");
        require(msg.value == months * pricePerMonth, "Incorrect payment amount.");

        // Calculate the new expiry timestamp for the user's subscription
        uint256 currentExpiry = subscriptions[msg.sender];
        uint256 newExpiry = block.timestamp + (months * 30 days);

        // Update subscription mapping
        if (currentExpiry > block.timestamp) {
            subscriptions[msg.sender] = currentExpiry + (months * 30 days);
        } else {
            subscriptions[msg.sender] = newExpiry;
        }

        // Transfer the payment to the Destra provider
        destraProvider.transfer(msg.value);

        // Emit event for Destra API integration
        emit NewSubscription(msg.sender, subscriptions[msg.sender]);

        // Emit event to notify the user
        emit SubscriptionSuccessful(msg.sender, subscriptions[msg.sender]);
    }

    /**
     * @dev Allows the contract owner to update the price per month for hosting services.
     * @param _pricePerMonth New price per month (in wei).
     */
    function updatePrice(uint256 _pricePerMonth) external {
        require(msg.sender == destraProvider, "Only the provider can update the price.");
        require(_pricePerMonth > 0, "Price per month must be positive.");
        pricePerMonth = _pricePerMonth;
    }

    /**
     * @dev Retrieves the subscription expiry timestamp for a given user.
     * @param user Address of the user.
     * @return Expiry timestamp of the user's subscription.
     */
    function getSubscriptionExpiry(address user) external view returns (uint256) {
        return subscriptions[user];
    }

    /**
     * @dev Modifier to restrict access to the Destra provider.
     */
    modifier onlyProvider() {
        require(msg.sender == destraProvider, "Caller is not the provider.");
        _;
    }
}
```
