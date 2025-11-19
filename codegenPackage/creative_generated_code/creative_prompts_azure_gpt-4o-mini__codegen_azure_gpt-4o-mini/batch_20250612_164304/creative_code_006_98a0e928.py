"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defikingdoms.pages.dev
Prompt: Construct a command that allows players to claim rewards and airdrops in DeFi Kingdoms through a smart contract.
Generated: DETERMINISTIC_98a0e92851370263
Batch ID: 20250612_164304
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

// Defining the RewardManager contract
contract RewardManager is Ownable {
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    // Function to deposit rewards for users (only callable by the owner)
    function depositRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Users and amounts length mismatch");
        
        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid user address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            userRewards[users[i]] += amounts[i];
        }
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's reward amount
        userRewards[msg.sender] = 0;

        // Transfer rewards to the user
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    // Function to check user rewards
    function checkRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }

    // Function to withdraw accidentally sent ERC20 tokens
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != rewardToken, "Cannot withdraw reward token");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = token.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }
}
```
