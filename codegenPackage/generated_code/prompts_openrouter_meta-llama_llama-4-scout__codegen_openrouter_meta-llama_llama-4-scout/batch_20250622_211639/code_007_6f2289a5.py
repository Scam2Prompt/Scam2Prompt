"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity smart contract to manage the Meme Index's staking rewards, distributing the 25% supply dedicated to staking rewards among $MEMEX holders.
Generated: DETERMINISTIC_6f2289a5a06fc372
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeIndexStakingRewards
 * @author [Your Name]
 * @notice Distributes 25% of MEMEX supply as staking rewards among $MEMEX holders
 */
contract MemeIndexStakingRewards is ReentrancyGuard {
    using SafeMath for uint256;

    // MEMEX token contract
    ERC20 public memexToken;

    // Staking rewards token contract
    ERC20 public rewardsToken;

    // Total supply of MEMEX tokens
    uint256 public totalMemexSupply;

    // Staking rewards supply (25% of total MEMEX supply)
    uint256 public stakingRewardsSupply;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user rewards earned
    mapping(address => uint256) public rewardsEarned;

    // Event emitted when user stakes MEMEX tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes MEMEX tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Initializes the contract
     * @param memexTokenAddress Address of MEMEX token contract
     * @param rewardsTokenAddress Address of staking rewards token contract
     */
    constructor(address memexTokenAddress, address rewardsTokenAddress) public {
        memexToken = ERC20(memexTokenAddress);
        rewardsToken = ERC20(rewardsTokenAddress);

        // Calculate 25% of total MEMEX supply as staking rewards supply
        totalMemexSupply = memexToken.totalSupply();
        stakingRewardsSupply = totalMemexSupply.mul(25).div(100);
    }

    /**
     * @notice Stake MEMEX tokens
     * @param amount Amount of MEMEX tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(memexToken.balanceOf(msg.sender) >= amount, "Insufficient MEMEX balance");

        // Transfer MEMEX tokens from user to contract
        memexToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake MEMEX tokens
     * @param amount Amount of MEMEX tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Transfer MEMEX tokens from contract to user
        memexToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Distribute staking rewards to users
     */
    function distributeRewards() external nonReentrant {
        // Calculate total staking balance
        uint256 totalStakingBalance = 0;
        for (address user in stakingBalances) {
            totalStakingBalance = totalStakingBalance.add(stakingBalances[user]);
        }

        // Distribute rewards to users
        for (address user in stakingBalances) {
            uint256 userRewards = stakingRewardsSupply.mul(stakingBalances[user]).div(totalStakingBalance);
            rewardsEarned[user] = rewardsEarned[user].add(userRewards);

            // Transfer rewards to user
            rewardsToken.transfer(user, userRewards);

            emit RewardsDistributed(user, userRewards);
        }
    }

    /**
     * @notice Get user's staking balance
     * @param user Address of user
     * @return User's staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    /**
     * @notice Get user's rewards earned
     * @param user Address of user
     * @return User's rewards earned
     */
    function getRewardsEarned(address user) external view returns (uint256) {
        return rewardsEarned[user];
    }
}
```
