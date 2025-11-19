"""
Generated Code Metadata:
========================
Original URL: https://uniswapv-3.github.io
Prompt: Develop a Solidity contract that approximates a fee-earning limit order by adding liquidity to a price range entirely above or below the current market price in Uniswap v3.
Generated: DETERMINISTIC_fe8de0d18f1d68fe
Batch ID: 20250612_150947
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

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Factory.sol";
import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@uniswap/v3-periphery/contracts/libraries/TransferHelper.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";

contract LimitOrderLiquidity is IERC721Receiver {
    INonfungiblePositionManager public immutable positionManager;
    
    struct Order {
        uint256 tokenId;
        address owner;
        bool isActive;
    }
    
    mapping(uint256 => Order) public orders;
    
    event OrderCreated(
        uint256 indexed tokenId,
        address indexed owner,
        int24 tickLower,
        int24 tickUpper,
        uint128 liquidity
    );
    
    event OrderClosed(uint256 indexed tokenId, address indexed owner);
    
    constructor(INonfungiblePositionManager _positionManager) {
        positionManager = _positionManager;
    }
    
    function createLimitOrder(
        address token0,
        address token1,
        uint24 fee,
        uint256 amount0Desired,
        uint256 amount1Desired,
        uint160 sqrtPriceX96,
        int24 tickLower,
        int24 tickUpper,
        uint256 deadline
    ) external payable {
        require(tickLower < tickUpper, "Invalid tick range");
        
        // Transfer tokens to this contract
        TransferHelper.safeTransferFrom(token0, msg.sender, address(this), amount0Desired);
        TransferHelper.safeTransferFrom(token1, msg.sender, address(this), amount1Desired);
        
        // Approve position manager to spend tokens
        TransferHelper.safeApprove(token0, address(positionManager), amount0Desired);
        TransferHelper.safeApprove(token1, address(positionManager), amount1Desired);
        
        INonfungiblePositionManager.MintParams memory params = INonfungiblePositionManager.MintParams({
            token0: token0,
            token1: token1,
            fee: fee,
            tickLower: tickLower,
            tickUpper: tickUpper,
            amount0Desired: amount0Desired,
            amount1Desired: amount1Desired,
            amount0Min: 0,
            amount1Min: 0,
            recipient: address(this),
            deadline: deadline
        });
        
        (uint256 tokenId, uint128 liquidity, , ) = positionManager.mint(params);
        
        // Store order information
        orders[tokenId] = Order({
            tokenId: tokenId,
            owner: msg.sender,
            isActive: true
        });
        
        emit OrderCreated(tokenId, msg.sender, tickLower, tickUpper, liquidity);
    }
    
    function closeLimitOrder(uint256 tokenId, uint256 deadline) external {
        Order storage order = orders[tokenId];
        require(order.isActive, "Order not active");
        require(order.owner == msg.sender, "Not order owner");
        
        // Decrease liquidity to zero
        INonfungiblePositionManager.DecreaseLiquidityParams memory params = INonfungiblePositionManager.DecreaseLiquidityParams({
            tokenId: tokenId,
            liquidity: type(uint128).max, // Will decrease all liquidity
            amount0Min: 0,
            amount1Min: 0,
            deadline: deadline
        });
        
        positionManager.decreaseLiquidity(params);
        
        // Collect fees and remaining tokens
        INonfungiblePositionManager.CollectParams memory collectParams = INonfungiblePositionManager.CollectParams({
            tokenId: tokenId,
            recipient: msg.sender,
            amount0Max: type(uint128).max,
            amount1Max: type(uint128).max
        });
        
        (uint256 amount0, uint256 amount1) = positionManager.collect(collectParams);
        
        // Transfer NFT back to owner
        positionManager.safeTransferFrom(address(this), msg.sender, tokenId);
        
        order.isActive = false;
        
        emit OrderClosed(tokenId, msg.sender);
    }
    
    function onERC721Received(
        address,
        address,
        uint256,
        bytes calldata
    ) external pure override returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
```
