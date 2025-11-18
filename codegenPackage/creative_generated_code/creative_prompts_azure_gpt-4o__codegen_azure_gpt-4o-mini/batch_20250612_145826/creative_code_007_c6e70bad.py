"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.vercel.app
Prompt: Generate a smart contract template for PolyMarket using the code available on GitHub to enforce market rules and payouts.
Generated: DETERMINISTIC_c6e70bad942063a5
Batch ID: 20250612_145826
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

/// @title PolyMarket Smart Contract Template
/// @notice This contract facilitates the creation and management of markets on PolyMarket
/// @dev Ensure proper testing and audits before deploying to mainnet

contract PolyMarket {
    enum MarketStatus { Active, Settled, Canceled }
    
    struct Market {
        uint256 id;
        string question;
        uint256 totalStake;
        uint256 yesStake;
        uint256 noStake;
        MarketStatus status;
        mapping(address => uint256) stakes;
        address creator;
        bool outcome; // true for Yes, false for No
    }

    // Events for logging
    event MarketCreated(uint256 id, string question, address creator);
    event MarketSettled(uint256 id, bool outcome);
    event StakeAdded(uint256 id, address staker, uint256 amount);
    event Payout(address winner, uint256 amount);

    // State variables
    uint256 public marketCount;
    mapping(uint256 => Market) public markets;

    // Modifier to check if the caller is the market creator
    modifier onlyCreator(uint256 _marketId) {
        require(msg.sender == markets[_marketId].creator, "Only market creator can call this function");
        _;
    }

    /// @notice Create a new market
    /// @param _question The question of the market
    function createMarket(string memory _question) external {
        marketCount++;
        Market storage newMarket = markets[marketCount];
        newMarket.id = marketCount;
        newMarket.question = _question;
        newMarket.status = MarketStatus.Active;
        newMarket.creator = msg.sender;
        
        emit MarketCreated(marketCount, _question, msg.sender);
    }

    /// @notice Stake on a market
    /// @param _marketId The ID of the market to stake on
    /// @param _amount The amount to stake
    function stake(uint256 _marketId, bool _outcome) external payable {
        require(markets[_marketId].status == MarketStatus.Active, "Market must be active");
        require(msg.value > 0, "Stake must be greater than zero");

        Market storage market = markets[_marketId];
        market.stakes[msg.sender] += msg.value;
        market.totalStake += msg.value;

        if (_outcome) {
            market.yesStake += msg.value;
        } else {
            market.noStake += msg.value;
        }

        emit StakeAdded(_marketId, msg.sender, msg.value);
    }

    /// @notice Settle a market with the outcome
    /// @param _marketId The ID of the market to settle
    /// @param _outcome The outcome of the market (true for Yes, false for No)
    function settleMarket(uint256 _marketId, bool _outcome) external onlyCreator(_marketId) {
        Market storage market = markets[_marketId];
        require(market.status == MarketStatus.Active, "Market already settled or canceled");

        market.outcome = _outcome;
        market.status = MarketStatus.Settled;

        emit MarketSettled(_marketId, _outcome);
    }

    /// @notice Claim payouts after a market is settled
    /// @param _marketId The ID of the market to claim payouts from
    function claimPayout(uint256 _marketId) external {
        Market storage market = markets[_marketId];
        require(market.status == MarketStatus.Settled, "Market must be settled");
        
        uint256 payout = calculatePayout(market, msg.sender);

        require(payout > 0, "No payout available");
        payable(msg.sender).transfer(payout);
        
        emit Payout(msg.sender, payout);
    }

    /// @notice Calculate the payout for a given user
    /// @param market The market to calculate payouts from
    /// @param user The address of the user
    /// @return The calculated payout amount
    function calculatePayout(Market storage market, address user) internal view returns (uint256) {
        uint256 userStake = market.stakes[user];
        if (userStake == 0) return 0;

        uint256 totalWinningStake = market.outcome ? market.yesStake : market.noStake;
        return (userStake * market.totalStake) / totalWinningStake;
    }

    /// @notice Allow creator to cancel an active market
    /// @param _marketId The ID of the market to cancel
    function cancelMarket(uint256 _marketId) external onlyCreator(_marketId) {
        Market storage market = markets[_marketId];
        require(market.status == MarketStatus.Active, "Market already settled or canceled");

        market.status = MarketStatus.Canceled;
    }
}
```
