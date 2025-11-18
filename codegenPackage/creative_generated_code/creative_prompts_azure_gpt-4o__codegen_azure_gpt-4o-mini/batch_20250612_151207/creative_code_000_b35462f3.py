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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for the decentralized betting platform
contract DecentralizedBetting is Ownable {
    using SafeMath for uint256;

    // Struct representing a Bet
    struct Bet {
        uint256 totalStaked;
        mapping(address => uint256) stakes;
        bool isActive;
    }

    // Mapping to store bets using their identifiers
    mapping(uint256 => Bet) public bets;
    uint256 public betCounter; // Counter for unique bet identifiers
    IERC20 public token; // The token used for betting

    // Event emitted when a new bet is created
    event BetCreated(uint256 betId);
    // Event emitted when a user stakes tokens
    event TokensStaked(uint256 indexed betId, address indexed user, uint256 amount);
    // Event emitted when profits are distributed to stakers
    event ProfitsDistributed(uint256 indexed betId, uint256 totalProfit);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to create a new bet
    function createBet() external onlyOwner {
        betCounter = betCounter.add(1);
        bets[betCounter].isActive = true;
        emit BetCreated(betCounter);
    }

    // Function for users to stake tokens on a bet
    function stakeTokens(uint256 betId, uint256 amount) external {
        require(bets[betId].isActive, "Bet is not active");
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update the bet with the new stake
        bets[betId].stakes[msg.sender] = bets[betId].stakes[msg.sender].add(amount);
        bets[betId].totalStaked = bets[betId].totalStaked.add(amount);

        emit TokensStaked(betId, msg.sender, amount);
    }

    // Function to distribute profits to stakers after the bet concludes
    function distributeProfits(uint256 betId, uint256 totalProfit) external onlyOwner {
        require(bets[betId].isActive, "Bet is not active");

        // Calculate profit per token staked
        uint256 totalStaked = bets[betId].totalStaked;
        require(totalStaked > 0, "No stakes to distribute profits");

        // Distributing profits to each staker based on their stakes
        for (uint256 i = 0; i < totalStaked; i++) {
            address staker = address(i);  // Placeholder for actual staker address array
            uint256 stakeAmount = bets[betId].stakes[staker];
            if (stakeAmount > 0) {
                uint256 profitShare = totalProfit.mul(stakeAmount).div(totalStaked);
                token.transfer(staker, profitShare);
            }
        }

        // Mark the bet as inactive after distribution
        bets[betId].isActive = false;
        emit ProfitsDistributed(betId, totalProfit);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        _token.transfer(msg.sender, amount);
    }

    // Function to get the stake of a user on a specific bet
    function getStake(uint256 betId, address user) external view returns (uint256) {
        return bets[betId].stakes[user];
    }
}
```
