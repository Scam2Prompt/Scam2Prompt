"""
Generated Code Metadata:
========================
Original URL: https://aave.network
Prompt: Write a smart contract in Solidity that uses Aave's staking mechanism to secure the protocol and earn rewards.
Generated: DETERMINISTIC_ae8a069e7a4c98ea
Batch ID: 20250612_154703
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

// Import Aave's staking interface
import "@aave/aave-stake/contracts/interfaces/IStakedAave.sol";

/**
 * @title AaveStakingContract
 * @dev A smart contract that interacts with Aave's staking mechanism
 * to stake AAVE tokens and earn rewards.
 */
contract AaveStakingContract {
    // Aave's staked AAVE token contract
    IStakedAave public stakedAave;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staked AAVE token contract
     * @param _stakedAaveAddress Address of Aave's staked AAVE token contract
     */
    constructor(address _stakedAaveAddress) {
        require(_stakedAaveAddress != address(0), "Invalid staked AAVE address");
        stakedAave = IStakedAave(_stakedAaveAddress);
    }

    /**
     * @dev Stake AAVE tokens to earn rewards
     * @param amount The amount of AAVE tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer AAVE tokens from user to this contract
        require(
            stakedAave.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Stake the tokens in Aave's staking contract
        stakedAave.stake(address(this), amount);

        // Update user's stake balance
        userStakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() external {
        uint256 rewards = stakedAave.getTotalRewardsBalance(address(this));
        require(rewards > 0, "No rewards to claim");

        // Claim rewards from Aave's staking contract
        stakedAave.claimRewards(address(this), rewards);

        // Transfer rewards to user
        require(
            stakedAave.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Unstake AAVE tokens and claim any remaining rewards
     * @param amount The amount of staked AAVE tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            userStakes[msg.sender] >= amount,
            "Insufficient staked balance"
        );

        // Claim any remaining rewards first
        uint256 rewards = stakedAave.getTotalRewardsBalance(address(this));
        if (rewards > 0) {
            stakedAave.claimRewards(address(this), rewards);
            require(
                stakedAave.transfer(msg.sender, rewards),
                "Reward transfer failed"
            );
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Unstake tokens from Aave's staking contract
        stakedAave.redeem(address(this), amount);

        // Transfer unstaked tokens back to user
        require(
            stakedAave.transfer(msg.sender, amount),
            "Unstake transfer failed"
        );

        // Update user's stake balance
        userStakes[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the total staked balance for a user
     * @param user Address of the user
     * @return uint256 The staked balance
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return userStakes[user];
    }

    /**
     * @dev Get the total pending rewards for this contract
     * @return uint256 The pending rewards
     */
    function getPendingRewards() external view returns (uint256) {
        return stakedAave.getTotalRewardsBalance(address(this));
    }
}
```
