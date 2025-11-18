"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiger-b75.pages.dev
Prompt: Provide an example of how to implement a reward-claiming mechanism in a decentralized application (Dapp) that supports multiple wallets, inspired by the BABY TIGER KING synchronizer feature.
Generated: DETERMINISTIC_8f95b8b74723b4c5
Batch ID: 20250612_152600
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
 * @title RewardClaimingMechanism
 * @dev A smart contract that allows users with multiple wallets to claim rewards in a decentralized application (DApp).
 */
contract RewardClaimingMechanism {
    // Event emitted when rewards are claimed.
    event RewardClaimed(address indexed walletAddress, uint256 amount);

    // Event emitted when a wallet is added to the reward system.
    event WalletAdded(address indexed walletAddress);

    // Event emitted when a wallet is removed from the reward system.
    event WalletRemoved(address indexed walletAddress);

    // Mapping to track registered wallets and their reward balances.
    mapping(address => uint256) private walletRewards;

    // Owner of the contract (admin privileges).
    address private owner;

    // Modifier to restrict access to owner-only functions.
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Modifier to ensure the wallet is registered.
    modifier onlyRegisteredWallet(address wallet) {
        require(walletRewards[wallet] > 0, "Wallet is not registered in the reward system.");
        _;
    }

    // Constructor to set the contract owner.
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a wallet to the reward system with an initial reward.
     * @param wallet The wallet address to be added.
     * @param initialReward The initial reward amount for the wallet.
     */
    function addWallet(address wallet, uint256 initialReward) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address.");
        require(walletRewards[wallet] == 0, "Wallet is already registered.");

        walletRewards[wallet] = initialReward;
        emit WalletAdded(wallet);
    }

    /**
     * @dev Remove a wallet from the reward system.
     * @param wallet The wallet address to be removed.
     */
    function removeWallet(address wallet) external onlyOwner {
        require(walletRewards[wallet] > 0, "Wallet is not registered.");

        delete walletRewards[wallet];
        emit WalletRemoved(wallet);
    }

    /**
     * @dev Claim rewards for a registered wallet.
     * @notice Wallets can claim their full reward balance.
     */
    function claimReward() external onlyRegisteredWallet(msg.sender) {
        uint256 rewardAmount = walletRewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim.");

        // Reset wallet rewards to zero before transferring to prevent re-entrancy attack.
        walletRewards[msg.sender] = 0;

        // Transfer the reward to the wallet (assuming rewards are in native currency).
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed.");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Check the reward balance of a registered wallet.
     * @param wallet The wallet address to check.
     * @return The reward balance of the wallet.
     */
    function checkRewardBalance(address wallet) external view returns (uint256) {
        return walletRewards[wallet];
    }

    /**
     * @dev Fallback function to receive Ether for funding rewards.
     */
    receive() external payable {}

    /**
     * @dev Withdraw Ether from the contract (owner-only function).
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance.");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdraw failed.");
    }
}
```
