"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayentest2.pages.dev
Prompt: Generate a Solidity contract for a staking mechanism that aligns with KAYEN Protocol's sustainable dual-token model and deflationary principles.
Generated: DETERMINISTIC_0bfe5acfd8f30cc2
Batch ID: 20250612_152906
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title KAYENStaking
 * @dev This contract implements a staking mechanism for the KAYEN Protocol's dual-token model.
 * It allows users to stake tokens to earn rewards while adhering to deflationary principles.
 */
contract KAYENStaking is ReentrancyGuard, Ownable {
    // Token used for staking
    IERC20 public stakingToken;
    // Token used for rewards
    IERC20 public rewardToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount;        // Amount staked by the user
        uint256 rewardDebt;    // Reward debt of the user
        uint256 lastUpdate;    // Timestamp of the last update
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in reward tokens)
    uint256 public rewardRate;

    // Event for when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event for when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event for when rewards are claimed
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract with the staking and reward tokens.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Initial reward rate.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward debt of the user before any stake or unstake operation.
     * @param user Address of the user to update.
     */
    function updateUserReward(address user) internal {
        Stake storage stake = stakes[user];
        if (stake.amount > 0) {
            uint256 pendingReward = (block.timestamp - stake.lastUpdate) * rewardRate * stake.amount / 1e18;
            stake.rewardDebt += pendingReward;
        }
        stake.lastUpdate = block.timestamp;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        updateUserReward(msg.sender);
        
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        Stake storage stake = stakes[msg.sender];
        stake.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount >= amount, "Insufficient staked amount");
        
        updateUserReward(msg.sender);

        stake.amount -= amount;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external nonReentrant {
        updateUserReward(msg.sender);

        Stake storage stake = stakes[msg.sender];
        uint256 reward = stake.rewardDebt;

        require(reward > 0, "No rewards to claim");
        stake.rewardDebt = 0;

        rewardToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRate New reward rate.
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        updateUserReward(msg.sender);
        rewardRate = newRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract (for emergencies).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount);
    }
}
```
