"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Generate code to implement a staking mechanism for a cryptocurrency token with tokenomics similar to Super Trump Coin, ensuring 4% of the supply is reserved for staking rewards.
Generated: DETERMINISTIC_313c1edd9b744682
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SuperTrumpCoin
 * @dev Implementation of a token with a staking mechanism and rewards.
 */
contract SuperTrumpCoin is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18;

    // Reserved for staking rewards (4% of total supply)
    uint256 public constant STAKING_REWARDS = TOTAL_SUPPLY.mul(4).div(100);

    // Keeps track of total staked tokens
    uint256 public totalStaked;

    // Mapping from user address to staked balance
    mapping(address => uint256) public stakedBalances;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    constructor() ERC20("Super Trump Coin", "STC") {
        _mint(msg.sender, TOTAL_SUPPLY.sub(STAKING_REWARDS)); // Mint total supply minus staking rewards to the owner
    }

    /**
     * @dev Allows a user to stake a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract for staking
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake a specified amount of tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distributes staking rewards to all stakers based on their stake.
     * Rewards are distributed proportional to the amount staked.
     */
    function distributeRewards() external onlyOwner {
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        uint256 rewards = STAKING_REWARDS.sub(totalStaked); // Calculate available rewards
        require(rewards > 0, "No rewards available");

        // Distribute rewards to stakers
        for (uint256 i = 0; i < totalStakers; i++) {
            address staker = stakers[i];
            uint256 reward = stakedBalances[staker].mul(rewards).div(totalStaked);
            if (reward > 0) {
                _transfer(address(this), staker, reward);
                emit RewardsDistributed(staker, reward);
            }
        }
    }

    // Additional functions and features can be added below
}
```

The above code provides a basic implementation of a staking mechanism for a cryptocurrency token. It includes features for staking, unstaking, and distributing rewards, following best practices for Solidity programming.
