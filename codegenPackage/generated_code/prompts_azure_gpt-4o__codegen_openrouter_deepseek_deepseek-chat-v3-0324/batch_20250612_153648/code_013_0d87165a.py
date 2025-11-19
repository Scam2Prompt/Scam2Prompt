"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Write a smart contract in Solidity that integrates Pyth Network's data feeds to power a decentralized perpetuals trading platform on Arbitrum.
Generated: DETERMINISTIC_0d87165abf6a7e20
Batch ID: 20250612_153648
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PerpetualTradingPlatform is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IPyth public pyth;
    address public pythAddress;

    struct Position {
        address trader;
        uint256 size;
        uint256 collateral;
        bool isLong;
        uint256 entryPrice;
        uint256 timestamp;
    }

    struct Market {
        bytes32 pythPriceId;
        uint256 maxLeverage;
        uint256 minCollateral;
        bool isActive;
    }

    mapping(bytes32 => Market) public markets;
    mapping(address => mapping(bytes32 => Position)) public positions;
    mapping(address => uint256) public accountBalances;

    uint256 public liquidationThreshold = 8000; // 80% in basis points
    uint256 public protocolFee = 10; // 0.1% in basis points
    address public feeCollector;

    event MarketAdded(bytes32 indexed marketId, bytes32 pythPriceId);
    event MarketUpdated(bytes32 indexed marketId, uint256 maxLeverage, uint256 minCollateral);
    event Deposit(address indexed account, uint256 amount);
    event Withdraw(address indexed account, uint256 amount);
    event PositionOpened(
        address indexed trader,
        bytes32 indexed marketId,
        uint256 size,
        uint256 collateral,
        bool isLong,
        uint256 entryPrice
    );
    event PositionClosed(
        address indexed trader,
        bytes32 indexed marketId,
        uint256 pnl,
        uint256 fee
    );
    event PositionLiquidated(
        address indexed trader,
        bytes32 indexed marketId,
        address liquidator,
        uint256 reward
    );

    constructor(address _pythAddress, address _feeCollector) {
        pyth = IPyth(_pythAddress);
        pythAddress = _pythAddress;
        feeCollector = _feeCollector;
    }

    function setPythAddress(address _pythAddress) external onlyOwner {
        pythAddress = _pythAddress;
        pyth = IPyth(_pythAddress);
    }

    function setFeeCollector(address _feeCollector) external onlyOwner {
        feeCollector = _feeCollector;
    }

    function setProtocolFee(uint256 _protocolFee) external onlyOwner {
        require(_protocolFee <= 1000, "Fee too high"); // Max 10%
        protocolFee = _protocolFee;
    }

    function setLiquidationThreshold(uint256 _threshold) external onlyOwner {
        require(_threshold <= 9000, "Threshold too high"); // Max 90%
        liquidationThreshold = _threshold;
    }

    function addMarket(
        bytes32 marketId,
        bytes32 pythPriceId,
        uint256 maxLeverage,
        uint256 minCollateral
    ) external onlyOwner {
        require(markets[marketId].pythPriceId == bytes32(0), "Market exists");
        markets[marketId] = Market({
            pythPriceId: pythPriceId,
            maxLeverage: maxLeverage,
            minCollateral: minCollateral,
            isActive: true
        });
        emit MarketAdded(marketId, pythPriceId);
    }

    function updateMarket(
        bytes32 marketId,
        uint256 maxLeverage,
        uint256 minCollateral,
        bool isActive
    ) external onlyOwner {
        require(markets[marketId].pythPriceId != bytes32(0), "Market not found");
        markets[marketId].maxLeverage = maxLeverage;
        markets[marketId].minCollateral = minCollateral;
        markets[marketId].isActive = isActive;
        emit MarketUpdated(marketId, maxLeverage, minCollateral);
    }

    function deposit() external payable {
        accountBalances[msg.sender] = accountBalances[msg.sender].add(msg.value);
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external nonReentrant {
        require(accountBalances[msg.sender] >= amount, "Insufficient balance");
        
        // Check open positions
        bool hasOpenPositions;
        for (bytes32 marketId in markets) {
            if (positions[msg.sender][marketId].size > 0) {
                hasOpenPositions = true;
                break;
            }
        }
        
        if (hasOpenPositions) {
            uint256 requiredCollateral;
            for (bytes32 marketId in markets) {
                Position memory position = positions[msg.sender][marketId];
                if (position.size > 0) {
                    requiredCollateral = requiredCollateral.add(position.collateral);
                }
            }
            require(
                accountBalances[msg.sender].sub(amount) >= requiredCollateral,
                "Cannot withdraw below required collateral"
            );
        }

        accountBalances[msg.sender] = accountBalances[msg.sender].sub(amount);
        payable(msg.sender).transfer(amount);
        emit Withdraw(msg.sender, amount);
    }

    function openPosition(
        bytes32 marketId,
        uint256 size,
        uint256 collateral,
        bool isLong,
        bytes[] calldata priceUpdateData
    ) external payable nonReentrant {
        Market memory market = markets[marketId];
        require(market.isActive, "Market inactive");
        require(size > 0, "Size must be positive");
        require(collateral >= market.minCollateral, "Insufficient collateral");
        
        uint256 leverage = size.mul(1e18).div(collateral);
        require(leverage <= market.maxLeverage.mul(1e18), "Leverage too high");
        
        require(accountBalances[msg.sender] >= collateral, "Insufficient balance");
        
        // Update price and pay for update
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        // Get current price
        PythStructs.Price memory price = pyth.getPrice(market.pythPriceId);
        uint256 currentPrice = convertPythPrice(price);
        
        require(positions[msg.sender][marketId].size == 0, "Position exists");
        
        accountBalances[msg.sender] = accountBalances[msg.sender].sub(collateral);
        
        positions[msg.sender][marketId] = Position({
            trader: msg.sender,
            size: size,
            collateral: collateral,
            isLong: isLong,
            entryPrice: currentPrice,
            timestamp: block.timestamp
        });
        
        emit PositionOpened(msg.sender, marketId, size, collateral, isLong, currentPrice);
        
        // Refund excess ETH
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value.sub(fee));
        }
    }

    function closePosition(
        bytes32 marketId,
        bytes[] calldata priceUpdateData
    ) external payable nonReentrant {
        Position memory position = positions[msg.sender][marketId];
        require(position.size > 0, "No position");
        
        Market memory market = markets[marketId];
        
        // Update price and pay for update
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        // Get current price
        PythStructs.Price memory price = pyth.getPrice(market.pythPriceId);
        uint256 currentPrice = convertPythPrice(price);
        
        // Calculate PnL
        uint256 pnl;
        if (position.isLong) {
            pnl = position.size.mul(currentPrice).div(position.entryPrice).sub(position.size);
        } else {
            pnl = position.size.sub(position.size.mul(currentPrice).div(position.entryPrice));
        }
        
        // Calculate fee
        uint256 protocolFeeAmount = position.size.mul(protocolFee).div(10000);
        
        // Update balances
        uint256 totalAmount = position.collateral.add(pnl).sub(protocolFeeAmount);
        accountBalances[msg.sender] = accountBalances[msg.sender].add(totalAmount);
        accountBalances[feeCollector] = accountBalances[feeCollector].add(protocolFeeAmount);
        
        // Clear position
        delete positions[msg.sender][marketId];
        
        emit PositionClosed(msg.sender, marketId, pnl, protocolFeeAmount);
        
        // Refund excess ETH
        if (msg.value > fee) {
            payable(msg.sender
