"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Write a smart contract in Solidity for staking WienerAI ($WAI) tokens that includes functionality for calculating rewards based on the APY mentioned on the website (1926% p/a).
Generated: DETERMINISTIC_05cecb652e594885
Batch ID: 20250612_145203
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for WienerAI ($WAI) tokens
contract WAIStaking {
    // State variables
    IERC20 public waiToken; // The WAI token contract
    uint256 public totalStaked; // Total amount of WAI tokens staked
    uint256 public constant APY = 1926; // Annual Percentage Yield (1926% p/a)
    uint256 public constant SECONDS_IN_A_YEAR = 365 days; // Number of seconds in a year

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to set the WAI token address
    constructor(address _waiToken) {
        waiToken = IERC20(_waiToken);
    }

    // Function to stake WAI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.timestamp; // Duration in seconds
        uint256 annualRewards = (userStake.amount * APY) / 100; // Annual rewards based on APY
        uint256 rewards = (annualRewards * stakedDuration) / SECONDS_IN_A_YEAR; // Calculate rewards based on duration

        return rewards + userStake.rewards; // Return total rewards
    }

    // Function to unstake WAI tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewards = calculateRewards(msg.sender); // Calculate rewards
        uint256 totalAmount = userStake.amount + rewards; // Total amount to return

        // Reset user's stake information
        userStake.amount = 0;
        userStake.timestamp = 0;
        userStake.rewards = 0;

        totalStaked -= userStake.amount;

        // Transfer staked tokens and rewards back to the user
        require(waiToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, rewards);
    }

    // Function to view user's total rewards
    function viewRewards() external view returns (uint256) {
        return calculateRewards(msg.sender);
    }
}
```
