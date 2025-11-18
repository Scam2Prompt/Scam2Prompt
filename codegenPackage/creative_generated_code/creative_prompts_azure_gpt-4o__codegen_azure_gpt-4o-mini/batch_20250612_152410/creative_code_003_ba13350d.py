"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Write a function in Solidity that facilitates betting on Meme Kombat battles, allowing users to choose their champion and place bets with their staked $MK tokens.
Generated: DETERMINISTIC_ba13350d0fe906b5
Batch ID: 20250612_152410
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

interface IMKToken {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract MemeKombatBetting {
    // State variables
    IMKToken public mkToken; // Interface for $MK token
    address public owner; // Contract owner
    uint256 public minimumBetAmount; // Minimum bet amount in $MK tokens

    struct Bet {
        address user; // User's address
        uint256 amount; // Bet amount
        uint256 championId; // Chosen champion ID
    }

    // Mapping of user addresses to their bets
    mapping(address => Bet) public bets;

    // Events
    event BetPlaced(address indexed user, uint256 amount, uint256 championId);
    event BetCanceled(address indexed user);

    // Constructor to initialize the contract
    constructor(address _mkTokenAddress, uint256 _minimumBetAmount) {
        mkToken = IMKToken(_mkTokenAddress);
        owner = msg.sender;
        minimumBetAmount = _minimumBetAmount;
    }

    // Function to place a bet on a chosen champion
    function placeBet(uint256 championId, uint256 amount) external {
        require(amount >= minimumBetAmount, "Bet amount below minimum");
        require(bets[msg.sender].amount == 0, "Existing bet found");

        // Transfer the $MK tokens from the user to this contract
        bool success = mkToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Store the bet information
        bets[msg.sender] = Bet(msg.sender, amount, championId);

        emit BetPlaced(msg.sender, amount, championId);
    }

    // Function to cancel an existing bet
    function cancelBet() external {
        Bet memory userBet = bets[msg.sender];
        require(userBet.amount > 0, "No bet to cancel");

        // Refund the $MK tokens to the user
        bool success = mkToken.transferFrom(address(this), msg.sender, userBet.amount);
        require(success, "Token refund failed");

        delete bets[msg.sender]; // Remove the bet

        emit BetCanceled(msg.sender);
    }

    // Function to withdraw funds (only owner can withdraw)
    function withdrawTokens(address to, uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        require(mkToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the specified address
        bool success = mkToken.transferFrom(address(this), to, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to get the current bet for a user
    function getUserBet(address user) external view returns (Bet memory) {
        return bets[user];
    }
}
```
