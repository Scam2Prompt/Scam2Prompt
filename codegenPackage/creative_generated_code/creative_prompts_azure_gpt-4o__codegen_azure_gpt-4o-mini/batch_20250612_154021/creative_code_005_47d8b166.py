"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwasterdex.com
Prompt: Develop a smart contract that interacts with Aster DEX to automate staking and reward distribution for supported assets like BTC and CAKE.
Generated: DETERMINISTIC_47d8b166505406b5
Batch ID: 20250612_154021
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
 * @title AsterDEXStaking
 * @dev This smart contract automates the staking and reward distribution
 * for supported assets like BTC and CAKE on Aster DEX.
 */
contract AsterDEXStaking is Ownable {
    using SafeMath for uint256;

    // Supported token interfaces
    IERC20 public btcToken;
    IERC20 public cakeToken;

    // User stakes mapping
    mapping(address => uint256) public stakingBalance;

    // Reward tracking
    mapping(address => uint256) public rewards;
    uint256 public totalStaked;

    // Reward rate for staking
    uint256 public rewardRate = 100; // Example rate, adjust as needed

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the token addresses for staking.
     * @param _btcToken Address of the BTC token contract.
     * @param _cakeToken Address of the CAKE token contract.
     */
    constructor(address _btcToken, address _cakeToken) {
        btcToken = IERC20(_btcToken);
        cakeToken = IERC20(_cakeToken);
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        require(btcToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update staking balance and total staked
        stakingBalance[msg.sender] = stakingBalance[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate and distribute rewards for the user.
     */
    function distributeRewards() internal {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to distribute");

        rewards[msg.sender] = 0; // Reset user rewards to zero
        require(cakeToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate rewards for a user based on their staked balance.
     * @param user Address of the user to calculate rewards for.
     * @return The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256) {
        return stakingBalance[user].mul(rewardRate).div(1000); // Example calculation
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingBalance[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards before unstaking
        distributeRewards();

        // Update staking balance and total staked
        stakingBalance[msg.sender] = stakingBalance[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        require(btcToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to set the reward rate (only owner).
     * @param newRate New reward rate to set.
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
