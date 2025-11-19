"""
Generated Code Metadata:
========================
Original URL: https://sourcecopy.pages.dev
Prompt: "Create a code example that demonstrates how to use the `IUniswapV2ERC20`, `IUniswapV2Factory`, and `IUniswapV2Pair` interfaces from the Uniswap V2 core library to interact with Uniswap Exchange."
Generated: DETERMINISTIC_bd1ee80f89caaa98
Batch ID: 20250622_204803
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

// Import Uniswap V2 interfaces
import "./IUniswapV2ERC20.sol";
import "./IUniswapV2Factory.sol";
import "./IUniswapV2Pair.sol";

contract UniswapV2Interactor {
    IUniswapV2Factory public factory;
    
    constructor(address _factory) {
        factory = IUniswapV2Factory(_factory);
    }
    
    /**
     * @dev Creates a pair for the given tokens if it doesn't exist
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @return pair Address of the created pair
     */
    function createPair(address tokenA, address tokenB) external returns (address pair) {
        require(tokenA != tokenB, "UniswapV2: IDENTICAL_ADDRESSES");
        require(tokenA != address(0) && tokenB != address(0), "UniswapV2: ZERO_ADDRESS");
        
        pair = factory.createPair(tokenA, tokenB);
        require(pair != address(0), "UniswapV2: PAIR_CREATION_FAILED");
        
        return pair;
    }
    
    /**
     * @dev Gets the pair address for two tokens
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @return pair Address of the pair (zero address if doesn't exist)
     */
    function getPair(address tokenA, address tokenB) external view returns (address pair) {
        return factory.getPair(tokenA, tokenB);
    }
    
    /**
     * @dev Gets the reserves of a pair
     * @param pair Address of the pair
     * @return reserveA Reserve of token0
     * @return reserveB Reserve of token1
     * @return blockTimestampLast Last block timestamp when reserves were updated
     */
    function getReserves(address pair) external view returns (uint112 reserveA, uint112 reserveB, uint32 blockTimestampLast) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        (reserveA, reserveB, blockTimestampLast) = uniswapPair.getReserves();
    }
    
    /**
     * @dev Gets the token balances of an address in a pair
     * @param pair Address of the pair
     * @param account Address to check balances for
     * @return balanceA Balance of token0
     * @return balanceB Balance of token1
     */
    function getTokenBalances(address pair, address account) external view returns (uint256 balanceA, uint256 balanceB) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        address token0 = uniswapPair.token0();
        address token1 = uniswapPair.token1();
        
        balanceA = IUniswapV2ERC20(token0).balanceOf(account);
        balanceB = IUniswapV2ERC20(token1).balanceOf(account);
    }
    
    /**
     * @dev Gets the total supply of LP tokens for a pair
     * @param pair Address of the pair
     * @return totalSupply Total supply of LP tokens
     */
    function getTotalSupply(address pair) external view returns (uint256 totalSupply) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        totalSupply = uniswapPair.totalSupply();
    }
    
    /**
     * @dev Approves tokens for a pair
     * @param token Address of the token to approve
     * @param spender Address of the spender (usually the pair)
     * @param amount Amount to approve
     */
    function approveToken(address token, address spender, uint256 amount) external {
        IUniswapV2ERC20(token).approve(spender, amount);
    }
    
    /**
     * @dev Gets the allowance of a spender for a token
     * @param token Address of the token
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @return allowance Current allowance
     */
    function getAllowance(address token, address owner, address spender) external view returns (uint256 allowance) {
        allowance = IUniswapV2ERC20(token).allowance(owner, spender);
    }
}
```
