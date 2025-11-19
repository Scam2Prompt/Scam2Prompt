"""
Generated Code Metadata:
========================
Original URL: https://eth-polymarket.ct.ws
Prompt: "Design a basic architecture for a decentralized prediction market on Ethereum, including smart contract structure."
Generated: DETERMINISTIC_886a353892f53dfa
Batch ID: 20250622_211156
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PredictionMarket
 * @dev A decentralized prediction market platform on Ethereum
 */
contract PredictionMarket is Ownable {
    using SafeMath for uint256;

    // Event declarations
    event MarketCreated(uint256 marketId, string question, uint256 closingTime);
    event BetPlaced(uint256 marketId, address bettor, bool outcome, uint256 amount);
    event MarketResolved(uint256 marketId, bool outcome);
    event PayoutClaimed(uint256 marketId, address bettor, uint256 amount);

    // Market structure
    struct Market {
        string question;
        uint256 closingTime;
        bool resolved;
        bool outcome;
        uint256 totalYesBets;
        uint256 totalNoBets;
        mapping(address => uint256) yesBets;
        mapping(address => uint256) noBets;
    }

    // Token used for betting
    IERC20 public bettingToken;

    // Mapping of market IDs to Market structs
    mapping(uint256 => Market) public markets;

    // Counter for market IDs
    uint256 public nextMarketId;

    /**
     * @dev Constructor initializes the betting token
     * @param _tokenAddress Address of the ERC20 token used for betting
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        bettingToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Creates a new prediction market
     * @param _question The prediction question
     * @param _closingTime Timestamp when the market closes
     */
    function createMarket(string memory _question, uint256 _closingTime) external onlyOwner {
        require(_closingTime > block.timestamp, "Closing time must be in the future");
        require(bytes(_question).length > 0, "Question cannot be empty");

        uint256 marketId = nextMarketId++;
        markets[marketId].question = _question;
        markets[marketId].closingTime = _closingTime;

        emit MarketCreated(marketId, _question, _closingTime);
    }

    /**
     * @dev Places a bet on a market outcome
     * @param _marketId ID of the market to bet on
     * @param _outcome True for "yes", false for "no"
     * @param _amount Amount of tokens to bet
     */
    function placeBet(uint256 _marketId, bool _outcome, uint256 _amount) external {
        require(_marketId < nextMarketId, "Invalid market ID");
        Market storage market = markets[_marketId];
        require(block.timestamp < market.closingTime, "Market closed");
        require(_amount > 0, "Bet amount must be positive");

        // Transfer tokens from bettor to contract
        require(bettingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        if (_outcome) {
            market.yesBets[msg.sender] = market.yesBets[msg.sender].add(_amount);
            market.totalYesBets = market.totalYesBets.add(_amount);
        } else {
            market.noBets[msg.sender] = market.noBets[msg.sender].add(_amount);
            market.totalNoBets = market.totalNoBets.add(_amount);
        }

        emit BetPlaced(_marketId, msg.sender, _outcome, _amount);
    }

    /**
     * @dev Resolves a market with the given outcome
     * @param _marketId ID of the market to resolve
     * @param _outcome The actual outcome (true/false)
     */
    function resolveMarket(uint256 _marketId, bool _outcome) external onlyOwner {
        require(_marketId < nextMarketId, "Invalid market ID");
        Market storage market = markets[_marketId];
        require(block.timestamp >= market.closingTime, "Market not yet closed");
        require(!market.resolved, "Market already resolved");

        market.resolved = true;
        market.outcome = _outcome;

        emit MarketResolved(_marketId, _outcome);
    }

    /**
     * @dev Claims payout for a resolved market
     * @param _marketId ID of the market to claim from
     */
    function claimPayout(uint256 _marketId) external {
        require(_marketId < nextMarketId, "Invalid market ID");
        Market storage market = markets[_marketId];
        require(market.resolved, "Market not resolved");

        uint256 payoutAmount;
        if (market.outcome) {
            require(market.yesBets[msg.sender] > 0, "No yes bets to claim");
            payoutAmount = calculatePayout(_marketId, true, market.yesBets[msg.sender]);
            market.yesBets[msg.sender] = 0;
        } else {
            require(market.noBets[msg.sender] > 0, "No no bets to claim");
            payoutAmount = calculatePayout(_marketId, false, market.noBets[msg.sender]);
            market.noBets[msg.sender] = 0;
        }

        require(bettingToken.transfer(msg.sender, payoutAmount), "Payout transfer failed");
        emit PayoutClaimed(_marketId, msg.sender, payoutAmount);
    }

    /**
     * @dev Calculates the payout for a bet
     * @param _marketId ID of the market
     * @param _outcome The outcome bet on
     * @param _betAmount Amount bet on the outcome
     * @return payout The calculated payout amount
     */
    function calculatePayout(uint256 _marketId, bool _outcome, uint256 _betAmount) public view returns (uint256 payout) {
        Market storage market = markets[_marketId];
        require(market.resolved, "Market not resolved");

        if (market.outcome == _outcome) {
            uint256 totalWinningBets = _outcome ? market.totalYesBets : market.totalNoBets;
            uint256 totalLosingBets = _outcome ? market.totalNoBets : market.totalYesBets;
            
            // Calculate payout: original bet + proportional share of losing bets
            payout = _betAmount.add(_betAmount.mul(totalLosingBets).div(totalWinningBets));
        } else {
            payout = 0;
        }
    }

    /**
     * @dev Gets the current bet amounts for a user in a market
     * @param _marketId ID of the market
     * @param _bettor Address of the bettor
     * @return yesBet Amount bet on "yes"
     * @return noBet Amount bet on "no"
     */
    function getUserBets(uint256 _marketId, address _bettor) external view returns (uint256 yesBet, uint256 noBet) {
        require(_marketId < nextMarketId, "Invalid market ID");
        Market storage market = markets[_marketId];
        return (market.yesBets[_bettor], market.noBets[_bettor]);
    }
}
```
