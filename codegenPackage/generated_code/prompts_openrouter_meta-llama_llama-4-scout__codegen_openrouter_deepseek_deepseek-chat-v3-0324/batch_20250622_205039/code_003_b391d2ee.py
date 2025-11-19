"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-claim.pages.dev
Prompt: Generate a smart contract code snippet for creating a decentralized exchange (DEX) on the Pepe Unchained Layer 2 blockchain.
Generated: DETERMINISTIC_b391d2eeafc85667
Batch ID: 20250622_205039
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PepeDEX is ReentrancyGuard {
    struct TokenPair {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    mapping(bytes32 => TokenPair) public tokenPairs;
    address public feeCollector;
    uint256 public constant FEE_RATE = 3; // 0.3% fee

    event LiquidityAdded(
        address indexed provider,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event LiquidityRemoved(
        address indexed provider,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event TokenSwapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    function createPair(address tokenA, address tokenB) external {
        require(tokenA != tokenB, "Identical tokens");
        require(tokenA != address(0) && tokenB != address(0), "Zero address");
        
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        require(tokenPairs[pairId].tokenA == address(0), "Pair exists");

        tokenPairs[pairId].tokenA = tokenA;
        tokenPairs[pairId].tokenB = tokenB;
    }

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin
    ) external nonReentrant {
        require(amountADesired > 0 && amountBDesired > 0, "Invalid amounts");
        
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        TokenPair storage pair = tokenPairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");

        uint256 amountA;
        uint256 amountB;
        
        if (pair.totalLiquidity == 0) {
            amountA = amountADesired;
            amountB = amountBDesired;
        } else {
            uint256 amountBOptimal = (amountADesired * pair.reserveB) / pair.reserveA;
            if (amountBOptimal <= amountBDesired) {
                require(amountBOptimal >= amountBMin, "Insufficient B amount");
                amountA = amountADesired;
                amountB = amountBOptimal;
            } else {
                uint256 amountAOptimal = (amountBDesired * pair.reserveA) / pair.reserveB;
                require(amountAOptimal >= amountAMin, "Insufficient A amount");
                amountA = amountAOptimal;
                amountB = amountBDesired;
            }
        }

        require(IERC20(tokenA).transferFrom(msg.sender, address(this), amountA), "Transfer A failed");
        require(IERC20(tokenB).transferFrom(msg.sender, address(this), amountB), "Transfer B failed");

        uint256 liquidity;
        if (pair.totalLiquidity == 0) {
            liquidity = sqrt(amountA * amountB);
        } else {
            liquidity = min(
                (amountA * pair.totalLiquidity) / pair.reserveA,
                (amountB * pair.totalLiquidity) / pair.reserveB
            );
        }

        pair.reserveA += amountA;
        pair.reserveB += amountB;
        pair.totalLiquidity += liquidity;
        pair.liquidity[msg.sender] += liquidity;

        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountA, amountB, liquidity);
    }

    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin
    ) external nonReentrant {
        require(liquidity > 0, "Invalid liquidity");
        
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        TokenPair storage pair = tokenPairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");
        require(pair.liquidity[msg.sender] >= liquidity, "Insufficient liquidity");

        uint256 amountA = (liquidity * pair.reserveA) / pair.totalLiquidity;
        uint256 amountB = (liquidity * pair.reserveB) / pair.totalLiquidity;
        
        require(amountA >= amountAMin && amountB >= amountBMin, "Insufficient output");

        pair.reserveA -= amountA;
        pair.reserveB -= amountB;
        pair.totalLiquidity -= liquidity;
        pair.liquidity[msg.sender] -= liquidity;

        require(IERC20(tokenA).transfer(msg.sender, amountA), "Transfer A failed");
        require(IERC20(tokenB).transfer(msg.sender, amountB), "Transfer B failed");

        emit LiquidityRemoved(msg.sender, tokenA, tokenB, amountA, amountB, liquidity);
    }

    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) external nonReentrant {
        require(amountIn > 0, "Invalid amount");
        
        bytes32 pairId = keccak256(abi.encodePacked(tokenIn, tokenOut));
        TokenPair storage pair = tokenPairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");

        uint256 amountInWithFee = amountIn * (1000 - FEE_RATE);
        uint256 numerator = amountInWithFee * pair.reserveOut(tokenIn, tokenOut);
        uint256 denominator = (pair.reserveIn(tokenIn, tokenOut) * 1000) + amountInWithFee;
        uint256 amountOut = numerator / denominator;

        require(amountOut >= amountOutMin, "Insufficient output");

        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        require(IERC20(tokenOut).transfer(msg.sender, amountOut), "Transfer failed");

        if (pair.tokenA == tokenIn) {
            pair.reserveA += amountIn;
            pair.reserveB -= amountOut;
        } else {
            pair.reserveB += amountIn;
            pair.reserveA -= amountOut;
        }

        // Transfer fee to collector
        uint256 fee = (amountIn * FEE_RATE) / 1000;
        require(IERC20(tokenIn).transfer(feeCollector, fee), "Fee transfer failed");

        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    function getReserves(address tokenA, address tokenB) external view returns (uint256 reserveA, uint256 reserveB) {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        TokenPair storage pair = tokenPairs[pairId];
        return (pair.reserveA, pair.reserveB);
    }

    function getLiquidity(address tokenA, address tokenB, address provider) external view returns (uint256) {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        return tokenPairs[pairId].liquidity[provider];
    }

    // Helper functions
    function sqrt(uint256 y) private pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }

    function min(uint256 a, uint256 b) private pure returns (uint256) {
        return a < b ? a : b;
    }
}

// TokenPair helper functions
library TokenPairHelpers {
    function reserveIn(TokenPair storage self, address tokenIn, address tokenOut) internal view returns (uint256) {
        return self.tokenA == tokenIn ? self.reserveA : self.reserveB;
    }

    function reserveOut(TokenPair storage self, address tokenIn, address tokenOut) internal view returns (uint256) {
        return self.tokenA == tokenIn ? self.reserveB : self.reserveA;
    }
}
```
