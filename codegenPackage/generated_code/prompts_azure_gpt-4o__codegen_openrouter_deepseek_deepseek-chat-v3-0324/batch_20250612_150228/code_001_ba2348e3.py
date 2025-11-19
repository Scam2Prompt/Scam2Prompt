"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-im.pages.dev
Prompt: Generate Solidity code for a staking contract that allows users to stake $QUBE tokens and earn rewards from the 5% sell tax reward pool, as described on the InQubeta platform.
Generated: DETERMINISTIC_ba2348e3eb0c86e2
Batch ID: 20250612_150228
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract QubeStaking is Ownable, ReentrancyGuard {
    IERC20 public qubeToken;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    uint256 public totalStaked;
    uint256 public rewardPool;
    uint256 public constant REWARD_RATE = 5; // 5% from sell tax
    uint256 public constant REWARD_PRECISION = 100;
    uint256 public lastRewardUpdate;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolUpdated(uint256 amount);

    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
        lastRewardUpdate = block.timestamp;
    }

    /**
     * @dev Update the reward pool with new funds from sell tax
     * @param amount The amount of QUBE tokens to add to the reward pool
     */
    function updateRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            qubeToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        rewardPool += amount;
        lastRewardUpdate = block.timestamp;
        emit RewardPoolUpdated(amount);
    }

    /**
     * @dev Stake QUBE tokens to earn rewards
     * @param amount The amount of QUBE tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            qubeToken.balanceOf(msg.sender) >= amount,
            "Insufficient balance"
        );

        _updateReward(msg.sender);

        require(
            qubeToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake QUBE tokens and claim any pending rewards
     * @param amount The amount of QUBE tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked");

        _updateReward(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        require(
            qubeToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0;
        require(
            qubeToken.transfer(msg.sender, reward),
            "Transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate and update user's reward
     * @param user The address of the staker
     */
    function _updateReward(address user) internal {
        if (stakes[user].amount == 0) return;

        uint256 reward = calculatePendingReward(user);
        stakes[user].rewardDebt += reward;
        stakes[user].lastClaimTime = block.timestamp;
    }

    /**
     * @dev Calculate pending reward for a user
     * @param user The address of the staker
     * @return The amount of pending rewards
     */
    function calculatePendingReward(address user) public view returns (uint256) {
        if (stakes[user].amount == 0 || totalStaked == 0) return 0;

        uint256 timeElapsed = block.timestamp - stakes[user].lastClaimTime;
        uint256 rewardPerToken = (rewardPool * REWARD_RATE * timeElapsed) / 
                               (totalStaked * REWARD_PRECISION * 365 days);
        
        return (stakes[user].amount * rewardPerToken) / 1e18;
    }

    /**
     * @dev Get user's staked amount and pending rewards
     * @param user The address of the staker
     * @return stakedAmount The amount of staked tokens
     * @return pendingReward The amount of pending rewards
     */
    function getUserInfo(address user) external view returns (uint256 stakedAmount, uint256 pendingReward) {
        stakedAmount = stakes[user].amount;
        pendingReward = stakes[user].rewardDebt + calculatePendingReward(user);
    }
}
```
