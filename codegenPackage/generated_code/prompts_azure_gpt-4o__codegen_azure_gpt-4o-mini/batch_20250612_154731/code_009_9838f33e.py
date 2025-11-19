"""
Generated Code Metadata:
========================
Original URL: https://jupagdex.com
Prompt: Write a Solidity contract that interacts with Jupiter's API to execute swaps and ensure the best rates for Solana-based tokens.
Generated: DETERMINISTIC_9838f33ed8b91b48
Batch ID: 20250612_154731
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

interface IJupiterAPI {
    function getBestSwapRate(
        address fromToken,
        address toToken,
        uint256 amount
    ) external view returns (uint256 bestRate, address[] memory swapPath);

    function executeSwap(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient
    ) external returns (uint256 receivedAmount);
}

contract TokenSwap is Ownable {
    using Address for address;

    // Jupiter API contract address
    IJupiterAPI public jupiterAPI;

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Jupiter API address
    constructor(address _jupiterAPI) {
        require(_jupiterAPI != address(0), "Invalid Jupiter API address");
        jupiterAPI = IJupiterAPI(_jupiterAPI);
    }

    // Function to set a new Jupiter API address (only owner)
    function setJupiterAPI(address _jupiterAPI) external onlyOwner {
        require(_jupiterAPI != address(0), "Invalid Jupiter API address");
        jupiterAPI = IJupiterAPI(_jupiterAPI);
    }

    // Function to swap tokens using Jupiter's API
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amount
    ) external returns (uint256 receivedAmount) {
        require(amount > 0, "Amount must be greater than zero");
        require(fromToken != toToken, "Cannot swap the same token");

        // Transfer tokens from the user to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Get the best swap rate and path from Jupiter API
        (uint256 bestRate, address[] memory swapPath) = jupiterAPI.getBestSwapRate(fromToken, toToken, amount);
        require(bestRate > 0, "No valid swap rate found");

        // Approve the Jupiter API to spend the tokens
        IERC20(fromToken).approve(address(jupiterAPI), amount);

        // Execute the swap
        receivedAmount = jupiterAPI.executeSwap(fromToken, toToken, amount, msg.sender);
        require(receivedAmount > 0, "Swap failed, received amount is zero");

        // Emit the swap executed event
        emit SwapExecuted(fromToken, toToken, amount, receivedAmount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
