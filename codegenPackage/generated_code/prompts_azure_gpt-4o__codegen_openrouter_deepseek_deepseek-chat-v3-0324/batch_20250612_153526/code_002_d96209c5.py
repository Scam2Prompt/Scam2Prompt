"""
Generated Code Metadata:
========================
Original URL: https://gainstrade.pages.dev
Prompt: Generate Solidity code for a smart contract that enables decentralized trading of crypto, forex, and commodities with guaranteed execution, inspired by the gTrade platform's features.
Generated: DETERMINISTIC_d96209c5a41d3433
Batch ID: 20250612_153526
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract DecentralizedTrading is Ownable {
    using SafeERC20 for IERC20;

    enum AssetType { CRYPTO, FOREX, COMMODITY }
    enum PositionType { LONG, SHORT }
    enum OrderStatus { PENDING, EXECUTED, CANCELED }

    struct Asset {
        string symbol;
        AssetType assetType;
        address priceFeed;
        bool isActive;
    }

    struct Position {
        address trader;
        uint256 assetId;
        PositionType positionType;
        uint256 leverage;
        uint256 margin;
        uint256 size;
        uint256 entryPrice;
        uint256 liquidationPrice;
        uint256 openTimestamp;
        bool isOpen;
    }

    struct Order {
        address trader;
        uint256 assetId;
        PositionType positionType;
        uint256 leverage;
        uint256 margin;
        uint256 size;
        uint256 desiredPrice;
        uint256 timestamp;
        OrderStatus status;
    }

    uint256 public constant PRICE_PRECISION = 1e8;
    uint256 public constant FEE_PRECISION = 1e6;
    uint256 public constant MAX_LEVERAGE = 100;

    uint256 public tradingFee = 3000; // 0.3% in FEE_PRECISION
    uint256 public liquidationFee = 5000; // 0.5% in FEE_PRECISION
    uint256 public minMargin = 1e16; // 0.01 ETH or equivalent

    Asset[] public assets;
    Position[] public positions;
    Order[] public orders;

    mapping(address => uint256[]) public userPositions;
    mapping(address => uint256[]) public userOrders;
    mapping(address => bool) public isWhitelistedToken;

    event AssetAdded(uint256 indexed assetId, string symbol, AssetType assetType);
    event AssetStatusChanged(uint256 indexed assetId, bool isActive);
    event PositionOpened(
        uint256 indexed positionId,
        address indexed trader,
        uint256 assetId,
        PositionType positionType,
        uint256 leverage,
        uint256 margin,
        uint256 size,
        uint256 entryPrice
    );
    event PositionClosed(
        uint256 indexed positionId,
        address indexed trader,
        uint256 pnl,
        uint256 closePrice
    );
    event PositionLiquidated(
        uint256 indexed positionId,
        address indexed liquidator,
        uint256 closePrice
    );
    event OrderPlaced(
        uint256 indexed orderId,
        address indexed trader,
        uint256 assetId,
        PositionType positionType,
        uint256 leverage,
        uint256 margin,
        uint256 size,
        uint256 desiredPrice
    );
    event OrderExecuted(uint256 indexed orderId, uint256 executionPrice);
    event OrderCanceled(uint256 indexed orderId);
    event FeesUpdated(uint256 tradingFee, uint256 liquidationFee);
    event MinMarginUpdated(uint256 minMargin);

    modifier onlyActiveAsset(uint256 assetId) {
        require(assetId < assets.length, "Invalid asset ID");
        require(assets[assetId].isActive, "Asset not active");
        _;
    }

    modifier onlyValidToken(address token) {
        require(isWhitelistedToken[token], "Token not whitelisted");
        _;
    }

    function addAsset(
        string memory symbol,
        AssetType assetType,
        address priceFeed
    ) external onlyOwner {
        assets.push(Asset(symbol, assetType, priceFeed, true));
        emit AssetAdded(assets.length - 1, symbol, assetType);
    }

    function setAssetStatus(uint256 assetId, bool isActive) external onlyOwner {
        require(assetId < assets.length, "Invalid asset ID");
        assets[assetId].isActive = isActive;
        emit AssetStatusChanged(assetId, isActive);
    }

    function whitelistToken(address token, bool whitelisted) external onlyOwner {
        isWhitelistedToken[token] = whitelisted;
    }

    function setFees(uint256 _tradingFee, uint256 _liquidationFee) external onlyOwner {
        require(_tradingFee <= FEE_PRECISION / 10, "Trading fee too high");
        require(_liquidationFee <= FEE_PRECISION / 10, "Liquidation fee too high");
        tradingFee = _tradingFee;
        liquidationFee = _liquidationFee;
        emit FeesUpdated(_tradingFee, _liquidationFee);
    }

    function setMinMargin(uint256 _minMargin) external onlyOwner {
        minMargin = _minMargin;
        emit MinMarginUpdated(_minMargin);
    }

    function getLatestPrice(uint256 assetId) public view returns (uint256) {
        (, int256 price, , , ) = AggregatorV3Interface(assets[assetId].priceFeed).latestRoundData();
        return uint256(price);
    }

    function openPosition(
        uint256 assetId,
        PositionType positionType,
        uint256 leverage,
        uint256 margin,
        address collateralToken
    ) external onlyActiveAsset(assetId) onlyValidToken(collateralToken) {
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");
        require(margin >= minMargin, "Margin too low");

        IERC20(collateralToken).safeTransferFrom(msg.sender, address(this), margin);

        uint256 currentPrice = getLatestPrice(assetId);
        uint256 size = (margin * leverage) / PRICE_PRECISION;
        uint256 liquidationPrice = calculateLiquidationPrice(
            currentPrice,
            positionType,
            leverage
        );

        Position memory newPosition = Position({
            trader: msg.sender,
            assetId: assetId,
            positionType: positionType,
            leverage: leverage,
            margin: margin,
            size: size,
            entryPrice: currentPrice,
            liquidationPrice: liquidationPrice,
            openTimestamp: block.timestamp,
            isOpen: true
        });

        positions.push(newPosition);
        uint256 positionId = positions.length - 1;
        userPositions[msg.sender].push(positionId);

        emit PositionOpened(
            positionId,
            msg.sender,
            assetId,
            positionType,
            leverage,
            margin,
            size,
            currentPrice
        );
    }

    function placeOrder(
        uint256 assetId,
        PositionType positionType,
        uint256 leverage,
        uint256 margin,
        uint256 desiredPrice,
        address collateralToken
    ) external onlyActiveAsset(assetId) onlyValidToken(collateralToken) {
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");
        require(margin >= minMargin, "Margin too low");

        IERC20(collateralToken).safeTransferFrom(msg.sender, address(this), margin);

        Order memory newOrder = Order({
            trader: msg.sender,
            assetId: assetId,
            positionType: positionType,
            leverage: leverage,
            margin: margin,
            size: (margin * leverage) / PRICE_PRECISION,
            desiredPrice: desiredPrice,
            timestamp: block.timestamp,
            status: OrderStatus.PENDING
        });

        orders.push(newOrder);
        uint256 orderId = orders.length - 1;
        userOrders[msg.sender].push(orderId);

        emit OrderPlaced(
            orderId,
            msg.sender,
            assetId,
            positionType,
            leverage,
            margin,
            newOrder.size,
            desiredPrice
        );
    }

    function executeOrder(uint256 orderId) external {
        require(orderId < orders.length, "Invalid order ID");
        Order storage order = orders[orderId];
        require(order.status == OrderStatus.PENDING, "Order not pending");

        uint256 currentPrice = getLatestPrice(order.assetId);
        bool priceConditionMet = (order.positionType == PositionType.LONG && currentPrice <= order.desiredPrice) ||
            (order.positionType == PositionType.SHORT && currentPrice >= order.desiredPrice);

        require(priceConditionMet, "Price condition not met");

        order.status = OrderStatus.EXECUTED;

        uint256 liquidationPrice = calculateLiquidationPrice(
            currentPrice,
            order.positionType,
            order.leverage
        );

        Position memory newPosition = Position({
            trader: order.trader,
            assetId: order.assetId,
            positionType: order.positionType,
            leverage: order.leverage,
            margin: order.margin,
            size: order.size,
            entryPrice: currentPrice,
            liquidationPrice: liquidationPrice,
            openTimestamp: block.timestamp,
            isOpen: true
        });

        positions.push(newPosition);
        uint256 positionId = positions.length - 1;
        userPositions[order.trader].push(position
