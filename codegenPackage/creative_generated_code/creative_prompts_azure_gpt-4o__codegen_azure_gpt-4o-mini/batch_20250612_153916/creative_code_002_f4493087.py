"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Develop a smart contract in Solidity that tracks referral fees for Unichain-Rooster NFT mints and automatically distributes rewards to the specified wallet address.
Generated: DETERMINISTIC_f4493087debe3ca9
Batch ID: 20250612_153916
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ReferralReward
 * @dev A smart contract for tracking referral fees and distributing rewards for NFT mints.
 */
contract ReferralReward is Ownable {
    // Event emitted when a referral reward is distributed
    event RewardDistributed(address indexed referrer, uint256 amount);

    // ERC20 token used for reward distribution
    IERC20 public rewardToken;

    // Mapping to store referral earnings
    mapping(address => uint256) public referralEarnings;

    // Mapping to track if an address has already referred
    mapping(address => bool) public hasReferred;

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Allows users to mint an NFT and track referrals.
     * @param referrer The address of the referrer.
     */
    function mintNFT(address referrer) external {
        require(referrer != msg.sender, "Cannot refer yourself");
        require(!hasReferred[referrer], "Referrer has already been used");

        // Logic to mint the NFT would go here
        // Example: UnichainRoosterNFT.mint(msg.sender);

        // Assign referral if valid
        if (referrer != address(0)) {
            hasReferred[referrer] = true;
            uint256 reward = calculateReward();
            referralEarnings[referrer] += reward;

            // Emit the reward distribution event
            emit RewardDistributed(referrer, reward);
        }
    }

    /**
     * @dev Calculates the reward based on some criteria.
     * @return The amount of reward to be distributed.
     */
    function calculateReward() internal pure returns (uint256) {
        // Implement actual reward logic here; for example:
        return 100 * 10 ** 18;  // Example reward amount in smallest units
    }

    /**
     * @dev Allows the owner to withdraw accumulated rewards.
     */
    function withdrawRewards() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No rewards to withdraw");

        // Transfer the rewards to the owner
        require(rewardToken.transfer(owner(), balance), "Transfer failed");
    }

    /**
     * @dev Allows the owner to update the reward token address.
     * @param newToken The new reward token address.
     */
    function updateRewardToken(IERC20 newToken) external onlyOwner {
        require(address(newToken) != address(0), "Invalid token address");
        rewardToken = newToken;
    }

    /**
     * @dev Allows referrers to check their earnings.
     * @return The earnings of the caller.
     */
    function checkEarnings() external view returns (uint256) {
        return referralEarnings[msg.sender];
    }
}
```
