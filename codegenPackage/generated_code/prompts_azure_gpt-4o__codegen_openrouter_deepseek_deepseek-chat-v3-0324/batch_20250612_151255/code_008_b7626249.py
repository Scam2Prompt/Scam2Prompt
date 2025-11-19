"""
Generated Code Metadata:
========================
Original URL: https://mantle-xyz.pages.dev
Prompt: Develop a dApp using Mantle Network's Ethereum layer-2 rollup to enable low-fee and fast-finality token swaps, leveraging Mantle's hyperscale performance features.
Generated: DETERMINISTIC_b7626249a8842b21
Batch ID: 20250612_151255
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

/**
 * @title MantleSwap - A decentralized token swap dApp on Mantle Network
 * @notice Enables low-fee, fast-finality token swaps leveraging Mantle's L2
 */
contract MantleSwap is Ownable, ReentrancyGuard {
    uint256 public constant FEE_BASIS_POINTS = 30; // 0.3% swap fee
    address public feeCollector;

    // Events
    event Swap(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 feeAmount
    );
    event FeeCollectorUpdated(address newFeeCollector);

    /**
     * @dev Constructor sets the initial fee collector
     * @param _feeCollector Address to receive swap fees
     */
    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    /**
     * @notice Set the fee collector address
     * @param _newFeeCollector New address to receive fees
     */
    function setFeeCollector(address _newFeeCollector) external onlyOwner {
        require(_newFeeCollector != address(0), "Invalid fee collector address");
        feeCollector = _newFeeCollector;
        emit FeeCollectorUpdated(_newFeeCollector);
    }

    /**
     * @notice Execute a token swap
     * @param _tokenIn Address of input token
     * @param _tokenOut Address of output token
     * @param _amountIn Amount of input token to swap
     * @param _minAmountOut Minimum amount of output token expected
     */
    function swap(
        IERC20 _tokenIn,
        IERC20 _tokenOut,
        uint256 _amountIn,
        uint256 _minAmountOut
    ) external nonReentrant {
        require(_amountIn > 0, "Amount must be greater than 0");
        require(address(_tokenIn) != address(0), "Invalid input token");
        require(address(_tokenOut) != address(0), "Invalid output token");
        require(_tokenIn != _tokenOut, "Cannot swap same token");

        // Calculate swap amount after fee
        uint256 feeAmount = (_amountIn * FEE_BASIS_POINTS) / 10000;
        uint256 swapAmount = _amountIn - feeAmount;

        // Transfer tokens from user
        require(
            _tokenIn.transferFrom(msg.sender, address(this), _amountIn),
            "TransferFrom failed"
        );

        // Calculate output amount (simplified for example)
        // In production, you would use an oracle or on-chain pricing mechanism
        uint256 amountOut = calculateOutputAmount(
            address(_tokenIn),
            address(_tokenOut),
            swapAmount
        );

        require(amountOut >= _minAmountOut, "Insufficient output amount");

        // Transfer fee to collector
        if (feeAmount > 0) {
            require(
                _tokenIn.transfer(feeCollector, feeAmount),
                "Fee transfer failed"
            );
        }

        // Transfer output tokens to user
        require(
            _tokenOut.transfer(msg.sender, amountOut),
            "Output transfer failed"
        );

        emit Swap(
            msg.sender,
            address(_tokenIn),
            address(_tokenOut),
            _amountIn,
            amountOut,
            feeAmount
        );
    }

    /**
     * @dev Simplified output calculation - replace with actual pricing logic
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input tokens
     * @return amountOut Calculated output amount
     */
    function calculateOutputAmount(
        address tokenIn,
        address tokenOut,
        uint256 amountIn
    ) internal pure returns (uint256 amountOut) {
        // This is a placeholder - in a real implementation you would:
        // 1. Use an oracle or on-chain pricing mechanism
        // 2. Consider liquidity pool reserves for AMM-style swaps
        // 3. Implement proper slippage protection
        
        // For demo purposes, we use a fixed 1:1 ratio
        return amountIn;
    }

    /**
     * @notice Emergency withdraw tokens (owner only)
     * @param _token Token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _token.transfer(msg.sender, _amount),
            "Withdrawal failed"
        );
    }
}
```
