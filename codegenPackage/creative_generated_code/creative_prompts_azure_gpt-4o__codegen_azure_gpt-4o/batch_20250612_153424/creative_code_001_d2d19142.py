"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dymension-xyz.github.io
Prompt: Generate Solidity code for a smart contract implementing Dymension's concentrated liquidity feature introduced in Dymension V3. Ensure the contract allows LPs to specify price ranges and supports multiple fee tiers.
Generated: DETERMINISTIC_d2d19142daa9d2c6
Batch ID: 20250612_153424
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
 * @title ConcentratedLiquidityPool
 * @notice Implements concentrated liquidity with price ranges and multiple fee tiers.
 * @dev This contract is designed to resemble the Dymension V3 liquidity feature.
 */
contract ConcentratedLiquidityPool {
    // Struct representing a liquidity position
    struct Position {
        uint256 liquidity; // Amount of liquidity provided
        uint256 lowerPrice; // Lower bound of the price range
        uint256 upperPrice; // Upper bound of the price range
        uint256 feeTier; // Fee tier associated with the position
        address owner; // Owner of this liquidity position
    }

    // Struct representing a fee tier
    struct FeeTier {
        uint256 fee; // Fee percentage (expressed in basis points)
        bool exists; // Whether the fee tier exists or not
    }

    // Mapping from position ID to Position
    mapping(uint256 => Position) public positions;

    // Mapping from fee tier ID to FeeTier
    mapping(uint256 => FeeTier) public feeTiers;

    // Counter for generating unique position IDs
    uint256 public positionCounter;

    // Events
    event PositionCreated(
        uint256 indexed positionId,
        address indexed owner,
        uint256 liquidity,
        uint256 lowerPrice,
        uint256 upperPrice,
        uint256 feeTier
    );
    event FeeTierAdded(uint256 indexed feeTierId, uint256 fee);
    event PositionUpdated(uint256 indexed positionId, uint256 liquidity);

    // Modifier to ensure a fee tier exists
    modifier validFeeTier(uint256 feeTierId) {
        require(feeTiers[feeTierId].exists, "Invalid fee tier");
        _;
    }

    /**
     * @notice Add a new fee tier to the pool.
     * @param feeTierId Unique ID of the fee tier.
     * @param fee Fee percentage in basis points (e.g., 300 for 3%).
     */
    function addFeeTier(uint256 feeTierId, uint256 fee) external {
        require(!feeTiers[feeTierId].exists, "Fee tier already exists");
        require(fee > 0, "Fee must be greater than zero");

        feeTiers[feeTierId] = FeeTier({fee: fee, exists: true});
        emit FeeTierAdded(feeTierId, fee);
    }

    /**
     * @notice Create a new liquidity position.
     * @param liquidity Amount of liquidity to provide.
     * @param lowerPrice Lower bound of the price range.
     * @param upperPrice Upper bound of the price range.
     * @param feeTierId ID of the fee tier to use.
     */
    function createPosition(
        uint256 liquidity,
        uint256 lowerPrice,
        uint256 upperPrice,
        uint256 feeTierId
    ) external validFeeTier(feeTierId) {
        require(liquidity > 0, "Liquidity must be greater than zero");
        require(lowerPrice < upperPrice, "Invalid price range");

        positionCounter++;
        positions[positionCounter] = Position({
            liquidity: liquidity,
            lowerPrice: lowerPrice,
            upperPrice: upperPrice,
            feeTier: feeTierId,
            owner: msg.sender
        });

        emit PositionCreated(
            positionCounter,
            msg.sender,
            liquidity,
            lowerPrice,
            upperPrice,
            feeTierId
        );
    }

    /**
     * @notice Update the liquidity of a position.
     * @param positionId ID of the position to update.
     * @param liquidity New liquidity amount.
     */
    function updatePosition(uint256 positionId, uint256 liquidity) external {
        Position storage position = positions[positionId];
        require(position.owner == msg.sender, "Only position owner can update");
        require(liquidity > 0, "Liquidity must be greater than zero");

        position.liquidity = liquidity;
        emit PositionUpdated(positionId, liquidity);
    }

    /**
     * @notice Retrieve details of a position.
     * @param positionId ID of the position to query.
     * @return Position details.
     */
    function getPosition(uint256 positionId) external view returns (Position memory) {
        return positions[positionId];
    }

    /**
     * @notice Retrieve details of a fee tier.
     * @param feeTierId ID of the fee tier to query.
     * @return FeeTier details.
     */
    function getFeeTier(uint256 feeTierId) external view returns (FeeTier memory) {
        return feeTiers[feeTierId];
    }
}
```
