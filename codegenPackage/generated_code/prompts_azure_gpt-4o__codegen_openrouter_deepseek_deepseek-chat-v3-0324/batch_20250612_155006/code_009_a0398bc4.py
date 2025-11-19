"""
Generated Code Metadata:
========================
Original URL: https://lotto.exchange
Prompt: Write a smart contract in Solidity to integrate a lottery system with Uniswap, similar to Lotto Exchange.
Generated: DETERMINISTIC_a0398bc4a0686853
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LotteryExchange is Ownable {
    IERC20 public token;
    IUniswapV2Router02 public uniswapRouter;
    
    uint256 public ticketPrice;
    uint256 public maxTicketsPerUser;
    uint256 public lotteryDuration;
    uint256 public lotteryStartTime;
    uint256 public lotteryId;
    
    uint256 public prizePool;
    uint256 public totalTicketsSold;
    
    mapping(uint256 => mapping(address => uint256)) public ticketsBought;
    mapping(uint256 => address[]) public participants;
    mapping(uint256 => address) public winners;
    
    event LotteryStarted(uint256 indexed lotteryId, uint256 startTime, uint256 duration);
    event TicketPurchased(address indexed buyer, uint256 amount, uint256 lotteryId);
    event LotteryEnded(uint256 indexed lotteryId, address winner, uint256 prize);
    event PrizeDistributed(address indexed winner, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    constructor(
        address _tokenAddress,
        address _uniswapRouter,
        uint256 _ticketPrice,
        uint256 _maxTicketsPerUser,
        uint256 _lotteryDuration
    ) {
        token = IERC20(_tokenAddress);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        ticketPrice = _ticketPrice;
        maxTicketsPerUser = _maxTicketsPerUser;
        lotteryDuration = _lotteryDuration;
    }
    
    function startLottery() external onlyOwner {
        require(lotteryStartTime == 0 || block.timestamp > lotteryStartTime + lotteryDuration, "Previous lottery not ended");
        
        lotteryId++;
        lotteryStartTime = block.timestamp;
        prizePool = 0;
        totalTicketsSold = 0;
        
        emit LotteryStarted(lotteryId, lotteryStartTime, lotteryDuration);
    }
    
    function buyTickets(uint256 _numberOfTickets) external {
        require(lotteryStartTime > 0, "Lottery not started");
        require(block.timestamp < lotteryStartTime + lotteryDuration, "Lottery ended");
        require(_numberOfTickets > 0, "Invalid ticket amount");
        require(ticketsBought[lotteryId][msg.sender] + _numberOfTickets <= maxTicketsPerUser, "Exceeds max tickets");
        
        uint256 totalCost = _numberOfTickets * ticketPrice;
        require(token.transferFrom(msg.sender, address(this), totalCost), "Token transfer failed");
        
        ticketsBought[lotteryId][msg.sender] += _numberOfTickets;
        totalTicketsSold += _numberOfTickets;
        prizePool += totalCost;
        
        for (uint256 i = 0; i < _numberOfTickets; i++) {
            participants[lotteryId].push(msg.sender);
        }
        
        emit TicketPurchased(msg.sender, _numberOfTickets, lotteryId);
    }
    
    function endLottery() external onlyOwner {
        require(lotteryStartTime > 0, "Lottery not started");
        require(block.timestamp >= lotteryStartTime + lotteryDuration, "Lottery not ended");
        require(prizePool > 0, "No prize pool");
        
        if (participants[lotteryId].length > 0) {
            uint256 randomIndex = _generateRandomNumber() % participants[lotteryId].length;
            address winner = participants[lotteryId][randomIndex];
            winners[lotteryId] = winner;
            
            uint256 prizeAmount = prizePool;
            prizePool = 0;
            
            require(token.transfer(winner, prizeAmount), "Prize transfer failed");
            
            emit LotteryEnded(lotteryId, winner, prizeAmount);
            emit PrizeDistributed(winner, prizeAmount);
        }
    }
    
    function _generateRandomNumber() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, participants[lotteryId].length)));
    }
    
    function swapTokensForETH(uint256 _amountIn) external onlyOwner {
        require(_amountIn > 0, "Invalid amount");
        require(token.transferFrom(msg.sender, address(this), _amountIn), "Transfer failed");
        
        token.approve(address(uniswapRouter), _amountIn);
        
        address[] memory path = new address[](2);
        path[0] = address(token);
        path[1] = uniswapRouter.WETH();
        
        uniswapRouter.swapExactTokensForETH(
            _amountIn,
            0,
            path,
            address(this),
            block.timestamp
        );
    }
    
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "ETH transfer failed");
        
        emit FundsWithdrawn(owner(), balance);
    }
    
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Invalid amount");
        require(token.transfer(owner(), _amount), "Token transfer failed");
        
        emit FundsWithdrawn(owner(), _amount);
    }
    
    function getParticipants(uint256 _lotteryId) external view returns (address[] memory) {
        return participants[_lotteryId];
    }
    
    function getCurrentLotteryInfo() external view returns (
        uint256 currentLotteryId,
        uint256 startTime,
        uint256 endTime,
        uint256 currentPrizePool,
        uint256 ticketsSold
    ) {
        return (
            lotteryId,
            lotteryStartTime,
            lotteryStartTime + lotteryDuration,
            prizePool,
            totalTicketsSold
        );
    }
}
```
