"""
Generated Code Metadata:
========================
Original URL: https://bafybeidtnckzvkdfd4adyg7s3vhgnsxy3sxyvceyaty6bcbuxmmlfvut3a.ipfs.dweb.link
Prompt: Recommend how to integrate Pendle's cross-chain compatibility for Ethereum, Arbitrum, BNB Chain, and Optimism in a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_07cfa1363b66d750
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/utils/Address.sol";

interface IPendleRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

interface ILayerZeroEndpoint {
    function send(
        uint16 _dstChainId,
        bytes calldata _destination,
        bytes calldata _payload,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external payable;
}

contract PendleCrossChainDeFi is ReentrancyGuard {
    using Address for address;
    
    address public owner;
    IPendleRouter public pendleRouter;
    ILayerZeroEndpoint public layerZeroEndpoint;
    
    // Chain IDs for supported networks
    uint16 constant ETHEREUM_CHAIN_ID = 1;
    uint16 constant ARBITRUM_CHAIN_ID = 42161;
    uint16 constant BNB_CHAIN_ID = 56;
    uint16 constant OPTIMISM_CHAIN_ID = 10;
    
    mapping(uint16 => address) public pendleRouters;
    mapping(uint16 => address) public layerZeroEndpoints;
    
    event CrossChainSwap(
        uint16 fromChainId,
        uint16 toChainId,
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOut
    );
    
    event LiquidityAdded(
        uint16 chainId,
        address indexed user,
        address tokenA,
        address tokenB,
        uint amountA,
        uint amountB,
        uint liquidity
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    constructor(
        address _pendleRouter,
        address _layerZeroEndpoint
    ) {
        owner = msg.sender;
        pendleRouter = IPendleRouter(_pendleRouter);
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        
        // Initialize default router addresses (can be updated later)
        pendleRouters[ETHEREUM_CHAIN_ID] = _pendleRouter;
        pendleRouters[ARBITRUM_CHAIN_ID] = _pendleRouter;
        pendleRouters[BNB_CHAIN_ID] = _pendleRouter;
        pendleRouters[OPTIMISM_CHAIN_ID] = _pendleRouter;
    }
    
    function setPendleRouter(uint16 chainId, address router) external onlyOwner {
        require(router != address(0), "Invalid router address");
        pendleRouters[chainId] = router;
    }
    
    function setLayerZeroEndpoint(uint16 chainId, address endpoint) external onlyOwner {
        require(endpoint != address(0), "Invalid endpoint address");
        layerZeroEndpoints[chainId] = endpoint;
    }
    
    function swapExactTokensCrossChain(
        uint16 toChainId,
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline,
        address zroPaymentAddress,
        bytes calldata adapterParams
    ) external payable nonReentrant {
        require(path.length >= 2, "Invalid path");
        require(toChainId == ETHEREUM_CHAIN_ID || 
               toChainId == ARBITRUM_CHAIN_ID || 
               toChainId == BNB_CHAIN_ID || 
               toChainId == OPTIMISM_CHAIN_ID, "Unsupported chain");
        
        IERC20 tokenIn = IERC20(path[0]);
        require(tokenIn.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        require(tokenIn.approve(address(pendleRouter), amountIn), "Approval failed");
        
        uint[] memory amounts = pendleRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            deadline
        );
        
        IERC20 tokenOut = IERC20(path[path.length - 1]);
        uint amountOut = amounts[amounts.length - 1];
        
        bytes memory payload = abi.encode(
            to,
            address(tokenOut),
            amountOut
        );
        
        layerZeroEndpoint.send{value: msg.value}(
            toChainId,
            abi.encodePacked(address(this)),
            payload,
            payable(msg.sender),
            zroPaymentAddress,
            adapterParams
        );
        
        emit CrossChainSwap(
            getCurrentChainId(),
            toChainId,
            msg.sender,
            address(tokenIn),
            address(tokenOut),
            amountIn,
            amountOut
        );
    }
    
    function addLiquidityCrossChain(
        uint16 toChainId,
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline,
        address zroPaymentAddress,
        bytes calldata adapterParams
    ) external payable nonReentrant {
        require(toChainId == ETHEREUM_CHAIN_ID || 
               toChainId == ARBITRUM_CHAIN_ID || 
               toChainId == BNB_CHAIN_ID || 
               toChainId == OPTIMISM_CHAIN_ID, "Unsupported chain");
        
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);
        
        IERC20(tokenA).approve(address(pendleRouter), amountADesired);
        IERC20(tokenB).approve(address(pendleRouter), amountBDesired);
        
        (uint amountA, uint amountB, uint liquidity) = pendleRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );
        
        bytes memory payload = abi.encode(
            to,
            tokenA,
            tokenB,
            amountA,
            amountB,
            liquidity
        );
        
        layerZeroEndpoint.send{value: msg.value}(
            toChainId,
            abi.encodePacked(address(this)),
            payload,
            payable(msg.sender),
            zroPaymentAddress,
            adapterParams
        );
        
        emit LiquidityAdded(
            getCurrentChainId(),
            msg.sender,
            tokenA,
            tokenB,
            amountA,
            amountB,
            liquidity
        );
    }
    
    function getCurrentChainId() internal view returns (uint16) {
        uint256 chainId;
        assembly {
            chainId := chainid()
        }
        return uint16(chainId);
    }
    
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal {
        // Implement cross-chain receive logic here
        // This would be called by LayerZero endpoint when a message is received
    }
    
    receive() external payable {}
    
    // Emergency functions
    function withdrawToken(address token, uint amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
    
    function withdrawEth(uint amount) external onlyOwner {
        payable(owner).transfer(amount);
    }
}
```
