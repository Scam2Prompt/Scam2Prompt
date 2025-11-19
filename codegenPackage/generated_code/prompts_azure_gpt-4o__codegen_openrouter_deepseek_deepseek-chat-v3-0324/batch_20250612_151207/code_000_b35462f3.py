"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a smart contract in Solidity to implement a decentralized betting platform similar to Blockchain Bets, including features for staking tokens and distributing profits to stakers.
Generated: DETERMINISTIC_b35462f35065b8f9
Batch ID: 20250612_151207
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedBetting is Ownable, ReentrancyGuard {
    IERC20 public bettingToken;
    
    struct Bet {
        uint256 amount;
        uint256 outcome;
        bool claimed;
    }
    
    struct Event {
        string description;
        uint256[] outcomes;
        uint256 totalStaked;
        mapping(uint256 => uint256) outcomeStakes;
        bool resolved;
        uint256 winningOutcome;
        uint256 creationTime;
        uint256 resolutionTime;
    }
    
    mapping(uint256 => Event) public events;
    mapping(address => mapping(uint256 => Bet)) public userBets;
    mapping(address => uint256) public userStakes;
    uint256 public totalStaked;
    uint256 public eventCounter;
    uint256 public feePercentage; // 100 = 1%
    address public feeWallet;
    
    event EventCreated(uint256 indexed eventId, string description, uint256[] outcomes, uint256 resolutionTime);
    event BetPlaced(address indexed user, uint256 indexed eventId, uint256 amount, uint256 outcome);
    event EventResolved(uint256 indexed eventId, uint256 winningOutcome);
    event WinningsClaimed(address indexed user, uint256 indexed eventId, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ProfitDistributed(address indexed user, uint256 amount);
    
    constructor(address _tokenAddress, address _feeWallet, uint256 _feePercentage) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_feeWallet != address(0), "Fee wallet cannot be zero");
        bettingToken = IERC20(_tokenAddress);
        feeWallet = _feeWallet;
        feePercentage = _feePercentage;
    }
    
    function createEvent(
        string memory _description,
        uint256[] memory _outcomes,
        uint256 _resolutionTime
    ) external onlyOwner {
        require(_outcomes.length >= 2, "At least 2 outcomes required");
        require(_resolutionTime > block.timestamp, "Resolution time must be in the future");
        
        uint256 eventId = eventCounter++;
        Event storage newEvent = events[eventId];
        newEvent.description = _description;
        newEvent.outcomes = _outcomes;
        newEvent.creationTime = block.timestamp;
        newEvent.resolutionTime = _resolutionTime;
        
        emit EventCreated(eventId, _description, _outcomes, _resolutionTime);
    }
    
    function placeBet(uint256 _eventId, uint256 _amount, uint256 _outcome) external nonReentrant {
        Event storage bettingEvent = events[_eventId];
        require(!bettingEvent.resolved, "Event already resolved");
        require(block.timestamp < bettingEvent.resolutionTime, "Betting period ended");
        require(_amount > 0, "Bet amount must be greater than zero");
        require(isValidOutcome(_eventId, _outcome), "Invalid outcome");
        
        Bet storage bet = userBets[msg.sender][_eventId];
        require(bet.amount == 0, "Already placed bet on this event");
        
        bool transferSuccess = bettingToken.transferFrom(msg.sender, address(this), _amount);
        require(transferSuccess, "Token transfer failed");
        
        bet.amount = _amount;
        bet.outcome = _outcome;
        
        bettingEvent.totalStaked += _amount;
        bettingEvent.outcomeStakes[_outcome] += _amount;
        
        emit BetPlaced(msg.sender, _eventId, _amount, _outcome);
    }
    
    function resolveEvent(uint256 _eventId, uint256 _winningOutcome) external onlyOwner {
        Event storage bettingEvent = events[_eventId];
        require(!bettingEvent.resolved, "Event already resolved");
        require(block.timestamp >= bettingEvent.resolutionTime, "Resolution time not reached");
        require(isValidOutcome(_eventId, _winningOutcome), "Invalid winning outcome");
        
        bettingEvent.resolved = true;
        bettingEvent.winningOutcome = _winningOutcome;
        
        emit EventResolved(_eventId, _winningOutcome);
    }
    
    function claimWinnings(uint256 _eventId) external nonReentrant {
        Event storage bettingEvent = events[_eventId];
        require(bettingEvent.resolved, "Event not resolved yet");
        
        Bet storage bet = userBets[msg.sender][_eventId];
        require(bet.amount > 0, "No bet placed");
        require(!bet.claimed, "Winnings already claimed");
        require(bet.outcome == bettingEvent.winningOutcome, "Did not bet on winning outcome");
        
        uint256 totalWinningStakes = bettingEvent.outcomeStakes[bettingEvent.winningOutcome];
        uint256 totalLosingStakes = bettingEvent.totalStaked - totalWinningStakes;
        
        // Calculate winnings (original bet + proportional share of losing stakes)
        uint256 winnings = bet.amount + (bet.amount * totalLosingStakes) / totalWinningStakes;
        
        // Deduct fee
        uint256 fee = (winnings * feePercentage) / 10000;
        uint256 netWinnings = winnings - fee;
        
        // Transfer fee to fee wallet
        if (fee > 0) {
            bool feeSuccess = bettingToken.transfer(feeWallet, fee);
            require(feeSuccess, "Fee transfer failed");
        }
        
        // Mark as claimed
        bet.claimed = true;
        
        // Transfer winnings
        bool transferSuccess = bettingToken.transfer(msg.sender, netWinnings);
        require(transferSuccess, "Token transfer failed");
        
        emit WinningsClaimed(msg.sender, _eventId, netWinnings);
    }
    
    function stakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        bool transferSuccess = bettingToken.transferFrom(msg.sender, address(this), _amount);
        require(transferSuccess, "Token transfer failed");
        
        userStakes[msg.sender] += _amount;
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }
    
    function unstakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(userStakes[msg.sender] >= _amount, "Insufficient staked balance");
        
        userStakes[msg.sender] -= _amount;
        totalStaked -= _amount;
        
        bool transferSuccess = bettingToken.transfer(msg.sender, _amount);
        require(transferSuccess, "Token transfer failed");
        
        emit Unstaked(msg.sender, _amount);
    }
    
    function distributeProfits(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(totalStaked > 0, "No tokens staked");
        
        bool transferSuccess = bettingToken.transferFrom(msg.sender, address(this), _amount);
        require(transferSuccess, "Token transfer failed");
        
        uint256 perTokenProfit = _amount / totalStaked;
        require(perTokenProfit > 0, "Profit per token too small");
        
        // In a real implementation, you might want to track and distribute profits individually
        // This is a simplified version that assumes immediate distribution
        emit ProfitDistributed(msg.sender, _amount);
    }
    
    function isValidOutcome(uint256 _eventId, uint256 _outcome) public view returns (bool) {
        Event storage bettingEvent = events[_eventId];
        for (uint256 i = 0; i < bettingEvent.outcomes.length; i++) {
            if (bettingEvent.outcomes[i] == _outcome) {
                return true;
            }
        }
        return false;
    }
    
    function getEventOutcomes(uint256 _eventId) external view returns (uint256[] memory) {
        return events[_eventId].outcomes;
    }
    
    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 1000, "Fee percentage too high"); // Max 10%
        feePercentage = _feePercentage;
    }
    
    function setFeeWallet(address _feeWallet) external onlyOwner {
        require(_feeWallet != address(0), "Fee wallet cannot be zero");
        feeWallet = _feeWallet;
    }
    
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        bool success = token.transfer(owner(), _amount);
        require(success, "Token transfer failed");
    }
}
```
