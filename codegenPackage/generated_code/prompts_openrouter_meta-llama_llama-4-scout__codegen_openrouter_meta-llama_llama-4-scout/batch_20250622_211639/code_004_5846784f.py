"""
Generated Code Metadata:
========================
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a smart contract using Solidity to create a decentralized meme coin index, including functions for buying, staking, and claiming rewards.
Generated: DETERMINISTIC_5846784f2346b2c5
Batch ID: 20250622_211639
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeCoinIndex
 * @author [Your Name]
 * @notice A decentralized meme coin index contract.
 */
contract MemeCoinIndex is Ownable {
    using SafeMath for uint256;

    // Mapping of users to their staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of users to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Meme coin token address
    address public memeCoinAddress;

    // Reward token address
    address public rewardTokenAddress;

    // Staking reward rate (per block)
    uint256 public stakingRewardRate;

    // Block number of last reward update
    uint256 public lastRewardUpdate;

    /**
     * @notice Constructor
     * @param _memeCoinAddress Meme coin token address
     * @param _rewardTokenAddress Reward token address
     * @param _stakingRewardRate Staking reward rate (per block)
     */
    constructor(
        address _memeCoinAddress,
        address _rewardTokenAddress,
        uint256 _stakingRewardRate
    ) {
        memeCoinAddress = _memeCoinAddress;
        rewardTokenAddress = _rewardTokenAddress;
        stakingRewardRate = _stakingRewardRate;
        lastRewardUpdate = block.number;
    }

    /**
     * @notice Buy meme coin
     * @param amount Amount to buy
     */
    function buyMemeCoin(uint256 amount) external {
        require(amount > 0, "Invalid amount");

        // Transfer meme coin to user
        IERC20(memeCoinAddress).transfer(msg.sender, amount);
    }

    /**
     * @notice Stake meme coin
     * @param amount Amount to stake
     */
    function stakeMemeCoin(uint256 amount) external {
        require(amount > 0, "Invalid amount");
        require(
            IERC20(memeCoinAddress).balanceOf(msg.sender) >= amount,
            "Insufficient balance"
        );

        // Transfer meme coin to contract
        IERC20(memeCoinAddress).transferFrom(msg.sender, address(this), amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStakingBalance = totalStakingBalance.add(amount);

        // Update reward balance
        updateRewardBalance(msg.sender);
    }

    /**
     * @notice Unstake meme coin
     * @param amount Amount to unstake
     */
    function unstakeMemeCoin(uint256 amount) external {
        require(amount > 0, "Invalid amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingBalance = totalStakingBalance.sub(amount);

        // Transfer meme coin to user
        IERC20(memeCoinAddress).transfer(msg.sender, amount);

        // Update reward balance
        updateRewardBalance(msg.sender);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        // Update reward balance
        updateRewardBalance(msg.sender);

        // Transfer rewards to user
        IERC20(rewardTokenAddress).transfer(msg.sender, rewardBalances[msg.sender]);

        // Reset reward balance
        rewardBalances[msg.sender] = 0;
    }

    /**
     * @notice Update reward balance
     * @param user User address
     */
    function updateRewardBalance(address user) internal {
        // Calculate reward
        uint256 reward = calculateReward(user);

        // Update reward balance
        rewardBalances[user] = rewardBalances[user].add(reward);
    }

    /**
     * @notice Calculate reward
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        // Calculate blocks since last reward update
        uint256 blocksSinceLastUpdate = block.number.sub(lastRewardUpdate);

        // Calculate reward
        uint256 reward = stakingBalances[user].mul(blocksSinceLastUpdate).mul(stakingRewardRate);

        return reward;
    }

    /**
     * @notice Update staking reward rate
     * @param _stakingRewardRate New staking reward rate (per block)
     */
    function updateStakingRewardRate(uint256 _stakingRewardRate) external onlyOwner {
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @notice Update last reward update block
     */
    function updateLastRewardUpdate() internal {
        lastRewardUpdate = block.number;
    }

    /**
     * @notice Withdraw meme coin from contract
     * @param amount Amount to withdraw
     */
    function withdrawMemeCoin(uint256 amount) external onlyOwner {
        IERC20(memeCoinAddress).transfer(msg.sender, amount);
    }

    /**
     * @notice Withdraw reward token from contract
     * @param amount Amount to withdraw
     */
    function withdrawRewardToken(uint256 amount) external onlyOwner {
        IERC20(rewardTokenAddress).transfer(msg.sender, amount);
    }
}
```
