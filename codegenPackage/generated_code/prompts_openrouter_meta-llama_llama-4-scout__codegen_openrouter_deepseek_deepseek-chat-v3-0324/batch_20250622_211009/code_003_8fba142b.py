"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Design a smart contract that utilizes Pyth Network's price feeds to update a decentralized perpetual swap platform on Arbitrum.
Generated: DETERMINISTIC_8fba142b23d75ce5
Batch ID: 20250622_211009
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

// Import Pyth Network interfaces
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PerpetualSwap {
    // Pyth Network contract
    IPyth public pyth;

    // Price feed ID for the trading pair (e.g., BTC/USD)
    bytes32 public priceFeedId;

    // Contract owner
    address public owner;

    // Position structure
    struct Position {
        address trader;
        uint256 size;
        uint256 entryPrice;
        bool isLong;
        uint256 lastUpdated;
    }

    // Mapping of position IDs to positions
    mapping(uint256 => Position) public positions;

    // Next position ID
    uint256 public nextPositionId;

    // Funding rate parameters
    uint256 public fundingRate;
    uint256 public lastFundingUpdate;

    // Events
    event PositionOpened(
        uint256 indexed positionId,
        address indexed trader,
        uint256 size,
        uint256 entryPrice,
        bool isLong
    );
    event PositionClosed(
        uint256 indexed positionId,
        address indexed trader,
        uint256 pnl
    );
    event PriceUpdated(uint256 newPrice);
    event FundingRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        owner = msg.sender;
        fundingRate = 0;
        lastFundingUpdate = block.timestamp;
    }

    /**
     * @dev Update the price feed from Pyth Network
     * @param priceUpdateData Pyth price update data
     */
    function updatePrice(bytes[] calldata priceUpdateData) external payable {
        // Update the price feed
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        emit PriceUpdated(uint256(price.price));
    }

    /**
     * @dev Open a new position
     * @param size Position size
     * @param isLong Whether the position is long
     */
    function openPosition(uint256 size, bool isLong) external {
        require(size > 0, "Size must be greater than 0");

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        require(price.price > 0, "Invalid price");

        // Create new position
        positions[nextPositionId] = Position({
            trader: msg.sender,
            size: size,
            entryPrice: uint256(price.price),
            isLong: isLong,
            lastUpdated: block.timestamp
        });

        emit PositionOpened(
            nextPositionId,
            msg.sender,
            size,
            uint256(price.price),
            isLong
        );

        nextPositionId++;
    }

    /**
     * @dev Close an existing position
     * @param positionId ID of the position to close
     */
    function closePosition(uint256 positionId) external {
        Position storage position = positions[positionId];
        require(position.trader == msg.sender, "Not your position");
        require(position.size > 0, "Position already closed");

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        require(price.price > 0, "Invalid price");

        // Calculate PnL
        uint256 pnl;
        if (position.isLong) {
            pnl = (position.size * uint256(price.price)) / position.entryPrice - position.size;
        } else {
            pnl = position.size - (position.size * uint256(price.price)) / position.entryPrice;
        }

        // Apply funding rate
        uint256 fundingAmount = (position.size * fundingRate * (block.timestamp - position.lastUpdated)) / (1 days);
        if (position.isLong) {
            pnl -= fundingAmount;
        } else {
            pnl += fundingAmount;
        }

        // Close position
        delete positions[positionId];

        emit PositionClosed(positionId, msg.sender, pnl);
    }

    /**
     * @dev Update funding rate
     * @param newRate New funding rate
     */
    function updateFundingRate(uint256 newRate) external onlyOwner {
        fundingRate = newRate;
        lastFundingUpdate = block.timestamp;
        emit FundingRateUpdated(newRate);
    }

    /**
     * @dev Transfer ownership
     * @param newOwner Address of new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }

    // Receive function to accept ETH for Pyth updates
    receive() external payable {}
}
```
