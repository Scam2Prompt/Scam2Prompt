"""
Generated Code Metadata:
========================
Original URL: https://invest-destreams.web.app
Prompt: Provide code to implement a rewards program for a blockchain-based platform, including cashback, airdrops, and rank-based benefits, as outlined in DeeStream's utility section.
Generated: DETERMINISTIC_34889503977994b4
Batch ID: 20250612_151853
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

contract RewardsProgram is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // User structure to track rewards and rank
    struct User {
        uint256 totalSpent;          // Total amount spent by user
        uint256 pendingCashback;     // Pending cashback rewards
        uint256 claimedRewards;      // Total rewards claimed
        uint256 lastAirdropClaimed;  // Timestamp of last airdrop claim
        uint8 rank;                  // User rank (0-4)
    }

    // Rank thresholds and benefits
    struct RankInfo {
        uint256 spendThreshold;      // Required spending to reach rank
        uint256 cashbackRate;        // Cashback percentage (100 = 1%)
        uint256 airdropAmount;       // Airdrop amount per period
        uint256 airdropInterval;     // Time between airdrops (seconds)
    }

    // Mapping of user addresses to their data
    mapping(address => User) public users;

    // Rank configuration (0-4, higher is better)
    RankInfo[5] public ranks;

    // Events
    event CashbackEarned(address indexed user, uint256 amount);
    event CashbackClaimed(address indexed user, uint256 amount);
    event AirdropClaimed(address indexed user, uint256 amount);
    event RankUp(address indexed user, uint8 newRank);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);

        // Initialize rank thresholds and benefits
        // Rank 0 (Basic)
        ranks[0] = RankInfo({
            spendThreshold: 0,
            cashbackRate: 50,       // 0.5%
            airdropAmount: 0,
            airdropInterval: 0
        });

        // Rank 1 (Silver)
        ranks[1] = RankInfo({
            spendThreshold: 1000 ether,
            cashbackRate: 100,      // 1%
            airdropAmount: 10 ether,
            airdropInterval: 30 days
        });

        // Rank 2 (Gold)
        ranks[2] = RankInfo({
            spendThreshold: 5000 ether,
            cashbackRate: 150,      // 1.5%
            airdropAmount: 25 ether,
            airdropInterval: 30 days
        });

        // Rank 3 (Platinum)
        ranks[3] = RankInfo({
            spendThreshold: 20000 ether,
            cashbackRate: 200,      // 2%
            airdropAmount: 50 ether,
            airdropInterval: 30 days
        });

        // Rank 4 (Diamond)
        ranks[4] = RankInfo({
            spendThreshold: 50000 ether,
            cashbackRate: 250,      // 2.5%
            airdropAmount: 100 ether,
            airdropInterval: 30 days
        });
    }

    /**
     * @dev Record a user's spending and calculate cashback
     * @param _user User address
     * @param _amount Amount spent
     */
    function recordSpending(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be positive");

        User storage user = users[_user];
        uint8 currentRank = user.rank;

        // Update total spent
        user.totalSpent += _amount;

        // Calculate and add cashback
        uint256 cashback = (_amount * ranks[currentRank].cashbackRate) / 10000;
        user.pendingCashback += cashback;

        emit CashbackEarned(_user, cashback);

        // Check for rank up
        _checkRankUp(_user);
    }

    /**
     * @dev Claim pending cashback rewards
     */
    function claimCashback() external nonReentrant {
        User storage user = users[msg.sender];
        uint256 amount = user.pendingCashback;
        require(amount > 0, "No cashback to claim");

        user.pendingCashback = 0;
        user.claimedRewards += amount;

        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
        emit CashbackClaimed(msg.sender, amount);
    }

    /**
     * @dev Claim available airdrop
     */
    function claimAirdrop() external nonReentrant {
        User storage user = users[msg.sender];
        uint8 currentRank = user.rank;
        RankInfo memory rankInfo = ranks[currentRank];

        require(rankInfo.airdropAmount > 0, "No airdrop for current rank");
        require(
            block.timestamp >= user.lastAirdropClaimed + rankInfo.airdropInterval,
            "Airdrop not available yet"
        );

        user.lastAirdropClaimed = block.timestamp;
        user.claimedRewards += rankInfo.airdropAmount;

        require(rewardToken.transfer(msg.sender, rankInfo.airdropAmount), "Transfer failed");
        emit AirdropClaimed(msg.sender, rankInfo.airdropAmount);
    }

    /**
     * @dev Internal function to check and update user rank
     * @param _user User address
     */
    function _checkRankUp(address _user) internal {
        User storage user = users[_user];
        uint8 currentRank = user.rank;
        uint8 newRank = currentRank;

        // Find highest rank user qualifies for
        for (uint8 i = 4; i > currentRank; i--) {
            if (user.totalSpent >= ranks[i].spendThreshold) {
                newRank = i;
                break;
            }
        }

        if (newRank > currentRank) {
            user.rank = newRank;
            emit RankUp(_user, newRank);
        }
    }

    /**
     * @dev Get user's current rank
     * @param _user User address
     * @return Current rank (0-4)
     */
    function getUserRank(address _user) external view returns (uint8) {
        return users[_user].rank;
    }

    /**
     * @dev Get user's pending rewards
     * @param _user User address
     * @return pendingCashback Pending cashback amount
     * @return nextAirdrop Timestamp when next airdrop is available (0 if none)
     */
    function getPendingRewards(address _user) external view returns (uint256 pendingCashback, uint256 nextAirdrop) {
        User memory user = users[_user];
        pendingCashback = user.pendingCashback;

        uint8 currentRank = user.rank;
        RankInfo memory rankInfo = ranks[currentRank];

        if (rankInfo.airdropAmount > 0) {
            nextAirdrop = user.lastAirdropClaimed + rankInfo.airdropInterval;
            if (block.timestamp < nextAirdrop) {
                // Return the next available time
                return (pendingCashback, nextAirdrop);
            }
        }

        // Airdrop is available now or not applicable
        return (pendingCashback, 0);
    }

    /**
     * @dev Admin function to update reward token address
     * @param _newToken New reward token address
     */
    function updateRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = IERC20(_newToken);
    }

    /**
     * @dev Admin function to withdraw excess tokens
     * @param _amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.transfer(owner(), _amount), "Transfer failed");
    }
}
```
