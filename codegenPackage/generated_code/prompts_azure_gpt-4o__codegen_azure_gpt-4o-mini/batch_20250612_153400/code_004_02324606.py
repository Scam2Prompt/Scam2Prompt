"""
Generated Code Metadata:
========================
Original URL: https://too1m.pages.dev
Prompt: Write a smart contract that leverages the BASE chain ecosystem to create a staking mechanism for $POON tokens, ensuring compatibility with the memecoin's roadmap.
Generated: DETERMINISTIC_0232460620aad91d
Batch ID: 20250612_153400
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

// Staking contract for $POON tokens
contract PoonStaking is Ownable {
    // Token to be staked
    IERC20 public immutable poonToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _poonToken) {
        poonToken = _poonToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(poonToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        poonToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        poonToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (example: 1% per day)
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewardRate = 1; // 1% per day
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (1 days * 100);

        return reward;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer rewards to the user
        poonToken.transfer(msg.sender, reward);

        // Reset the staking timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to view user's stake
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= poonToken.balanceOf(address(this)), "Insufficient contract balance");
        poonToken.transfer(msg.sender, amount);
    }
}
```
