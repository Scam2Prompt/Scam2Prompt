"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofinance-claim.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to stake ONDO tokens and earn rewards based on their participation in the Ondo ecosystem.
Generated: DETERMINISTIC_ea4716c0f4ce9d0f
Batch ID: 20250612_163720
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for ONDO tokens
contract OndoStaking is Ownable {
    // Struct to hold user staking data
    struct Stake {
        uint256 amount;   // Amount of ONDO tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // ERC20 token interface for ONDO
    IERC20 public ondoToken;

    // Reward rate (e.g., 1% per week)
    uint256 public rewardRate = 100; // in basis points (1% = 100)

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the ONDO token address
    constructor(address _ondoToken) {
        require(_ondoToken != address(0), "Invalid token address");
        ondoToken = IERC20(_ondoToken);
    }

    // Function to stake ONDO tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(ondoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(ondoToken.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens to the contract
        ondoToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on user's stake
    function calculateReward(address user) public view returns (uint256) {
        Stake memory stakeData = stakes[user];
        if (stakeData.amount == 0) {
            return 0; // No stake, no reward
        }

        uint256 duration = block.timestamp - stakeData.timestamp; // Duration in seconds
        uint256 reward = (stakeData.amount * rewardRate * duration) / (10000 * 1 weeks); // Convert to weeks
        return reward;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        
        // Transfer staked tokens back to the user
        ondoToken.transfer(msg.sender, stakeData.amount);

        // Transfer rewards to the user
        if (reward > 0) {
            ondoToken.transfer(msg.sender, reward);
        }

        // Reset user's stake data
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, stakeData.amount, reward);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(ondoToken), "Use the unstake function for ONDO");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new reward rate (onlyOwner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
    }
}
```
