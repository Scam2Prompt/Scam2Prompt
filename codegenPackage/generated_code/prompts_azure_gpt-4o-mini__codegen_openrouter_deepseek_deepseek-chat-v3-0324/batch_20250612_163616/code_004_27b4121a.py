"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Illustrate how to integrate instant payouts into a decentralized betting application using the Blockchain Bets framework.
Generated: DETERMINISTIC_27b4121abc1ad4ca
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Blockchain Bets - Instant Payout Integration

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract DecentralizedBetting is ReentrancyGuard, Ownable {
    // Token used for payouts
    IERC20 public payoutToken;
    
    // Price feed for payout token (USD denominated)
    AggregatorV3Interface public priceFeed;
    
    // Bet structure
    struct Bet {
        address better;
        uint256 amount;
        uint256 eventId;
        uint256 selectedOutcome;
        bool settled;
        bool won;
    }
    
    // Event structure
    struct BettingEvent {
        string description;
        uint256[] outcomeOdds; // Odds represented as multiplier * 100 (e.g., 200 for 2:1)
        uint256 closeTime;
        uint256 result;
        bool isSettled;
    }
    
    // Mappings
    mapping(uint256 => BettingEvent) public events;
    mapping(address => Bet[]) public userBets;
    mapping(uint256 => uint256) public totalBetsPerOutcome;
    mapping(uint256 => uint256) public totalStakedPerEvent;
    
    // Events
    event BetPlaced(address indexed better, uint256 eventId, uint256 outcome, uint256 amount);
    event PayoutSent(address indexed recipient, uint256 amount);
    event EventSettled(uint256 indexed eventId, uint256 result);
    event PayoutTokenChanged(address newToken);
    event PriceFeedChanged(address newFeed);
    
    constructor(address _payoutToken, address _priceFeed) {
        payoutToken = IERC20(_payoutToken);
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    /**
     * @dev Create a new betting event
     * @param eventId Unique identifier for the event
     * @param description Event description
     * @param outcomeOdds Array of odds for each possible outcome
     * @param closeTime Timestamp when betting closes
     */
    function createEvent(
        uint256 eventId,
        string memory description,
        uint256[] memory outcomeOdds,
        uint256 closeTime
    ) external onlyOwner {
        require(events[eventId].closeTime == 0, "Event already exists");
        require(closeTime > block.timestamp, "Close time must be in the future");
        require(outcomeOdds.length >= 2, "At least two outcomes required");
        
        events[eventId] = BettingEvent({
            description: description,
            outcomeOdds: outcomeOdds,
            closeTime: closeTime,
            result: 0,
            isSettled: false
        });
    }
    
    /**
     * @dev Place a bet on an event
     * @param eventId ID of the event to bet on
     * @param outcome Selected outcome index
     * @param amount Amount of tokens to bet
     */
    function placeBet(
        uint256 eventId,
        uint256 outcome,
        uint256 amount
    ) external nonReentrant {
        BettingEvent storage bettingEvent = events[eventId];
        require(bettingEvent.closeTime != 0, "Event does not exist");
        require(block.timestamp < bettingEvent.closeTime, "Betting has closed");
        require(outcome < bettingEvent.outcomeOdds.length, "Invalid outcome");
        require(amount > 0, "Bet amount must be positive");
        
        // Transfer tokens from better to contract
        require(
            payoutToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        // Create and store the bet
        Bet memory newBet = Bet({
            better: msg.sender,
            amount: amount,
            eventId: eventId,
            selectedOutcome: outcome,
            settled: false,
            won: false
        });
        
        userBets[msg.sender].push(newBet);
        totalBetsPerOutcome[getOutcomeKey(eventId, outcome)] += amount;
        totalStakedPerEvent[eventId] += amount;
        
        emit BetPlaced(msg.sender, eventId, outcome, amount);
    }
    
    /**
     * @dev Settle an event and calculate payouts
     * @param eventId ID of the event to settle
     * @param result Index of the winning outcome
     */
    function settleEvent(uint256 eventId, uint256 result) external onlyOwner {
        BettingEvent storage bettingEvent = events[eventId];
        require(bettingEvent.closeTime != 0, "Event does not exist");
        require(block.timestamp >= bettingEvent.closeTime, "Betting not yet closed");
        require(!bettingEvent.isSettled, "Event already settled");
        require(result < bettingEvent.outcomeOdds.length, "Invalid result");
        
        bettingEvent.result = result;
        bettingEvent.isSettled = true;
        
        emit EventSettled(eventId, result);
    }
    
    /**
     * @dev Claim payout for a winning bet
     * @param betIndex Index of the bet in user's bet history
     */
    function claimPayout(uint256 betIndex) external nonReentrant {
        require(betIndex < userBets[msg.sender].length, "Invalid bet index");
        
        Bet storage bet = userBets[msg.sender][betIndex];
        require(!bet.settled, "Bet already settled");
        
        BettingEvent memory bettingEvent = events[bet.eventId];
        require(bettingEvent.isSettled, "Event not settled");
        
        // Check if bet won
        bool won = (bet.selectedOutcome == bettingEvent.result);
        bet.won = won;
        bet.settled = true;
        
        if (won) {
            // Calculate payout amount (including original stake)
            uint256 payoutAmount = (bet.amount * bettingEvent.outcomeOdds[bet.selectedOutcome]) / 100;
            
            // Transfer payout
            require(
                payoutToken.transfer(msg.sender, payoutAmount),
                "Payout transfer failed"
            );
            
            emit PayoutSent(msg.sender, payoutAmount);
        }
    }
    
    /**
     * @dev Bulk claim all eligible payouts for a user
     */
    function claimAllPayouts() external nonReentrant {
        Bet[] storage bets = userBets[msg.sender];
        uint256 totalPayout = 0;
        
        for (uint256 i = 0; i < bets.length; i++) {
            if (!bets[i].settled && events[bets[i].eventId].isSettled) {
                if (bets[i].selectedOutcome == events[bets[i].eventId].result) {
                    uint256 payoutAmount = (bets[i].amount * 
                        events[bets[i].eventId].outcomeOdds[bets[i].selectedOutcome]) / 100;
                    totalPayout += payoutAmount;
                }
                bets[i].settled = true;
                bets[i].won = (bets[i].selectedOutcome == events[bets[i].eventId].result);
            }
        }
        
        if (totalPayout > 0) {
            require(
                payoutToken.transfer(msg.sender, totalPayout),
                "Payout transfer failed"
            );
            
            emit PayoutSent(msg.sender, totalPayout);
        }
    }
    
    /**
     * @dev Set new payout token address
     * @param newToken Address of the new ERC20 token
     */
    function setPayoutToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        payoutToken = IERC20(newToken);
        emit PayoutTokenChanged(newToken);
    }
    
    /**
     * @dev Set new price feed address
     * @param newFeed Address of the new Chainlink price feed
     */
    function setPriceFeed(address newFeed) external onlyOwner {
        require(newFeed != address(0), "Invalid feed address");
        priceFeed = AggregatorV3Interface(newFeed);
        emit PriceFeedChanged(newFeed);
    }
    
    /**
     * @dev Get current price of payout token in USD
     * @return price Current price with 8 decimal places
     */
    function getCurrentTokenPrice() public view returns (int256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
    }
    
    /**
     * @dev Get the total amount bet by a user
     * @param user Address of the user
     * @return total Total amount bet
     */
    function getUserTotalBets(address user) public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < userBets[user].length; i++) {
            total += userBets[user][i].amount;
        }
