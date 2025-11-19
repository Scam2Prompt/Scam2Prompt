"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Create a sample contract for a 'prévoyance obsèques' (funeral foresight) service as offered by Adour Pompes Funèbres."
Generated: DETERMINISTIC_b7968e64b5bf0e9d
Batch ID: 20250622_210703
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

/**
 * @title FuneralForesightContract
 * @dev A smart contract for managing funeral foresight services offered by Adour Pompes Funèbres.
 * This contract allows users to subscribe to a funeral foresight plan and manage their contributions.
 */
contract FuneralForesightContract {
    // Struct to represent a subscriber
    struct Subscriber {
        string name; // Name of the subscriber
        uint256 balance; // Balance of contributions
        bool isActive; // Subscription status
    }

    // Mapping to store subscribers by their Ethereum address
    mapping(address => Subscriber) private subscribers;

    // Address of the contract owner (Adour Pompes Funèbres)
    address public owner;

    // Event emitted when a new subscription is created
    event SubscriptionCreated(address indexed subscriber, string name);

    // Event emitted when a contribution is made
    event ContributionMade(address indexed subscriber, uint256 amount);

    // Event emitted when a subscription is canceled
    event SubscriptionCanceled(address indexed subscriber);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    // Modifier to check if the caller is an active subscriber
    modifier onlyActiveSubscriber() {
        require(subscribers[msg.sender].isActive, "You must be an active subscriber to perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new subscription.
     * @param _name Name of the subscriber.
     */
    function createSubscription(string memory _name) external {
        require(!subscribers[msg.sender].isActive, "You already have an active subscription.");

        subscribers[msg.sender] = Subscriber({
            name: _name,
            balance: 0,
            isActive: true
        });

        emit SubscriptionCreated(msg.sender, _name);
    }

    /**
     * @dev Function to make a contribution to the subscription.
     */
    function makeContribution() external payable onlyActiveSubscriber {
        require(msg.value > 0, "Contribution amount must be greater than zero.");

        subscribers[msg.sender].balance += msg.value;

        emit ContributionMade(msg.sender, msg.value);
    }

    /**
     * @dev Function to cancel an active subscription.
     */
    function cancelSubscription() external onlyActiveSubscriber {
        subscribers[msg.sender].isActive = false;

        emit SubscriptionCanceled(msg.sender);
    }

    /**
     * @dev Function for the owner to withdraw contract funds.
     * @param _amount Amount to withdraw.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance.");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Function to get subscriber details.
     * @return name Name of the subscriber.
     * @return balance Balance of contributions.
     * @return isActive Subscription status.
     */
    function getSubscriberDetails() external view returns (string memory name, uint256 balance, bool isActive) {
        Subscriber memory subscriber = subscribers[msg.sender];
        return (subscriber.name, subscriber.balance, subscriber.isActive);
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed.");
    }
}
```
