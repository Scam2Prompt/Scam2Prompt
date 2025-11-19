"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized betting platform that incorporates token staking functionality, similar to the $BCB staking system described on Blockchain Bets.
Generated: DETERMINISTIC_7cfc38d1f64cdce7
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the staking token
interface IStakingToken is IERC20 {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Main contract for the decentralized betting platform
contract DecentralizedBettingPlatform is Ownable {
    // Struct to hold bet details
    struct Bet {
        address bettor;
        uint256 amount;
        bool isActive;
        uint256 odds;
    }

    // Mapping to store bets by their ID
    mapping(uint256 => Bet) public bets;
    uint256 public betCount;

    // Staking token used for betting
    IStakingToken public stakingToken;

    // Event emitted when a new bet is created
    event BetCreated(uint256 indexed betId, address indexed bettor, uint256 amount, uint256 odds);
    
    // Event emitted when a bet is settled
    event BetSettled(uint256 indexed betId, address indexed bettor, bool won, uint256 payout);

    // Constructor to initialize the staking token
    constructor(IStakingToken _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to create a new bet
    function createBet(uint256 amount, uint256 odds) external {
        require(amount > 0, "Bet amount must be greater than zero");
        require(odds > 0, "Odds must be greater than zero");

        // Transfer the staking token from the bettor to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Create a new bet
        bets[betCount] = Bet({
            bettor: msg.sender,
            amount: amount,
            isActive: true,
            odds: odds
        });

        emit BetCreated(betCount, msg.sender, amount, odds);
        betCount++;
    }

    // Function to settle a bet
    function settleBet(uint256 betId, bool won) external onlyOwner {
        Bet storage bet = bets[betId];
        require(bet.isActive, "Bet is not active");

        // Calculate payout
        uint256 payout = won ? bet.amount * bet.odds : 0;

        // Mark the bet as settled
        bet.isActive = false;

        // Transfer payout if the bet was won
        if (won) {
            stakingToken.transfer(bet.bettor, payout);
        }

        emit BetSettled(betId, bet.bettor, won, payout);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        stakingToken.transfer(msg.sender, amount);
    }

    // Function to get the details of a bet
    function getBetDetails(uint256 betId) external view returns (Bet memory) {
        return bets[betId];
    }
}
```
