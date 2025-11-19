"""
Generated Code Metadata:
========================
Original URL: https://polymarket.de
Prompt: "Generate a code snippet for a simple prediction market contract using Solidity for Ethereum-based platforms."
Generated: DETERMINISTIC_dbf3e1b00e3c3126
Batch ID: 20250622_204803
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Simple Prediction Market Contract
 * @author [Your Name]
 * @notice A basic prediction market contract for Ethereum-based platforms.
 */
contract SimplePredictionMarket {
    using SafeMath for uint256;

    // Enum for market status
    enum MarketStatus { Open, Closed, Settled }

    // Struct for market data
    struct Market {
        address creator;
        string question;
        uint256 creationTime;
        uint256 closeTime;
        uint256 yesVotes;
        uint256 noVotes;
        MarketStatus status;
        mapping(address => bool) voted;
    }

    // Mapping of market IDs to market data
    mapping(uint256 => Market) public markets;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Event emitted when a new market is created
    event NewMarket(uint256 indexed marketId, address creator, string question);

    // Event emitted when a user votes on a market
    event VoteCast(uint256 indexed marketId, address voter, bool vote);

    // Event emitted when a market is closed
    event MarketClosed(uint256 indexed marketId);

    // Event emitted when a market is settled
    event MarketSettled(uint256 indexed marketId, bool outcome);

    // Counter for market IDs
    uint256 public marketIdCounter;

    // Token used for payments
    IERC20 public token;

    /**
     * @notice Constructor for the SimplePredictionMarket contract.
     * @param _token Address of the token used for payments.
     */
    constructor(IERC20 _token) public {
        token = _token;
    }

    /**
     * @notice Creates a new prediction market.
     * @param _question The question being asked in the market.
     * @param _closeTime The time at which the market will close.
     */
    function createMarket(string memory _question, uint256 _closeTime) public {
        require(_closeTime > block.timestamp, "Close time must be in the future");

        Market memory market;
        market.creator = msg.sender;
        market.question = _question;
        market.creationTime = block.timestamp;
        market.closeTime = _closeTime;
        market.status = MarketStatus.Open;

        marketIdCounter++;
        markets[marketIdCounter] = market;

        emit NewMarket(marketIdCounter, msg.sender, _question);
    }

    /**
     * @notice Votes on a market.
     * @param _marketId The ID of the market to vote on.
     * @param _vote The vote to cast (true for yes, false for no).
     */
    function vote(uint256 _marketId, bool _vote) public {
        Market storage market = markets[_marketId];
        require(market.status == MarketStatus.Open, "Market is not open");
        require(market.closeTime > block.timestamp, "Market is closed");
        require(!market.voted[msg.sender], "User has already voted");

        if (_vote) {
            market.yesVotes = market.yesVotes.add(1);
        } else {
            market.noVotes = market.noVotes.add(1);
        }

        market.voted[msg.sender] = true;

        emit VoteCast(_marketId, msg.sender, _vote);
    }

    /**
     * @notice Closes a market.
     * @param _marketId The ID of the market to close.
     */
    function closeMarket(uint256 _marketId) public {
        Market storage market = markets[_marketId];
        require(market.creator == msg.sender, "Only the creator can close the market");
        require(market.status == MarketStatus.Open, "Market is not open");
        require(market.closeTime <= block.timestamp, "Market is not yet closable");

        market.status = MarketStatus.Closed;

        emit MarketClosed(_marketId);
    }

    /**
     * @notice Settles a market.
     * @param _marketId The ID of the market to settle.
     * @param _outcome The outcome of the market (true for yes, false for no).
     */
    function settleMarket(uint256 _marketId, bool _outcome) public {
        Market storage market = markets[_marketId];
        require(market.status == MarketStatus.Closed, "Market is not closed");

        market.status = MarketStatus.Settled;

        if (_outcome) {
            // Distribute tokens to yes voters
            uint256 totalVotes = market.yesVotes.add(market.noVotes);
            uint256 payout = token.balanceOf(address(this)).div(totalVotes).mul(market.yesVotes);
            for (address voter in market.voted) {
                if (market.voted[voter] && _outcome) {
                    balances[voter] = balances[voter].add(payout);
                }
            }
        } else {
            // Distribute tokens to no voters
            uint256 totalVotes = market.yesVotes.add(market.noVotes);
            uint256 payout = token.balanceOf(address(this)).div(totalVotes).mul(market.noVotes);
            for (address voter in market.voted) {
                if (market.voted[voter] && !_outcome) {
                    balances[voter] = balances[voter].add(payout);
                }
            }
        }

        emit MarketSettled(_marketId, _outcome);
    }

    /**
     * @notice Withdraws tokens from the contract.
     */
    function withdraw() public {
        uint256 balance = balances[msg.sender];
        require(balance > 0, "User has no balance");

        balances[msg.sender] = 0;
        token.transfer(msg.sender, balance);
    }
}
```
