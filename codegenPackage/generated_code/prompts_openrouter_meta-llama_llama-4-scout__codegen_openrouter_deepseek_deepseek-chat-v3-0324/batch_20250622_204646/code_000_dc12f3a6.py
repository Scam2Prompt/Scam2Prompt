"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized betting platform that utilizes token staking and instant payouts, similar to Blockchain Bets Club.
Generated: DETERMINISTIC_dc12f3a6c56792ec
Batch ID: 20250622_204646
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
        address bettor;
        uint256 amount;
        uint256 selectedOption;
        bool claimed;
    }
    
    struct Event {
        string name;
        uint256[] options;
        uint256 winningOption;
        bool isSettled;
        uint256 totalStaked;
        mapping(uint256 => uint256) optionStakes;
    }
    
    mapping(uint256 => Event) public events;
    mapping(uint256 => mapping(address => Bet)) public bets;
    mapping(address => uint256[]) public userEvents;
    
    uint256 public eventCount;
    uint256 public platformFee; // Basis points (e.g., 100 = 1%)
    address public feeRecipient;
    
    event EventCreated(uint256 eventId, string name, uint256[] options);
    event BetPlaced(uint256 eventId, address bettor, uint256 amount, uint256 selectedOption);
    event EventSettled(uint256 eventId, uint256 winningOption);
    event WinningsClaimed(uint256 eventId, address bettor, uint256 amount);
    
    constructor(address _tokenAddress, uint256 _platformFee, address _feeRecipient) {
        bettingToken = IERC20(_tokenAddress);
        platformFee = _platformFee;
        feeRecipient = _feeRecipient;
    }
    
    function createEvent(string memory _name, uint256[] memory _options) external onlyOwner {
        require(_options.length >= 2, "At least 2 options required");
        
        uint256 eventId = eventCount++;
        Event storage newEvent = events[eventId];
        newEvent.name = _name;
        newEvent.options = _options;
        
        emit EventCreated(eventId, _name, _options);
    }
    
    function placeBet(uint256 _eventId, uint256 _amount, uint256 _selectedOption) external nonReentrant {
        Event storage bettingEvent = events[_eventId];
        require(!bettingEvent.isSettled, "Event already settled");
        require(_selectedOption < bettingEvent.options.length, "Invalid option");
        
        Bet storage userBet = bets[_eventId][msg.sender];
        require(userBet.amount == 0, "Already placed bet on this event");
        
        require(bettingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        
        userBet.bettor = msg.sender;
        userBet.amount = _amount;
        userBet.selectedOption = _selectedOption;
        
        bettingEvent.totalStaked += _amount;
        bettingEvent.optionStakes[_selectedOption] += _amount;
        
        userEvents[msg.sender].push(_eventId);
        
        emit BetPlaced(_eventId, msg.sender, _amount, _selectedOption);
    }
    
    function settleEvent(uint256 _eventId, uint256 _winningOption) external onlyOwner {
        Event storage bettingEvent = events[_eventId];
        require(!bettingEvent.isSettled, "Event already settled");
        require(_winningOption < bettingEvent.options.length, "Invalid winning option");
        
        bettingEvent.winningOption = _winningOption;
        bettingEvent.isSettled = true;
        
        emit EventSettled(_eventId, _winningOption);
    }
    
    function claimWinnings(uint256 _eventId) external nonReentrant {
        Event storage bettingEvent = events[_eventId];
        require(bettingEvent.isSettled, "Event not settled yet");
        
        Bet storage userBet = bets[_eventId][msg.sender];
        require(userBet.amount > 0, "No bet placed");
        require(!userBet.claimed, "Already claimed");
        require(userBet.selectedOption == bettingEvent.winningOption, "Didn't win this bet");
        
        uint256 totalStakedOnWinningOption = bettingEvent.optionStakes[bettingEvent.winningOption];
        uint256 totalStakedOnLosingOptions = bettingEvent.totalStaked - totalStakedOnWinningOption;
        
        uint256 platformCut = (totalStakedOnLosingOptions * platformFee) / 10000;
        uint256 winningPool = totalStakedOnLosingOptions - platformCut;
        
        uint256 userShare = (userBet.amount * winningPool) / totalStakedOnWinningOption;
        uint256 payout = userBet.amount + userShare;
        
        userBet.claimed = true;
        
        if (platformCut > 0) {
            require(bettingToken.transfer(feeRecipient, platformCut), "Fee transfer failed");
        }
        
        require(bettingToken.transfer(msg.sender, payout), "Payout transfer failed");
        
        emit WinningsClaimed(_eventId, msg.sender, payout);
    }
    
    function updatePlatformFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee too high"); // Max 10%
        platformFee = _newFee;
    }
    
    function updateFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid address");
        feeRecipient = _newRecipient;
    }
    
    function getUserBets(address _user) external view returns (uint256[] memory) {
        return userEvents[_user];
    }
    
    function getEventOptions(uint256 _eventId) external view returns (uint256[] memory) {
        return events[_eventId].options;
    }
}
```
