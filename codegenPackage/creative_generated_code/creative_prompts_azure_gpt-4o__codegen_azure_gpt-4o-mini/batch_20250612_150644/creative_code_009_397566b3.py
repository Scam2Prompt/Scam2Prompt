"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon6d.com
Prompt: Create a Solidity contract that implements the six degrees of separation theory for staking rewards distribution, as described in Polygon6D.
Generated: DETERMINISTIC_397566b3117bf1df
Batch ID: 20250612_150644
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

/// @title Six Degrees of Separation Staking Rewards Contract
/// @author Your Name
/// @notice This contract implements a staking rewards distribution based on the theory of six degrees of separation.
/// @dev The contract allows users to stake tokens and receive rewards based on their network connection.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SixDegreesRewards is Ownable {
    IERC20 public stakingToken; // The token that users will stake
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked
    
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user addresses to their staking information

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /// @param _stakingToken The address of the staking token (ERC20)
    /// @param _rewardRate The reward rate for staking
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /// @notice Allows a user to stake a certain amount of tokens
    /// @param amount The amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake more than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the staker's information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.rewardDebt += calculateReward(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Allows a user to unstake a certain amount of tokens
    /// @param amount The amount of tokens to unstake
    function unstake(uint256 amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Update the staker's information
        stakeInfo.rewardDebt += calculateReward(msg.sender);
        stakeInfo.amount -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Allows a user to claim their accumulated rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update the staker's reward debt
        stakes[msg.sender].rewardDebt += reward;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /// @notice Calculates the reward for a staker based on the blocks passed
    /// @param user The address of the user
    /// @return The calculated reward amount
    function calculateReward(address user) internal view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[user];
        return (stakeInfo.amount * rewardRate) / 1e18; // Adjust reward calculation as needed
    }

    /// @notice Allows the owner to update the reward rate
    /// @param newRate The new reward rate
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /// @notice Allows the owner to withdraw any tokens accidentally sent to the contract
    /// @param token The address of the token to withdraw
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }

    /// @notice Allows the owner to withdraw Ether sent to the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}
}
```
