"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that distributes $SCOTTY token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_b3b5a8a8570ea8ec
Batch ID: 20250622_210216
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

// Smart contract for distributing SCOTTY token rewards
contract StakingRewards is Ownable {
    // State variables
    IERC20 public scottyToken; // The SCOTTY token contract
    uint256 public annualReturnPercentage; // Annual return percentage for rewards
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SCOTTY token address
    constructor(address _scottyToken, uint256 _annualReturnPercentage) {
        require(_scottyToken != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0, "Annual return must be positive");

        scottyToken = IERC20(_scottyToken);
        annualReturnPercentage = _annualReturnPercentage;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update total staked and user's staked amount
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;
    }

    // Function to calculate and distribute rewards
    function distributeRewards() external {
        require(totalStaked > 0, "No tokens staked");

        // Calculate rewards for each user based on their share of the staking pool
        uint256 userShare = (stakedAmount[msg.sender] * 1e18) / totalStaked; // User's share in basis points
        uint256 userRewards = (userShare * annualReturnPercentage * totalStaked) / (100 * 1e18); // Calculate rewards

        // Update rewards mapping
        rewards[msg.sender] += userRewards;

        // Emit event for rewards distribution
        emit RewardsDistributed(msg.sender, userRewards);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset user's rewards to zero before transferring
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(scottyToken.transfer(msg.sender, rewardAmount), "Transfer failed");
    }

    // Function to update the annual return percentage (only owner can call)
    function updateAnnualReturnPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage > 0, "Annual return must be positive");
        annualReturnPercentage = newPercentage;
    }

    // Function to withdraw staked tokens (only owner can call)
    function withdrawStakedTokens(uint256 amount) external onlyOwner {
        require(amount <= totalStaked, "Insufficient staked tokens");
        totalStaked -= amount;
        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
