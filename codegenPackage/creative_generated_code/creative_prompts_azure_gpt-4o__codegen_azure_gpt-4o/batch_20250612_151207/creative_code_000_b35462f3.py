"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a smart contract in Solidity to implement a decentralized betting platform similar to Blockchain Bets, including features for staking tokens and distributing profits to stakers.
Generated: DETERMINISTIC_b35462f35065b8f9
Batch ID: 20250612_151207
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

/**
 * @title Decentralized Betting Platform
 * @dev This smart contract implements staking and decentralized betting functionality
 */
contract BettingPlatform {
    // Struct to represent a bet
    struct Bet {
        uint256 amount;
        uint256 outcome;
        address bettor;
        bool claimed;
    }

    // Mapping to store bets by ID
    mapping(uint256 => Bet) public bets;
    uint256 public betCounter;

    // Events
    event BetPlaced(uint256 indexed betId, address indexed bettor, uint256 amount, uint256 outcome);
    event BetClaimed(uint256 indexed betId, address indexed bettor, uint256 payout);
    event Staked(address indexed staker, uint256 amount);
    event ProfitsDistributed(address indexed staker, uint256 profit);

    // Token staking
    mapping(address => uint256) public stakes;
    uint256 public totalStaked;

    // Owner address
    address public owner;

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to place bets on a specific outcome
     * @param outcome The outcome they are betting on (e.g., 1 for Team A, 2 for Team B)
     */
    function placeBet(uint256 outcome) external payable {
        require(msg.value > 0, "Bet amount must be greater than zero");
        require(outcome > 0, "Invalid outcome");

        bets[betCounter] = Bet({
            amount: msg.value,
            outcome: outcome,
            bettor: msg.sender,
            claimed: false
        });

        emit BetPlaced(betCounter, msg.sender, msg.value, outcome);
        betCounter++;
    }

    /**
     * @dev Allows bettors to claim winnings after the outcome is finalized
     * @param betId The ID of the bet they want to claim
     * @param winningOutcome The outcome that won
     */
    function claimBet(uint256 betId, uint256 winningOutcome) external {
        Bet storage bet = bets[betId];
        require(bet.bettor == msg.sender, "You are not the bettor");
        require(!bet.claimed, "Bet already claimed");

        // If the bettor selected the winning outcome, they receive double their bet amount
        if (bet.outcome == winningOutcome) {
            uint256 payout = bet.amount * 2;
            bet.claimed = true;
            (bool success, ) = msg.sender.call{value: payout}("");
            require(success, "Payout failed");

            emit BetClaimed(betId, msg.sender, payout);
        } else {
            bet.claimed = true; // Mark the bet as claimed even if they lost
        }
    }

    /**
     * @dev Allows users to stake tokens in the platform to receive a share of the profits
     */
    function stakeTokens() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Distributes profits to stakers proportionally to their stake
     * @param profitAmount The total amount of profit to distribute
     */
    function distributeProfits(uint256 profitAmount) external onlyOwner {
        require(address(this).balance >= profitAmount, "Insufficient contract balance");

        for (address staker : stakers) {
            uint256 stakerShare = (stakes[staker] * profitAmount) / totalStaked;
            (bool success, ) = staker.call{value: stakerShare}("");
            require(success, "Profit distribution failed");

            emit ProfitsDistributed(staker, stakerShare);
        }
    }

    /**
     * @dev Allows the owner to withdraw remaining funds (e.g., unclaimed bets)
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }
}
```
