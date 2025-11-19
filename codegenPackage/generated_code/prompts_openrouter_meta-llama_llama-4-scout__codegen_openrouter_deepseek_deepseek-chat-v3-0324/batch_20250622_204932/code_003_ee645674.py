"""
Generated Code Metadata:
========================
Original URL: https://axieinfinty.github.io
Prompt: Design a simple decentralized exchange (DEX) protocol using Axie Infinity's AMM model and smart contracts, assuming a basic understanding of Solidity.
Generated: DETERMINISTIC_ee645674f7fff24d
Batch ID: 20250622_204932
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SimpleDEX
 * @dev A simple decentralized exchange implementing Axie Infinity's AMM model
 */
contract SimpleDEX is ReentrancyGuard {
    using SafeMath for uint256;

    // Token pair structure
    struct Pair {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    // Pair ID to Pair mapping
    mapping(bytes32 => Pair) public pairs;
    address[] public tokenList;
    mapping(address => bool) public isTokenListed;

    // Events
    event PairCreated(address indexed tokenA, address indexed tokenB, bytes32 pairId);
    event LiquidityAdded(address indexed provider, bytes32 pairId, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed provider, bytes32 pairId, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swap(address indexed sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Creates a new token pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     */
    function createPair(address tokenA, address tokenB) external {
        require(tokenA != tokenB, "SimpleDEX: identical addresses");
        require(tokenA != address(0) && tokenB != address(0), "SimpleDEX: zero address");
        
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        require(pairs[pairId].tokenA == address(0), "SimpleDEX: pair already exists");

        pairs[pairId].tokenA = tokenA;
        pairs[pairId].tokenB = tokenB;

        if (!isTokenListed[tokenA]) {
            tokenList.push(tokenA);
            isTokenListed[tokenA] = true;
        }
        if (!isTokenListed[tokenB]) {
            tokenList.push(tokenB);
            isTokenListed[tokenB] = true;
        }

        emit PairCreated(tokenA, tokenB, pairId);
    }

    /**
     * @dev Adds liquidity to a pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired
    ) external nonReentrant {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "SimpleDEX: pair does not exist");

        uint256 amountA;
        uint256 amountB;

        if (pair.reserveA == 0 && pair.reserveB == 0) {
            amountA = amountADesired;
            amountB = amountBDesired;
        } else {
            uint256 amountBOptimal = quote(amountADesired, pair.reserveA, pair.reserveB);
            if (amountBOptimal <= amountBDesired) {
                amountA = amountADesired;
                amountB = amountBOptimal;
            } else {
                uint256 amountAOptimal = quote(amountBDesired, pair.reserveB, pair.reserveA);
                amountA = amountAOptimal;
                amountB = amountBDesired;
            }
        }

        require(amountA > 0 && amountB > 0, "SimpleDEX: insufficient liquidity");

        // Transfer tokens from user
        safeTransferFrom(tokenA, msg.sender, address(this), amountA);
        safeTransferFrom(tokenB, msg.sender, address(this), amountB);

        // Mint liquidity tokens
        uint256 liquidity;
        if (pair.totalLiquidity == 0) {
            liquidity = sqrt(amountA.mul(amountB));
        } else {
            liquidity = min(
                amountA.mul(pair.totalLiquidity) / pair.reserveA,
                amountB.mul(pair.totalLiquidity) / pair.reserveB
            );
        }

        require(liquidity > 0, "SimpleDEX: insufficient liquidity minted");

        // Update reserves and liquidity
        pair.reserveA = pair.reserveA.add(amountA);
        pair.reserveB = pair.reserveB.add(amountB);
        pair.totalLiquidity = pair.totalLiquidity.add(liquidity);
        pair.liquidity[msg.sender] = pair.liquidity[msg.sender].add(liquidity);

        emit LiquidityAdded(msg.sender, pairId, amountA, amountB, liquidity);
    }

    /**
     * @dev Removes liquidity from a pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param liquidity Amount of liquidity tokens to remove
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity
    ) external nonReentrant {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "SimpleDEX: pair does not exist");
        require(pair.liquidity[msg.sender] >= liquidity, "SimpleDEX: insufficient liquidity");

        uint256 amountA = liquidity.mul(pair.reserveA) / pair.totalLiquidity;
        uint256 amountB = liquidity.mul(pair.reserveB) / pair.totalLiquidity;

        require(amountA > 0 && amountB > 0, "SimpleDEX: insufficient liquidity burned");

        // Update reserves and liquidity
        pair.reserveA = pair.reserveA.sub(amountA);
        pair.reserveB = pair.reserveB.sub(amountB);
        pair.totalLiquidity = pair.totalLiquidity.sub(liquidity);
        pair.liquidity[msg.sender] = pair.liquidity[msg.sender].sub(liquidity);

        // Transfer tokens to user
        safeTransfer(tokenA, msg.sender, amountA);
        safeTransfer(tokenB, msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, pairId, amountA, amountB, liquidity);
    }

    /**
     * @dev Swaps tokens using the pair's liquidity
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input tokens to swap
     */
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn
    ) external nonReentrant {
        require(tokenIn != tokenOut, "SimpleDEX: identical addresses");
        bytes32 pairId = keccak256(abi.encodePacked(tokenIn, tokenOut));
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "SimpleDEX: pair does not exist");

        (uint256 reserveIn, uint256 reserveOut) = tokenIn == pair.tokenA 
            ? (pair.reserveA, pair.reserveB) 
            : (pair.reserveB, pair.reserveA);

        uint256 amountInWithFee = amountIn.mul(997);
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(1000).add(amountInWithFee);
        uint256 amountOut = numerator / denominator;

        require(amountOut > 0, "SimpleDEX: insufficient output amount");

        // Transfer tokens
        safeTransferFrom(tokenIn, msg.sender, address(this), amountIn);
        safeTransfer(tokenOut, msg.sender, amountOut);

        // Update reserves
        if (tokenIn == pair.tokenA) {
            pair.reserveA = pair.reserveA.add(amountIn);
            pair.reserveB = pair.reserveB.sub(amountOut);
        } else {
            pair.reserveB = pair.reserveB.add(amountIn);
            pair.reserveA = pair.reserveA.sub(amountOut);
        }

        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Helper functions
    function quote(uint256 amountA, uint256 reserveA, uint256 reserveB) public pure returns (uint256 amountB) {
        require(amountA > 0, "SimpleDEX: insufficient amount");
        require(reserveA > 0 && reserveB > 0, "SimpleDEX: insufficient liquidity");
        amountB = amountA
