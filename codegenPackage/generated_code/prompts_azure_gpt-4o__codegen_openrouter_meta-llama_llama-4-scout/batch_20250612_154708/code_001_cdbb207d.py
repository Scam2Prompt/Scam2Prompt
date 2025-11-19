"""
Generated Code Metadata:
========================
Original URL: https://alienbasse.org
Prompt: Create a smart contract for staking ALB tokens on Alien Base, ensuring compatibility with its advanced staking models and cross-chain trading features.
Generated: DETERMINISTIC_cdbb207d802109c1
Batch ID: 20250612_154708
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title ALB Staking Contract
 * @author [Your Name]
 * @notice This contract enables staking of ALB tokens on Alien Base, 
 *          compatible with advanced staking models and cross-chain trading features.
 */
contract ALBStakingContract is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public userStakingBalances;

    // Mapping of user reward balances
    mapping (address => uint256) public userRewardBalances;

    // ALB token contract
    IERC20 public albToken;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Total staked ALB tokens
    uint256 public totalStaked;

    // Event emitted when user stakes ALB tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes ALB tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param albTokenAddress Address of the ALB token contract
     * @param stakingRewardRate Initial staking reward rate
     */
    constructor(address albTokenAddress, uint256 stakingRewardRate) public {
        albToken = IERC20(albTokenAddress);
        stakingRewardRate = stakingRewardRate;
    }

    /**
     * @dev Stake ALB tokens
     * @param amount Amount of ALB tokens to stake
     */
    function stake(uint256 amount) public whenNotPaused {
        require(amount > 0, "Invalid stake amount");
        require(albToken.transferFrom(msg.sender, address(this), amount), "ALB token transfer failed");

        userStakingBalances[msg.sender] = userStakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake ALB tokens
     * @param amount Amount of ALB tokens to unstake
     */
    function unstake(uint256 amount) public whenNotPaused {
        require(amount > 0, "Invalid unstake amount");
        require(userStakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        userStakingBalances[msg.sender] = userStakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(albToken.transfer(msg.sender, amount), "ALB token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() public whenNotPaused {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        userRewardBalances[msg.sender] = 0;
        require(albToken.transfer(msg.sender, rewards), "ALB token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user
     * @param user Address of the user
     * @return Rewards amount
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedBalance = userStakingBalances[user];
        uint256 rewards = stakedBalance.mul(stakingRewardRate).div(10000);
        return rewards.add(userRewardBalances[user]);
    }

    /**
     * @dev Update staking reward rate
     * @param newStakingRewardRate New staking reward rate
     */
    function updateStakingRewardRate(uint256 newStakingRewardRate) public onlyOwner {
        stakingRewardRate = newStakingRewardRate;
    }

    /**
     * @dev Pause the contract
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
