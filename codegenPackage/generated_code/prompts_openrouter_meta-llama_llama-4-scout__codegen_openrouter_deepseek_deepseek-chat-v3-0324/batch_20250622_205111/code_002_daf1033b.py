"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Generate a smart contract code for creating a custom Synthetix Perps integrator, enabling traders to access up to 50x leverage on various markets.
Generated: DETERMINISTIC_daf1033bd1aa3de1
Batch ID: 20250622_205111
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
import "@synthetixio/core-contracts/contracts/interfaces/IERC20.sol";
import "@synthetixio/perps-v2/contracts/interfaces/IMarket.sol";
import "@synthetixio/perps-v2/contracts/interfaces/IExchangeRates.sol";

/**
 * @title Synthetix Perps Integrator
 * @notice Allows traders to access leveraged positions on Synthetix Perps markets
 * @dev This contract integrates with Synthetix Perps V2 markets
 */
contract SynthetixPerpsIntegrator is Ownable {
    IExchangeRates public exchangeRates;
    uint256 public constant MAX_LEVERAGE = 50;
    uint256 public constant BASIS_POINTS = 10000;

    struct Position {
        uint256 marketId;
        uint256 size;
        uint256 margin;
        int256 entryPrice;
        uint256 leverage;
    }

    mapping(address => mapping(uint256 => Position)) public positions;
    mapping(uint256 => address) public marketIdToAddress;

    event PositionOpened(
        address indexed trader,
        uint256 marketId,
        uint256 size,
        uint256 margin,
        int256 entryPrice,
        uint256 leverage
    );
    event PositionClosed(
        address indexed trader,
        uint256 marketId,
        uint256 size,
        uint256 pnl
    );

    /**
     * @param _exchangeRates Address of Synthetix ExchangeRates contract
     */
    constructor(address _exchangeRates) {
        require(_exchangeRates != address(0), "Invalid exchange rates address");
        exchangeRates = IExchangeRates(_exchangeRates);
    }

    /**
     * @notice Add a supported market
     * @param marketId Synthetix market ID
     * @param marketAddress Address of the market contract
     */
    function addMarket(uint256 marketId, address marketAddress) external onlyOwner {
        require(marketAddress != address(0), "Invalid market address");
        marketIdToAddress[marketId] = marketAddress;
    }

    /**
     * @notice Open a leveraged position
     * @param marketId Synthetix market ID
     * @param margin Amount of margin to deposit
     * @param leverage Desired leverage (up to MAX_LEVERAGE)
     * @param desiredPrice Desired entry price (slippage protection)
     */
    function openPosition(
        uint256 marketId,
        uint256 margin,
        uint256 leverage,
        int256 desiredPrice
    ) external {
        require(margin > 0, "Margin must be positive");
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");
        require(marketIdToAddress[marketId] != address(0), "Market not supported");

        IMarket market = IMarket(marketIdToAddress[marketId]);
        uint256 size = (margin * leverage) / BASIS_POINTS;

        // Get current price from exchange rates
        (int256 currentPrice, ) = exchangeRates.rateAndInvalid(marketId);
        require(
            desiredPrice == 0 || 
            (desiredPrice > 0 && currentPrice <= desiredPrice) || 
            (desiredPrice < 0 && currentPrice >= desiredPrice),
            "Slippage too high"
        );

        // Transfer margin from trader
        IERC20(market.baseAsset()).transferFrom(msg.sender, address(this), margin);

        // Approve and open position
        IERC20(market.baseAsset()).approve(address(market), margin);
        market.openPosition(marketId, size, margin);

        // Record position
        positions[msg.sender][marketId] = Position({
            marketId: marketId,
            size: size,
            margin: margin,
            entryPrice: currentPrice,
            leverage: leverage
        });

        emit PositionOpened(msg.sender, marketId, size, margin, currentPrice, leverage);
    }

    /**
     * @notice Close an existing position
     * @param marketId Synthetix market ID
     * @param desiredPrice Desired exit price (slippage protection)
     */
    function closePosition(uint256 marketId, int256 desiredPrice) external {
        Position memory position = positions[msg.sender][marketId];
        require(position.size > 0, "No position to close");

        IMarket market = IMarket(marketIdToAddress[marketId]);

        // Get current price from exchange rates
        (int256 currentPrice, ) = exchangeRates.rateAndInvalid(marketId);
        require(
            desiredPrice == 0 || 
            (desiredPrice > 0 && currentPrice <= desiredPrice) || 
            (desiredPrice < 0 && currentPrice >= desiredPrice),
            "Slippage too high"
        );

        // Close position
        market.closePosition(marketId, position.size);

        // Calculate PnL
        int256 priceDelta = currentPrice - position.entryPrice;
        uint256 pnl = (uint256(priceDelta) * position.size) / BASIS_POINTS;

        // Transfer funds back to trader
        uint256 totalAmount = position.margin + pnl;
        IERC20(market.baseAsset()).transfer(msg.sender, totalAmount);

        // Clear position
        delete positions[msg.sender][marketId];

        emit PositionClosed(msg.sender, marketId, position.size, pnl);
    }

    /**
     * @notice Emergency withdraw funds (owner only)
     * @param token Token address to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner(), amount);
    }
}
```
