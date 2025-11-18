"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a smart contract in Solidity that supports staking "FREE SHAVACADOO" tokens and includes functions for staking, withdrawing, and calculating rewards.
Generated: DETERMINISTIC_c447c6266181aeaa
Batch ID: 20250612_150440
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

/**
 * @title Staking Contract for FREE SHAVACADOO Tokens
 * @dev This contract allows users to stake SHAVACADOO tokens, withdraw their stake, and claim rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FreeShavacadooStaking is Ownable {
    // The ERC20 token being staked
    IERC20 public shavacadooToken;

    // Reward rate in percentage per year (e.g., 10% is represented as 10)
    uint256 public rewardRate;

    // Mapping of user address to staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Timestamp of the last update for rewards calculation
        uint256 rewards; // Accumulated rewards
    }
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Constructor for initializing the staking contract.
     * @param _shavacadooToken Address of the FREE SHAVACADOO token contract.
     * @param _rewardRate Annual reward rate in percentage.
     */
    constructor(IERC20 _shavacadooToken, uint256 _rewardRate) {
        require(address(_shavacadooToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        shavacadooToken = _shavacadooToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to be staked.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        require(shavacadooToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards before withdrawal
        updateRewards(msg.sender);

        // Deduct the amount from staked balance
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(shavacadooToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards available to claim");

        // Reset rewards for the user
        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        require(shavacadooToken.transfer(msg.sender, rewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function updateRewards(address _user) internal {
        StakeInfo storage stakeInfo = stakes[_user];
        if (stakeInfo.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;
            uint256 newRewards = (stakeInfo.amount * rewardRate * timeElapsed) / (100 * 365 days);
            stakeInfo.rewards += newRewards;
        }
        stakeInfo.lastUpdated = block.timestamp;
    }

    /**
     * @dev Get the total staked amount and rewards for a user.
     * @param _user Address of the user.
     * @return stakedAmount Total staked amount.
     * @return rewards Total accumulated rewards.
     */
    function getStakeInfo(address _user) external view returns (uint256 stakedAmount, uint256 rewards) {
        StakeInfo memory stakeInfo = stakes[_user];
        stakedAmount = stakeInfo.amount;
        rewards = stakeInfo.rewards + ((stakeInfo.amount * rewardRate * (block.timestamp - stakeInfo.lastUpdated)) / (100 * 365 days));
    }
}
```
