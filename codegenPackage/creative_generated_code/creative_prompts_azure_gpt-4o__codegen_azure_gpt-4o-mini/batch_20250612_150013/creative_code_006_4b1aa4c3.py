"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolver-node.pages.dev
Prompt: Create a smart contract for staking decentralized tokens using Neutral Protocol's "Stake Tokens" feature. Include logic for calculating rewards.
Generated: DETERMINISTIC_4b1aa4c379e0c353
Batch ID: 20250612_150013
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

// Import the necessary interfaces for ERC20
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for Decentralized Tokens
 * @dev This contract allows users to stake tokens and earn rewards based on the amount staked and the duration of staking.
 */
contract StakingContract is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 reward;        // Accumulated rewards
        uint256 lastStakedAt;  // Timestamp of the last stake
    }

    // Mapping of user addresses to their staking info
    mapping(address => Stake) private stakes;

    // The token being staked
    IERC20 public stakingToken;

    // Reward rate: tokens rewarded per second per staked token
    uint256 public rewardRate = 1e18; // Example: 1 Token per second for each staked token

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Sets the staking token and initializes the contract
     * @param _stakingToken Address of the ERC20 token that is used for staking
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens in the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the user's rewards before staking
        _updateReward(msg.sender);

        // Transfer the tokens to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakedAt = block.timestamp;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update the user's rewards before withdrawal
        _updateReward(msg.sender);

        // Transfer the staked amount back to the user
        stakingToken.transfer(msg.sender, userStake.amount);

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, userStake.amount);
        
        // Reset user's stake
        userStake.amount = 0;
        userStake.reward = 0;
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.reward > 0, "No rewards to claim");

        // Calculate the reward to claim
        uint256 rewardToClaim = userStake.reward;

        // Reset user's reward
        userStake.reward = 0;

        // Transfer the reward to the user
        stakingToken.transfer(msg.sender, rewardToClaim);

        // Emit the RewardClaimed event
        emit RewardClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to update rewards for a user
     * @param user Address of the user whose rewards need to be updated
     */
    function _updateReward(address user) internal {
        Stake storage userStake = stakes[user];

        // Calculate earned rewards since the last staking
        uint256 timeStaked = block.timestamp - userStake.lastStakedAt;
        userStake.reward += (userStake.amount * rewardRate * timeStaked) / 1e18;

        // Update the last staking time
        userStake.lastStakedAt = block.timestamp;
    }

    /**
     * @dev Set the reward rate
     * @param newRate New reward rate to set
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /**
     * @dev Get the staking information for a user
     * @param user Address of the user
     * @return amount Staked amount
     * @return reward Accumulated reward
     * @return lastStakedAt Timestamp of last stake
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 reward, uint256 lastStakedAt) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.reward, userStake.lastStakedAt);
    }
}
```
