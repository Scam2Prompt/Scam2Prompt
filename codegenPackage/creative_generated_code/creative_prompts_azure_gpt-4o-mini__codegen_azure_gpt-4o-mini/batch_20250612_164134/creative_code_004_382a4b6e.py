"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-ca.web.app
Prompt: Outline the steps to integrate the $MPEPE token into a sports betting platform, focusing on the smart contract requirements and user safety measures highlighted in the Mpeppe documentation.
Generated: DETERMINISTIC_382a4b6e60e58b30
Batch ID: 20250612_164134
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

// Import OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Define the Smart Contract for the Sports Betting Platform
contract SportsBettingPlatform is Ownable, ReentrancyGuard {
    // Events for logging bet placements and withdrawals
    event BetPlaced(address indexed user, uint256 amount, uint256 indexed eventId);
    event Withdrawn(address indexed user, uint256 amount);

    // The accepted token for betting
    IERC20 public mpepeToken;

    // Structure to hold user bets
    struct Bet {
        uint256 amount;
        uint256 eventId;
    }

    // Mapping of user addresses to their bets
    mapping(address => Bet[]) public userBets;

    // Constructor to initialize the platform with the $MPEPE token address
    constructor(address tokenAddress) {
        mpepeToken = IERC20(tokenAddress);
    }

    // Function to place a bet on a specific event
    function placeBet(uint256 eventId, uint256 amount) external nonReentrant {
        require(amount > 0, "Bet amount must be greater than zero.");
        require(mpepeToken.balanceOf(msg.sender) >= amount, "Insufficient $MPEPE balance.");
        require(mpepeToken.allowance(msg.sender, address(this)) >= amount, "Token allowance required.");

        // Transfer the $MPEPE tokens from the user to this contract
        bool sent = mpepeToken.transferFrom(msg.sender, address(this), amount);
        require(sent, "Token transfer failed.");

        // Record the user's bet
        userBets[msg.sender].push(Bet(amount, eventId));

        emit BetPlaced(msg.sender, amount, eventId);
    }

    // Function to withdraw $MPEPE tokens from the contract
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero.");
        require(mpepeToken.balanceOf(address(this)) >= amount, "Contract balance insufficient.");

        // Transfer the $MPEPE tokens back to the user
        bool sent = mpepeToken.transfer(msg.sender, amount);
        require(sent, "Token transfer failed.");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get user bets
    function getUserBets(address user) external view returns (Bet[] memory) {
        return userBets[user];
    }

    // Function to change the $MPEPE token address if needed (only owner)
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        mpepeToken = IERC20(newTokenAddress);
    }
}
```
