"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scottytheai.web.app
Prompt: Write a smart contract in Solidity for staking $SCOTTY tokens with customizable lock periods and reward multipliers, as described in the Scotty AI staking system.
Generated: DETERMINISTIC_1bb613136b05c21a
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottyStaking
 * @dev A smart contract for staking $SCOTTY tokens with customizable lock periods and reward multipliers
 */
contract ScottyStaking is Ownable {
    using SafeMath for uint256;

    // Structure to hold staking details
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 lockPeriod; // Lock period in seconds
        uint256 startTime;  // Time when the stake was created
        uint256 rewards;     // Accumulated rewards
    }

    IERC20 public scottyToken; // The ERC20 token being staked
    mapping(address => Stake[]) public stakes; // Mapping of user address to their stakes

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress The address of the $SCOTTY token contract.
     */
    constructor(IERC20 _tokenAddress) {
        scottyToken = _tokenAddress;
    }

    /**
     * @dev Stakes a specific amount of $SCOTTY tokens with a chosen lock period.
     * @param amount The amount of $SCOTTY tokens to stake.
     * @param lockPeriod The lock period for the stake in seconds.
     */
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockPeriod > 0, "Lock period must be greater than zero");
        
        // Transfer tokens from the user to the contract
        scottyToken.transferFrom(msg.sender, address(this), amount);

        // Create a new stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            lockPeriod: lockPeriod,
            startTime: block.timestamp,
            rewards: 0
        }));

        emit Staked(msg.sender, amount, lockPeriod);
    }

    /**
     * @dev Calculates the rewards for a specific stake.
     * @param stake The stake for which to calculate rewards.
     * @return The calculated rewards.
     */
    function calculateRewards(Stake memory stake) internal view returns (uint256) {
        // Simple reward calculation based on stake amount and duration
        uint256 duration = block.timestamp.sub(stake.startTime);
        uint256 multiplier = stake.lockPeriod > 0 ? stake.lockPeriod.div(1 weeks) : 1;
        return stake.amount.mul(duration).mul(multiplier).div(1 ether); // Adjust as necessary for reward token precision
    }

    /**
     * @dev Unstakes the specified stake and claims rewards.
     * @param stakeIndex The index of the stake to unstake.
     */
    function unstake(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        
        Stake storage stake = stakes[msg.sender][stakeIndex];
        require(block.timestamp >= stake.startTime.add(stake.lockPeriod), "Stake is still locked");

        // Calculate rewards
        stake.rewards = calculateRewards(stake);

        // Transfer staked tokens back to the user
        scottyToken.transfer(msg.sender, stake.amount);

        // Transfer rewards to the user (implement reward token logic as necessary)
        // Assuming rewards are paid in the same token for simplicity
        scottyToken.transfer(msg.sender, stake.rewards);

        // Remove the stake by replacing it with the last one
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        emit Unstaked(msg.sender, stake.amount, stake.rewards);
    }

    /**
     * @dev Allows the owner to withdraw accidentally sent tokens from the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(msg.sender, amount);
    }
}
```
