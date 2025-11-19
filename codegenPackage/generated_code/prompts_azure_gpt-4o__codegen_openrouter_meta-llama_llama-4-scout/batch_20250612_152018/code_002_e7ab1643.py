"""
Generated Code Metadata:
========================
Original URL: https://agix-reward.com
Prompt: Generate a smart contract in Solidity to enable AGIX token staking and reward distribution based on on-chain activity, as described in the SingularityNET rewards event.
Generated: DETERMINISTIC_e7ab16435fad68a1
Batch ID: 20250612_152018
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AGIX Staking Contract
 * @author SingularityNET
 * @notice Enables AGIX token staking and reward distribution based on on-chain activity
 */
contract AgixStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward accumulations
    mapping(address => uint256) public rewardAccumulations;

    // AGIX token contract
    IERC20 public agixToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Total staked AGIX
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward distribution block
    uint256 public lastRewardBlock;

    // Reward distribution start block
    uint256 public rewardStartBlock;

    // Event emitted when user stakes AGIX
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes AGIX
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param agixTokenAddress AGIX token contract address
     * @param rewardTokenAddress Reward token contract address
     * @param rewardPerBlock Reward per block
     * @param rewardStartBlock Reward distribution start block
     */
    constructor(
        address agixTokenAddress,
        address rewardTokenAddress,
        uint256 rewardPerBlock,
        uint256 rewardStartBlock
    ) public {
        agixToken = IERC20(agixTokenAddress);
        rewardToken = IERC20(rewardTokenAddress);
        rewardPerBlock = rewardPerBlock;
        rewardStartBlock = rewardStartBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake AGIX tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Invalid stake amount");
        require(agixToken.balanceOf(msg.sender) >= amount, "Insufficient AGIX balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        agixToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake AGIX tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        agixToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);

        // Distribute rewards
        distributeRewards(msg.sender);
    }

    /**
     * @dev Distribute rewards to user
     * @param user User to distribute rewards to
     */
    function distributeRewards(address user) internal {
        if (block.number < rewardStartBlock) {
            return;
        }

        uint256 rewards = calculateRewards(user);
        if (rewards > 0) {
            rewardAccumulations[user] = rewardAccumulations[user].add(rewards);
            rewardToken.safeTransfer(user, rewards);

            emit RewardsDistributed(user, rewards);
        }
    }

    /**
     * @dev Calculate rewards for user
     * @param user User to calculate rewards for
     * @return Rewards for user
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakingBalance = stakingBalances[user];
        if (stakingBalance == 0) {
            return 0;
        }

        uint256 blocksElapsed = block.number.sub(lastRewardBlock);
        if (blocksElapsed == 0) {
            return 0;
        }

        uint256 rewards = stakingBalance.mul(rewardPerBlock).mul(blocksElapsed).div(totalStaked);
        return rewards;
    }

    /**
     * @dev Update reward per block
     * @param newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 newRewardPerBlock) public onlyOwner {
        rewardPerBlock = newRewardPerBlock;
    }

    /**
     * @dev Update last reward distribution block
     * @param newLastRewardBlock New last reward distribution block
     */
    function updateLastRewardBlock(uint256 newLastRewardBlock) public onlyOwner {
        lastRewardBlock = newLastRewardBlock;
    }
}
```
