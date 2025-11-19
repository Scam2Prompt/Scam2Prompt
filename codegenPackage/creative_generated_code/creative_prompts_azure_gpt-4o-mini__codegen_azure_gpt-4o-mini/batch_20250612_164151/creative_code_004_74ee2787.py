"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Develop a Solidity contract that allows users to stake their $PEPU tokens and receive rewards on the Pepe Unchained blockchain.
Generated: DETERMINISTIC_74ee27877327910f
Batch ID: 20250612_164151
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

// Import the interface for ERC20 tokens to interact with $PEPU token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeStaking
 * @dev A staking contract for $PEPU token, allowing users to stake their tokens
 * and earn rewards over time.
 */
contract PepeStaking is ReentrancyGuard, Ownable {
    IERC20 public pepuToken; // Instance of the $PEPU token
    uint256 public rewardRate; // Rate of rewards per token staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewards; // Total accumulated rewards

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt of the user
    }

    mapping(address => StakeInfo) public stakes; // Mapping to track user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the $PEPU token address and reward rate.
     * @param _pepuToken Address of the $PEPU token contract.
     * @param _rewardRate The reward rate for staking.
     */
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount Amount of $PEPU tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient $PEPU balance");

        // Update user's stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);

        // Update total staked amount
        totalStaked += amount;

        // Transfer $PEPU tokens from user to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param amount Amount of $PEPU tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.amount -= amount;

        // Update total staked amount
        totalStaked -= amount;

        // Transfer $PEPU tokens back to user
        pepuToken.transfer(msg.sender, amount);

        // Claim rewards
        uint256 rewards = claimRewards();
        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim pending rewards for the user.
     * @return The amount of rewards claimed.
     */
    function claimRewards() public nonReentrant returns (uint256) {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt += pendingRewards;

        // Transfer rewards to user
        totalRewards += pendingRewards; // For tracking total rewards
        pepuToken.transfer(msg.sender, pendingRewards);

        return pendingRewards;
    }

    /**
     * @dev Calculate the pending rewards for a user.
     * @param user Address of the user to calculate rewards for.
     * @return The amount of pending rewards.
     */
    function calculatePendingRewards(address user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        return (userStake.amount * rewardRate) - userStake.rewardDebt;
    }

    /**
     * @dev Owner can update the reward rate.
     * @param newRewardRate New reward rate to be set.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
