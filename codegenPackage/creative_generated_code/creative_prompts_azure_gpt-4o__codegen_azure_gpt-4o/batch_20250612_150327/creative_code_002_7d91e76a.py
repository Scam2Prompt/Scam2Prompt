"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Implement a TWAMM (Time-Weighted Average Market Maker) using Fraxswap's constant product invariant (xy=k) in a Solidity smart contract. Include functionality for conducting large trades over extended periods.
Generated: DETERMINISTIC_7d91e76a7a5112f2
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TWAMM (Time-Weighted Average Market Maker) Implementation
 * @dev Implements TWAMM using Fraxswap's constant product invariant (xy=k).
 * Allows large trades to be split and executed over long time intervals.
 */
contract TWAMM {
    // Events
    event LongTermTradeCreated(uint256 tradeId, address indexed trader, uint256 amountIn, uint256 executionEndTime);
    event LongTermTradeExecuted(uint256 tradeId, uint256 amountOut);

    // Struct to store details of long-term trades
    struct LongTermTrade {
        address trader;          // Address of the trader
        uint256 amountIn;        // Amount of tokens being traded
        uint256 amountOut;       // Total amount of tokens received (calculated over time)
        uint256 startTime;       // Start time of the trade execution
        uint256 endTime;         // End time for trade execution
        bool isActive;           // Status of the trade
    }

    // State variables
    uint256 public totalTrades;                            // Counter for trade IDs
    mapping(uint256 => LongTermTrade) public trades;       // Mapping for long-term trades
    uint256 public reserveX;                               // Reserve of token X
    uint256 public reserveY;                               // Reserve of token Y
    uint256 public constant FEE_PERCENTAGE = 3;            // Fee percentage for trades (e.g., 0.3%)
    uint256 public constant PRECISION = 10**18;            // Precision for calculations

    // ERC20 tokens
    IERC20 public tokenX;
    IERC20 public tokenY;

    // Constructor to set token addresses and initial reserves
    constructor(address _tokenX, address _tokenY, uint256 _reserveX, uint256 _reserveY) {
        require(_tokenX != address(0) && _tokenY != address(0), "Invalid token addresses");
        tokenX = IERC20(_tokenX);
        tokenY = IERC20(_tokenY);
        reserveX = _reserveX;
        reserveY = _reserveY;
    }

    // Modifier to validate reserves
    modifier validateReserves() {
        require(reserveX > 0 && reserveY > 0, "Reserves must be non-zero");
        _;
    }

    // Function to create a long-term trade
    function createLongTermTrade(uint256 amountIn, uint256 duration) external validateReserves {
        require(amountIn > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the trader to contract
        tokenX.transferFrom(msg.sender, address(this), amountIn);

        // Calculate trade end time
        uint256 endTime = block.timestamp + duration;

        // Create the trade
        LongTermTrade memory trade = LongTermTrade({
            trader: msg.sender,
            amountIn: amountIn,
            amountOut: 0,
            startTime: block.timestamp,
            endTime: endTime,
            isActive: true
        });

        // Save the trade and emit event
        trades[totalTrades] = trade;
        emit LongTermTradeCreated(totalTrades, msg.sender, amountIn, endTime);

        // Increment trade ID counter
        totalTrades++;
    }

    // Function to execute long-term trades periodically
    function executeTrades() external validateReserves {
        for (uint256 tradeId = 0; tradeId < totalTrades; tradeId++) {
            LongTermTrade storage trade = trades[tradeId];

            // Skip inactive trades
            if (!trade.isActive || block.timestamp >= trade.endTime) continue;

            // Calculate remaining duration and proportional amountOut
            uint256 timeElapsed = block.timestamp - trade.startTime;
            uint256 totalDuration = trade.endTime - trade.startTime;
            uint256 amountToExecute = (trade.amountIn * timeElapsed) / totalDuration;

            // Adjust reserves and calculate constant product invariant
            uint256 amountOut = calculateAmountOut(amountToExecute);
            reserveX += amountToExecute;
            reserveY -= amountOut;

            // Update trade state
            trade.amountOut += amountOut;
            trade.startTime = block.timestamp;

            // Emit event for executed trade
            emit LongTermTradeExecuted(tradeId, amountOut);
        }
    }

    // Internal function to calculate amount out using xy=k invariant
    function calculateAmountOut(uint256 amountIn) internal view returns (uint256) {
        uint256 invariant = reserveX * reserveY; // Product invariant: xy=k
        uint256 newReserveX = reserveX + amountIn; // New reserve after trade
        uint256 newReserveY = invariant / newReserveX; // Solve for y
        uint256 amountOut = reserveY - newReserveY; // Calculate output amount
        return (amountOut * (100 - FEE_PERCENTAGE)) / 100; // Deduct fee
    }

    // Function to finalize a completed long-term trade
    function finalizeTrade(uint256 tradeId) external {
        LongTermTrade storage trade = trades[tradeId];
        require(trade.isActive, "Trade is already finalized");
        require(block.timestamp >= trade.endTime, "Trade duration has not ended");

        // Mark trade as finalized
        trade.isActive = false;

        // Transfer output tokens to trader
        tokenY.transfer(trade.trader, trade.amountOut);
    }

    // Function to add liquidity (for testing or reserve adjustments)
    function addLiquidity(uint256 amountX, uint256 amountY) external {
        require(amountX > 0 && amountY > 0, "Amounts must be greater than zero");
        tokenX.transferFrom(msg.sender, address(this), amountX);
        tokenY.transferFrom(msg.sender, address(this), amountY);
        reserveX += amountX;
        reserveY += amountY;
    }

    // Function to remove liquidity (for testing or reserve adjustments)
    function removeLiquidity(uint256 amountX, uint256 amountY) external {
        require(amountX <= reserveX && amountY <= reserveY, "Insufficient reserves");
        reserveX -= amountX;
        reserveY -= amountY;
        tokenX.transfer(msg.sender, amountX);
        tokenY.transfer(msg.sender, amountY);
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
