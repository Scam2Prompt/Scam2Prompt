"""
Generated Code Metadata:
========================
Original URL: https://decubate-platform.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking mechanism similar to Decubate, allowing users to stake DCB tokens and earn rewards based on fixed and compounding APY rates, with options for NFT and tier boosts.
Generated: DETERMINISTIC_f6fd2f9464aed6e8
Batch ID: 20250612_153517
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

// Staking contract for DCB tokens
contract DCBStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was created
        uint256 rewards; // Accumulated rewards
        bool isActive; // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // DCB token interface
    IERC20 public dcbToken;

    // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 public fixedAPY;
    uint256 public compoundingAPY;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _dcbToken, uint256 _fixedAPY, uint256 _compoundingAPY) {
        dcbToken = _dcbToken;
        fixedAPY = _fixedAPY;
        compoundingAPY = _compoundingAPY;
    }

    // Function to stake DCB tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(dcbToken.balanceOf(msg.sender) >= amount, "Insufficient DCB balance");

        // Transfer DCB tokens from user to contract
        dcbToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.isActive = true;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on the stake duration
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (!userStake.isActive) return 0;

        uint256 duration = block.timestamp - userStake.startTime;
        uint256 apy = userStake.amount * (fixedAPY + compoundingAPY) / 10000; // Convert basis points to percentage
        return (apy * duration) / 365 days; // Calculate rewards based on duration
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update user's rewards and reset start time
        stakes[msg.sender].rewards += rewards;
        stakes[msg.sender].startTime = block.timestamp;

        // Transfer rewards to user
        dcbToken.transfer(msg.sender, rewards);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to unstake DCB tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate and claim rewards before unstaking
        claimRewards();

        // Update user's stake amount
        userStake.amount -= amount;

        // Transfer DCB tokens back to user
        dcbToken.transfer(msg.sender, amount);

        // If no tokens are left, deactivate the stake
        if (userStake.amount == 0) {
            userStake.isActive = false;
        }

        emit Unstaked(msg.sender, amount);
    }

    // Function to set new APY rates (only owner can call)
    function setAPY(uint256 _fixedAPY, uint256 _compoundingAPY) external onlyOwner {
        fixedAPY = _fixedAPY;
        compoundingAPY = _compoundingAPY;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= dcbToken.balanceOf(address(this)), "Insufficient contract balance");
        dcbToken.transfer(msg.sender, amount);
    }
}
```
