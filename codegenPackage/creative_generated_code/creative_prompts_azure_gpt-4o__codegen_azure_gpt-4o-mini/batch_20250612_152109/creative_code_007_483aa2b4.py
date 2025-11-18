"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Solidity smart contract for a token-based affiliate reward system, allowing users to earn rewards for referring others, as described in the $SCORP token use cases.
Generated: DETERMINISTIC_483aa2b40e13c9d9
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// AffiliateRewardSystem is a contract for a token-based affiliate reward system
contract AffiliateRewardSystem is Ownable {
    using SafeMath for uint256;

    // Token to be used for rewards
    IERC20 public rewardToken;

    // Structure to hold affiliate information
    struct Affiliate {
        address referrer;
        uint256 rewardsEarned;
    }

    // Mapping of user addresses to their affiliate data
    mapping(address => Affiliate) public affiliates;

    // Event emitted when a new referral is made
    event NewReferral(address indexed referrer, address indexed referral);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Function to register a referral
    function registerReferral(address _referrer) external {
        // Ensure the caller does not already have a referrer
        require(affiliates[msg.sender].referrer == address(0), "Already registered");

        // Set the referrer for the caller
        affiliates[msg.sender].referrer = _referrer;

        // Emit the NewReferral event
        emit NewReferral(_referrer, msg.sender);
    }

    // Function to reward referrer and referral
    function rewardReferral(address _referral) external onlyOwner {
        Affiliate storage referralAffiliate = affiliates[_referral];
        
        // Ensure the referral has a referrer
        require(referralAffiliate.referrer != address(0), "No referrer found");

        // Define the reward amount (can be adjusted)
        uint256 rewardAmount = 100 * 10 ** 18; // Example: 100 tokens

        // Transfer the reward tokens to the referrer
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        
        // Update rewards for both referrer and referral
        referralAffiliate.rewardsEarned += rewardAmount;
        affiliates[referralAffiliate.referrer].rewardsEarned += rewardAmount;

        // Transfer tokens to the referrer
        rewardToken.transfer(referralAffiliate.referrer, rewardAmount);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(referralAffiliate.referrer, rewardAmount);
    }

    // Function for users to claim their earned rewards
    function claimRewards() external {
        Affiliate storage affiliate = affiliates[msg.sender];

        // Check if user has any rewards to claim
        uint256 amount = affiliate.rewardsEarned;
        require(amount > 0, "No rewards to claim");

        // Reset rewards after claiming
        affiliate.rewardsEarned = 0;

        // Ensure the contract has enough tokens for the claim
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the reward tokens to the user
        rewardToken.transfer(msg.sender, amount);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        rewardToken.transfer(msg.sender, amount);
    }
}
```
