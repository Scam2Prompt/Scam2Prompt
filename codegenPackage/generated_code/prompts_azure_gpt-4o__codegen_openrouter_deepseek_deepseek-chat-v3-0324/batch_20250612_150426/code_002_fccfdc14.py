"""
Generated Code Metadata:
========================
Original URL: https://hyperliquid.how
Prompt: Create a Solidity smart contract for managing a vault on Hyperliquid's L1, incorporating features like profit sharing, liquidation of overleveraged accounts, and automated market-making strategies.
Generated: DETERMINISTIC_fccfdc140412f2d7
Batch ID: 20250612_150426
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract HyperliquidVault is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Structs
    struct Position {
        address trader;
        uint256 collateral;
        uint256 size;
        uint256 entryPrice;
        bool isLong;
        uint256 lastUpdated;
    }

    struct ProfitShare {
        address recipient;
        uint256 share; // Basis points (10000 = 100%)
    }

    // Constants
    uint256 public constant BASIS_POINTS = 10000;
    uint256 public constant LIQUIDATION_THRESHOLD = 8500; // 85% in basis points
    uint256 public constant MAX_LEVERAGE = 10;

    // State variables
    IERC20 public baseToken;
    uint256 public totalCollateral;
    uint256 public totalShares;
    mapping(address => uint256) public shares;
    mapping(address => Position) public positions;
    ProfitShare[] public profitShares;
    uint256 public performanceFee; // Basis points

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event PositionOpened(address indexed trader, uint256 collateral, uint256 size, bool isLong);
    event PositionClosed(address indexed trader, uint256 pnl);
    event PositionLiquidated(address indexed trader, uint256 liquidatedAmount);
    event ProfitDistributed(address indexed recipient, uint256 amount);
    event PerformanceFeeCollected(uint256 amount);

    constructor(
        address _baseToken,
        uint256 _performanceFee,
        ProfitShare[] memory _profitShares
    ) {
        require(_performanceFee <= BASIS_POINTS, "Invalid performance fee");
        baseToken = IERC20(_baseToken);
        performanceFee = _performanceFee;

        for (uint256 i = 0; i < _profitShares.length; i++) {
            require(_profitShares[i].share <= BASIS_POINTS, "Invalid profit share");
            profitShares.push(_profitShares[i]);
        }
    }

    // Modifiers
    modifier onlyTrader(address trader) {
        require(positions[trader].trader == msg.sender, "Not the trader");
        _;
    }

    // External functions
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        baseToken.safeTransferFrom(msg.sender, address(this), amount);
        
        if (totalShares == 0) {
            shares[msg.sender] = amount;
            totalShares = amount;
        } else {
            uint256 newShares = (amount * totalShares) / totalCollateral;
            shares[msg.sender] += newShares;
            totalShares += newShares;
        }
        
        totalCollateral += amount;
        emit Deposit(msg.sender, amount);
    }

    function withdraw(uint256 shareAmount) external nonReentrant {
        require(shareAmount > 0 && shareAmount <= shares[msg.sender], "Invalid share amount");
        
        uint256 withdrawAmount = (shareAmount * totalCollateral) / totalShares;
        shares[msg.sender] -= shareAmount;
        totalShares -= shareAmount;
        totalCollateral -= withdrawAmount;
        
        baseToken.safeTransfer(msg.sender, withdrawAmount);
        emit Withdraw(msg.sender, withdrawAmount);
    }

    function openPosition(
        uint256 collateral,
        uint256 size,
        bool isLong
    ) external nonReentrant {
        require(collateral > 0, "Collateral must be greater than 0");
        require(size <= collateral * MAX_LEVERAGE, "Exceeds max leverage");
        require(positions[msg.sender].trader == address(0), "Position already exists");

        // In a real implementation, this would interact with Hyperliquid's L1
        // For this example, we're just storing the position
        positions[msg.sender] = Position({
            trader: msg.sender,
            collateral: collateral,
            size: size,
            entryPrice: getCurrentPrice(),
            isLong: isLong,
            lastUpdated: block.timestamp
        });

        emit PositionOpened(msg.sender, collateral, size, isLong);
    }

    function closePosition() external nonReentrant onlyTrader(msg.sender) {
        Position storage position = positions[msg.sender];
        require(position.trader != address(0), "No position exists");

        uint256 currentPrice = getCurrentPrice();
        uint256 pnl = calculatePnl(position, currentPrice);
        uint256 totalValue = position.collateral + pnl;

        // Apply performance fee if profit
        if (pnl > 0) {
            uint256 fee = (pnl * performanceFee) / BASIS_POINTS;
            totalValue -= fee;
            emit PerformanceFeeCollected(fee);
        }

        // Distribute profits according to shares
        distributeProfits(pnl);

        delete positions[msg.sender];
        emit PositionClosed(msg.sender, pnl);
    }

    function liquidatePosition(address trader) external nonReentrant {
        Position storage position = positions[trader];
        require(position.trader != address(0), "No position exists");

        uint256 currentPrice = getCurrentPrice();
        uint256 pnl = calculatePnl(position, currentPrice);
        uint256 collateralRatio = ((position.collateral + pnl) * BASIS_POINTS) / position.size;

        require(collateralRatio < LIQUIDATION_THRESHOLD, "Position not liquidatable");

        // Liquidate the position
        uint256 liquidatedAmount = position.collateral + pnl;
        delete positions[trader];
        emit PositionLiquidated(trader, liquidatedAmount);
    }

    // Internal functions
    function calculatePnl(Position memory position, uint256 currentPrice) internal pure returns (int256) {
        if (position.isLong) {
            return int256((position.size * (currentPrice - position.entryPrice)) / position.entryPrice);
        } else {
            return int256((position.size * (position.entryPrice - currentPrice)) / position.entryPrice);
        }
    }

    function distributeProfits(uint256 profit) internal {
        if (profit == 0) return;

        for (uint256 i = 0; i < profitShares.length; i++) {
            ProfitShare memory share = profitShares[i];
            uint256 amount = (profit * share.share) / BASIS_POINTS;
            if (amount > 0) {
                baseToken.safeTransfer(share.recipient, amount);
                emit ProfitDistributed(share.recipient, amount);
            }
        }
    }

    // View functions
    function getCurrentPrice() public view returns (uint256) {
        // In a real implementation, this would fetch from an oracle
        // For this example, we return a fixed price
        return 1000 * 10 ** 18; // $1000 in 18 decimals
    }

    function getPositionHealth(address trader) public view returns (uint256) {
        Position memory position = positions[trader];
        if (position.trader == address(0)) return 0;

        uint256 currentPrice = getCurrentPrice();
        int256 pnl = calculatePnl(position, currentPrice);
        uint256 collateralValue = uint256(int256(position.collateral) + pnl);

        return (collateralValue * BASIS_POINTS) / position.size;
    }

    // Admin functions
    function setPerformanceFee(uint256 newFee) external onlyOwner {
        require(newFee <= BASIS_POINTS, "Invalid performance fee");
        performanceFee = newFee;
    }

    function addProfitShare(address recipient, uint256 share) external onlyOwner {
        require(share <= BASIS_POINTS, "Invalid profit share");
        profitShares.push(ProfitShare(recipient, share));
    }

    function removeProfitShare(uint256 index) external onlyOwner {
        require(index < profitShares.length, "Invalid index");
        profitShares[index] = profitShares[profitShares.length - 1];
        profitShares.pop();
    }

    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
