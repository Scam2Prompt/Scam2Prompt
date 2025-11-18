"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksy.farm
Prompt: Generate a smart contract in Solidity for a staking mechanism that could be integrated into a platform like Banksy.farm.
Generated: DETERMINISTIC_8ce339b1d9948428
Batch ID: 20250612_154057
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking ERC20 tokens
 */
contract StakingContract is Ownable, ReentrancyGuard {
    // Struct to hold information about each staker
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Timestamp of the stake
    }

    // Mapping of addresses to their stakes
    mapping(address => Stake) private stakes;

    // ERC20 token to be staked
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     */
    function unstake() external nonReentrant {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");

        // Reset the stake
        stakes[msg.sender].amount = 0;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim rewards (if any) based on the staking mechanism
     * Note: Reward calculation logic should be implemented based on your requirements
     */
    function claimRewards() external nonReentrant {
        // Implement reward logic here based on the staked amount and time
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user
        // Assuming rewards are also of the same token type; modify as needed
        require(stakingToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate rewards based on staked amount and time
     * @param user Address of the user to calculate rewards for
     * @return rewards Amount of rewards to be claimed
     */
    function calculateRewards(address user) internal view returns (uint256 rewards) {
        // Example reward calculation: 10% of staked amount per year (simplified)
        Stake memory userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.timestamp;
            rewards = (userStake.amount * stakingDuration * 10) / (365 days * 100);
        }
    }

    /**
     * @dev Get the staked amount of a user
     * @param user Address of the user
     * @return amount Amount of tokens staked
     */
    function getStakedAmount(address user) external view returns (uint256 amount) {
        return stakes[user].amount;
    }

    /**
     * @dev Get the staking timestamp of a user
     * @param user Address of the user
     * @return timestamp Timestamp of the stake
     */
    function getStakeTimestamp(address user) external view returns (uint256 timestamp) {
        return stakes[user].timestamp;
    }
}
```
