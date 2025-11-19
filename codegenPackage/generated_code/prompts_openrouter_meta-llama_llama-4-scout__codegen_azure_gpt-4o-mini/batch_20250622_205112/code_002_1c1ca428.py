"""
Generated Code Metadata:
========================
Original URL: https://holdstation.pages.dev
Prompt: Generate a code snippet in Solidity to implement a simple token subscription model with a hard cap and hard cap per user, similar to the one described on the Holdstation launchpad.
Generated: DETERMINISTIC_1c1ca4282edff742
Batch ID: 20250622_205112
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

/**
 * @title TokenSubscription
 * @dev A simple token subscription model with a hard cap and individual user cap.
 */
contract TokenSubscription is Ownable {
    // The token being used for subscriptions
    IERC20 public subscriptionToken;

    // Total hard cap for the subscription
    uint256 public totalHardCap;

    // Hard cap per user
    uint256 public userHardCap;

    // Total amount subscribed
    uint256 public totalSubscribed;

    // Mapping to track user subscriptions
    mapping(address => uint256) public userSubscriptions;

    // Event emitted when a user subscribes
    event Subscribed(address indexed user, uint256 amount);

    // Event emitted when a subscription is canceled
    event Canceled(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token and caps.
     * @param _subscriptionToken Address of the subscription token
     * @param _totalHardCap Total hard cap for the subscription
     * @param _userHardCap Hard cap per user
     */
    constructor(IERC20 _subscriptionToken, uint256 _totalHardCap, uint256 _userHardCap) {
        require(_totalHardCap > 0, "Total hard cap must be greater than zero");
        require(_userHardCap > 0, "User hard cap must be greater than zero");
        
        subscriptionToken = _subscriptionToken;
        totalHardCap = _totalHardCap;
        userHardCap = _userHardCap;
    }

    /**
     * @dev Subscribe to the token model.
     * @param amount Amount of tokens to subscribe
     */
    function subscribe(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(totalSubscribed + amount <= totalHardCap, "Total hard cap exceeded");
        require(userSubscriptions[msg.sender] + amount <= userHardCap, "User hard cap exceeded");

        // Update user and total subscriptions
        userSubscriptions[msg.sender] += amount;
        totalSubscribed += amount;

        // Transfer tokens from user to this contract
        require(subscriptionToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Subscribed(msg.sender, amount);
    }

    /**
     * @dev Cancel subscription and withdraw tokens.
     * @param amount Amount of tokens to withdraw
     */
    function cancelSubscription(uint256 amount) external {
        require(userSubscriptions[msg.sender] >= amount, "Insufficient subscription amount");

        // Update user subscriptions
        userSubscriptions[msg.sender] -= amount;
        totalSubscribed -= amount;

        // Transfer tokens back to the user
        require(subscriptionToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Canceled(msg.sender, amount);
    }

    /**
     * @dev Withdraw remaining tokens from the contract (only owner).
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = subscriptionToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(subscriptionToken.transfer(msg.sender, balance), "Token transfer failed");
    }
}
```
