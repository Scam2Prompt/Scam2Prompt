"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogepreneur-io.pages.dev
Prompt: Write a smart contract to handle token staking and passive income distribution for DogePreneur token holders, following the platform’s outlined process.
Generated: DETERMINISTIC_a6d4747b71546b10
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract DogePreneurStaking is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp when the tokens were staked
    }

    // Mapping from user addresses to their respective stakes
    mapping(address => Stake) private stakes;

    // Token to be staked
    IERC20 public dogePreneurToken;

    // Annual interest rate in percentage (e.g., 5% = 500)
    uint256 public annualInterestRate;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the token address and interest rate
    constructor(IERC20 _token, uint256 _annualInterestRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_annualInterestRate > 0, "Interest rate must be greater than zero");
        
        dogePreneurToken = _token;
        annualInterestRate = _annualInterestRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(dogePreneurToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from user to the contract
        dogePreneurToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 yearlyRewards = (userStake.amount * annualInterestRate) / 10000; // Convert percentage to decimal
        uint256 rewards = (yearlyRewards * stakingDuration) / 365 days; // Calculate rewards based on time staked

        return rewards;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewards = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount + rewards;

        // Reset user's stake to zero
        stakes[msg.sender].amount = 0;

        // Transfer staked tokens and rewards back to the user
        dogePreneurToken.transfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount, rewards);
    }

    // Function to view the user's stake
    function viewStake(address user) external view returns (uint256 amountStaked, uint256 rewards) {
        amountStaked = stakes[user].amount;
        rewards = calculateRewards(user);
    }

    // Allow the owner to update the annual interest rate
    function updateAnnualInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");
        annualInterestRate = newRate;
    }
}
```
