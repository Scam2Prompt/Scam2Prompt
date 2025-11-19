"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: Generate a smart contract in Solidity for a cryptocurrency lottery system, inspired by the MyLottoCoin example mentioned on the Binance Wallet Consulting page.
Generated: DETERMINISTIC_688c172a9ae18580
Batch ID: 20250612_150947
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LottoCoinLottery is Ownable, ReentrancyGuard {
    // Lottery parameters
    uint256 public ticketPrice;
    uint256 public maxTicketsPerUser;
    uint256 public lotteryDuration;
    uint256 public lotteryStartTime;
    uint256 public lotteryEndTime;
    
    // Lottery state
    bool public lotteryActive;
    uint256 public totalTicketsSold;
    address[] public participants;
    address public winningAddress;
    uint256 public winningAmount;
    
    // Token contract
    IERC20 public lottoToken;
    
    // User ticket tracking
    mapping(address => uint256) public userTickets;
    
    // Events
    event LotteryStarted(uint256 startTime, uint256 endTime);
    event TicketPurchased(address indexed buyer, uint256 tickets);
    event LotteryEnded(address indexed winner, uint256 amount);
    event PrizeClaimed(address indexed winner, uint256 amount);
    
    constructor(
        address _lottoToken,
        uint256 _ticketPrice,
        uint256 _maxTicketsPerUser,
        uint256 _lotteryDuration
    ) {
        require(_lottoToken != address(0), "Invalid token address");
        require(_ticketPrice > 0, "Ticket price must be > 0");
        require(_maxTicketsPerUser > 0, "Max tickets per user must be > 0");
        require(_lotteryDuration > 0, "Lottery duration must be > 0");
        
        lottoToken = IERC20(_lottoToken);
        ticketPrice = _ticketPrice;
        maxTicketsPerUser = _maxTicketsPerUser;
        lotteryDuration = _lotteryDuration;
    }
    
    // Start a new lottery
    function startLottery() external onlyOwner {
        require(!lotteryActive, "Lottery is already active");
        require(lottoToken.balanceOf(address(this)) > 0, "No prize funds available");
        
        lotteryStartTime = block.timestamp;
        lotteryEndTime = block.timestamp + lotteryDuration;
        lotteryActive = true;
        
        // Reset previous lottery data
        delete participants;
        totalTicketsSold = 0;
        winningAddress = address(0);
        winningAmount = 0;
        
        emit LotteryStarted(lotteryStartTime, lotteryEndTime);
    }
    
    // Purchase lottery tickets
    function buyTickets(uint256 _ticketCount) external nonReentrant {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp < lotteryEndTime, "Lottery has ended");
        require(_ticketCount > 0, "Must buy at least 1 ticket");
        require(
            userTickets[msg.sender] + _ticketCount <= maxTicketsPerUser,
            "Exceeds max tickets per user"
        );
        
        uint256 totalCost = ticketPrice * _ticketCount;
        require(
            lottoToken.transferFrom(msg.sender, address(this), totalCost),
            "Token transfer failed"
        );
        
        // Add user to participants if this is their first ticket
        if (userTickets[msg.sender] == 0) {
            participants.push(msg.sender);
        }
        
        userTickets[msg.sender] += _ticketCount;
        totalTicketsSold += _ticketCount;
        
        emit TicketPurchased(msg.sender, _ticketCount);
    }
    
    // End the lottery and select winner
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp >= lotteryEndTime, "Lottery has not ended yet");
        
        lotteryActive = false;
        
        if (participants.length > 0) {
            // Select random winner
            uint256 randomIndex = _getRandomNumber() % participants.length;
            winningAddress = participants[randomIndex];
            winningAmount = lottoToken.balanceOf(address(this));
            
            emit LotteryEnded(winningAddress, winningAmount);
        }
    }
    
    // Claim prize by winner
    function claimPrize() external nonReentrant {
        require(!lotteryActive, "Lottery is still active");
        require(msg.sender == winningAddress, "You are not the winner");
        require(winningAmount > 0, "No prize to claim");
        
        uint256 prizeAmount = winningAmount;
        winningAmount = 0;
        
        require(
            lottoToken.transfer(msg.sender, prizeAmount),
            "Prize transfer failed"
        );
        
        emit PrizeClaimed(msg.sender, prizeAmount);
    }
    
    // Emergency withdraw funds (only owner)
    function emergencyWithdraw() external onlyOwner {
        require(!lotteryActive, "Lottery is active");
        uint256 balance = lottoToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        require(
            lottoToken.transfer(owner(), balance),
            "Withdrawal failed"
        );
    }
    
    // Get random number (not truly random, but sufficient for demo)
    function _getRandomNumber() private view returns (uint256) {
        return uint256(
            keccak256(
                abi.encodePacked(
                    block.difficulty,
                    block.timestamp,
                    participants.length
                )
            )
        );
    }
    
    // Get participant count
    function getParticipantCount() external view returns (uint256) {
        return participants.length;
    }
    
    // Get contract token balance
    function getPrizePool() external view returns (uint256) {
        return lottoToken.balanceOf(address(this));
    }
}
```
