"""
Generated Code Metadata:
========================
Original URL: https://bafybeicl6dcseudnsbfjhdpevb2qppfqdiqbalqpmd4kdifgdzpdduqykq.ipfs.dweb.link
Prompt: Design a smart contract for an automated market maker (AMM) on zkLink X, referencing its product documentation and whitepaper.
Generated: DETERMINISTIC_e7e16113d3f67512
Batch ID: 20250622_205751
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
 * @title zkAMM - Automated Market Maker for zkLink X
 * @notice Implements constant product market maker (x*y=k) with zkLink X integration
 * @dev Supports ERC20 token pairs with fee mechanism and liquidity provider rewards
 */
contract zkAMM is ReentrancyGuard {
    using SafeMath for uint256;

    // Token pair structure
    struct Pair {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalSupply;
        mapping(address => uint256) liquidity;
    }

    // Constants
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public constant PROTOCOL_FEE = 30; // 0.3%
    uint256 public constant LP_FEE = 20; // 0.2%

    // State variables
    mapping(bytes32 => Pair) public pairs;
    address public feeCollector;

    // Events
    event PairCreated(address indexed tokenA, address indexed tokenB, bytes32 pairId);
    event LiquidityAdded(
        bytes32 indexed pairId,
        address indexed provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event LiquidityRemoved(
        bytes32 indexed pairId,
        address indexed provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    event Swap(
        bytes32 indexed pairId,
        address indexed sender,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Constructor sets the fee collector address
     * @param _feeCollector Address to collect protocol fees
     */
    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    /**
     * @notice Creates a new token pair
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @return pairId The ID of the created pair
     */
    function createPair(address tokenA, address tokenB) external returns (bytes32 pairId) {
        require(tokenA != address(0) && tokenB != address(0), "Zero address");
        require(tokenA != tokenB, "Identical tokens");
        
        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
        pairId = keccak256(abi.encodePacked(token0, token1));
        
        require(pairs[pairId].tokenA == address(0), "Pair exists");
        
        pairs[pairId].tokenA = token0;
        pairs[pairId].tokenB = token1;
        
        emit PairCreated(token0, token1, pairId);
        return pairId;
    }

    /**
     * @notice Adds liquidity to a pair
     * @param pairId The ID of the pair
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add
     * @param amountBMin Minimum amount of tokenB to add
     * @param to Address to receive liquidity tokens
     * @return liquidity Amount of liquidity tokens minted
     */
    function addLiquidity(
        bytes32 pairId,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to
    ) external nonReentrant returns (uint256 liquidity) {
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");
        require(to != address(0), "Invalid to address");
        
        (uint256 amountA, uint256 amountB) = _calculateLiquidityAmounts(
            pairId,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin
        );
        
        _safeTransferFrom(pair.tokenA, msg.sender, address(this), amountA);
        _safeTransferFrom(pair.tokenB, msg.sender, address(this), amountB);
        
        uint256 totalSupply = pair.totalSupply;
        if (totalSupply == 0) {
            liquidity = sqrt(amountA.mul(amountB));
        } else {
            liquidity = min(
                amountA.mul(totalSupply) / pair.reserveA,
                amountB.mul(totalSupply) / pair.reserveB
            );
        }
        
        require(liquidity > 0, "Insufficient liquidity minted");
        
        pair.reserveA = pair.reserveA.add(amountA);
        pair.reserveB = pair.reserveB.add(amountB);
        pair.totalSupply = totalSupply.add(liquidity);
        pair.liquidity[to] = pair.liquidity[to].add(liquidity);
        
        emit LiquidityAdded(pairId, to, amountA, amountB, liquidity);
        return liquidity;
    }

    /**
     * @notice Removes liquidity from a pair
     * @param pairId The ID of the pair
     * @param liquidity Amount of liquidity tokens to remove
     * @param amountAMin Minimum amount of tokenA to receive
     * @param amountBMin Minimum amount of tokenB to receive
     * @param to Address to receive the tokens
     * @return amountA Amount of tokenA received
     * @return amountB Amount of tokenB received
     */
    function removeLiquidity(
        bytes32 pairId,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin,
        address to
    ) external nonReentrant returns (uint256 amountA, uint256 amountB) {
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");
        require(to != address(0), "Invalid to address");
        require(liquidity > 0, "Insufficient liquidity");
        require(pair.liquidity[msg.sender] >= liquidity, "Insufficient user liquidity");
        
        uint256 totalSupply = pair.totalSupply;
        amountA = liquidity.mul(pair.reserveA) / totalSupply;
        amountB = liquidity.mul(pair.reserveB) / totalSupply;
        
        require(amountA >= amountAMin && amountB >= amountBMin, "Insufficient output amount");
        
        pair.reserveA = pair.reserveA.sub(amountA);
        pair.reserveB = pair.reserveB.sub(amountB);
        pair.totalSupply = totalSupply.sub(liquidity);
        pair.liquidity[msg.sender] = pair.liquidity[msg.sender].sub(liquidity);
        
        _safeTransfer(pair.tokenA, to, amountA);
        _safeTransfer(pair.tokenB, to, amountB);
        
        emit LiquidityRemoved(pairId, msg.sender, amountA, amountB, liquidity);
        return (amountA, amountB);
    }

    /**
     * @notice Swaps tokens in a pair
     * @param pairId The ID of the pair
     * @param amountIn Amount of input token
     * @param amountOutMin Minimum amount of output token
     * @param tokenIn Address of input token
     * @param to Address to receive output tokens
     * @return amountOut Amount of output tokens received
     */
    function swap(
        bytes32 pairId,
        uint256 amountIn,
        uint256 amountOutMin,
        address tokenIn,
        address to
    ) external nonReentrant returns (uint256 amountOut) {
        Pair storage pair = pairs[pairId];
        require(pair.tokenA != address(0), "Pair doesn't exist");
        require(to != address(0), "Invalid to address");
        require(amountIn > 0, "Insufficient input amount");
        
        (address token0, ) = pair.tokenA < pair.tokenB 
            ? (pair.tokenA, pair.tokenB) 
            : (pair.tokenB, pair.tokenA);
        
        bool isToken0 = tokenIn == token0;
        require(tokenIn == pair.tokenA || tokenIn == pair.tokenB, "Invalid token");
        
        (uint256 reserveIn, uint256 reserveOut) = isToken0
            ? (pair.reserveA, pair.reserveB)
            : (pair.reserveB, pair.reserveA);
        
        uint256 amountInWithFee = amountIn.mul(FEE_DENOMINATOR.sub(PROTOCOL_FEE.add(LP_FEE)));
        amountOut = reserveOut.mul(amountInWithFee) / (reserveIn.mul(FEE
