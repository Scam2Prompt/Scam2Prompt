"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-we.pages.dev
Prompt: How can I implement a smart contract to manage staking rewards for AITECH with compounding options?
Generated: DETERMINISTIC_55b2e23c3dda516d
Batch ID: 20250612_161353
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for managing staking rewards with compounding options.
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken; // The ERC20 token being staked
    uint256 public rewardRate; // The rate at which rewards are accrued
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public constant REWARD_INTERVAL = 1 days; // Reward interval for compounding

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 lastClaimed; // Last time rewards were claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate; // Set the reward rate (in tokens per second)
    }

    /**
     * @notice Stake an amount of tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update the user's stake before transferring tokens
        Stake storage userStake = stakes[msg.sender];
        _claimRewards(); // Claim any pending rewards before staking

        // Update user's stake amount and last claimed time
        userStake.amount += amount;
        userStake.lastClaimed = block.timestamp;

        totalStaked += amount;

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake an amount of tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        _claimRewards(); // Claim any pending rewards before unstaking

        // Update the stake and total staked
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim the accrued rewards for the sender
     */
    function claimRewards() external {
        _claimRewards();
    }

    /**
     * @dev Internal function to claim rewards for the sender
     */
    function _claimRewards() internal {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        if (reward > 0) {
            userStake.lastClaimed = block.timestamp; // Update the last claimed time
            require(stakingToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardsClaimed(msg.sender, reward);
        }
    }

    /**
     * @notice Calculate the total rewards for a given user
     * @param user The address of the user
     * @return The total accrued rewards
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakedTime = block.timestamp - userStake.lastClaimed;
        return (userStake.amount * rewardRate * stakedTime) / REWARD_INTERVAL;
    }

    /**
     * @notice Set a new reward rate, can only be called by the owner
     * @param newRewardRate The new reward rate
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
