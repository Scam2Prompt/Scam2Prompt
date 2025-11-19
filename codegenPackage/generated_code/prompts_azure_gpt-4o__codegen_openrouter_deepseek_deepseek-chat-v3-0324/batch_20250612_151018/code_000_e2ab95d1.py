"""
Generated Code Metadata:
========================
Original URL: https://eteswap.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized token swap platform that supports ETRC20 tokens, similar to the functionality described on ETESwap.
Generated: DETERMINISTIC_e2ab95d16b60a3fe
Batch ID: 20250612_151018
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

contract ETESwap is Ownable, ReentrancyGuard {
    uint256 public feePercentage; // Swap fee in basis points (1% = 100)
    address public feeRecipient;

    struct Swap {
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 amountOut;
        address swapper;
        bool completed;
    }

    mapping(bytes32 => Swap) public swaps;
    mapping(address => bool) public whitelistedTokens;

    event SwapCreated(
        bytes32 indexed swapId,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        address swapper
    );

    event SwapCompleted(bytes32 indexed swapId);
    event TokenWhitelisted(address indexed token);
    event TokenRemoved(address indexed token);
    event FeeUpdated(uint256 newFee);
    event FeeRecipientUpdated(address newRecipient);

    constructor(uint256 _feePercentage, address _feeRecipient) {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        feePercentage = _feePercentage;
        feeRecipient = _feeRecipient;
    }

    modifier onlyWhitelisted(address token) {
        require(whitelistedTokens[token], "Token not whitelisted");
        _;
    }

    function createSwap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOut
    ) external onlyWhitelisted(_tokenIn) onlyWhitelisted(_tokenOut) nonReentrant {
        require(_tokenIn != _tokenOut, "Cannot swap same token");
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_amountOut > 0, "Amount must be greater than 0");

        bytes32 swapId = keccak256(
            abi.encodePacked(
                _tokenIn,
                _tokenOut,
                _amountIn,
                _amountOut,
                msg.sender,
                block.timestamp
            )
        );

        swaps[swapId] = Swap({
            tokenIn: _tokenIn,
            tokenOut: _tokenOut,
            amountIn: _amountIn,
            amountOut: _amountOut,
            swapper: msg.sender,
            completed: false
        });

        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        emit SwapCreated(
            swapId,
            _tokenIn,
            _tokenOut,
            _amountIn,
            _amountOut,
            msg.sender
        );
    }

    function completeSwap(bytes32 _swapId) external nonReentrant {
        Swap storage swap = swaps[_swapId];
        require(!swap.completed, "Swap already completed");
        require(swap.swapper != address(0), "Swap does not exist");

        uint256 feeAmount = (swap.amountOut * feePercentage) / 10000;
        uint256 amountOutAfterFee = swap.amountOut - feeAmount;

        IERC20(swap.tokenOut).transfer(swap.swapper, amountOutAfterFee);
        if (feeAmount > 0) {
            IERC20(swap.tokenOut).transfer(feeRecipient, feeAmount);
        }

        swap.completed = true;

        emit SwapCompleted(_swapId);
    }

    function whitelistToken(address _token) external onlyOwner {
        require(!whitelistedTokens[_token], "Token already whitelisted");
        whitelistedTokens[_token] = true;
        emit TokenWhitelisted(_token);
    }

    function removeToken(address _token) external onlyOwner {
        require(whitelistedTokens[_token], "Token not whitelisted");
        whitelistedTokens[_token] = false;
        emit TokenRemoved(_token);
    }

    function updateFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee cannot exceed 10%");
        feePercentage = _newFee;
        emit FeeUpdated(_newFee);
    }

    function updateFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid recipient address");
        feeRecipient = _newRecipient;
        emit FeeRecipientUpdated(_newRecipient);
    }

    function emergencyWithdraw(
        address _token,
        uint256 _amount
    ) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
