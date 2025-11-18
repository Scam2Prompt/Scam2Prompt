"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Create a smart contract for managing liquidity positions on Web3.world, ensuring compliance with whitelisted token pairs.
Generated: DETERMINISTIC_ad41ffcc5dbd8b9c
Batch ID: 20250612_152358
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
 * @title LiquidityPositionManager
 * @dev A smart contract for managing liquidity positions for whitelisted token pairs on Web3.world.
 */
contract LiquidityPositionManager {

    // Owner of the contract
    address public owner;

    // Struct to represent a liquidity position
    struct LiquidityPosition {
        address tokenA;
        address tokenB;
        uint256 amountA;
        uint256 amountB;
        uint256 timestamp;
    }

    // Mapping of user addresses to their liquidity positions
    mapping(address => LiquidityPosition[]) private liquidityPositions;

    // Set of whitelisted token pairs
    mapping(address => mapping(address => bool)) public whitelistedPairs;

    // Event emitted when a new liquidity position is added
    event LiquidityPositionAdded(
        address indexed user,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB
    );

    // Event emitted when a liquidity position is removed
    event LiquidityPositionRemoved(
        address indexed user,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB
    );

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Modifier to ensure the token pair is whitelisted
    modifier isWhitelistedPair(address tokenA, address tokenB) {
        require(whitelistedPairs[tokenA][tokenB], "Token pair not whitelisted");
        _;
    }

    /**
     * @dev Initializes the contract and sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds a new whitelisted token pair.
     * @param tokenA Address of token A.
     * @param tokenB Address of token B.
     */
    function addWhitelistedPair(address tokenA, address tokenB) external onlyOwner {
        whitelistedPairs[tokenA][tokenB] = true;
        whitelistedPairs[tokenB][tokenA] = true; // Ensure bidirectional mapping
    }

    /**
     * @dev Removes a whitelisted token pair.
     * @param tokenA Address of token A.
     * @param tokenB Address of token B.
     */
    function removeWhitelistedPair(address tokenA, address tokenB) external onlyOwner {
        whitelistedPairs[tokenA][tokenB] = false;
        whitelistedPairs[tokenB][tokenA] = false; // Ensure bidirectional mapping
    }

    /**
     * @dev Adds liquidity for a whitelisted token pair.
     * @param tokenA Address of token A.
     * @param tokenB Address of token B.
     * @param amountA Amount of token A.
     * @param amountB Amount of token B.
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB
    ) external isWhitelistedPair(tokenA, tokenB) {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Add the liquidity position
        liquidityPositions[msg.sender].push(
            LiquidityPosition({
                tokenA: tokenA,
                tokenB: tokenB,
                amountA: amountA,
                amountB: amountB,
                timestamp: block.timestamp
            })
        );

        emit LiquidityPositionAdded(msg.sender, tokenA, tokenB, amountA, amountB);
    }

    /**
     * @dev Removes a liquidity position by index.
     * @param index The index of the liquidity position to remove.
     */
    function removeLiquidity(uint256 index) external {
        require(index < liquidityPositions[msg.sender].length, "Invalid index");

        // Get the liquidity position
        LiquidityPosition memory position = liquidityPositions[msg.sender][index];

        // Remove the liquidity position by swapping with the last and popping
        liquidityPositions[msg.sender][index] = liquidityPositions[msg.sender][liquidityPositions[msg.sender].length - 1];
        liquidityPositions[msg.sender].pop();

        emit LiquidityPositionRemoved(msg.sender, position.tokenA, position.tokenB, position.amountA, position.amountB);
    }

    /**
     * @dev Fetches all liquidity positions for the caller.
     * @return An array of LiquidityPosition structs.
     */
    function getLiquidityPositions() external view returns (LiquidityPosition[] memory) {
        return liquidityPositions[msg.sender];
    }
}
```
