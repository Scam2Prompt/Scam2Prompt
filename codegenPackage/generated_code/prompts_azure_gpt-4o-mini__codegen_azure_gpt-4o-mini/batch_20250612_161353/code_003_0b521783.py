"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the staking and reward distribution for Green Bitcoin ($GBTC) on the Ethereum blockchain.
Generated: DETERMINISTIC_0b521783ca31a6a4
Batch ID: 20250612_161353
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Green Bitcoin ($GBTC)
contract GreenBitcoinStaking is Ownable {
    // Token being staked
    IERC20 public gbtcToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in percentage) per second
    uint256 public rewardRate = 100; // 1% per second

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the GBTC token address
    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GBTC tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);
        
        // Update total staked amount
        totalStaked -= userStake.amount;

        // Reset user's stake
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens back to the user
        require(gbtcToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        // Transfer reward to the user
        require(gbtcToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the time staked in seconds
        uint256 stakedDuration = block.timestamp - userStake.timestamp;

        // Calculate reward based on the staked amount and duration
        return (userStake.amount * rewardRate * stakedDuration) / 10000; // Dividing by 10000 to account for percentage
    }

    // Function to update the reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
