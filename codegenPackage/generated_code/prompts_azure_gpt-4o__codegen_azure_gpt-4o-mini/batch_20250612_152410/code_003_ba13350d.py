"""
Generated Code Metadata:
========================
Original URL: https://memeskombat.pages.dev
Prompt: Write a function in Solidity that facilitates betting on Meme Kombat battles, allowing users to choose their champion and place bets with their staked $MK tokens.
Generated: DETERMINISTIC_ba13350d0fe906b5
Batch ID: 20250612_152410
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MemeKombatBetting {
    // State variables
    IERC20 public mkToken; // The $MK token contract
    address public owner; // Owner of the contract
    uint256 public totalBets; // Total amount of bets placed

    // Struct to represent a bet
    struct Bet {
        address better; // Address of the user placing the bet
        uint256 amount; // Amount of $MK tokens staked
        uint256 championId; // ID of the chosen champion
    }

    // Mapping to store bets by user address
    mapping(address => Bet) public bets;

    // Events
    event BetPlaced(address indexed better, uint256 amount, uint256 championId);
    event BetWithdrawn(address indexed better, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _mkToken) {
        mkToken = _mkToken;
        owner = msg.sender;
    }

    // Function to place a bet on a champion
    function placeBet(uint256 _championId, uint256 _amount) external {
        require(_amount > 0, "Bet amount must be greater than zero");
        require(mkToken.balanceOf(msg.sender) >= _amount, "Insufficient $MK balance");

        // Transfer $MK tokens from the user to this contract
        require(mkToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Store the bet
        bets[msg.sender] = Bet(msg.sender, _amount, _championId);
        totalBets += _amount;

        emit BetPlaced(msg.sender, _amount, _championId);
    }

    // Function to withdraw a bet
    function withdrawBet() external {
        Bet memory userBet = bets[msg.sender];
        require(userBet.amount > 0, "No bet to withdraw");

        // Reset the user's bet
        uint256 amountToWithdraw = userBet.amount;
        delete bets[msg.sender];
        totalBets -= amountToWithdraw;

        // Transfer the $MK tokens back to the user
        require(mkToken.transfer(msg.sender, amountToWithdraw), "Token transfer failed");

        emit BetWithdrawn(msg.sender, amountToWithdraw);
    }

    // Function to check the bet of a user
    function getUserBet(address _better) external view returns (Bet memory) {
        return bets[_better];
    }

    // Function to withdraw contract balance (only owner)
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = mkToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(mkToken.transfer(owner, balance), "Token transfer failed");
    }
}
```
