"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Create a Solidity contract for a lottery system tied to a meme-based cryptocurrency token, referencing the "Rich Pepe" special meme lottery concept.
Generated: DETERMINISTIC_0906640f2cb9e6eb
Batch ID: 20250612_153420
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

contract RichPepeLottery is Ownable, ReentrancyGuard {
    IERC20 public memeToken;
    uint256 public ticketPrice;
    uint256 public lotteryDuration;
    uint256 public lotteryStartTime;
    uint256 public lotteryId;
    uint256 public prizePool;
    uint256 public maxTicketsPerUser;
    
    struct Lottery {
        uint256 id;
        uint256 startTime;
        uint256 endTime;
        uint256 prizePool;
        address[] participants;
        address winner;
        bool claimed;
    }
    
    mapping(uint256 => Lottery) public lotteries;
    mapping(uint256 => mapping(address => uint256)) public ticketsBought;
    mapping(address => uint256) public winnings;
    
    event LotteryStarted(uint256 indexed lotteryId, uint256 startTime, uint256 endTime);
    event TicketPurchased(uint256 indexed lotteryId, address indexed buyer, uint256 amount);
    event WinnerSelected(uint256 indexed lotteryId, address indexed winner, uint256 prize);
    event PrizeClaimed(uint256 indexed lotteryId, address indexed winner, uint256 amount);
    
    constructor(
        address _memeToken,
        uint256 _ticketPrice,
        uint256 _lotteryDuration,
        uint256 _maxTicketsPerUser
    ) {
        require(_memeToken != address(0), "Invalid token address");
        require(_ticketPrice > 0, "Ticket price must be > 0");
        require(_lotteryDuration > 0, "Duration must be > 0");
        
        memeToken = IERC20(_memeToken);
        ticketPrice = _ticketPrice;
        lotteryDuration = _lotteryDuration;
        maxTicketsPerUser = _maxTicketsPerUser;
    }
    
    function startLottery() external onlyOwner {
        require(block.timestamp >= lotteryStartTime + lotteryDuration || lotteryStartTime == 0, "Previous lottery not ended");
        
        lotteryId++;
        lotteryStartTime = block.timestamp;
        
        lotteries[lotteryId] = Lottery({
            id: lotteryId,
            startTime: block.timestamp,
            endTime: block.timestamp + lotteryDuration,
            prizePool: prizePool,
            participants: new address[](0),
            winner: address(0),
            claimed: false
        });
        
        prizePool = 0;
        
        emit LotteryStarted(lotteryId, block.timestamp, block.timestamp + lotteryDuration);
    }
    
    function buyTickets(uint256 _amount) external nonReentrant {
        require(block.timestamp < lotteries[lotteryId].endTime, "Lottery ended");
        require(_amount > 0, "Must buy at least 1 ticket");
        require(ticketsBought[lotteryId][msg.sender] + _amount <= maxTicketsPerUser, "Exceeds max tickets per user");
        
        uint256 totalCost = ticketPrice * _amount;
        require(memeToken.transferFrom(msg.sender, address(this), totalCost), "Token transfer failed");
        
        prizePool += totalCost;
        lotteries[lotteryId].prizePool += totalCost;
        
        for (uint256 i = 0; i < _amount; i++) {
            lotteries[lotteryId].participants.push(msg.sender);
        }
        
        ticketsBought[lotteryId][msg.sender] += _amount;
        
        emit TicketPurchased(lotteryId, msg.sender, _amount);
    }
    
    function selectWinner() external onlyOwner {
        require(block.timestamp >= lotteries[lotteryId].endTime, "Lottery not ended");
        require(lotteries[lotteryId].participants.length > 0, "No participants");
        require(lotteries[lotteryId].winner == address(0), "Winner already selected");
        
        uint256 randomIndex = uint256(
            keccak256(
                abi.encodePacked(
                    block.difficulty,
                    block.timestamp,
                    lotteries[lotteryId].participants.length
                )
            )
        ) % lotteries[lotteryId].participants.length;
        
        address winner = lotteries[lotteryId].participants[randomIndex];
        lotteries[lotteryId].winner = winner;
        winnings[winner] += lotteries[lotteryId].prizePool;
        
        emit WinnerSelected(lotteryId, winner, lotteries[lotteryId].prizePool);
    }
    
    function claimPrize(uint256 _lotteryId) external nonReentrant {
        require(lotteries[_lotteryId].winner == msg.sender, "Not the winner");
        require(!lotteries[_lotteryId].claimed, "Prize already claimed");
        require(winnings[msg.sender] > 0, "No winnings to claim");
        
        uint256 amount = winnings[msg.sender];
        winnings[msg.sender] = 0;
        lotteries[_lotteryId].claimed = true;
        
        require(memeToken.transfer(msg.sender, amount), "Token transfer failed");
        
        emit PrizeClaimed(_lotteryId, msg.sender, amount);
    }
    
    function setTicketPrice(uint256 _ticketPrice) external onlyOwner {
        require(_ticketPrice > 0, "Ticket price must be > 0");
        ticketPrice = _ticketPrice;
    }
    
    function setLotteryDuration(uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be > 0");
        lotteryDuration = _duration;
    }
    
    function setMaxTicketsPerUser(uint256 _maxTickets) external onlyOwner {
        maxTicketsPerUser = _maxTickets;
    }
    
    function getParticipants(uint256 _lotteryId) external view returns (address[] memory) {
        return lotteries[_lotteryId].participants;
    }
    
    function getParticipantCount(uint256 _lotteryId) external view returns (uint256) {
        return lotteries[_lotteryId].participants.length;
    }
    
    function getCurrentLottery() external view returns (Lottery memory) {
        return lotteries[lotteryId];
    }
}
```
