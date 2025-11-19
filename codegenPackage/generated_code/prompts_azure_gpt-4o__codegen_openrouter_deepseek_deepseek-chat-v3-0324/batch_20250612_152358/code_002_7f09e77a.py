"""
Generated Code Metadata:
========================
Original URL: https://zeek.social
Prompt: Generate a smart contract in Solidity for managing referral codes and rewards distribution, inspired by Zeek Network's SocialFi model.
Generated: DETERMINISTIC_7f09e77a92dfcac4
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ReferralManager is Ownable, ReentrancyGuard {
    // Struct to store referral information
    struct ReferralInfo {
        address referrer;
        uint256 totalReferrals;
        uint256 totalRewards;
        uint256 pendingRewards;
        uint256 claimedRewards;
    }

    // Struct to store reward tier configuration
    struct RewardTier {
        uint256 minStake;
        uint256 rewardPercentage;
    }

    // Mapping from user address to referral info
    mapping(address => ReferralInfo) public referrals;

    // Mapping from referral code to address
    mapping(string => address) public referralCodes;

    // Mapping from address to referral code
    mapping(address => string) public userCodes;

    // Reward tiers configuration
    RewardTier[] public rewardTiers;

    // The token used for rewards
    IERC20 public rewardToken;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Events
    event ReferralCodeGenerated(address indexed user, string code);
    event ReferralRegistered(address indexed referrer, address indexed referee, string code);
    event RewardsDistributed(address indexed referrer, address indexed referee, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardTierAdded(uint256 minStake, uint256 rewardPercentage);
    event RewardTokenUpdated(address newToken);

    // Modifier to check if referral code exists
    modifier validReferralCode(string memory code) {
        require(referralCodes[code] != address(0), "Invalid referral code");
        _;
    }

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);

        // Initialize with default tiers
        rewardTiers.push(RewardTier({minStake: 100 ether, rewardPercentage: 10})); // 10% for 100 tokens
        rewardTiers.push(RewardTier({minStake: 500 ether, rewardPercentage: 15})); // 15% for 500 tokens
        rewardTiers.push(RewardTier({minStake: 1000 ether, rewardPercentage: 20})); // 20% for 1000 tokens
    }

    /**
     * @dev Generate a unique referral code for the caller
     * @param code The desired referral code (must be unique)
     */
    function generateReferralCode(string memory code) external {
        require(bytes(code).length > 0, "Code cannot be empty");
        require(referralCodes[code] == address(0), "Code already exists");
        require(bytes(userCodes[msg.sender]).length == 0, "User already has a code");

        referralCodes[code] = msg.sender;
        userCodes[msg.sender] = code;

        emit ReferralCodeGenerated(msg.sender, code);
    }

    /**
     * @dev Register a referral using a valid code
     * @param code The referral code to use
     */
    function registerReferral(string memory code) external validReferralCode(code) {
        address referrer = referralCodes[code];
        require(referrer != msg.sender, "Cannot refer yourself");

        ReferralInfo storage referrerInfo = referrals[referrer];
        ReferralInfo storage refereeInfo = referrals[msg.sender];

        require(refereeInfo.referrer == address(0), "Already registered with a referrer");

        refereeInfo.referrer = referrer;
        referrerInfo.totalReferrals += 1;

        emit ReferralRegistered(referrer, msg.sender, code);
    }

    /**
     * @dev Distribute rewards based on staking amount and tier
     * @param referee The address of the user who staked
     * @param amount The amount staked
     */
    function distributeRewards(address referee, uint256 amount) external onlyOwner nonReentrant {
        ReferralInfo storage refereeInfo = referrals[referee];
        address referrer = refereeInfo.referrer;

        if (referrer == address(0)) {
            return; // No referrer, no rewards
        }

        uint256 rewardPercentage = getRewardPercentage(amount);
        if (rewardPercentage == 0) {
            return; // No reward for this tier
        }

        uint256 rewardAmount = (amount * rewardPercentage) / 100;
        if (rewardAmount == 0) {
            return; // Reward too small
        }

        ReferralInfo storage referrerInfo = referrals[referrer];
        referrerInfo.totalRewards += rewardAmount;
        referrerInfo.pendingRewards += rewardAmount;
        totalRewardsDistributed += rewardAmount;

        emit RewardsDistributed(referrer, referee, rewardAmount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        ReferralInfo storage userInfo = referrals[msg.sender];
        uint256 pending = userInfo.pendingRewards;
        require(pending > 0, "No rewards to claim");

        userInfo.pendingRewards = 0;
        userInfo.claimedRewards += pending;

        require(rewardToken.transfer(msg.sender, pending), "Token transfer failed");

        emit RewardsClaimed(msg.sender, pending);
    }

    /**
     * @dev Add a new reward tier
     * @param minStake Minimum stake amount for this tier
     * @param rewardPercentage Reward percentage for this tier
     */
    function addRewardTier(uint256 minStake, uint256 rewardPercentage) external onlyOwner {
        require(rewardPercentage > 0, "Percentage must be positive");
        rewardTiers.push(RewardTier({minStake: minStake, rewardPercentage: rewardPercentage}));
        emit RewardTierAdded(minStake, rewardPercentage);
    }

    /**
     * @dev Update the reward token address
     * @param newToken Address of the new reward token
     */
    function updateRewardToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        rewardToken = IERC20(newToken);
        emit RewardTokenUpdated(newToken);
    }

    /**
     * @dev Get the reward percentage for a given stake amount
     * @param amount The staked amount
     * @return The reward percentage (0 if no tier matches)
     */
    function getRewardPercentage(uint256 amount) public view returns (uint256) {
        uint256 highestTier = 0;
        for (uint256 i = 0; i < rewardTiers.length; i++) {
            if (amount >= rewardTiers[i].minStake && rewardTiers[i].rewardPercentage > highestTier) {
                highestTier = rewardTiers[i].rewardPercentage;
            }
        }
        return highestTier;
    }

    /**
     * @dev Get the number of reward tiers
     * @return The number of tiers
     */
    function getRewardTierCount() external view returns (uint256) {
        return rewardTiers.length;
    }

    /**
     * @dev Emergency withdraw tokens from contract
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
