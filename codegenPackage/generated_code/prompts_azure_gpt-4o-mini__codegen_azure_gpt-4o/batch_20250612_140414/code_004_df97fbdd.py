"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.nfts2.me
Prompt: How can I promote an NFT collection effectively while integrating a referral program that rewards users with ETH on the Arbitrum blockchain?
Generated: DETERMINISTIC_df97fbdd0ee0943a
Batch ID: 20250612_140414
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
 * @title NFTCollectionReferral
 * @dev A smart contract to promote an NFT collection with a referral program
 *      that rewards users with ETH on the Arbitrum blockchain.
 */
contract NFTCollectionReferral {
    // Owner of the contract
    address public owner;

    // Mapping to store referral balances
    mapping(address => uint256) public referralBalances;

    // Event emitted when a referral reward is distributed
    event ReferralRewardDistributed(address indexed referrer, uint256 amount);

    // Event emitted when the owner withdraws funds
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to promote an NFT collection and distribute referral rewards.
     * @param referrer The address of the referrer.
     */
    function promoteNFTCollection(address referrer) external payable {
        require(msg.value > 0, "ETH must be sent to promote the collection");
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "Self-referral is not allowed");

        // Calculate referral reward (e.g., 10% of the sent ETH)
        uint256 referralReward = (msg.value * 10) / 100;

        // Update the referrer's balance
        referralBalances[referrer] += referralReward;

        // Emit an event for the referral reward distribution
        emit ReferralRewardDistributed(referrer, referralReward);
    }

    /**
     * @dev Function for referrers to withdraw their accumulated rewards.
     */
    function withdrawReferralRewards() external {
        uint256 reward = referralBalances[msg.sender];
        require(reward > 0, "No rewards available for withdrawal");

        // Reset the referrer's balance before transferring to prevent reentrancy attacks
        referralBalances[msg.sender] = 0;

        // Transfer the reward to the referrer
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Function for the owner to withdraw contract funds.
     */
    function withdrawContractFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        // Transfer the contract balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH transfer failed");

        // Emit an event for the funds withdrawal
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract's current balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
