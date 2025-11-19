"""
Generated Code Metadata:
========================
Original URL: https://dappauctionchainclaim.pages.dev
Prompt: Design a staking and unstaking system for a token on Swift Network, incorporating features like reward claiming, migration, and rectification.
Generated: DETERMINISTIC_fa23d21386d6fe74
Batch ID: 20250622_205435
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A contract for staking and unstaking tokens with reward claiming and migration features.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking data
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second
    uint256 public rewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event Migration(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the token to be staked.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.lastStakedTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        userStake.amount = userStake.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller.
     */
    function claimRewards() public {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        userStake.rewardDebt = userStake.rewardDebt.add(reward);
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a user.
     * @param user Address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp.sub(userStake.lastStakedTime);
        return userStake.amount.mul(rewardRate).mul(timeStaked).div(1e18);
    }

    /**
     * @dev Migrate staked tokens to a new contract.
     * @param newContract Address of the new staking contract.
     */
    function migrate(address newContract) external onlyOwner {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No tokens to migrate");

        stakes[msg.sender].amount = 0; // Reset user's stake
        totalStaked = totalStaked.sub(amount);
        require(stakingToken.transfer(newContract, amount), "Transfer failed");

        emit Migration(msg.sender, amount);
    }

    /**
     * @dev Set a new reward rate.
     * @param newRewardRate New reward rate per second.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
