"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Create a tutorial for using Moxie’s smart contracts to reward downstream influence and organic actions by Farcaster members.
Generated: DETERMINISTIC_ac2ba6c4d8f16ec0
Batch ID: 20250612_151027
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
 * @title MoxieRewardContract
 * @dev A smart contract to reward Farcaster members for downstream influence and organic actions
 */
contract MoxieRewardContract {
    // Address of the contract owner
    address public owner;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed recipient, uint256 rewardAmount);

    // Mapping to store member influence scores
    mapping(address => uint256) public influenceScores;

    // Mapping to store organic actions completed by members
    mapping(address => uint256) public organicActions;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize contract and set the owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update member influence scores (owner-only function)
     * @param member Address of the Farcaster member
     * @param score New influence score for the member
     */
    function updateInfluenceScore(address member, uint256 score) external onlyOwner {
        require(member != address(0), "Invalid member address");
        influenceScores[member] = score;
    }

    /**
     * @dev Function to record organic actions of members (owner-only function)
     * @param member Address of the Farcaster member
     * @param actions Number of organic actions completed
     */
    function recordOrganicActions(address member, uint256 actions) external onlyOwner {
        require(member != address(0), "Invalid member address");
        organicActions[member] += actions;
    }

    /**
     * @dev Function to calculate reward based on influence score and organic actions
     * @param member Address of the Farcaster member
     * @return Reward amount calculated
     */
    function calculateReward(address member) public view returns (uint256) {
        require(member != address(0), "Invalid member address");
        uint256 score = influenceScores[member];
        uint256 actions = organicActions[member];
        // Example reward formula: 10 tokens per influence score + 5 tokens per organic action
        return (score * 10) + (actions * 5);
    }

    /**
     * @dev Function to distribute reward to a Farcaster member
     * @param member Address of the Farcaster member
     */
    function distributeReward(address member) external onlyOwner {
        require(member != address(0), "Invalid member address");
        uint256 rewardAmount = calculateReward(member);
        require(rewardAmount > 0, "No reward calculated");

        // Transfer the reward (assumes the contract has sufficient balance)
        (bool success, ) = member.call{value: rewardAmount}("");
        require(success, "Reward distribution failed");

        // Emit an event to notify reward distribution
        emit RewardDistributed(member, rewardAmount);

        // Reset member's scores and actions after reward distribution
        influenceScores[member] = 0;
        organicActions[member] = 0;
    }

    /**
     * @dev Function to deposit ether into the contract (payable)
     */
    function depositFunds() external payable {
        require(msg.value > 0, "No funds deposited");
    }

    /**
     * @dev Function to withdraw all ether from the contract (owner-only function)
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract's Ether balance
     * @return Contract's Ether balance
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
