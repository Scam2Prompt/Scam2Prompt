"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aria.fyi
Prompt: Write a function in Solidity to implement economic incentives for decentralization within the Arianee Protocol, leveraging ARIA20 token mechanics.
Generated: DETERMINISTIC_e2a8d6b940b9301d
Batch ID: 20250612_154932
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

// Importing the ERC20 interface for the ARIA20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// The IncentiveContract is focused on implementing economic incentives for decentralization
contract IncentiveContract {
    // State variables
    IERC20 public ariaToken; // The ARIA20 token contract
    address public owner; // The owner of the contract

    // Mapping to keep track of user rewards
    mapping(address => uint256) public rewards;

    // Events for logging
    event RewardDistributed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the ARIA20 token address and the owner
    constructor(address _ariaToken) {
        ariaToken = IERC20(_ariaToken);
        owner = msg.sender;
    }

    // Function to distribute rewards to users based on contribution
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Users and amounts length mismatch");
        
        for (uint256 i = 0; i < users.length; i++) {
            require(ariaToken.balanceOf(address(this)) >= amounts[i], "Insufficient contract balance for reward distribution");
            rewards[users[i]] += amounts[i];
            emit RewardDistributed(users[i], amounts[i]);
        }
    }

    // Function for users to withdraw their earned rewards
    function withdrawRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw");
        
        rewards[msg.sender] = 0; // Reset the user's reward to prevent re-entrancy attack

        // Transfer ARIA tokens to the user
        bool success = ariaToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, rewardAmount);
    }

    // Function to withdraw ARIA tokens from the contract by the owner
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(ariaToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        bool success = ariaToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    // Function to check the reward balance of a user
    function checkRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
