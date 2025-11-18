"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degen-claim.pages.dev
Prompt: Write a Solidity contract to track and distribute rewards to content creators based on the "Las Vegas of blockchains" concept on the Degen chain.
Generated: DETERMINISTIC_8c88c47b90864f21
Batch ID: 20250612_154809
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
 * @title RewardDistributor
 * @dev A contract to track and distribute rewards to content creators based on engagement
 */
contract RewardDistributor {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed creator, uint256 amount);

    // Mapping to track the total rewards for each content creator
    mapping(address => uint256) private rewards;

    // Mapping to track if an address is a registered content creator
    mapping(address => bool) private isCreator;

    // Owner of the contract
    address public owner;

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyCreator() {
        require(isCreator[msg.sender], "Caller is not a registered content creator");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a content creator
     * @param creator The address of the content creator to register
     */
    function registerCreator(address creator) external onlyOwner {
        require(creator != address(0), "Invalid address");
        require(!isCreator[creator], "Already registered");

        isCreator[creator] = true;
    }

    /**
     * @dev Distribute rewards to a content creator
     * @param creator The address of the content creator
     * @param amount The amount of rewards to distribute
     */
    function distributeRewards(address creator, uint256 amount) external onlyOwner {
        require(isCreator[creator], "Not a registered creator");
        require(amount > 0, "Amount must be greater than zero");

        // Update the rewards mapping
        rewards[creator] += amount;

        // Emit the rewards distributed event
        emit RewardsDistributed(creator, amount);
    }

    /**
     * @dev Claim rewards for the content creator
     */
    function claimRewards() external onlyCreator {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the creator's rewards to zero before transferring
        rewards[msg.sender] = 0;

        // Transfer the rewards to the content creator
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Allow the contract to receive ETH
     */
    receive() external payable {}

    /**
     * @dev Get the total rewards of a content creator
     * @param creator The address of the content creator
     * @return The total rewards of the content creator
     */
    function getRewards(address creator) external view returns (uint256) {
        return rewards[creator];
    }
}
```
