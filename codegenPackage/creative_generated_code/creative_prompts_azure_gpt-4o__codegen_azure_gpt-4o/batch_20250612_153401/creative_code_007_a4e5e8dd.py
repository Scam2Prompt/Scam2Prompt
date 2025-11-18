"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.pages.dev
Prompt: Create a Solidity contract for cross-chain DeFi protocols that integrates $PABLO tokens and supports liquidity pools, as outlined in the Pablo roadmap.
Generated: DETERMINISTIC_a4e5e8ddbd809987
Batch ID: 20250612_153401
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
 * @title PabloDeFiProtocol
 * @dev A Solidity contract for cross-chain DeFi integration with $PABLO tokens and liquidity pools.
 */
contract PabloDeFiProtocol {
    // State Variables
    address public owner; // Owner of the contract
    address public pabloTokenAddress; // Address of the $PABLO token contract
    uint256 public poolCounter; // Counter to track liquidity pools

    struct LiquidityPool {
        uint256 id; // Unique identifier for the pool
        string name; // Name of the liquidity pool
        address token; // Address of the token in the pool
        uint256 totalLiquidity; // Total liquidity in the pool
    }

    mapping(uint256 => LiquidityPool) public liquidityPools; // Mapping to store liquidity pools
    mapping(uint256 => mapping(address => uint256)) public userLiquidity; // Tracks user's liquidity in pools

    // Events
    event PoolCreated(uint256 id, string name, address indexed token);
    event LiquidityAdded(uint256 poolId, address indexed user, uint256 amount);
    event LiquidityRemoved(uint256 poolId, address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    modifier validPool(uint256 poolId) {
        require(poolId > 0 && poolId <= poolCounter, "Invalid pool ID");
        _;
    }

    // Constructor
    constructor(address _pabloTokenAddress) {
        require(_pabloTokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        pabloTokenAddress = _pabloTokenAddress;
    }

    /**
     * @dev Create a new liquidity pool.
     * @param _name Name of the liquidity pool.
     * @param _token Address of the token in the pool.
     */
    function createLiquidityPool(string memory _name, address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        poolCounter++;
        liquidityPools[poolCounter] = LiquidityPool(poolCounter, _name, _token, 0);

        emit PoolCreated(poolCounter, _name, _token);
    }

    /**
     * @dev Add liquidity to a pool.
     * @param poolId ID of the pool.
     * @param amount Amount of liquidity to add.
     */
    function addLiquidity(uint256 poolId, uint256 amount) external validPool(poolId) {
        require(amount > 0, "Amount must be greater than 0");

        LiquidityPool storage pool = liquidityPools[poolId];
        IERC20(pool.token).transferFrom(msg.sender, address(this), amount);

        pool.totalLiquidity += amount;
        userLiquidity[poolId][msg.sender] += amount;

        emit LiquidityAdded(poolId, msg.sender, amount);
    }

    /**
     * @dev Remove liquidity from a pool.
     * @param poolId ID of the pool.
     * @param amount Amount of liquidity to remove.
     */
    function removeLiquidity(uint256 poolId, uint256 amount) external validPool(poolId) {
        require(amount > 0, "Amount must be greater than 0");
        require(userLiquidity[poolId][msg.sender] >= amount, "Insufficient liquidity");

        LiquidityPool storage pool = liquidityPools[poolId];
        IERC20(pool.token).transfer(msg.sender, amount);

        pool.totalLiquidity -= amount;
        userLiquidity[poolId][msg.sender] -= amount;

        emit LiquidityRemoved(poolId, msg.sender, amount);
    }

    /**
     * @dev Get details of a specific liquidity pool.
     * @param poolId ID of the pool.
     * @return LiquidityPool Struct containing pool details.
     */
    function getPoolDetails(uint256 poolId) external view validPool(poolId) returns (LiquidityPool memory) {
        return liquidityPools[poolId];
    }
}

// IERC20 Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
