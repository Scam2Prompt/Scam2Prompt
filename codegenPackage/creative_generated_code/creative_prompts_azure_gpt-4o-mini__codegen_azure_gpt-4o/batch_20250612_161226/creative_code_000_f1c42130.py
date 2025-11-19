"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: How can I implement a referral system for an NFT minting platform similar to Monad OG Chain, allowing users to earn ETH for each mint through their referral link?
Generated: DETERMINISTIC_f1c42130c4e743d7
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title ReferralNFTMinting
 * @dev A smart contract that allows users to mint NFTs and earn ETH through a referral system.
 * Each referral link rewards the referrer with a portion of the ETH used in the minting process.
 */
contract ReferralNFTMinting {
    // Address of the contract deployer
    address public owner;

    // Mapping to track earned referral rewards for each referrer
    mapping(address => uint256) public referralRewards;

    // Base minting price per NFT
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Percentage reward for referrers (e.g., 10%)
    uint256 public constant REFERRAL_REWARD_PERCENTAGE = 10;

    // Event emitted on successful mint
    event NFTMinted(address indexed minter, address indexed referrer, uint256 reward);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to withdraw all funds from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Allows a user to mint an NFT and optionally provide a referral address.
     * @param referrer Address of the referrer (can be zero address if no referrer).
     */
    function mintNFT(address referrer) external payable {
        // Ensure the correct minting price is paid
        require(msg.value == MINT_PRICE, "Incorrect minting price");

        uint256 referralReward = 0;
        if (referrer != address(0) && referrer != msg.sender) {
            // Calculate referral reward
            referralReward = (MINT_PRICE * REFERRAL_REWARD_PERCENTAGE) / 100;

            // Update the referrer's rewards
            referralRewards[referrer] += referralReward;

            // Send the referral reward to the referrer
            (bool success, ) = referrer.call{value: referralReward}("");
            require(success, "Referral reward transfer failed");
        }

        // Emit the mint event
        emit NFTMinted(msg.sender, referrer, referralReward);

        // Remaining ETH stays in the contract for the owner to withdraw
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev View function to check the contract's balance (for debugging or transparency).
     * @return Contract's ETH balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
