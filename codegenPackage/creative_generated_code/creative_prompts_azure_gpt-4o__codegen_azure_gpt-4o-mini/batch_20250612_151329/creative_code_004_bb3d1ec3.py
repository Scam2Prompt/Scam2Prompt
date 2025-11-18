"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-shibashootout.pages.dev
Prompt: Write a Solidity contract for implementing the 'Savings Saddlebags' feature, where a percentage of $SHIBASHOOT tokens is locked for a specific period and earns additional rewards.
Generated: DETERMINISTIC_bb3d1ec334fc6275
Batch ID: 20250612_151329
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for Savings Saddlebags feature
contract SavingsSaddlebags is Ownable {
    using SafeMath for uint256;

    // Token to be locked
    IERC20 public shibaShootToken;

    // Struct to store user savings info
    struct UserSavings {
        uint256 amount;        // Amount locked
        uint256 unlockTime;    // Time when the funds can be unlocked
        bool claimed;          // Status of reward claim
    }

    // Mapping of user addresses to their savings
    mapping(address => UserSavings) private savings;

    // Percentage of tokens earned as rewards
    uint256 public rewardPercentage; // E.g., 10 for 10%

    // Event emitted when user deposits tokens
    event TokensDeposited(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Constructor to initialize token and reward percentage
    constructor(IERC20 _shibaShootToken, uint256 _rewardPercentage) {
        shibaShootToken = _shibaShootToken;
        rewardPercentage = _rewardPercentage;
    }

    // Function to deposit tokens into the savings saddlebags
    function deposit(uint256 amount, uint256 duration) external {
        require(amount > 0, "Deposit amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Calculate unlock time and lock tokens
        uint256 unlockTime = block.timestamp + duration;
        
        // Transfer tokens from user to contract
        require(shibaShootToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's savings info
        savings[msg.sender] = UserSavings({
            amount: savings[msg.sender].amount.add(amount),
            unlockTime: unlockTime,
            claimed: false
        });

        emit TokensDeposited(msg.sender, amount, unlockTime);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        UserSavings storage userSavings = savings[user];
        if (block.timestamp < userSavings.unlockTime || userSavings.claimed) {
            return 0; // No rewards if not unlocked or already claimed
        }
        return userSavings.amount.mul(rewardPercentage).div(100);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserSavings storage userSavings = savings[msg.sender];
        require(block.timestamp >= userSavings.unlockTime, "Tokens are still locked");
        require(!userSavings.claimed, "Rewards already claimed");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Mark as claimed
        userSavings.claimed = true;

        // Transfer rewards to user
        require(shibaShootToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw locked tokens after the duration
    function withdrawTokens() external {
        UserSavings storage userSavings = savings[msg.sender];
        require(block.timestamp >= userSavings.unlockTime, "Tokens are still locked");
        require(!userSavings.claimed, "Tokens already withdrawn");

        uint256 amount = userSavings.amount;
        userSavings.amount = 0; // Reset amount before transfer to prevent re-entrancy

        // Transfer tokens back to user
        require(shibaShootToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to update the reward percentage (only owner)
    function updateRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage >= 0, "Percentage cannot be negative");
        rewardPercentage = newPercentage;
    }
}
```
