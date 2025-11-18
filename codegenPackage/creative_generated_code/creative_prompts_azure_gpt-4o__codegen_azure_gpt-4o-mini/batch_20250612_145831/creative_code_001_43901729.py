"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soonverse.pages.dev
Prompt: Generate code using Solidity to create a smart contract that integrates $SOON token functionality for a play-to-earn Web3 game.
Generated: DETERMINISTIC_439017294514874c
Batch ID: 20250612_145831
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

// Importing the ERC20 interface for the $SOON token functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the play-to-earn game integrating $SOON token
contract PlayToEarnGame is Ownable {
    // IERC20 interface for $SOON token
    IERC20 public soonToken;

    // Mapping to track player scores
    mapping(address => uint256) public playerScores;
    
    // Event emitted when a player earns points
    event PointsEarned(address indexed player, uint256 points);

    // Event emitted when a player redeems points for $SOON tokens
    event PointsRedeemed(address indexed player, uint256 amount);

    // Constructor to initialize the $SOON token address
    constructor(address _soonTokenAddress) {
        require(_soonTokenAddress != address(0), "Invalid token address");
        soonToken = IERC20(_soonTokenAddress);
    }

    // Function to allow players to earn points
    function earnPoints(uint256 points) external {
        require(points > 0, "Points must be greater than zero");
        
        // Increment the player's score
        playerScores[msg.sender] += points;

        // Emit event for points earned
        emit PointsEarned(msg.sender, points);
    }

    // Function to redeem points for $SOON tokens
    function redeemPoints(uint256 points) external {
        uint256 amountToRedeem = points * 10 ** 18; // Assuming 1 point = 1 $SOON token

        require(playerScores[msg.sender] >= points, "Insufficient points");
        require(soonToken.balanceOf(address(this)) >= amountToRedeem, "Insufficient $SOON tokens in contract");

        // Deduct points from player score
        playerScores[msg.sender] -= points;

        // Transfer $SOON tokens to the player
        bool success = soonToken.transfer(msg.sender, amountToRedeem);
        require(success, "Token transfer failed");

        // Emit event for points redeemed
        emit PointsRedeemed(msg.sender, amountToRedeem);
    }

    // Function for the owner to deposit $SOON tokens into the contract
    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        bool success = soonToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token deposit failed");
    }

    // Function for the owner to withdraw $SOON tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(soonToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        bool success = soonToken.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }
}
```
