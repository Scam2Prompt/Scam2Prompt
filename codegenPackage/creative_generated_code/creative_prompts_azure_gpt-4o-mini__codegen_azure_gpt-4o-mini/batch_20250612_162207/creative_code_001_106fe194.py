"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake DOGE20 tokens and earn passive rewards based on their stake percentage.
Generated: DETERMINISTIC_106fe1940f1090a8
Batch ID: 20250612_162207
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

// Importing the ERC20 interface for DOGE20 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for DOGE20 Tokens
 * @notice This smart contract allows users to stake DOGE20 tokens and earn rewards based on their stake percentage.
 */
contract Doge20Staking is Ownable {
    // Struct to store staker information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of DOGE20 tokens staked
    uint256 public totalStaked;

    // The reward rate per block (customize as needed)
    uint256 public rewardPerBlock = 1e18; // 1 DOGE20 token reward per block

    // The address of the DOGE20 token contract
    IERC20 public doge20Token;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the DOGE20 token address
     * @param _doge20Token The address of the DOGE20 token contract
     */
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /**
     * @dev Function to stake DOGE20 tokens
     * @param _amount The amount of DOGE20 tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer DOGE20 tokens from the user to the contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake DOGE20 tokens
     * @param _amount The amount of DOGE20 tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked amount");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate pending rewards for a user
     * @return The amount of rewards pending for the user
     */
    function pendingRewards() external view returns (uint256) {
        Staker storage staker = stakers[msg.sender];
        return (staker.amountStaked * rewardPerBlock) / totalStaked - staker.rewardDebt;
    }

    /**
     * @dev Function to claim rewards
     */
    function claimRewards() external {
        uint256 reward = pendingRewards();

        require(reward > 0, "No rewards to claim");

        // Update reward debt for the user
        stakers[msg.sender].rewardDebt += reward;

        // Transfer rewards to the user
        doge20Token.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }
}
```
