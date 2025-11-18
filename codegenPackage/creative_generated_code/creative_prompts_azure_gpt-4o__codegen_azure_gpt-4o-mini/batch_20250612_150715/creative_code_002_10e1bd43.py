"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfoxs.live
Prompt: Develop a staking rewards system in Solidity inspired by Galaxy Fox, where the staking pool is funded by transaction fees and the treasury supports token deflation.
Generated: DETERMINISTIC_10e1bd4384f2fd82
Batch ID: 20250612_150715
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingRewards
 * @dev A smart contract for a staking rewards system funded by transaction fees and a treasury for token deflation.
 */
contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // ERC20 token being staked
    IERC20 public stakingToken;
    // Total staked amount
    uint256 public totalStaked;
    // Mapping to keep track of staked balances
    mapping(address => uint256) public stakedBalances;
    // Mapping to store rewards for each staker
    mapping(address => uint256) public rewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with a staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalStaked = totalStaked.add(amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked = totalStaked.sub(amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to stakers based on the staking pool
     */
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), rewardAmount), "Transfer failed");

        for (uint256 i = 0; i < totalStaked; i++) {
            address staker = address(i); // Placeholder for staker's address
            uint256 stakerBalance = stakedBalances[staker];
            if (stakerBalance > 0) {
                uint256 stakerReward = rewardAmount.mul(stakerBalance).div(totalStaked);
                rewards[staker] = rewards[staker].add(stakerReward);
            }
        }
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev View total rewards for a specific address
     * @param account Address of the account to query
     * @return Total rewards of the account
     */
    function viewRewards(address account) external view returns (uint256) {
        return rewards[account];
    }

    /**
     * @dev Get the staked balance of a specific address
     * @param account Address of the account to query
     * @return Staked balance of the account
     */
    function getStakedBalance(address account) external view returns (uint256) {
        return stakedBalances[account];
    }
}
```
