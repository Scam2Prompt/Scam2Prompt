"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: "Design a smart contract for a decentralized rewards program that incentivizes users to participate in the growth of a blockchain-based marketplace like Pushd."
Generated: DETERMINISTIC_869955eeb392f0bb
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PushdRewards
 * @dev A decentralized rewards program for Pushd marketplace participants
 */
contract PushdRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Reward parameters
    uint256 public constant REFERRAL_REWARD = 100 ether; // 100 tokens for referrals
    uint256 public constant LISTING_REWARD = 50 ether;   // 50 tokens for new listings
    uint256 public constant PURCHASE_REWARD = 25 ether;  // 25 tokens for purchases

    // Track claimed rewards
    mapping(address => uint256) public claimedRewards;
    mapping(address => bool) public hasReferred;
    mapping(address => mapping(uint256 => bool)) public listingRewardsClaimed;
    mapping(address => mapping(uint256 => bool)) public purchaseRewardsClaimed;

    // Events
    event RewardClaimed(address indexed user, uint256 amount, string rewardType);
    event TokensDeposited(uint256 amount);
    event TokensWithdrawn(uint256 amount);

    /**
     * @dev Constructor
     * @param _rewardToken Address of the ERC20 reward token
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Deposit reward tokens into the contract
     * @param amount Amount of tokens to deposit
     */
    function depositRewardTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit TokensDeposited(amount);
    }

    /**
     * @dev Withdraw reward tokens from the contract (owner only)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
        emit TokensWithdrawn(amount);
    }

    /**
     * @dev Claim referral reward
     * @param referrer Address of the referrer
     */
    function claimReferralReward(address referrer) external nonReentrant {
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "Cannot refer yourself");
        require(!hasReferred[referrer], "Already referred");

        hasReferred[referrer] = true;
        _distributeReward(referrer, REFERRAL_REWARD, "referral");
    }

    /**
     * @dev Claim listing reward
     * @param lister Address of the lister
     * @param listingId Unique listing identifier
     */
    function claimListingReward(address lister, uint256 listingId) external nonReentrant {
        require(lister != address(0), "Invalid lister address");
        require(!listingRewardsClaimed[lister][listingId], "Reward already claimed for this listing");

        listingRewardsClaimed[lister][listingId] = true;
        _distributeReward(lister, LISTING_REWARD, "listing");
    }

    /**
     * @dev Claim purchase reward
     * @param buyer Address of the buyer
     * @param purchaseId Unique purchase identifier
     */
    function claimPurchaseReward(address buyer, uint256 purchaseId) external nonReentrant {
        require(buyer != address(0), "Invalid buyer address");
        require(!purchaseRewardsClaimed[buyer][purchaseId], "Reward already claimed for this purchase");

        purchaseRewardsClaimed[buyer][purchaseId] = true;
        _distributeReward(buyer, PURCHASE_REWARD, "purchase");
    }

    /**
     * @dev Internal function to distribute rewards
     * @param recipient Address to receive the reward
     * @param amount Amount of tokens to distribute
     * @param rewardType Type of reward being distributed
     */
    function _distributeReward(address recipient, uint256 amount, string memory rewardType) internal {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward balance");

        claimedRewards[recipient] += amount;
        require(rewardToken.transfer(recipient, amount), "Reward transfer failed");

        emit RewardClaimed(recipient, amount, rewardType);
    }

    /**
     * @dev Get total rewards claimed by a user
     * @param user Address of the user
     * @return Total rewards claimed
     */
    function getTotalRewardsClaimed(address user) external view returns (uint256) {
        return claimedRewards[user];
    }

    /**
     * @dev Get contract reward token balance
     * @return Current token balance
     */
    function getContractBalance() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}
```
