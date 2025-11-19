"""
Generated Code Metadata:
========================
Original URL: https://stakewise.eu
Prompt: Create a smart contract example that interacts with StakeWise for staking Ethereum and distributing rewards.
Generated: DETERMINISTIC_b2ec348573be2dc1
Batch ID: 20250612_145832
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakeWise Staking Contract
 * @author [Your Name]
 * @notice This contract interacts with StakeWise for staking Ethereum and distributing rewards.
 */
contract StakeWiseStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // StakeWise staking pool address
    address public stakeWiseStakingPool;

    // Reward token address
    address public rewardToken;

    // Staking event
    event Staked(address indexed user, uint256 amount);

    // Unstaking event
    event Unstaked(address indexed user, uint256 amount);

    // Reward distribution event
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakeWiseStakingPool StakeWise staking pool address
     * @param _rewardToken Reward token address
     */
    constructor(address _stakeWiseStakingPool, address _rewardToken) public {
        require(_stakeWiseStakingPool != address(0), "StakeWise staking pool address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        stakeWiseStakingPool = _stakeWiseStakingPool;
        rewardToken = _rewardToken;
    }

    /**
     * @dev Stake Ethereum through StakeWise
     * @param amount Amount of Ethereum to stake
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer Ethereum to StakeWise staking pool
        (bool sent, ) = payable(stakeWiseStakingPool).call{value: amount}("");
        require(sent, "Failed to send Ethereum to StakeWise staking pool");

        // Update user staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake Ethereum from StakeWise
     * @param amount Amount of Ethereum to unstake
     */
    function unstake(uint256 amount) public {
        require(amount > 0, "Unstaking amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "User staking balance is insufficient");

        // Update user staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Transfer Ethereum from StakeWise staking pool
        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "Failed to send Ethereum from StakeWise staking pool");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to users
     */
    function distributeRewards() public onlyOwner {
        // Calculate total staking balance
        uint256 totalStakingBalance = 0;
        for (address user in stakingBalances) {
            totalStakingBalance = totalStakingBalance.add(stakingBalances[user]);
        }

        // Calculate total reward amount
        uint256 totalRewardAmount = IERC20(rewardToken).balanceOf(address(this));

        // Distribute rewards to users
        for (address user in stakingBalances) {
            uint256 userRewardAmount = totalRewardAmount.mul(stakingBalances[user]).div(totalStakingBalance);
            rewardBalances[user] = rewardBalances[user].add(userRewardAmount);

            // Transfer reward to user
            IERC20(rewardToken).transfer(user, userRewardAmount);

            emit RewardDistributed(user, userRewardAmount);
        }
    }

    /**
     * @dev Withdraw reward
     */
    function withdrawReward() public {
        require(rewardBalances[msg.sender] > 0, "User reward balance is zero");

        uint256 rewardAmount = rewardBalances[msg.sender];
        rewardBalances[msg.sender] = 0;

        // Transfer reward to user
        IERC20(rewardToken).transfer(msg.sender, rewardAmount);
    }
}
```
