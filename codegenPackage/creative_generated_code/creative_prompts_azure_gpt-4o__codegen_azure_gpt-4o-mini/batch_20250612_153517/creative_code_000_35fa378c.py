"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-paalai.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake $PAAL tokens and earn rewards based on different APY configurations (e.g., 35% APY for 14 days, 80% APY for 28 days, 105% APY for 56 days).
Generated: DETERMINISTIC_35fa378cd785475d
Batch ID: 20250612_153517
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for staking $PAAL tokens
contract Staking {
    // Struct to hold information about each stake
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 startTime;    // Timestamp when the stake was initiated
        uint256 duration;     // Duration of the stake in seconds
        bool withdrawn;       // Status of the stake (withdrawn or not)
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reference to the $PAAL token contract
    IERC20 public paalToken;

    // APY configurations in basis points (e.g., 3500 = 35%)
    mapping(uint256 => uint256) public apyConfigs;

    // Events for logging
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to set the $PAAL token address and initialize APY configurations
    constructor(address _paalToken) {
        paalToken = IERC20(_paalToken);
        apyConfigs[14 days] = 3500;  // 35% APY for 14 days
        apyConfigs[28 days] = 8000;  // 80% APY for 28 days
        apyConfigs[56 days] = 10500; // 105% APY for 56 days
    }

    // Function to stake $PAAL tokens
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(apyConfigs[duration] > 0, "Invalid duration");

        // Transfer $PAAL tokens from the user to the contract
        require(paalToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Create or update the user's stake
        stakes[msg.sender] = Stake(amount, block.timestamp, duration, false);
        
        emit Staked(msg.sender, amount, duration);
    }

    // Function to withdraw the staked tokens along with rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake duration not yet over");

        // Calculate rewards based on APY
        uint256 rewards = (userStake.amount * apyConfigs[userStake.duration] * userStake.duration) / (10000 * 365 days);

        // Update the withdrawn status
        userStake.withdrawn = true;

        // Transfer the staked amount and rewards to the user
        require(paalToken.transfer(msg.sender, userStake.amount + rewards), "Transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    // Function to check the staked amount and rewards
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 rewards) {
        Stake storage userStake = stakes[user];
        require(userStake.amount > 0, "No active stake");

        rewards = (userStake.amount * apyConfigs[userStake.duration] * (block.timestamp - userStake.startTime)) / (10000 * userStake.duration);
        return (userStake.amount, rewards);
    }
}
```
