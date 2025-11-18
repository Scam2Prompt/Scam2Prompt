"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-io-landing-production.pages.dev
Prompt: Provide an example of using the 1inch RabbitHole feature to protect against sandwich attacks during token swaps in a smart contract.
Generated: DETERMINISTIC_ee55c3c4e8806923
Batch ID: 20250612_154954
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IOneInch {
    function swap(
        bytes calldata swapData
    ) external payable returns (uint256 returnAmount, uint256 gasCost);
}

contract SandwichProtection is Ownable, ReentrancyGuard {
    IOneInch public oneInchRouter;

    // Event to log swaps
    event TokenSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the 1inch Router address
    constructor(address _oneInchRouter) {
        require(_oneInchRouter != address(0), "Invalid router address");
        oneInchRouter = IOneInch(_oneInchRouter);
    }

    // Function to perform a token swap with sandwich attack protection
    function protectedSwap(bytes calldata swapData, uint256 maxSlippage) external nonReentrant {
        // Getting the initial balance of the token that will be swapped
        (address tokenIn, address tokenOut, uint256 amountIn) = _decodeSwapData(swapData);
        uint256 initialBalance = IERC20(tokenOut).balanceOf(address(this));

        // Executing the swap
        (uint256 returnAmount, uint256 gasCost) = oneInchRouter.swap{value: msg.value}(swapData);

        // Checking for sandwich attack by comparing token balances
        uint256 finalBalance = IERC20(tokenOut).balanceOf(address(this));
        require(finalBalance >= initialBalance, "Sandwich attack detected: final balance is less than initial");

        // Ensuring slippage is within acceptable limits
        uint256 expectedAmount = amountIn * (100 - maxSlippage) / 100;
        require(returnAmount >= expectedAmount, "Slippage exceeded: received amount is less than expected");

        // Emitting the swap event
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, returnAmount);
    }

    // Internal function to decode swap data (assuming specific format)
    function _decodeSwapData(bytes calldata swapData) internal pure returns (address tokenIn, address tokenOut, uint256 amountIn) {
        // Decode the swap data (this is just an example, actual implementation may vary)
        // The swapData must contain the token addresses and amount information
        (tokenIn, tokenOut, amountIn) = abi.decode(swapData, (address, address, uint256));
    }

    // Function to withdraw tokens that are mistakenly sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
