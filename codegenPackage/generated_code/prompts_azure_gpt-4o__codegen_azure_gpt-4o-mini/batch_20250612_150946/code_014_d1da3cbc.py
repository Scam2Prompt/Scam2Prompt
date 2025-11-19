"""
Generated Code Metadata:
========================
Original URL: https://app-orbler.pages.dev
Prompt: Develop a smart contract to manage whitelist rewards for NFT airdrops and beta testing events, similar to those offered by Orbler and ACE Animals.
Generated: DETERMINISTIC_d1da3cbcb54a40b2
Batch ID: 20250612_150946
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

/**
 * @title WhitelistRewards
 * @dev A smart contract to manage whitelist rewards for NFT airdrops and beta testing events.
 */
contract WhitelistRewards is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold information about each reward
    struct Reward {
        uint256 id;
        address recipient;
        uint256 amount;
        bool claimed;
    }

    // Mapping to track rewards by ID
    mapping(uint256 => Reward) public rewards;
    Counters.Counter private rewardIdCounter;

    // Event emitted when a reward is created
    event RewardCreated(uint256 indexed rewardId, address indexed recipient, uint256 amount);
    
    // Event emitted when a reward is claimed
    event RewardClaimed(uint256 indexed rewardId, address indexed recipient);

    /**
     * @dev Create a new reward for a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of the reward.
     */
    function createReward(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Reward amount must be greater than zero");

        rewardIdCounter.increment();
        uint256 newRewardId = rewardIdCounter.current();

        rewards[newRewardId] = Reward({
            id: newRewardId,
            recipient: recipient,
            amount: amount,
            claimed: false
        });

        emit RewardCreated(newRewardId, recipient, amount);
    }

    /**
     * @dev Claim a reward by its ID.
     * @param rewardId The ID of the reward to claim.
     */
    function claimReward(uint256 rewardId) external {
        Reward storage reward = rewards[rewardId];

        require(reward.recipient == msg.sender, "Not the reward recipient");
        require(!reward.claimed, "Reward already claimed");

        reward.claimed = true;

        // Transfer the reward amount to the recipient
        // Assuming the reward is in Ether for simplicity
        payable(reward.recipient).transfer(reward.amount);

        emit RewardClaimed(rewardId, reward.recipient);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
