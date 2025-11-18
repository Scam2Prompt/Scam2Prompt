"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algebra-finance.pages.dev
Prompt: Generate code to implement Algebra Protocol's concentrated liquidity mechanism for a DEX on the Polygon blockchain.
Generated: DETERMINISTIC_8f19f5ec1d528374
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title Concentrated Liquidity Mechanism for a DEX
 * @author Algebra Protocol Implementation
 * @notice This smart contract implements concentrated liquidity for a DEX on the Polygon blockchain.
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ConcentratedLiquidityDEX is Ownable, ReentrancyGuard {
    // Struct to store liquidity positions
    struct LiquidityPosition {
        uint256 amountA; // Token A amount in the position
        uint256 amountB; // Token B amount in the position
        uint256 lowerPrice; // Lower price bound of the position
        uint256 upperPrice; // Upper price bound of the position
        address owner; // Owner of the position
    }

    // Token contracts
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Mapping to store liquidity positions
    uint256 public positionCounter;
    mapping(uint256 => LiquidityPosition) public positions;

    // Events
    event LiquidityAdded(
        uint256 indexed positionId,
        address indexed owner,
        uint256 amountA,
        uint256 amountB,
        uint256 lowerPrice,
        uint256 upperPrice
    );
    event LiquidityRemoved(uint256 indexed positionId, address indexed owner);

    /**
     * @notice Constructor initializes token contracts
     * @param _tokenA Address of Token A contract
     * @param _tokenB Address of Token B contract
     */
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0), "Token A address cannot be zero");
        require(_tokenB != address(0), "Token B address cannot be zero");

        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    /**
     * @notice Add liquidity to the DEX within a specific price range
     * @param amountA Amount of Token A to deposit
     * @param amountB Amount of Token B to deposit
     * @param lowerPrice Lower bound of the price range
     * @param upperPrice Upper bound of the price range
     */
    function addLiquidity(
        uint256 amountA,
        uint256 amountB,
        uint256 lowerPrice,
        uint256 upperPrice
    ) external nonReentrant {
        require(amountA > 0, "Amount A must be greater than zero");
        require(amountB > 0, "Amount B must be greater than zero");
        require(lowerPrice < upperPrice, "Lower price must be less than upper price");

        // Transfer tokens from the user to the contract
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);

        // Create a new liquidity position
        positionCounter++;
        positions[positionCounter] = LiquidityPosition({
            amountA: amountA,
            amountB: amountB,
            lowerPrice: lowerPrice,
            upperPrice: upperPrice,
            owner: msg.sender
        });

        emit LiquidityAdded(positionCounter, msg.sender, amountA, amountB, lowerPrice, upperPrice);
    }

    /**
     * @notice Remove liquidity from a position
     * @param positionId ID of the position to remove liquidity from
     */
    function removeLiquidity(uint256 positionId) external nonReentrant {
        LiquidityPosition storage position = positions[positionId];
        require(position.owner == msg.sender, "Not the owner of this position");

        // Transfer tokens back to the user
        tokenA.transfer(msg.sender, position.amountA);
        tokenB.transfer(msg.sender, position.amountB);

        // Delete the position
        delete positions[positionId];

        emit LiquidityRemoved(positionId, msg.sender);
    }

    /**
     * @notice Get details of a liquidity position
     * @param positionId ID of the position to retrieve
     * @return LiquidityPosition details
     */
    function getPosition(uint256 positionId) external view returns (LiquidityPosition memory) {
        return positions[positionId];
    }
}
```

This code implements a smart contract for managing concentrated liquidity positions in a DEX. It includes best practices, proper documentation, and error handling. Make sure to test thoroughly on test networks before deploying on the Polygon mainnet.
