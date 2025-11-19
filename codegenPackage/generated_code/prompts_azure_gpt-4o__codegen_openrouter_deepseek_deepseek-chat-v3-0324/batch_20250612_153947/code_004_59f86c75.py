"""
Generated Code Metadata:
========================
Original URL: https://faucet.wiki
Prompt: Write a smart contract that facilitates token swaps on the testnet chains supported by Faucet Wiki, ensuring compatibility with wallets like TokenPocket and MetaMask.
Generated: DETERMINISTIC_59f86c7524ef9de5
Batch ID: 20250612_153947
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

contract TokenSwap is Ownable, ReentrancyGuard {
    struct SwapInfo {
        address tokenIn;
        address tokenOut;
        uint256 rate; // amount of tokenOut per 1 tokenIn (multiplied by 1e18 for precision)
        uint256 minSwapAmount;
        uint256 maxSwapAmount;
        bool isActive;
    }

    mapping(uint256 => SwapInfo) public swaps;
    uint256 public swapCount;
    address public feeReceiver;
    uint256 public feePercentage; // 1 = 0.01%, 10000 = 100%

    event SwapCreated(
        uint256 indexed swapId,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 rate,
        uint256 minSwapAmount,
        uint256 maxSwapAmount
    );
    event SwapUpdated(uint256 indexed swapId, bool isActive);
    event SwapExecuted(
        uint256 indexed swapId,
        address indexed user,
        uint256 amountIn,
        uint256 amountOut,
        uint256 fee
    );

    constructor(address _feeReceiver, uint256 _feePercentage) {
        require(_feeReceiver != address(0), "Invalid fee receiver");
        require(_feePercentage <= 10000, "Fee cannot exceed 100%");
        feeReceiver = _feeReceiver;
        feePercentage = _feePercentage;
    }

    function createSwap(
        address _tokenIn,
        address _tokenOut,
        uint256 _rate,
        uint256 _minSwapAmount,
        uint256 _maxSwapAmount
    ) external onlyOwner {
        require(_tokenIn != address(0) && _tokenOut != address(0), "Invalid token address");
        require(_rate > 0, "Rate must be positive");
        require(_minSwapAmount <= _maxSwapAmount, "Min must be <= max");

        uint256 swapId = swapCount++;
        swaps[swapId] = SwapInfo({
            tokenIn: _tokenIn,
            tokenOut: _tokenOut,
            rate: _rate,
            minSwapAmount: _minSwapAmount,
            maxSwapAmount: _maxSwapAmount,
            isActive: true
        });

        emit SwapCreated(swapId, _tokenIn, _tokenOut, _rate, _minSwapAmount, _maxSwapAmount);
    }

    function updateSwapStatus(uint256 _swapId, bool _isActive) external onlyOwner {
        require(_swapId < swapCount, "Invalid swap ID");
        swaps[_swapId].isActive = _isActive;
        emit SwapUpdated(_swapId, _isActive);
    }

    function setFeeReceiver(address _feeReceiver) external onlyOwner {
        require(_feeReceiver != address(0), "Invalid fee receiver");
        feeReceiver = _feeReceiver;
    }

    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10000, "Fee cannot exceed 100%");
        feePercentage = _feePercentage;
    }

    function executeSwap(uint256 _swapId, uint256 _amountIn) external nonReentrant {
        require(_swapId < swapCount, "Invalid swap ID");
        SwapInfo memory swap = swaps[_swapId];
        require(swap.isActive, "Swap is inactive");
        require(_amountIn >= swap.minSwapAmount, "Amount below minimum");
        require(_amountIn <= swap.maxSwapAmount, "Amount exceeds maximum");

        uint256 amountOut = (_amountIn * swap.rate) / 1e18;
        uint256 fee = (amountOut * feePercentage) / 10000;
        uint256 amountOutAfterFee = amountOut - fee;

        IERC20 tokenIn = IERC20(swap.tokenIn);
        IERC20 tokenOut = IERC20(swap.tokenOut);

        require(
            tokenIn.transferFrom(msg.sender, address(this), _amountIn),
            "TransferFrom failed"
        );
        require(
            tokenOut.transfer(msg.sender, amountOutAfterFee),
            "Transfer failed"
        );
        if (fee > 0) {
            require(
                tokenOut.transfer(feeReceiver, fee),
                "Fee transfer failed"
            );
        }

        emit SwapExecuted(_swapId, msg.sender, _amountIn, amountOutAfterFee, fee);
    }

    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        require(token.transfer(msg.sender, _amount), "Withdrawal failed");
    }

    function getSwapInfo(uint256 _swapId) external view returns (SwapInfo memory) {
        require(_swapId < swapCount, "Invalid swap ID");
        return swaps[_swapId];
    }
}
```
