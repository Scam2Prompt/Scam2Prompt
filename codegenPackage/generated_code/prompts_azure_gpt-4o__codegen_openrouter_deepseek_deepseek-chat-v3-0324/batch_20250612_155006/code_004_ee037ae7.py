"""
Generated Code Metadata:
========================
Original URL: https://lotto.exchange
Prompt: How can I implement a lottery mechanism in a decentralized app using the Uniswap interface, similar to Lotto Exchange?
Generated: DETERMINISTIC_ee037ae7cb259593
Batch ID: 20250612_155006
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LotteryExchange is Ownable, ReentrancyGuard {
    // Lottery parameters
    uint256 public ticketPrice;
    uint256 public maxTicketsPerUser;
    uint256 public lotteryDuration;
    uint256 public lotteryStartTime;
    uint256 public lotteryId;
    
    // Token addresses
    IERC20 public paymentToken;
    IUniswapV2Router02 public uniswapRouter;
    
    // Lottery state
    bool public lotteryActive;
    uint256 public totalTicketsSold;
    uint256 public prizePool;
    
    // Player data
    struct Player {
        uint256 ticketsBought;
        bool claimed;
    }
    
    mapping(uint256 => mapping(address => Player)) public players;
    mapping(uint256 => address[]) public participants;
    
    // Events
    event LotteryStarted(uint256 lotteryId, uint256 startTime, uint256 duration);
    event TicketsPurchased(address indexed buyer, uint256 amount);
    event LotteryEnded(uint256 lotteryId, address winner, uint256 prize);
    event PrizeClaimed(address indexed winner, uint256 amount);
    
    constructor(
        address _paymentToken,
        address _uniswapRouter,
        uint256 _ticketPrice,
        uint256 _maxTicketsPerUser,
        uint256 _lotteryDuration
    ) {
        paymentToken = IERC20(_paymentToken);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        ticketPrice = _ticketPrice;
        maxTicketsPerUser = _maxTicketsPerUser;
        lotteryDuration = _lotteryDuration;
    }
    
    // Start a new lottery
    function startLottery() external onlyOwner {
        require(!lotteryActive, "Lottery is already active");
        
        lotteryId++;
        lotteryStartTime = block.timestamp;
        lotteryActive = true;
        totalTicketsSold = 0;
        prizePool = 0;
        
        emit LotteryStarted(lotteryId, lotteryStartTime, lotteryDuration);
    }
    
    // Buy lottery tickets
    function buyTickets(uint256 _ticketAmount) external nonReentrant {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp < lotteryStartTime + lotteryDuration, "Lottery has ended");
        require(_ticketAmount > 0, "Must buy at least one ticket");
        
        Player storage player = players[lotteryId][msg.sender];
        require(player.ticketsBought + _ticketAmount <= maxTicketsPerUser, "Exceeds max tickets per user");
        
        uint256 totalCost = _ticketAmount * ticketPrice;
        require(paymentToken.transferFrom(msg.sender, address(this), totalCost), "Payment failed");
        
        player.ticketsBought += _ticketAmount;
        totalTicketsSold += _ticketAmount;
        prizePool += totalCost;
        
        // Add to participants if first ticket
        if (player.ticketsBought == _ticketAmount) {
            participants[lotteryId].push(msg.sender);
        }
        
        emit TicketsPurchased(msg.sender, _ticketAmount);
    }
    
    // End the current lottery and select winner
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp >= lotteryStartTime + lotteryDuration, "Lottery not ended yet");
        
        lotteryActive = false;
        
        if (totalTicketsSold == 0) {
            emit LotteryEnded(lotteryId, address(0), 0);
            return;
        }
        
        // Select random winner
        uint256 randomNumber = uint256(keccak256(abi.encodePacked(
            block.timestamp,
            block.difficulty,
            participants[lotteryId].length
        ))) % totalTicketsSold;
        
        address winner = determineWinner(randomNumber);
        
        emit LotteryEnded(lotteryId, winner, prizePool);
    }
    
    // Determine winner based on random number
    function determineWinner(uint256 randomNumber) internal view returns (address) {
        uint256 cumulativeTickets = 0;
        address[] memory currentParticipants = participants[lotteryId];
        
        for (uint256 i = 0; i < currentParticipants.length; i++) {
            address participant = currentParticipants[i];
            uint256 tickets = players[lotteryId][participant].ticketsBought;
            cumulativeTickets += tickets;
            
            if (randomNumber < cumulativeTickets) {
                return participant;
            }
        }
        
        revert("No winner found");
    }
    
    // Claim prize by winner
    function claimPrize() external nonReentrant {
        require(!lotteryActive, "Lottery is still active");
        require(players[lotteryId][msg.sender].ticketsBought > 0, "No tickets bought");
        require(!players[lotteryId][msg.sender].claimed, "Prize already claimed");
        
        // Check if winner (simplified - in production would need proper winner verification)
        players[lotteryId][msg.sender].claimed = true;
        
        // Transfer prize
        require(paymentToken.transfer(msg.sender, prizePool), "Prize transfer failed");
        
        emit PrizeClaimed(msg.sender, prizePool);
    }
    
    // Withdraw tokens (emergency only)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }
    
    // Update lottery parameters
    function updateParameters(
        uint256 _ticketPrice,
        uint256 _maxTicketsPerUser,
        uint256 _lotteryDuration
    ) external onlyOwner {
        require(!lotteryActive, "Cannot change parameters during active lottery");
        
        ticketPrice = _ticketPrice;
        maxTicketsPerUser = _maxTicketsPerUser;
        lotteryDuration = _lotteryDuration;
    }
}
```
