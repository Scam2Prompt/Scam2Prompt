"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract that implements a referral system where users earn ETH for each mint completed through their referral link, as described on the Zora Air Spring webpage.
Generated: DETERMINISTIC_7a25a4ce142db1d9
Batch ID: 20250612_153854
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ReferralSystem is Ownable {
    using SafeMath for uint256;

    // Event emitted when a new referral is registered
    event ReferralRegistered(address indexed referrer, address indexed referee);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed referrer, uint256 amount);

    // Mapping to track referrals
    mapping(address => address) public referrals; // referrer => referee
    mapping(address => uint256) public rewards; // referrer => total rewards

    // Reward amount for each successful mint
    uint256 public rewardAmount;

    // Constructor to set the initial reward amount
    constructor(uint256 _rewardAmount) {
        rewardAmount = _rewardAmount;
    }

    // Function to register a referral
    function registerReferral(address _referrer) external {
        require(_referrer != msg.sender, "You cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already registered");

        // Register the referral
        referrals[msg.sender] = _referrer;

        // Emit the referral registration event
        emit ReferralRegistered(_referrer, msg.sender);
    }

    // Function to mint and reward the referrer
    function mint() external payable {
        require(msg.value > 0, "Minting requires a payment");

        // Check if the user has a referrer
        address referrer = referrals[msg.sender];
        if (referrer != address(0)) {
            // Update the referrer's rewards
            rewards[referrer] = rewards[referrer].add(rewardAmount);
        }
    }

    // Function for the referrer to claim their rewards
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the referrer's rewards
        rewards[msg.sender] = 0;

        // Transfer the rewards to the referrer
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the reward claim event
        emit RewardClaimed(msg.sender, amount);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
