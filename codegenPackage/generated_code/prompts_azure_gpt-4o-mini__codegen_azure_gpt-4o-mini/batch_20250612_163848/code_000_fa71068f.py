"""
Generated Code Metadata:
========================
Original URL: https://btceftoken.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake Bitcoin ETF Tokens (BTCETF) and earn rewards based on the amount staked.
Generated: DETERMINISTIC_fa71068fc58238c6
Batch ID: 20250612_163848
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

// Importing the ERC20 interface for interacting with the BTCETF token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Bitcoin ETF Tokens (BTCETF)
contract BTCETFStaking is Ownable {
    // Token to be staked
    IERC20 public btcEFTToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per token staked (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the BTCETF token address and reward rate
    constructor(IERC20 _btcEFTToken, uint256 _rewardRate) {
        btcEFTToken = _btcEFTToken;
        rewardRate = _rewardRate;
    }

    // Function to stake BTCETF tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(btcEFTToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to the contract
        btcEFTToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculateReward(userStake.amount);

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        userStake.rewardDebt -= calculateReward(amount);

        // Transfer tokens back to the user
        btcEFTToken.transfer(msg.sender, amount);

        // Update total staked amount
        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(userStake.amount) - userStake.rewardDebt;

        require(reward > 0, "No rewards available");

        // Update user's reward debt
        userStake.rewardDebt += reward;

        // Transfer rewards to the user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on the amount staked
    function calculateReward(uint256 amount) internal view returns (uint256) {
        return amount * rewardRate;
    }

    // Function to withdraw contract's ETH balance (only owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
