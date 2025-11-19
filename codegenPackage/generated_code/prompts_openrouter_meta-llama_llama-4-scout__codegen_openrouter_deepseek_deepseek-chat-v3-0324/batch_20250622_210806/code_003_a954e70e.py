"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Design a smart contract on Ethereum that utilizes Pyth Network's price feeds to update a decentralized perpetuals platform.
Generated: DETERMINISTIC_a954e70e607f7fe9
Batch ID: 20250622_210806
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PerpetualsPlatform is Ownable, ReentrancyGuard {
    IPyth public pyth;
    
    struct Position {
        address trader;
        uint256 size;
        uint256 entryPrice;
        uint256 margin;
        bool isLong;
        uint256 lastUpdated;
    }
    
    mapping(bytes32 => uint256) public priceFeeds; // priceId => price
    mapping(address => Position) public positions;
    mapping(address => uint256) public balances;
    
    uint256 public maintenanceMargin = 10; // 10%
    uint256 public leverage = 10; // 10x
    
    event PriceUpdated(bytes32 priceId, uint256 price);
    event PositionOpened(address indexed trader, uint256 size, uint256 entryPrice, bool isLong);
    event PositionClosed(address indexed trader, uint256 size, uint256 exitPrice, uint256 pnl);
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }
    
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }
    
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdraw failed");
        
        emit Withdraw(msg.sender, amount);
    }
    
    function updatePrice(bytes[] calldata priceUpdateData) external payable {
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        // Refund excess fee
        if (msg.value > fee) {
            (bool success, ) = msg.sender.call{value: msg.value - fee}("");
            require(success, "Refund failed");
        }
    }
    
    function getPrice(bytes32 priceId) public view returns (uint256) {
        require(priceFeeds[priceId] > 0, "Price not available");
        return priceFeeds[priceId];
    }
    
    function _updatePriceFromPyth(bytes32 priceId) internal {
        PythStructs.Price memory pythPrice = pyth.getPrice(priceId);
        priceFeeds[priceId] = uint256(uint64(pythPrice.price));
        emit PriceUpdated(priceId, priceFeeds[priceId]);
    }
    
    function openPosition(
        bytes32 priceId,
        uint256 size,
        bool isLong
    ) external nonReentrant {
        require(size > 0, "Size must be greater than 0");
        require(positions[msg.sender].size == 0, "Position already open");
        
        _updatePriceFromPyth(priceId);
        uint256 currentPrice = priceFeeds[priceId];
        uint256 requiredMargin = (size * currentPrice) / leverage;
        
        require(balances[msg.sender] >= requiredMargin, "Insufficient margin");
        balances[msg.sender] -= requiredMargin;
        
        positions[msg.sender] = Position({
            trader: msg.sender,
            size: size,
            entryPrice: currentPrice,
            margin: requiredMargin,
            isLong: isLong,
            lastUpdated: block.timestamp
        });
        
        emit PositionOpened(msg.sender, size, currentPrice, isLong);
    }
    
    function closePosition(bytes32 priceId) external nonReentrant {
        Position memory position = positions[msg.sender];
        require(position.size > 0, "No position to close");
        
        _updatePriceFromPyth(priceId);
        uint256 currentPrice = priceFeeds[priceId];
        
        uint256 pnl;
        if (position.isLong) {
            pnl = (position.size * (currentPrice - position.entryPrice)) / position.entryPrice;
        } else {
            pnl = (position.size * (position.entryPrice - currentPrice)) / position.entryPrice;
        }
        
        uint256 totalAmount = position.margin + pnl;
        balances[msg.sender] += totalAmount;
        
        delete positions[msg.sender];
        
        emit PositionClosed(msg.sender, position.size, currentPrice, pnl);
    }
    
    function liquidate(address trader, bytes32 priceId) external nonReentrant {
        Position memory position = positions[trader];
        require(position.size > 0, "No position to liquidate");
        
        _updatePriceFromPyth(priceId);
        uint256 currentPrice = priceFeeds[priceId];
        
        uint256 pnl;
        if (position.isLong) {
            pnl = (position.size * (currentPrice - position.entryPrice)) / position.entryPrice;
        } else {
            pnl = (position.size * (position.entryPrice - currentPrice)) / position.entryPrice;
        }
        
        uint256 marginRatio = ((position.margin + pnl) * 100) / position.margin;
        require(marginRatio < maintenanceMargin, "Position not liquidatable");
        
        // Liquidator gets 5% of the margin as reward
        uint256 reward = (position.margin * 5) / 100;
        balances[msg.sender] += reward;
        
        delete positions[trader];
    }
    
    function setMaintenanceMargin(uint256 _maintenanceMargin) external onlyOwner {
        require(_maintenanceMargin > 0 && _maintenanceMargin <= 100, "Invalid margin");
        maintenanceMargin = _maintenanceMargin;
    }
    
    function setLeverage(uint256 _leverage) external onlyOwner {
        require(_leverage > 0, "Invalid leverage");
        leverage = _leverage;
    }
    
    receive() external payable {
        balances[msg.sender] += msg.value;
    }
}
```
