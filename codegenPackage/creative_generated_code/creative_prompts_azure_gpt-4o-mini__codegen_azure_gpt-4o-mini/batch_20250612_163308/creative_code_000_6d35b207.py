"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: How can I implement a trading system on LooksRare that allows users to earn LOOKS tokens for every NFT transaction?
Generated: DETERMINISTIC_6d35b207a3d1da39
Batch ID: 20250612_163308
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LooksRareTrading is a contract that allows users to earn LOOKS tokens for every NFT transaction
contract LooksRareTrading is Ownable {
    // Address of the LOOKS token contract
    IERC20 public looksToken;

    // Mapping to track user earnings
    mapping(address => uint256) public earnings;

    // Event emitted for every successful transaction
    event EarnedLOOKS(address indexed user, uint256 amount);

    // Constructor to set the LOOKS token address
    constructor(address _looksToken) {
        require(_looksToken != address(0), "Invalid token address");
        looksToken = IERC20(_looksToken);
    }

    // Function to process a trade and reward LOOKS tokens
    function processTrade(address user, uint256 tradeValue) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(tradeValue > 0, "Trade value must be greater than zero");

        // Calculate the amount of LOOKS tokens to reward (e.g., 10% of the trade value)
        uint256 rewardAmount = (tradeValue * 10) / 100;

        // Update the user's earnings
        earnings[user] += rewardAmount;

        // Emit the event for the transaction
        emit EarnedLOOKS(user, rewardAmount);
    }

    // Function for users to claim their LOOKS tokens
    function claimLOOKS() external {
        uint256 amountToClaim = earnings[msg.sender];
        require(amountToClaim > 0, "No LOOKS to claim");

        // Reset the user's earnings before transferring to prevent reentrancy
        earnings[msg.sender] = 0;

        // Transfer LOOKS tokens to the user
        bool success = looksToken.transfer(msg.sender, amountToClaim);
        require(success, "Token transfer failed");

        // Emit an event for the claim action (optional)
        emit EarnedLOOKS(msg.sender, amountToClaim);
    }

    // Function to withdraw tokens in case of emergency or contract upgrades
    function withdrawTokens(address _token) external onlyOwner {
        require(_token != address(looksToken), "Cannot withdraw LOOKS token");
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }

    // Function to withdraw LOOKS tokens if needed
    function withdrawLOOKS() external onlyOwner {
        uint256 balance = looksToken.balanceOf(address(this));
        require(balance > 0, "No LOOKS tokens to withdraw");
        looksToken.transfer(owner(), balance);
    }
}
```
