"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-etftoken.web.app
Prompt: Write a smart contract in Solidity that allows users to stake ERC-20 tokens like BTCETF and withdraw rewards after a 7-day lock-up period. Include dynamic reward calculations based on the total tokens staked.
Generated: DETERMINISTIC_574227decefbd274
Batch ID: 20250612_152410
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

contract TokenStaking is Ownable {
    // The ERC-20 token to be staked
    IERC20 public stakingToken;

    // Reward structure
    uint256 public rewardRatePerTokenPerDay = 1; // 1 token rewarded per day per staked token

    // Lock-up period
    uint256 public constant LOCKUP_PERIOD = 7 days;

    // Staker structure
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastActionTime;
    }

    // Mapping of user address to staker data
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    event TokensStaked(address indexed user, uint256 amount);
    event RewardsWithdrawn(address indexed user, uint256 reward);
    event TokensUnstaked(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        Staker storage staker = stakers[msg.sender];

        // Update rewards for the user before modifying state
        staker.rewardDebt = pendingReward(msg.sender);
        staker.lastActionTime = block.timestamp;

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker and global state
        staker.stakedAmount += _amount;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Calculate the pending reward for a user.
     * @param _user The address of the user.
     * @return The pending reward amount.
     */
    function pendingReward(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        if (staker.stakedAmount == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - staker.lastActionTime;
        uint256 reward = (staker.stakedAmount * rewardRatePerTokenPerDay * elapsedTime) / 1 days;

        return reward + staker.rewardDebt;
    }

    /**
     * @dev Withdraw rewards after the lock-up period.
     */
    function withdrawRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(block.timestamp >= staker.lastActionTime + LOCKUP_PERIOD, "Lock-up period not met");

        uint256 reward = pendingReward(msg.sender);
        require(reward > 0, "No rewards to withdraw");

        // Reset reward debt and update last action time
        staker.rewardDebt = 0;
        staker.lastActionTime = block.timestamp;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens after the lock-up period.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(staker.stakedAmount >= _amount, "Not enough tokens staked");
        require(block.timestamp >= staker.lastActionTime + LOCKUP_PERIOD, "Lock-up period not met");

        // Update rewards before modifying state
        staker.rewardDebt = pendingReward(msg.sender);

        // Update staker and global state
        staker.stakedAmount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Unstake transfer failed");

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Update reward rate per token per day. Only owner can call this.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRatePerTokenPerDay = _newRewardRate;
    }
}
```
