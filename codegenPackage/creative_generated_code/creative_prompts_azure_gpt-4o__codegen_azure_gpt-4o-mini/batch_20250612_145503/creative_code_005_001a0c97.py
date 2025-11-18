"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Develop a Solidity contract for a staking mechanism that allows users to stake and unstake Omikami tokens while earning rewards.
Generated: DETERMINISTIC_001a0c9711679542
Batch ID: 20250612_145503
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

// Importing the required OpenZeppelin contracts for ERC20 token interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A simple staking contract allowing users to stake and unstake an ERC20 token (Omikami),
 * while earning rewards based on the amount and duration of their stake.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // ERC20 token being staked
    IERC20 public stakingToken;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Structure to hold user stake details
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the user
        uint256 lastUpdated;   // Last time the user staked/unstaked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Events for staking and unstaking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the staking contract with the token and reward rate.
     * @param _stakingToken Address of the Omikami token contract.
     * @param _rewardRate Initial reward rate.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];

        // Update rewards for existing stake
        userStake.rewardDebt = userStake.rewardDebt.add(earnedRewards(msg.sender));
        userStake.amount = userStake.amount.add(amount);
        userStake.lastUpdated = block.timestamp;
        
        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards for existing stake
        userStake.rewardDebt = userStake.rewardDebt.add(earnedRewards(msg.sender));
        
        // Transfer tokens back to the user
        userStake.amount = userStake.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        // Claiming rewards
        uint256 reward = userStake.rewardDebt;
        userStake.rewardDebt = 0;

        emit Unstaked(msg.sender, amount, reward);
        // Transfer the rewards to the user
        if (reward > 0) {
            require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
        }
    }

    /**
     * @dev Function to calculate the rewards earned by a user.
     * @param user The address of the user.
     * @return uint256 The amount of rewards earned.
     */
    function earnedRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 timeStaked = block.timestamp.sub(userStake.lastUpdated);
        return userStake.amount.mul(rewardRate).mul(timeStaked).div(1e18);
    }

    /**
     * @dev Function to update the reward rate.
     * @param newRate The new reward rate to be set.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }
}
```
