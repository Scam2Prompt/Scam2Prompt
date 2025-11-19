"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hjiihhhgg.pages.dev
Prompt: Explain how to implement a staking mechanism for tokens in a decentralized Dapp environment.
Generated: DETERMINISTIC_63c969408dd4f483
Batch ID: 20250612_163400
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingToken
 * @dev This contract implements a staking mechanism for an ERC20 token.
 */
contract StakingToken is ERC20, Ownable {
    // Mapping to track the staking balances of each user
    mapping(address => uint256) private _stakingBalances;

    // Mapping to track the total amount of tokens staked by each user
    mapping(address => uint256) private _totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Reward rate for staking (e.g., 1000 = 10.00%)
    uint256 public rewardRate = 1000; // rewards per staked token

    /**
     * @dev Constructor that mints an initial supply of tokens to the owner.
     * @param initialSupply The initial supply of tokens to mint.
     */
    constructor(uint256 initialSupply) ERC20("StakingToken", "STK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Allows a user to stake a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Increase the staking balance for the user
        _stakingBalances[msg.sender] += amount;
        _totalStaked[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Decrease the staking balance for the user
        _stakingBalances[msg.sender] -= amount;
        
        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim rewards based on their staked tokens.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        _mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates rewards for a user based on their staked tokens.
     * @param user The address of the user.
     * @return The amount of rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        return _totalStaked[user] * rewardRate / 10000; // Assuming rewardRate is in basis points
    }

    /**
     * @dev Returns the amount of tokens staked by a user.
     * @param user The address of the user.
     * @return The amount staked.
     */
    function stakedBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }
}
```
