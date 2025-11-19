"""
Generated Code Metadata:
========================
Original URL: https://steep-zebra-teeny.on-fleek.app
Prompt: Generate a code snippet in Solidity to create a simple token swapping smart contract on the Arbitrum network, inspired by Zeedex's functionality.
Generated: DETERMINISTIC_99b20f61312dcfd7
Batch ID: 20250622_205030
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

contract TokenSwapper is Ownable, ReentrancyGuard {
    uint256 public feePercentage; // Fee percentage (e.g., 10 for 0.1%)
    address public feeRecipient;

    event Swap(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 feeAmount
    );
    event FeeUpdated(uint256 newFee);
    event FeeRecipientUpdated(address newRecipient);

    constructor(uint256 _feePercentage, address _feeRecipient) {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        
        feePercentage = _feePercentage;
        feeRecipient = _feeRecipient;
    }

    /**
     * @dev Swap tokens with fee deduction
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input tokens to swap
     * @param minAmountOut Minimum amount of output tokens expected
     */
    function swap(
        IERC20 tokenIn,
        IERC20 tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external nonReentrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(address(tokenIn) != address(tokenOut), "Cannot swap same tokens");

        // Calculate fee and transfer amount
        uint256 feeAmount = (amountIn * feePercentage) / 10000;
        uint256 transferAmount = amountIn - feeAmount;

        // Transfer tokens from user to contract
        require(
            tokenIn.transferFrom(msg.sender, address(this), amountIn),
            "TransferFrom failed"
        );

        // Transfer fee to fee recipient
        if (feeAmount > 0) {
            require(
                tokenIn.transfer(feeRecipient, feeAmount),
                "Fee transfer failed"
            );
        }

        // Get contract balance of output token
        uint256 contractBalance = tokenOut.balanceOf(address(this));
        require(contractBalance >= transferAmount, "Insufficient liquidity");

        // Transfer output tokens to user
        require(
            tokenOut.transfer(msg.sender, transferAmount),
            "Transfer failed"
        );

        emit Swap(
            msg.sender,
            address(tokenIn),
            address(tokenOut),
            amountIn,
            transferAmount,
            feeAmount
        );
    }

    /**
     * @dev Update swap fee percentage
     * @param _newFee New fee percentage (e.g., 10 for 0.1%)
     */
    function updateFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee cannot exceed 10%");
        feePercentage = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @dev Update fee recipient address
     * @param _newRecipient New fee recipient address
     */
    function updateFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid fee recipient");
        feeRecipient = _newRecipient;
        emit FeeRecipientUpdated(_newRecipient);
    }

    /**
     * @dev Withdraw ERC20 tokens from contract (emergency only)
     * @param token Token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(
            token.transfer(msg.sender, amount),
            "Withdrawal failed"
        );
    }
}
```
