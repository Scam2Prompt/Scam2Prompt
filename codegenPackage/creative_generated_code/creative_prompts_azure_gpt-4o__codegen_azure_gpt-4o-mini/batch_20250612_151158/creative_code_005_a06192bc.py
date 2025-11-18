"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secured-everlodge.pages.dev
Prompt: Write code for a staking mechanism that rewards users with passive income and exclusive benefits, similar to the Everlodge token staking system.
Generated: DETERMINISTIC_a06192bcc6854f1a
Batch ID: 20250612_151158
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

// Interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev This contract allows users to stake tokens and earn rewards.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // User's stake information
    struct Stake {
        uint256 amount;  // Amount of tokens staked
        uint256 startTime;  // Timestamp when the stake was made
        uint256 reward;  // Reward accumulated
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Reward rate in tokens per second
    uint256 public rewardRate = 1e18; // 1 token per second for simplicity

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateChanged(uint256 newRate);

    /**
     * @dev Constructor to set the staking token address.
     * @param _stakingToken Address of the ERC20 token to be staked.
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Allows users to stake a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake zero tokens");
        
        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        
        // Update the stake before transferring tokens
        userStake.reward = 0; // Reset reward to zero after calculation
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0; // Reset staked amount

        // Transfer the staked tokens and reward to the user
        stakingToken.transfer(msg.sender, amountToUnstake);
        if (reward > 0) {
            stakingToken.transfer(msg.sender, reward);
        }
        
        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    /**
     * @dev Calculate the reward for a given user.
     * @param user The address of the user.
     * @return The total reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (block.timestamp - userStake.startTime) * rewardRate * userStake.amount / 1e18;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRate The new reward rate to be set.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
        emit RewardRateChanged(newRate);
    }
}
```
