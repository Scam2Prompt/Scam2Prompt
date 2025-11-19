"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Design a liquidity pool for a decentralized exchange (DEX) that integrates Thoreum's token, considering its protocol-owned liquidity and market buying mechanisms.
Generated: DETERMINISTIC_d9909d3df743a8e5
Batch ID: 20250622_210236
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
 * @title ThoreumDEXPool
 * @dev A liquidity pool for Thoreum token with protocol-owned liquidity and market buying mechanisms
 */
contract ThoreumDEXPool is ReentrancyGuard {
    using SafeMath for uint256;

    // Token addresses
    address public immutable tokenA; // Thoreum token
    address public immutable tokenB; // Paired token (e.g., ETH, BNB, etc.)

    // Protocol-owned liquidity
    address public protocolOwner;
    uint256 public protocolLiquidityShare; // Percentage of liquidity owned by protocol (e.g., 1000 = 10%)

    // Pool reserves
    uint256 public reserveA;
    uint256 public reserveB;

    // Total supply of LP tokens
    uint256 public totalSupply;

    // Mapping of LP token balances
    mapping(address => uint256) public balanceOf;

    // Events
    event Mint(address indexed sender, uint256 amountA, uint256 amountB);
    event Burn(address indexed sender, uint256 amountA, uint256 amountB, address indexed to);
    event Swap(
        address indexed sender,
        uint256 amountIn,
        uint256 amountOut,
        address tokenIn,
        address tokenOut,
        address indexed to
    );
    event ProtocolLiquidityAdded(uint256 amountA, uint256 amountB);
    event ProtocolLiquidityRemoved(uint256 amountA, uint256 amountB);

    constructor(address _tokenA, address _tokenB, address _protocolOwner, uint256 _protocolLiquidityShare) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        require(_protocolOwner != address(0), "Invalid protocol owner");
        require(_protocolLiquidityShare <= 10000, "Invalid protocol share"); // Max 100%

        tokenA = _tokenA;
        tokenB = _tokenB;
        protocolOwner = _protocolOwner;
        protocolLiquidityShare = _protocolLiquidityShare;
    }

    /**
     * @dev Mints LP tokens by adding liquidity
     * @param amountA Amount of tokenA to add
     * @param amountB Amount of tokenB to add
     */
    function mint(uint256 amountA, uint256 amountB) external nonReentrant {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");

        uint256 _reserveA = reserveA;
        uint256 _reserveB = reserveB;
        uint256 liquidity;

        if (totalSupply == 0) {
            liquidity = sqrt(amountA.mul(amountB));
            
            // Protocol-owned liquidity
            uint256 protocolLiquidity = liquidity.mul(protocolLiquidityShare).div(10000);
            balanceOf[protocolOwner] = protocolLiquidity;
            totalSupply = liquidity.add(protocolLiquidity);
            
            emit ProtocolLiquidityAdded(
                amountA.mul(protocolLiquidityShare).div(10000),
                amountB.mul(protocolLiquidityShare).div(10000)
            );
        } else {
            liquidity = min(
                amountA.mul(totalSupply) / _reserveA,
                amountB.mul(totalSupply) / _reserveB
            );
        }

        require(liquidity > 0, "Insufficient liquidity minted");
        
        // Transfer tokens from sender
        _safeTransferFrom(tokenA, msg.sender, address(this), amountA);
        _safeTransferFrom(tokenB, msg.sender, address(this), amountB);

        // Update reserves
        reserveA = _reserveA.add(amountA);
        reserveB = _reserveB.add(amountB);
        
        // Mint LP tokens
        balanceOf[msg.sender] = balanceOf[msg.sender].add(liquidity);
        totalSupply = totalSupply.add(liquidity);

        emit Mint(msg.sender, amountA, amountB);
    }

    /**
     * @dev Burns LP tokens and withdraws liquidity
     * @param liquidity Amount of LP tokens to burn
     * @param to Address to receive withdrawn tokens
     */
    function burn(uint256 liquidity, address to) external nonReentrant {
        require(liquidity > 0, "Insufficient liquidity burned");
        require(balanceOf[msg.sender] >= liquidity, "Insufficient balance");

        uint256 _reserveA = reserveA;
        uint256 _reserveB = reserveB;
        
        uint256 amountA = liquidity.mul(_reserveA) / totalSupply;
        uint256 amountB = liquidity.mul(_reserveB) / totalSupply;

        // Burn LP tokens
        balanceOf[msg.sender] = balanceOf[msg.sender].sub(liquidity);
        totalSupply = totalSupply.sub(liquidity);

        // Transfer tokens to recipient
        _safeTransfer(tokenA, to, amountA);
        _safeTransfer(tokenB, to, amountB);

        // Update reserves
        reserveA = _reserveA.sub(amountA);
        reserveB = _reserveB.sub(amountB);

        emit Burn(msg.sender, amountA, amountB, to);
    }

    /**
     * @dev Swaps tokens using the pool
     * @param amountIn Amount of input token
     * @param tokenIn Input token address
     * @param tokenOut Output token address
     * @param to Address to receive output tokens
     */
    function swap(uint256 amountIn, address tokenIn, address tokenOut, address to) external nonReentrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(tokenIn == tokenA || tokenIn == tokenB, "Invalid input token");
        require(tokenOut == tokenA || tokenOut == tokenB, "Invalid output token");
        require(tokenIn != tokenOut, "Same token swap not allowed");

        (uint256 _reserveA, uint256 _reserveB) = (reserveA, reserveB);
        uint256 amountOut;

        if (tokenIn == tokenA) {
            amountOut = getAmountOut(amountIn, _reserveA, _reserveB);
            _safeTransferFrom(tokenA, msg.sender, address(this), amountIn);
            _safeTransfer(tokenB, to, amountOut);
            reserveA = _reserveA.add(amountIn);
            reserveB = _reserveB.sub(amountOut);
        } else {
            amountOut = getAmountOut(amountIn, _reserveB, _reserveA);
            _safeTransferFrom(tokenB, msg.sender, address(this), amountIn);
            _safeTransfer(tokenA, to, amountOut);
            reserveB = _reserveB.add(amountIn);
            reserveA = _reserveA.sub(amountOut);
        }

        emit Swap(msg.sender, amountIn, amountOut, tokenIn, tokenOut, to);
    }

    /**
     * @dev Calculates output amount for a swap
     * @param amountIn Input amount
     * @param reserveIn Reserve of input token
     * @param reserveOut Reserve of output token
     * @return amountOut Output amount
     */
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        
        uint256 amountInWithFee = amountIn.mul(997); // 0.3% fee
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(1000).add(amountInWithFee);
        return numerator / denominator;
    }

    /**
     * @dev Protocol function to remove protocol-owned liquidity
     * @param amountA Amount of tokenA to remove
     * @param amountB Amount of tokenB to remove
     */
    function removeProtocolLiquidity(uint256 amountA, uint256 amountB) external {
        require(msg.sender == protocolOwner, "Only protocol owner");
        
        uint256 liquidity = balanceOf[protocolOwner];
        require(liquidity > 0, "No protocol liquidity");
        
        uint256 _reserveA = reserveA;
        uint256 _reserveB = reserveB;
        
        uint256 expectedAmountA = liquidity.mul(_reserveA) / totalSupply;
        uint256 expectedAmountB = liquidity.mul(_reserveB) / totalSupply;
        
        require(amountA <= expectedAmountA && amountB <= expectedAmountB, "Amount exceeds protocol share");

        // Burn LP tokens
        balanceOf[protocolOwner] = balanceOf[protocolOwner].sub(liquidity);
        totalSupply = totalSupply.sub(liquidity);

        // Transfer tokens to protocol owner
        _
