"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Develop a Solidity-based decentralized exchange smart contract for Ethereum Classic Vision, incorporating features mentioned in the ETCV white paper.
Generated: DETERMINISTIC_c55a8ab80f997f1b
Batch ID: 20250612_151847
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
 * @title ETCV Decentralized Exchange
 * @dev A decentralized exchange contract for Ethereum Classic Vision
 */
contract ETCVDex is ReentrancyGuard {
    using SafeMath for uint256;

    // Contract owner
    address public owner;

    // Trading fee percentage (0.3% as per ETCV whitepaper)
    uint256 public constant FEE_PERCENTAGE = 30; // 0.3% (30 basis points)
    uint256 public constant FEE_DENOMINATOR = 10000;

    // Token pair structure
    struct TokenPair {
        address tokenA;
        address tokenB;
        bool isActive;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
        mapping(address => uint256) balancesA;
        mapping(address => uint256) balancesB;
    }

    // All token pairs
    TokenPair[] public tokenPairs;

    // Mapping for quick lookup of token pairs
    mapping(address => mapping(address => uint256)) public pairIndex;

    // Events
    event PairCreated(address indexed tokenA, address indexed tokenB, uint256 pairId);
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swap(address indexed sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validPair(uint256 _pairId) {
        require(_pairId < tokenPairs.length, "Invalid pair ID");
        require(tokenPairs[_pairId].isActive, "Pair is not active");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new token pair
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     */
    function createPair(address _tokenA, address _tokenB) external onlyOwner {
        require(_tokenA != _tokenB, "Cannot pair token with itself");
        require(pairIndex[_tokenA][_tokenB] == 0, "Pair already exists");

        uint256 newPairId = tokenPairs.length;
        TokenPair storage newPair = tokenPairs.push();
        newPair.tokenA = _tokenA;
        newPair.tokenB = _tokenB;
        newPair.isActive = true;

        pairIndex[_tokenA][_tokenB] = newPairId + 1; // +1 to distinguish from default 0
        pairIndex[_tokenB][_tokenA] = newPairId + 1;

        emit PairCreated(_tokenA, _tokenB, newPairId);
    }

    /**
     * @dev Add liquidity to a token pair
     * @param _pairId ID of the token pair
     * @param _amountA Amount of token A to add
     * @param _amountB Amount of token B to add
     */
    function addLiquidity(uint256 _pairId, uint256 _amountA, uint256 _amountB) 
        external 
        nonReentrant 
        validPair(_pairId) 
    {
        TokenPair storage pair = tokenPairs[_pairId];
        
        require(_amountA > 0 && _amountB > 0, "Amounts must be greater than 0");

        // Transfer tokens from user to contract
        IERC20(pair.tokenA).transferFrom(msg.sender, address(this), _amountA);
        IERC20(pair.tokenB).transferFrom(msg.sender, address(this), _amountB);

        uint256 liquidity;
        if (pair.totalLiquidity == 0) {
            liquidity = sqrt(_amountA.mul(_amountB));
        } else {
            liquidity = min(
                _amountA.mul(pair.totalLiquidity) / pair.balancesA[address(this)],
                _amountB.mul(pair.totalLiquidity) / pair.balancesB[address(this)]
            );
        }

        require(liquidity > 0, "Insufficient liquidity minted");

        // Update balances and liquidity
        pair.balancesA[address(this)] = pair.balancesA[address(this)].add(_amountA);
        pair.balancesB[address(this)] = pair.balancesB[address(this)].add(_amountB);
        pair.liquidity[msg.sender] = pair.liquidity[msg.sender].add(liquidity);
        pair.totalLiquidity = pair.totalLiquidity.add(liquidity);

        emit LiquidityAdded(msg.sender, _amountA, _amountB, liquidity);
    }

    /**
     * @dev Remove liquidity from a token pair
     * @param _pairId ID of the token pair
     * @param _liquidity Amount of liquidity to remove
     */
    function removeLiquidity(uint256 _pairId, uint256 _liquidity) 
        external 
        nonReentrant 
        validPair(_pairId) 
    {
        TokenPair storage pair = tokenPairs[_pairId];
        
        require(_liquidity > 0, "Liquidity must be greater than 0");
        require(pair.liquidity[msg.sender] >= _liquidity, "Insufficient liquidity");

        // Calculate amounts to withdraw
        uint256 amountA = _liquidity.mul(pair.balancesA[address(this)]) / pair.totalLiquidity;
        uint256 amountB = _liquidity.mul(pair.balancesB[address(this)]) / pair.totalLiquidity;

        // Update balances and liquidity
        pair.balancesA[address(this)] = pair.balancesA[address(this)].sub(amountA);
        pair.balancesB[address(this)] = pair.balancesB[address(this)].sub(amountB);
        pair.liquidity[msg.sender] = pair.liquidity[msg.sender].sub(_liquidity);
        pair.totalLiquidity = pair.totalLiquidity.sub(_liquidity);

        // Transfer tokens back to user
        IERC20(pair.tokenA).transfer(msg.sender, amountA);
        IERC20(pair.tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, amountA, amountB, _liquidity);
    }

    /**
     * @dev Execute a token swap
     * @param _pairId ID of the token pair
     * @param _tokenIn Address of input token
     * @param _amountIn Amount of input token
     * @param _minAmountOut Minimum amount of output token expected
     */
    function swap(
        uint256 _pairId,
        address _tokenIn,
        uint256 _amountIn,
        uint256 _minAmountOut
    ) external nonReentrant validPair(_pairId) {
        TokenPair storage pair = tokenPairs[_pairId];
        
        require(_amountIn > 0, "Amount must be greater than 0");
        require(
            _tokenIn == pair.tokenA || _tokenIn == pair.tokenB,
            "Invalid input token"
        );

        address tokenOut = _tokenIn == pair.tokenA ? pair.tokenB : pair.tokenA;
        
        // Calculate output amount
        uint256 reserveIn = _tokenIn == pair.tokenA 
            ? pair.balancesA[address(this)] 
            : pair.balancesB[address(this)];
        uint256 reserveOut = _tokenIn == pair.tokenA 
            ? pair.balancesB[address(this)] 
            : pair.balancesA[address(this)];
        
        uint256 amountInWithFee = _amountIn.mul(FEE_DENOMINATOR.sub(FEE_PERCENTAGE));
        uint256 amountOut = reserveOut.mul(amountInWithFee) / 
            (reserveIn.mul(FEE_DENOMINATOR).add(amountInWithFee));
        
        require(amountOut >= _minAmountOut, "Insufficient output amount");

        // Transfer input tokens from user
        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        // Update balances
        if (_tokenIn == pair.tokenA) {
            pair.balancesA[address(this)] = pair.balancesA[address(this)].add(_amountIn);
            pair.balancesB[address(this)] = pair.balancesB[address(this)].sub(amountOut);
        } else {
            pair.balancesB[address(this)] = pair.balancesB[address(this)].add(_amountIn);
            pair.balancesA[address(this)] = pair.balancesA[address(this)].sub(
