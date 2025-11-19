"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt.pages.dev
Prompt: Describe the steps to implement a staking mechanism for $GIGA tokens and provide a code example for a smart contract that manages staking rewards.
Generated: DETERMINISTIC_76777a89f9cc690b
Batch ID: 20250612_162203
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingRewardContract
 * @author [Your Name]
 * @notice A smart contract for managing staking rewards for $GIGA tokens.
 */
contract StakingRewardContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward rate (per block)
    uint256 public rewardRate;

    // $GIGA token contract
    ERC20 public gigToken;

    /**
     * @notice Constructor for StakingRewardContract
     * @param _gigTokenAddress Address of the $GIGA token contract
     * @param _rewardRate Staking reward rate (per block)
     */
    constructor(address _gigTokenAddress, uint256 _rewardRate) {
        require(_gigTokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        gigToken = ERC20(_gigTokenAddress);
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake $GIGA tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(gigToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        gigToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking balance and total staked
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake $GIGA tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance and total staked
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        gigToken.transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to user
        gigToken.transfer(msg.sender, rewards);
    }

    /**
     * @notice Calculate staking rewards for a user
     * @param _user User address
     * @return Reward amount
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakingBalance = stakingBalances[_user];
        uint256 rewards = stakingBalance.mul(rewardRate);
        return rewards.add(rewardBalances[_user]);
    }

    /**
     * @notice Update reward balance for a user
     * @param _user User address
     * @param _rewards Additional rewards
     */
    function updateRewardBalance(address _user, uint256 _rewards) internal {
        rewardBalances[_user] = rewardBalances[_user].add(_rewards);
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to handle ERC20 token reception
    function tokenFallback(address _from, uint256 _value, bytes calldata _data) external {
        // Do nothing, as we don't use this functionality
    }
}
```
