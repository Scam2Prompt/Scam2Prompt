"""
Generated Code Metadata:
========================
Original URL: https://pulsemex.com
Prompt: Suggest improvements to the PulseX DEX protocol, building upon its fork from Uniswap V2 and PancakeSwap V2.
Generated: DETERMINISTIC_d054b6e9b7bcd641
Batch ID: 20250622_211952
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title PulseX Enhanced Protocol
 * @notice Improvements over PulseX (Uniswap V2/PancakeSwap V2 fork)
 */
contract PulseXEnhanced {
    address public immutable factory;
    address public immutable router;
    address public immutable WETH;
    
    // Protocol fee parameters
    uint256 public constant PROTOCOL_FEE_BPS = 5; // 0.05% protocol fee
    uint256 public constant MAX_SWAP_FEE_BPS = 30; // 0.3% max swap fee
    
    // Fee recipient address
    address public feeRecipient;
    
    // Mapping to track custom swap fees per pair
    mapping(address => uint256) public pairSwapFees;
    
    // Events
    event PairSwapFeeUpdated(address indexed pair, uint256 feeBps);
    event FeeRecipientUpdated(address indexed newRecipient);
    event ProtocolFeeCollected(address indexed pair, uint256 amount);
    
    /**
     * @param _factory Uniswap V2 compatible factory address
     * @param _router Uniswap V2 compatible router address
     * @param _WETH Wrapped native token address
     * @param _feeRecipient Address to receive protocol fees
     */
    constructor(
        address _factory,
        address _router,
        address _WETH,
        address _feeRecipient
    ) {
        require(_factory != address(0), "Invalid factory");
        require(_router != address(0), "Invalid router");
        require(_WETH != address(0), "Invalid WETH");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        
        factory = _factory;
        router = _router;
        WETH = _WETH;
        feeRecipient = _feeRecipient;
    }
    
    /**
     * @notice Set custom swap fee for a pair
     * @dev Only callable by the pair contract
     * @param feeBps Fee in basis points (1 = 0.01%)
     */
    function setPairSwapFee(uint256 feeBps) external {
        require(IUniswapV2Factory(factory).getPair(msg.sender, address(0)) != address(0), "Not a valid pair");
        require(feeBps <= MAX_SWAP_FEE_BPS, "Fee too high");
        pairSwapFees[msg.sender] = feeBps;
        emit PairSwapFeeUpdated(msg.sender, feeBps);
    }
    
    /**
     * @notice Update fee recipient address
     * @dev Only callable by owner
     * @param newRecipient New fee recipient address
     */
    function updateFeeRecipient(address newRecipient) external {
        require(msg.sender == feeRecipient, "Unauthorized");
        require(newRecipient != address(0), "Invalid address");
        feeRecipient = newRecipient;
        emit FeeRecipientUpdated(newRecipient);
    }
    
    /**
     * @notice Enhanced swap function with protocol fee
     * @param amountIn Amount of input tokens
     * @param amountOutMin Minimum amount of output tokens
     * @param path Swap path (token addresses)
     * @param to Recipient address
     * @param deadline Transaction deadline
     */
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts) {
        require(path.length >= 2, "Invalid path");
        
        // Calculate protocol fee
        uint256 protocolFee = (amountIn * PROTOCOL_FEE_BPS) / 10000;
        uint256 amountInAfterFee = amountIn - protocolFee;
        
        // Transfer tokens from sender
        TransferHelper.safeTransferFrom(
            path[0], msg.sender, address(this), amountIn
        );
        
        // Take protocol fee
        TransferHelper.safeTransfer(path[0], feeRecipient, protocolFee);
        emit ProtocolFeeCollected(path[0], protocolFee);
        
        // Approve router to spend tokens
        TransferHelper.safeApprove(path[0], router, amountInAfterFee);
        
        // Get pair swap fee or use default
        address pair = IUniswapV2Factory(factory).getPair(path[0], path[1]);
        uint256 swapFee = pairSwapFees[pair] > 0 ? pairSwapFees[pair] : 25; // Default 0.25%
        
        // Execute swap through router
        amounts = IUniswapV2Router02(router).swapExactTokensForTokens(
            amountInAfterFee,
            amountOutMin,
            path,
            to,
            deadline
        );
        
        // Additional checks for large swaps
        if (amountIn > 1 ether) {
            _validatePriceImpact(path, amounts);
        }
    }
    
    /**
     * @notice Internal function to validate price impact
     * @dev Reverts if price impact is too high
     * @param path Swap path
     * @param amounts Swap amounts
     */
    function _validatePriceImpact(
        address[] memory path,
        uint256[] memory amounts
    ) internal view {
        uint256 expectedOut = IUniswapV2Router02(router).getAmountsOut(
            amounts[0],
            path
        )[path.length - 1];
        
        uint256 priceImpact = ((expectedOut - amounts[amounts.length - 1]) * 10000) / expectedOut;
        require(priceImpact < 100, "Price impact too high"); // Max 1% price impact
    }
    
    // Additional utility functions would be added here...
}

// Helper library for safe transfers
library TransferHelper {
    function safeTransfer(
        address token,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSelector(0xa9059cbb, to, value)
        );
        require(
            success && (data.length == 0 || abi.decode(data, (bool))),
            "Transfer failed"
        );
    }

    function safeTransferFrom(
        address token,
        address from,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSelector(0x23b872dd, from, to, value)
        );
        require(
            success && (data.length == 0 || abi.decode(data, (bool))),
            "TransferFrom failed"
        );
    }

    function safeApprove(
        address token,
        address spender,
        uint256 value
    ) internal {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSelector(0x095ea7b3, spender, value)
        );
        require(
            success && (data.length == 0 || abi.decode(data, (bool))),
            "Approve failed"
        );
    }
}
```
