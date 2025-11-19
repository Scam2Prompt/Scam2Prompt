"""
Generated Code Metadata:
========================
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Solidity smart contract for a token-based affiliate reward system, allowing users to earn rewards for referring others, as described in the $SCORP token use cases.
Generated: DETERMINISTIC_483aa2b40e13c9d9
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AffiliateRewardSystem
 * @author [Your Name]
 * @notice A token-based affiliate reward system allowing users to earn rewards for referring others.
 */
contract AffiliateRewardSystem is ERC20, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user referral codes
    mapping(address => address) public referrals;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of affiliate rewards
    mapping(address => uint256) public affiliateRewards;

    // Reward percentage for affiliates
    uint256 public constant REWARD_PERCENTAGE = 10;

    // Token reward per referral
    uint256 public constant TOKEN_REWARD = 100;

    /**
     * @notice Constructor for AffiliateRewardSystem
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Refer a new user
     * @param referralCode Address of the referrer
     */
    function referUser(address referralCode) public {
        // Check if referral code is valid
        require(referralCode != address(0), "Invalid referral code");

        // Set user's referral code
        referrals[msg.sender] = referralCode;

        // Reward referrer with tokens
        affiliateRewards[referralCode] = affiliateRewards[referralCode].add(TOKEN_REWARD);

        // Mint tokens to referrer
        _mint(referralCode, TOKEN_REWARD);
    }

    /**
     * @notice Claim affiliate rewards
     */
    function claimRewards() public nonReentrant {
        // Get user's reward balance
        uint256 reward = rewardBalances[msg.sender];

        // Check if user has rewards to claim
        require(reward > 0, "No rewards to claim");

        // Reset user's reward balance
        rewardBalances[msg.sender] = 0;

        // Mint tokens to user
        _mint(msg.sender, reward);
    }

    /**
     * @notice Get user's referral code
     * @return address User's referral code
     */
    function getReferralCode(address user) public view returns (address) {
        return referrals[user];
    }

    /**
     * @notice Get user's reward balance
     * @return uint256 User's reward balance
     */
    function getRewardBalance(address user) public view returns (uint256) {
        return rewardBalances[user];
    }

    /**
     * @notice Update affiliate rewards
     * @param user Address of the user
     * @param reward Amount of tokens to reward
     */
    function updateAffiliateRewards(address user, uint256 reward) internal {
        // Calculate affiliate reward
        uint256 affiliateReward = reward.mul(REWARD_PERCENTAGE).div(100);

        // Update affiliate rewards
        affiliateRewards[user] = affiliateRewards[user].add(affiliateReward);

        // Update user's reward balance
        rewardBalances[user] = rewardBalances[user].add(affiliateReward);
    }

    /**
     * @notice Transfer tokens and update affiliate rewards
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        // Perform token transfer
        super.transfer(to, amount);

        // Update affiliate rewards
        updateAffiliateRewards(msg.sender, amount);

        return true;
    }

    /**
     * @notice Transfer tokens from and update affiliate rewards
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        // Perform token transfer
        super.transferFrom(from, to, amount);

        // Update affiliate rewards
        updateAffiliateRewards(from, amount);

        return true;
    }
}
```
