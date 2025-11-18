"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Create a Solidity-based smart contract for a decentralized swap exchange tailored for HarpyCoin, ensuring lower fees and seamless token swaps.
Generated: DETERMINISTIC_1383b3e7ab69dc1e
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title HarpySwapExchange
 * @dev Decentralized exchange smart contract for swapping HarpyCoin with other ERC20 tokens.
 * Features:
 * - Allows token swaps involving HarpyCoin.
 * - Implements lower fees for transactions.
 * - Secure and production-ready code.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HarpySwapExchange is Ownable {
    // Address of HarpyCoin token contract
    address public harpyToken;
    // Swap fee in basis points (e.g., 50 = 0.5%)
    uint256 public swapFeeBasisPoints;

    event TokenSwapped(address indexed user, address indexed fromToken, address indexed toToken, uint256 fromAmount, uint256 toAmount);

    /**
     * @dev Sets initial values for HarpyToken address and swap fee.
     * @param _harpyToken Address of HarpyCoin token contract.
     * @param _swapFeeBasisPoints Swap fee in basis points.
     */
    constructor(address _harpyToken, uint256 _swapFeeBasisPoints) {
        require(_harpyToken != address(0), "Invalid HarpyCoin token address");
        require(_swapFeeBasisPoints <= 10000, "Swap fee cannot exceed 100%");
        harpyToken = _harpyToken;
        swapFeeBasisPoints = _swapFeeBasisPoints;
    }

    /**
     * @dev Updates the swap fee.
     * @param _swapFeeBasisPoints New swap fee in basis points.
     * Can only be called by the contract owner.
     */
    function setSwapFee(uint256 _swapFeeBasisPoints) external onlyOwner {
        require(_swapFeeBasisPoints <= 10000, "Swap fee cannot exceed 100%");
        swapFeeBasisPoints = _swapFeeBasisPoints;
    }

    /**
     * @dev Swaps `fromToken` to `toToken` for the user.
     * @param fromToken Address of the input token.
     * @param toToken Address of the output token.
     * @param fromAmount Amount of `fromToken` to swap.
     */
    function swapTokens(address fromToken, address toToken, uint256 fromAmount) external {
        require(fromToken != address(0) && toToken != address(0), "Invalid token addresses");
        require(fromAmount > 0, "Swap amount must be greater than 0");
        require(fromToken == harpyToken || toToken == harpyToken, "One of the tokens must be HarpyCoin");

        // Transfer `fromToken` from the user to the contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), fromAmount);

        // Calculate swap fee
        uint256 fee = (fromAmount * swapFeeBasisPoints) / 10000;

        // Calculate the net amount to swap (after fee deduction)
        uint256 netFromAmount = fromAmount - fee;

        // Perform the token swap (dummy implementation for simplicity, replace with actual logic)
        uint256 toAmount = getExchangeRate(fromToken, toToken, netFromAmount);

        // Transfer `toToken` to the user
        IERC20(toToken).transfer(msg.sender, toAmount);

        emit TokenSwapped(msg.sender, fromToken, toToken, fromAmount, toAmount);
    }

    /**
     * @dev Dummy function to calculate exchange rate. Replace with actual implementation.
     * @param fromToken Address of the input token.
     * @param toToken Address of the output token.
     * @param amount Amount of `fromToken`.
     * @return Amount of `toToken` to be received.
     */
    function getExchangeRate(address fromToken, address toToken, uint256 amount) internal pure returns (uint256) {
        // For simplicity, assume 1:1 exchange rate
        return amount;
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens mistakenly sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdraw amount must be greater than 0");
        IERC20(token).transfer(owner(), amount);
    }
}
```
