"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Write a smart contract for pairing any two ERC-20 tokens using Carbon DeFi's adjustable order conditions and custom fee tiers.
Generated: DETERMINISTIC_77e03b9a22d82ace
Batch ID: 20250612_154239
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
 * @title TokenPairingContract
 * @dev Smart contract for pairing two ERC-20 tokens using Carbon DeFi's adjustable order conditions and custom fee tiers.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenPairingContract {
    address public owner;

    struct Pair {
        address tokenA;
        address tokenB;
        uint256 feeTier; // Fee tier in basis points (e.g., 25 = 0.25%)
        uint256 minAmountA; // Minimum amount of Token A required
        uint256 minAmountB; // Minimum amount of Token B required
        bool isActive; // Is the pairing active
    }

    mapping(bytes32 => Pair) public pairs; // Store pairings by unique hash identifier

    event PairCreated(bytes32 indexed pairId, address tokenA, address tokenB, uint256 feeTier);
    event PairUpdated(bytes32 indexed pairId, uint256 feeTier, uint256 minAmountA, uint256 minAmountB);
    event PairDeleted(bytes32 indexed pairId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Create a new pair for two ERC-20 tokens.
     * @param tokenA Address of the first ERC-20 token.
     * @param tokenB Address of the second ERC-20 token.
     * @param feeTier Fee tier in basis points.
     * @param minAmountA Minimum amount of Token A required.
     * @param minAmountB Minimum amount of Token B required.
     */
    function createPair(
        address tokenA,
        address tokenB,
        uint256 feeTier,
        uint256 minAmountA,
        uint256 minAmountB
    ) external onlyOwner {
        require(tokenA != address(0) && tokenB != address(0), "Token addresses cannot be zero");
        require(feeTier > 0, "Fee tier must be greater than zero");
        require(minAmountA > 0 && minAmountB > 0, "Minimum amounts must be greater than zero");

        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB, block.timestamp));
        pairs[pairId] = Pair(tokenA, tokenB, feeTier, minAmountA, minAmountB, true);

        emit PairCreated(pairId, tokenA, tokenB, feeTier);
    }

    /**
     * @notice Update the conditions of an existing pair.
     * @param pairId The unique identifier of the pair.
     * @param feeTier New fee tier in basis points.
     * @param minAmountA New minimum amount of Token A required.
     * @param minAmountB New minimum amount of Token B required.
     */
    function updatePair(
        bytes32 pairId,
        uint256 feeTier,
        uint256 minAmountA,
        uint256 minAmountB
    ) external onlyOwner {
        require(pairs[pairId].isActive, "Pair does not exist or is not active");
        
        pairs[pairId].feeTier = feeTier;
        pairs[pairId].minAmountA = minAmountA;
        pairs[pairId].minAmountB = minAmountB;

        emit PairUpdated(pairId, feeTier, minAmountA, minAmountB);
    }

    /**
     * @notice Delete an existing pair.
     * @param pairId The unique identifier of the pair.
     */
    function deletePair(bytes32 pairId) external onlyOwner {
        require(pairs[pairId].isActive, "Pair does not exist or is not active");
        
        pairs[pairId].isActive = false;

        emit PairDeleted(pairId);
    }

    /**
     * @notice Execute a trade between two ERC-20 tokens using specified pair conditions.
     * @param pairId The unique identifier of the pair.
     * @param amountA Amount of Token A to trade.
     */
    function executeTrade(bytes32 pairId, uint256 amountA) external {
        Pair storage pair = pairs[pairId];
        require(pair.isActive, "Pair is not active");
        require(amountA >= pair.minAmountA, "Insufficient Token A amount");

        uint256 amountB = calculateAmountB(pair, amountA);
        require(amountB >= pair.minAmountB, "Insufficient Token B amount");

        IERC20(pair.tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(pair.tokenB).transfer(msg.sender, amountB);
    }

    /**
     * @notice Calculate the amount of Token B required for a given amount of Token A.
     * @param pair The pair details.
     * @param amountA Amount of Token A to trade.
     * @return The required amount of Token B.
     */
    function calculateAmountB(Pair memory pair, uint256 amountA) private pure returns (uint256) {
        uint256 fee = (amountA * pair.feeTier) / 10000;
        return amountA - fee;
    }
}
```
