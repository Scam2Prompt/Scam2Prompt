"""
Generated Code Metadata:
========================
Original URL: https://cmkjdwoihjif.com
Prompt: Create a Solidity smart contract to optimize trading routes on a decentralized exchange with low slippage and deep liquidity, inspired by KittenSwap's trading features.
Generated: DETERMINISTIC_f08e6df075957712
Batch ID: 20250612_153849
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUniswapV2Router {
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract KittenSwapOptimizer is Ownable, ReentrancyGuard {
    struct Route {
        address router;
        address[] path;
    }

    mapping(address => mapping(address => Route[])) public routes;
    uint public maxHops = 3;
    uint public slippageTolerance = 50; // 0.5% default slippage tolerance (basis points)
    uint public constant MAX_SLIPPAGE = 1000; // 10% max slippage (basis points)

    event RouteAdded(address indexed fromToken, address indexed toToken, address router, address[] path);
    event RouteRemoved(address indexed fromToken, address indexed toToken, uint index);
    event SwapExecuted(
        address indexed sender,
        address indexed fromToken,
        address indexed toToken,
        uint amountIn,
        uint amountOut
    );

    constructor() {}

    /**
     * @dev Add a trading route between two tokens
     * @param fromToken The token to swap from
     * @param toToken The token to swap to
     * @param router The router address (e.g., Uniswap, Sushiswap)
     * @param path The swap path (token addresses)
     */
    function addRoute(
        address fromToken,
        address toToken,
        address router,
        address[] memory path
    ) external onlyOwner {
        require(path.length >= 2, "Invalid path length");
        require(path[0] == fromToken, "First token in path must be fromToken");
        require(path[path.length - 1] == toToken, "Last token in path must be toToken");
        require(path.length <= maxHops + 1, "Path exceeds max hops");

        routes[fromToken][toToken].push(Route(router, path));
        emit RouteAdded(fromToken, toToken, router, path);
    }

    /**
     * @dev Remove a trading route
     * @param fromToken The token to swap from
     * @param toToken The token to swap to
     * @param index The index of the route to remove
     */
    function removeRoute(
        address fromToken,
        address toToken,
        uint index
    ) external onlyOwner {
        require(index < routes[fromToken][toToken].length, "Index out of bounds");
        
        // Move last element to deleted spot
        if (index != routes[fromToken][toToken].length - 1) {
            routes[fromToken][toToken][index] = routes[fromToken][toToken][routes[fromToken][toToken].length - 1];
        }
        
        routes[fromToken][toToken].pop();
        emit RouteRemoved(fromToken, toToken, index);
    }

    /**
     * @dev Set maximum allowed hops for routes
     * @param _maxHops New maximum hops value
     */
    function setMaxHops(uint _maxHops) external onlyOwner {
        require(_maxHops > 0 && _maxHops <= 5, "Invalid max hops");
        maxHops = _maxHops;
    }

    /**
     * @dev Set slippage tolerance (in basis points)
     * @param _slippageTolerance New slippage tolerance (1 = 0.01%)
     */
    function setSlippageTolerance(uint _slippageTolerance) external onlyOwner {
        require(_slippageTolerance <= MAX_SLIPPAGE, "Slippage too high");
        slippageTolerance = _slippageTolerance;
    }

    /**
     * @dev Find the best route for a token swap
     * @param fromToken The token to swap from
     * @param toToken The token to swap to
     * @param amountIn The amount of fromToken to swap
     * @return bestRouter The best router address
     * @return bestPath The best path
     * @return amountOut The expected amount out
     */
    function findBestRoute(
        address fromToken,
        address toToken,
        uint amountIn
    ) public view returns (address bestRouter, address[] memory bestPath, uint amountOut) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(fromToken != toToken, "Tokens must be different");

        Route[] storage availableRoutes = routes[fromToken][toToken];
        require(availableRoutes.length > 0, "No routes available");

        bestRouter = address(0);
        bestPath = new address[](0);
        amountOut = 0;

        for (uint i = 0; i < availableRoutes.length; i++) {
            Route memory route = availableRoutes[i];
            try IUniswapV2Router(route.router).getAmountsOut(amountIn, route.path) returns (uint[] memory amounts) {
                uint currentAmountOut = amounts[amounts.length - 1];
                if (currentAmountOut > amountOut) {
                    amountOut = currentAmountOut;
                    bestRouter = route.router;
                    bestPath = route.path;
                }
            } catch {
                continue; // Skip if the route fails
            }
        }

        require(bestRouter != address(0), "No valid routes found");
        return (bestRouter, bestPath, amountOut);
    }

    /**
     * @dev Execute a token swap using the best available route
     * @param fromToken The token to swap from
     * @param toToken The token to swap to
     * @param amountIn The amount of fromToken to swap
     * @param amountOutMin Minimum amount of toToken to receive
     * @param deadline Deadline for the swap
     * @return amounts The amounts swapped
     */
    function swap(
        address fromToken,
        address toToken,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external nonReentrant returns (uint[] memory amounts) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline expired");

        // Transfer tokens from sender to contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);

        // Find best route
        (address bestRouter, address[] memory bestPath, uint expectedAmountOut) = findBestRoute(
            fromToken,
            toToken,
            amountIn
        );

        // Calculate minimum amount out with slippage tolerance
        uint minAmountOut = (expectedAmountOut * (10000 - slippageTolerance)) / 10000;
        require(amountOutMin <= minAmountOut, "Slippage too high");

        // Approve router to spend tokens
        IERC20(fromToken).approve(bestRouter, amountIn);

        // Execute swap
        amounts = IUniswapV2Router(bestRouter).swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            bestPath,
            msg.sender,
            deadline
        );

        emit SwapExecuted(msg.sender, fromToken, toToken, amountIn, amounts[amounts.length - 1]);
        return amounts;
    }

    /**
     * @dev Emergency withdraw tokens sent to the contract
     * @param token The token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
