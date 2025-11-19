"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract for the $GGG token using Solidity, incorporating token utility and metrics as described in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_cafea3cc8bd6cb88
Batch ID: 20250622_211123
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
 * @title Good Games Guild Token ($GGG)
 * @author Good Games Guild
 * @notice Implementation of the $GGG token as described in the Good Games Guild whitepaper.
 */
contract GoodGamesGuildToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of addresses to their respective staking rewards
    mapping(address => uint256) private _stakingRewards;

    // Total staking rewards distributed
    uint256 private _totalStakingRewards;

    // Token metrics
    uint256 private _totalStaked;
    uint256 private _totalTokenSupply;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event StakingRewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the GoodGamesGuildToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _totalTokenSupply = 0;
        _totalStaked = 0;
    }

    /**
     * @notice Stakes a specified amount of $GGG tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);

        // Transfer tokens from user's account to staking
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstakes a specified amount of $GGG tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);

        // Transfer tokens from staking to user's account
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Distributes staking rewards to users.
     * @param amount The amount of rewards to distribute.
     */
    function distributeStakingRewards(uint256 amount) external {
        require(amount > 0, "Invalid reward amount");

        _totalStakingRewards = _totalStakingRewards.add(amount);

        // Transfer rewards from contract to users
        for (address user in _stakingBalances) {
            uint256 userRewards = _stakingRewards[user].add(amount.mul(_stakingBalances[user]).div(_totalStaked));
            _stakingRewards[user] = userRewards;

            emit StakingRewardsDistributed(user, userRewards);
        }
    }

    /**
     * @notice Calculates the staking rewards for a user.
     * @param user The address of the user.
     * @return The staking rewards for the user.
     */
    function getStakingRewards(address user) external view returns (uint256) {
        return _stakingRewards[user];
    }

    /**
     * @notice Calculates the staking balance for a user.
     * @param user The address of the user.
     * @return The staking balance for the user.
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Calculates the total staking rewards distributed.
     * @return The total staking rewards distributed.
     */
    function getTotalStakingRewards() external view returns (uint256) {
        return _totalStakingRewards;
    }

    /**
     * @notice Calculates the total staked tokens.
     * @return The total staked tokens.
     */
    function getTotalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Override ERC20 functions to prevent direct token transfers to contract
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(to != address(this), "Cannot transfer tokens directly to contract");
        return super.transfer(to, amount);
    }

    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(to != address(this), "Cannot transfer tokens directly to contract");
        return super.transferFrom(from, to, amount);
    }
}
```
